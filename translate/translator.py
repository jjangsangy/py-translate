# -*- coding: utf-8 -*-
"""
translator
~~~~~~~~~~

Defines the interaction with the translation service.
Since the program interfaces with the google web service, this
module deals with the client side logic of pushing the translation request
to the the server.
"""

import json
import functools

try:
    from urllib.request import urlopen, Request, quote
    from urllib.parse import urlencode

except ImportError:
    from urllib2 import urlopen, Request, quote
    from urllib import urlencode

from .__version__ import __version__ as version
from .__version__ import __build__ as build


__all__ = 'push_url', 'translator'

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

    @functools.wraps(site)
    def connection(*args, **kwargs):

        req_stream = str()
        req        = None

        agent   = 'py-translate v{version} {build}'.format(**globals())
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
