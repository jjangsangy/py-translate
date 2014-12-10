# -*- coding: utf-8 -*-
"""
coroutines
~~~~~~~~~~

All functions definied within this file are essentially coroutines or
helper functions for working with coroutines.

Therefore members follow the coroutine pattern either as consumers, producers or
consumer/producers
"""

from __future__ import print_function

from sys import stdin, stdout
from functools import wraps, partial, reduce
from multiprocessing import cpu_count
from multiprocessing.dummy import Pool as ThreadPool

from concurrent.futures import ThreadPoolExecutor, as_completed

__all__ = 'coroutine', 'chunk', 'spool', 'source', 'set_task', 'write_stream'

# TODO: Get rid of this global variable
MAX_WORK = cpu_count() * 8

def coroutine(func):
    """
    Initializes coroutine essentially priming it to the yield statement.
    Used as a decorator over functions that generate coroutines.

    .. code-block:: python

        # Basic coroutine producer/consumer pattern
        from translate import coroutine

        @coroutine
        def coroutine_foo(bar):
            try:
                while True:
                    baz = (yield)
                    bar.send(baz)

            except GeneratorExit:
                bar.close()

    :param func: Unprimed Generator
    :type func: Function

    :return: Initialized Coroutine
    :rtype: Function
    """

    @wraps(func)
    def initialization(*args, **kwargs):

        start = func(*args, **kwargs)
        next(start)

        return start

    return initialization


def accumulator(init, update):
    """
    Generic accumulator function.

    :param init:  Initial Value
    :param update: Value to accumulate

    :return: Combined Values
    """
    return (
        init + len(update)
            if isinstance(init, int) else
        init + update
    )


def write_stream(trans, output):
    """
    :param script: Translated Text
    :type script: Iterable

    :return None:
    """
    for line in trans['sentences']:
        if line.get(output, None):
            stdout.write(line[output])

    stdout.write('\n')
    stdout.flush()

    return None

@coroutine
def set_task(translation_function, source, dest, translit=False):
    """
    Task Setter Coroutine

    End point destination coroutine of a purely consumer type.
    Delegates Text IO to the `write_stream` function.

    :param translation_function: Translator
    :type translation_function: Function

    :param source: Source Language Code
    :type source: String

    :param dest: Destination Language Code
    :type dest: String
    """
    task      = tuple()
    workers   = ThreadPoolExecutor(max_workers=MAX_WORK)
    translate = partial(translation_function, source, dest)
    output    = ('translit' if translit else 'trans')
    url_futures = dict()

    try:
        while True:
            task = yield
            url_futures.update([(workers.submit(translate, msg), msg) for msg in task])

    except GeneratorExit:

        for future in as_completed(url_futures):
            if not future.exception():
                result = future.result()
                write_stream(result, output)
            else:
                raise future.exception()

        workers.shutdown(wait=True)

@coroutine
def chunk(task):
    """
    Chunk text into a queue and send by copy to a task setter coroutine.
    Once a queue has been built it is sent by copy and then destroyed.

    :param task: Task setter
    :type task: Coroutine
    """
    queue = ()

    try:
        while True:

            while len(queue) < MAX_WORK:
                line   = (yield)
                queue += (line,)

            task.send(queue)
            queue = ()

    except GeneratorExit:
        task.send(queue)
        task.close()

@coroutine
def spool(iterable, maxlen=1500):
    """
    Consumes text streams and spools them together for more io
    efficient processes.

    :param iterable: Sends text stream for further processing
    :type iterable: Coroutine

    :param maxlen: Maximum query string size
    :type maxlen: Integer
    """
    words, text = 0, ''

    try:
        while True:

            while words < maxlen:
                stream = yield
                text   = reduce(accumulator, stream, text)
                words  = reduce(accumulator, stream, words)

            iterable.send(text)

            words, text = 0, ''

    except GeneratorExit:
        iterable.send(text)
        iterable.close()

# TODO: Implement FileIO
def source(target):
    """
    Coroutine starting point. Produces text stream and forwards to consumers

    :param target: Target coroutine consumer
    :type target: Coroutine
    """

    if stdin.isatty():
        # target.send(args.file)
        return

    for line in stdin:
        target.send(line)

    target.close()
