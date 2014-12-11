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

import operator

from sys import stdin, stdout
from functools import wraps, partial, reduce
from collections import deque
from multiprocessing import cpu_count, Queue
from multiprocessing.dummy import Pool as ThreadPool

from concurrent.futures import ThreadPoolExecutor

__all__ = 'coroutine', 'spool', 'source', 'set_task', 'write_stream'

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

def write_stream(script, output='trans'):
    """
    :param script: Translated Text
    :type script: Iterable

    :return None:
    """
    for line in script['sentences']:

        if line.get(output, None):
            stdout.write(line[output])

    stdout.write('\n')


# TODO: Get rid of all this context crap
@coroutine
def set_task(translator, translit=False):
    """
    Task Setter Coroutine

    End point destination coroutine of a purely consumer type.
    Delegates Text IO to the `write_stream` function.

    :param translation_function: Translator
    :type translation_function: Function

    :param translit: Transliteration Switch
    :type: Bool
    """
    # Initialize Task Queue
    task    = str()
    queue   = deque()

    # Callable Objects
    first   = operator.itemgetter(0)
    done    = operator.methodcaller('done')
    result  = operator.methodcaller('result')

    # Function Partial
    output  = ('translit' if translit else 'trans')
    stream  = partial(write_stream, output=output)

    # Worker Thread Pool
    maxwork = cpu_count() * 32
    workers = ThreadPoolExecutor(maxwork)

    try:
        while True:

            task = yield
            queue.append(workers.submit(translator, task))

            while queue and done(first(queue)):
                stream(result(queue.pop()))

    except GeneratorExit:
        workers.shutdown(wait=True)
        list(map(stream,(map(result,queue))))

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

    for line in stdin:
        target.send(line)

    return target.close()
