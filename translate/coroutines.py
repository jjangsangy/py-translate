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

__all__ = 'coroutine', 'chunk', 'spool', 'source', 'set_task', 'write_stream'

# TODO: Get rid of this global variable
MAX_WORK = cpu_count() ** 2

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
    return (
        init + len(update)
            if isinstance(init, int) else
        init + update
    )


def write_stream(script):
    """
    :param script: Translated Text
    :type script: Iterable

    :return None:
    """
    for trans in script:

        for line in trans['sentences']:
            stdout.write(line['trans'])
        stdout.write('\n')

    return None

@coroutine
def set_task(translation_function, source, dest):
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
    translator     = partial(translation_function, source, dest)
    tasks, workers = (), ThreadPool(MAX_WORK)

    try:
        while True:
            tasks = yield
            write_stream(workers.map(translator, tasks))

    except GeneratorExit:
        workers.close()
        workers.join()

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
    Consumes text streams and spools them together for more io efficient processes.

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
