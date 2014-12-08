# -*- coding: utf-8 -*-
"""
coroutines
~~~~~~~~~~

All functions definied within this file are essentially coroutines and
therefore follow the coroutine pattern either as consumers, producers or
consumer/producers.

"""
try:
    from urllib.parse import quote
except ImportError:
    from urllib2 import quote

from sys import stdin, stdout
from functools import wraps, partial, reduce
from multiprocessing.dummy import Pool as ThreadPool

__all__ = 'coroutine', 'chunk', 'spool', 'source', 'set_task', 'write_stream'

# TODO: Get rid of this global variable
MAX_WORK = 10

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


def write_stream(script):
    """
    :param script: Translated Text
    :type script: Iterable

    :return None:
    """

    list(map(stdout.write,
        (lines['trans'] for trans in script for lines in trans['sentences'])
    ))

    stdout.write('\n')


@coroutine
def set_task(translation_function, source, dest):
    """
    Task Setter Coroutine

    :param translation_function: Translator
    :type translation_function: Function

    :param source: Source Language Code
    :type source: String

    :param dest: Destination Language Code
    :type dest: String
    """
    tasks       = []
    workers     = ThreadPool(MAX_WORK)
    interpreter = partial(translation_function, source, dest)

    try:
        while True:
            tasks = yield
            write_stream(workers.map(interpreter, tasks))

    except GeneratorExit:
        write_stream(workers.map(interpreter, tasks))
        workers.close(); workers.join()

@coroutine
def chunk(task):
    """
    Chunk text into a queue and send by copy to a task setter coroutine.
    Once a queue has been built it is sent by copy and then destroyed.

    :param task: Task setter
    :type task: Coroutine
    """
    task_queue = []

    try:
        while True:

            while len(task_queue) < MAX_WORK:
                line = yield
                task_queue.append(line)

            task.send(task_queue)
            task_queue = []

    except GeneratorExit:
        task.send(task_queue)
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
    words = 0
    spool = ''

    try:
        while True:

            while words < maxlen:
                stream = yield
                spool += stream
                words += len(quote(stream).encode('utf-8'))

            iterable.send(spool)
            words = 0
            spool = str()

    except GeneratorExit:
        iterable.send(spool)
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
