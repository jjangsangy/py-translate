# -*- coding: utf-8 -*-
"""
coroutines
~~~~~~~~~~

"""
try:
    from urllib.parse import quote
except ImportError:
    from urllib2 import quote

from sys import stdin, stdout
from multiprocessing.dummy import Pool as ThreadPool
from functools import wraps, partial

__all__ = 'coroutine', 'chunk', 'spool', 'source', 'set_task', 'write_stream'

# TODO: Get rid of this global variable
MAX_WORK = 10

def coroutine(func):
    """
    Initializes coroutine by calling it's next method. Used in a decorator fashion over functions that
    generate coroutines.

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
    for trans in script:

        for line in trans['sentences']:
            stdout.write(line['trans'])

        stdout.write('\n')

    return None


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
    pool, tasks = ThreadPool(MAX_WORK), []
    interpreter = partial(translation_function, source, dest)

    try:
        while True:
            tasks = yield
            write_stream(pool.map(interpreter, tasks))

    except GeneratorExit:
        write_stream(pool.map(interpreter, tasks))
        pool.close(); pool.join()

@coroutine
def chunk(task):
    """
    Chunk text into a queue and send by copy to a task setter coroutine.
    Once a queue has been built it is sent by copy and then destroyed.

    :param task: Task setter
    :type task: Coroutine
    """
    task_queue = list()

    try:
        while True:

            while len(task_queue) < MAX_WORK:
                line = yield
                task_queue.append(line)
            task.send(task_queue)
            task_queue = list()

    except GeneratorExit:
        task.send(task_queue)
        task.close()


@coroutine
def spool(iterable, maxsize=1500):
    """
    Consumes text streams and spools them together for more io efficient processes.

    :param iterable: Sends text stream for further processing
    :type iterable: Coroutine
    """
    wordcount = 0
    spool     = str()

    try:
        while True:

            while wordcount < maxsize:
                stream = (yield)
                spool += stream
                wordcount += len(quote(stream).encode('utf-8'))

            iterable.send(spool)
            wordcount = 0
            spool     = str()

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
