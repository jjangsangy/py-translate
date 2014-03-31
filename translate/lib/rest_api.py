# -*- coding: utf-8 -*-
'''
This module has been depreciated.

Althought Google Translate does offer a RESTful API service,
the current model requires a Developers account  on a pay per use
basis and exposes application logic to handle
authentication using Public API keys.
The current revision of this script will query and
parse the translate webapp for free (in reasonable use cases)
using the urllib module implemented from Python 3.4.
This overall simplifies dependencies and considerably
improves the install process.
'''

import json
from functools import wraps
from os.path import join, abspath

try:
    import requests
except ImportError:
    from sys import stderr, exit
    stderr.write('Failed to import request module')
    exit(1)

def language_decorator(response):
    @wraps(response)
    def wrapper(*args, **kwargs):
        return response(*args, **kwargs).json()
    return wrapper

@language_decorator
def discover_languages(target=None):
    ''' Returns a list of languages codes supported by the API.
    A target language parameter can optionally be set to specify output'''
    base = 'https://www.googleapis.com/language/translate/v2/languages'
    key = api_key('translate_api.key')
    params = {
        'key': key,
        'target': target
        }
    return requests.get(base, params=params)

def post_request(target, source, *content):
    base = 'https://www.googleapis.com/language/translate/v2'
    key = api_key('translate_api.key')
    params = {
        'key': key,
        'format': 'text',
        'prettyprint': 'true',
        'source': source,
        'target': target,
        'q': content
    }
    headers = {'X-HTTP-Method-Override': 'GET'}
    return requests.post(base, params=params, headers=headers)

def request_config(mod):
    '''Loads configuration file'''
    filepath = abspath(join('static', 'config.json'))
    with open(filepath, 'rt') as configuration:
        config = json.load(configuration)[mod]
    return config

def get_key(secret):
    '''Retrieves API key from file.'''
    secret = abspath(join('..', 'etc', 'secret.key'))
    with open(secret, 'rt') as key:
        api_key = key.readlines()
    return api_key

