# -*- coding: utf-8 -*-
'''
translator
~~~~~~~~~~

Definies the interaction with the translation service.
Since the program interfaces with the google web service, this
module deals with the client side logic of pushing the translation request
to the the server.
'''

import json
from functools import wraps

try:
    from urllib.request import quote, build_opener, urlopen, Request
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import quote, build_opener, urlopen, Request
    from urllib import urlencode


def push_url(site):
    '''
    Decorator that wraps the translator method and performs the GET HTTP request.

    Returns a dict response object from the server containing the translated
    text and metadata of the request body
    '''
    @wraps(site)
    def connection(*args, **kwargs):
        # Declare the header and create the Request object.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:27.0) Gecko/20100101 Firefox/27.0'}
        url = site(*args, **kwargs)
        request = Request(url, headers=headers)
        # Make HTTP Request
        req = urlopen(request)
        req_stream = req.read().decode('UTF-8')
        req.close()
        return json.loads(req_stream)

    return connection


@push_url
def translator(source, target, phrase):
    '''
    Returns the url encoded string that will be pushed to the translation
    server for parsing.

    :param source: Language code for translation source
    :param target: Language code that source will be translate into
    :param phrase: Text body string that will be url encoded and translated

    List of acceptable language codes for source and target languages
    can be found as a JSON file in the etc directory.

    Some source languages are limited in scope of the possible target languages
    that are available.

    .. code-block:: python
        :emphasize-lines: 3

        >>> import translate
        >>> translator('en', 'zh-TW', 'Hello World!')
            '你好世界！'

    '''
    base = 'http://translate.google.com/translate_a/t'
    params = urlencode({
            'client': 'webapp',
            'ie': 'UTF-8',
            'oe': 'UTF-8',
            'sl': source,
            'tl': target,
            'q': phrase
        })
    url = '?'.join([base, params])
    return url
