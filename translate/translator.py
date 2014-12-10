# -*- coding: utf-8 -*-
"""
translator
~~~~~~~~~~

Defines the interaction with the translation service.
Since the program interfaces with the google web service, this
module deals with the client side logic of pushing the translation request
to the the server.
"""

import functools

from requests.adapters import HTTPAdapter
from requests import Session, Request, codes

__all__ = 'push_url', 'translator'

def push_url(request):
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

    @functools.wraps(request)
    def connection(*args, **kwargs):
        """
        Inner function that makes the http connection.
        """
        content  = dict()
        sess     = Session()

        sess.mount('http://',  HTTPAdapter(max_retries=2))
        sess.mount('https://', HTTPAdapter(max_retries=2))

        prepare  = sess.prepare_request(request(*args, **kwargs))
        response = sess.send(prepare, timeout=(3.05, 5), verify=True)

        if response.status_code != codes.ok:
            response.raise_for_status()

        return response.json()

    return connection


@push_url
def translator(source, target, phrase, version='0.0 test', charset='utf-8'):
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

    :return: Request Object
    :rtype: Request
    """

    base    = 'https://translate.google.com/translate_a/t'
    agent   = 'py-translate v{}'.format(version)

    headers = {'User-Agent': agent,
               'Content-Type': 'application/json; charset={}'.format(charset)}

    params  = {'client': 'webapp', 'ie': 'utf-8', 'oe': 'utf-8',
                   'sl':   source, 'tl':  target,  'q': phrase, }

    return Request('GET', url=base, params=params, headers=headers)
