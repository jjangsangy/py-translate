# -*- coding: utf-8 -*-
"""
translator
~~~~~~~~~~

Defines the interaction with the translation service.
Since the program interfaces with the google web service, this
module deals with the client side logic of pushing the translation request
to the the server.
"""

import sys
import json

from multiprocessing.dummy import Pool as ThreadPool
from functools import wraps, partial

try:
    from urllib.request import urlopen, Request, quote
    from urllib.parse import urlencode

except ImportError:
    from urllib2 import urlopen, Request, quote
    from urllib import urlencode

__all__ = ['push_url', 'translator', 'coroutine', 'chunk', 'spool', 'source', 'set_task', 'write_stream']

# TODO: Get rid of this global variable
MAX_WORK = 10

def push_url(site):
    '''
    Decorates a function returning the url of translation API.
    Creates and maintains HTTP connection state

    Returns a dict response object from the server containing the translated
    text and metadata of the request body

    :param site: translator
    :type site: Function

    :return: HTTP Response
    :rtype: Function
    '''

    @wraps(site)
    def connection(*args, **kwargs):

        req_stream = str()
        req        = None

        agent   = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:27.0) Gecko/20100101 Firefox/27.0'
        headers = {'User-Agent': agent}
        url     = site(*args, **kwargs)
        request = Request(url, headers=headers)

        try:
            req        = urlopen(request)
            req_stream = req.read()
            req_stream = req_stream.decode('utf-8')

        finally:
            req.close()

        return json.loads(req_stream)

    return connection


@push_url
def translator(source, target, phrase):
    """
    Returns the url encoded string that will be pushed to the translation
    server for parsing.

    List of acceptable language codes for source and target languages
    can be found as a JSON file in the etc directory.

    Some source languages are limited in scope of the possible target languages
    that are available.

    .. code-block:: python

        >>> from translate import translator
        >>> translator('en', 'zh-TW', 'Hello World!')
            '你好世界！'

    :param source: Language code for translation source
    :type source: String

    :param target: Language code that source will be translate into
    :type target: String

    :param phrase: Text body string that will be url encoded and translated
    :type phrase: String

    :return: url
    :rtype: String
    """
    base   = 'http://translate.google.com/translate_a/t'
    params = urlencode(
        {
        'client': 'webapp',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'sl': source,
            'tl': target,
             'q': phrase,
        }
    )
    url    = '?'.join([base, params])

    return url


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
        try:
            start.__next__()

        except AttributeError:
            start.next()

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
            sys.stdout.write(line['trans'])

        sys.stdout.write('\n')

    return None


@coroutine
def set_task(source, dest):
    """
    Task Setter Coroutine

    :param source: Source Language Code
    :type source: String

    :param dest: Destination Language Code
    :type dest: String
    """
    pool, tasks = ThreadPool(MAX_WORK), []
    interpreter = partial(translator, source, dest)

    try:
        while True:
            tasks = (yield)
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
                line = (yield)
                task_queue.append(line)
            task.send(task_queue)
            task_queue = list()

    except GeneratorExit:
        task.send(task_queue)
        task.close()


@coroutine
def spool(iterable):
    """
    Consumes text streams and spools them together for more io efficient processes.

    :param iterable: Sends text stream for further processing
    :type iterable: Coroutine
    """
    wordcount = 0
    spool     = str()

    try:
        while True:

            # Wind up Spool
            while wordcount < 1500:
                stream = (yield)
                spool += stream
                wordcount += len(quote(stream).encode('utf-8'))

            else:
                iterable.send(spool)

            # Rewind Spool
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

    if sys.stdin.isatty():
        # target.send(args.file)
        return

    for line in sys.stdin:
        target.send(line)

    target.close()
