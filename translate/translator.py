# -*- coding: utf-8 -*-
"""
translator
~~~~~~~~~~

Defines the interaction with the translation service.
Since the program interfaces with the google web service, this
module deals with the client side logic of pushing the translation request
to the the server.
"""

from __future__ import print_function, unicode_literals

import sys
import json
from functools import wraps

try:
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import urlopen, Request
    from urllib import urlencode

__all__ = [
    'push_url',
    'translator',
    'coroutine',
    'text_sink',
    'spooler',
    'source'
]


def push_url(site):
    '''
    Decorator that wraps the translator method and performs
    the GET HTTP request.

    Returns a dict response object from the server containing the translated
    text and metadata of the request body
    '''

    @wraps(site)
    def connection(*args, **kwargs):
        agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:27.0) Gecko/20100101 Firefox/27.0'
        headers = {'User-Agent': agent}
        url = site(*args, **kwargs)
        request = Request(url, headers=headers)

        # Make HTTP Request
        req = urlopen(request)
        req_stream = req.read().decode('utf-8')
        req.close()
        return json.loads(req_stream)

    return connection


@push_url
def translator(source, target, phrase):
    """
    Returns the url encoded string that will be pushed to the translation
    server for parsing.

    :param source: Language code for translation source
    :type source: str
    :param target: Language code that source will be translate into
    :type target: str
    :param phrase: Text body string that will be url encoded and translated
    :type phrase: str
    :returns: url
    :rtype: str

    List of acceptable language codes for source and target languages
    can be found as a JSON file in the etc directory.

    Some source languages are limited in scope of the possible target languages
    that are available.

    .. code-block:: python

        >>> import translate
        >>> translator('en', 'zh-TW', 'Hello World!')
            '你好世界！'

    """
    base = 'http://translate.google.com/translate_a/t'
    params = urlencode({
        'client': 'webapp',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'sl': source,
        'tl': target,
        'q': phrase
    })
    url = '?'.join([base, params])
    return url


def coroutine(func):
    """Coroutine decorator primes first call to next"""

    @wraps(func)
    def initialization(*args, **kwargs):
        start = func(*args, **kwargs)
        try:
            start.__next__()
        except AttributeError:
            start.next()
        return start

    return initialization


@coroutine
def text_sink(source, dest):
    """Coroutine end-point. Outputs text stream into translator"""
    while True:
        line = (yield)
        translation = translator(source, dest, line)['sentences']
        for line in translation:
            print(line['trans'].encode('utf-8').decode('utf-8'), end='')


# Make less http requests by chunking.
# Google maxes chunks sizes around 2k characters
@coroutine
def spooler(iterable):
    """Consumes text stream and spools into larger chunk for processing"""
    try:
        while True:
            wordcount, spool = 0, str()
            while wordcount < 200:
                stream = (yield)
                spool += stream
                wordcount += len(stream)
            else:
                iterable.send(spool)
    finally:
        iterable.send(spool)
        sys.stdout.write('\n')


def source(target):
    """Coroutine start point. Produces text stream and forwards to consumers"""
    stripper = (
        '{}'.format(
            line.replace(r'\n', r' ').\
                 replace(r'\t', r' ').\
                 replace(r'\r', r' ')
        )
        for line in sys.stdin:
            for strip in stripper:
                target.send(strip)
    target.close()
