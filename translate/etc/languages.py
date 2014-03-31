# -*- coding: utf-8 -*-
import sys
import os
import json
from functools import wraps

import requests

_language_codes = ('lt', 'bs', 'no', 'ht', 'ja', 'af', 'ur', 'hmn', 'el', 'lo',
                   'mt', 'pl', 'ko', 'th', 'la', 'sk', 'ka', 'zh', 'tr', 'cs',
                   'es', 'sv', 'vi', 'hu', 'ru', 'te', 'fa', 'bn', 'sl', 'mk',
                   'yi', 'bg', 'ro', 'iw', 'ar', 'et', 'fr', 'ca', 'ceb',
                'zh-TW', 'eo', 'cy', 'pt', 'nl', 'ta', 'sw', 'uk', 'be', 'it',
                   'lv', 'de', 'sq', 'sr', 'km', 'fi', 'hr', 'is', 'gl', 'id',
                   'jw', 'gu', 'kn', 'eu', 'hi', 'mr', 'da', 'az', 'en', 'tl',
                   'ms', 'ga')

def get_key(secret):
    '''Retrieves API key from file.'''
    with open(secret, 'rt') as key:
        api_key = key.readlines()
    return api_key

# Need to make API Request in order to validate that languages are supported
def discover_languages(target):
    base = 'https://www.googleapis.com/language/translate/v2/languages'
    key = get_key('secret.key')
    params = {
        'key': key,
        'target': target
        }
    return requests.get(base, params=params).json(encoding='ascii')

def main():
    language_reference = 'supported_translations.json'
    if os.path.isfile(language_reference):
        os.remove(language_reference)

    supported = dict()
    for code in _language_codes:
        supported[code] = discover_languages(code)['data']['languages']
    # Do not generate escaped ascii unicode
    with open(language_reference,'w') as languages:
        json.dump(supported, languages, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
