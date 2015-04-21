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

import sys
import operator

from functools import wraps, partial, reduce
from concurrent.futures import ThreadPoolExecutor

__all__ = ['coroutine', 'spool', 'source', 'set_task', 'write_stream', 'accumulator']


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

    .. code-block:: python

        # Simplest Form
        >>> a = 'this' + ' '
        >>> b = 'that'
        >>> c = functools.reduce(accumulator, a, b)
        >>> c
        'this that'

        # The type of the initial value determines output type.
        >>> a = 5
        >>> b = Hello
        >>> c = functools.reduce(accumulator, a, b)
        >>> c
        10

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

    :param output: Output Type (either 'trans' or 'translit')
    :type output: String
    """
    first    = operator.itemgetter(0)
    sentence, _ = script
    printer  = partial(print, file=sys.stdout, end='')

    for line in sentence:
        if isinstance(first(line), str):
            printer(first(line))
        else:
            printer(first(line).encode('UTF-8'))

    printer('\n')

    return sys.stdout.flush()



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
    :type translit: Boolean
    """
    # Initialize Task Queue
    task    = str()
    queue   = list()

    # Function Partial
    output  = ('translit' if translit else 'trans')
    stream  = partial(write_stream, output=output)
    workers = ThreadPoolExecutor(max_workers=8)

    try:
        while True:

            task = yield
            queue.append(task)

    except GeneratorExit:
        list(map(stream, workers.map(translator, queue)))

@coroutine
def spool(iterable, maxlen=1250):
    """
    Consumes text streams and spools them together for more io
    efficient processes.

    :param iterable: Sends text stream for further processing
    :type iterable: Coroutine

    :param maxlen: Maximum query string size
    :type maxlen: Integer
    """
    words = int()
    text  = str()

    try:
        while True:

            while words < maxlen:
                stream = yield
                text   = reduce(accumulator, stream, text)
                words  = reduce(accumulator, stream, words)

            iterable.send(text)
            words = int()
            text  = str()

    except GeneratorExit:
        iterable.send(text)
        iterable.close()


def source(target, inputstream=sys.stdin):
    """
    Coroutine starting point. Produces text stream and forwards to consumers

    :param target: Target coroutine consumer
    :type target: Coroutine

    :param inputstream: Input Source
    :type inputstream: BufferedTextIO Object
    """
    for line in inputstream:

        while len(line) > 600:
            init, sep, line = line.partition(' ')
            assert len(init) <= 600
            target.send(''.join([init, sep]))

        target.send(line)

    inputstream.close()

    return target.close()
