# -*- coding: utf-8 -*-
import json
from os.path import abspath

import requests

_language_codes = ('lt', 'bs', 'no', 'ht', 'ja', 'af', 'ur', 'hmn', 'el', 'lo',
                   'mt', 'pl', 'ko', 'th', 'la', 'sk', 'ka', 'zh', 'tr', 'cs',
                   'es', 'sv', 'vi', 'hu', 'ru', 'te', 'fa', 'bn', 'sl', 'mk',
                   'yi', 'bg', 'ro', 'iw', 'ar', 'et', 'fr', 'ca', 'ceb',
                   'zh-TW', 'eo', 'cy', 'pt', 'nl', 'ta', 'sw', 'uk', 'be',
                   'it', 'lv', 'de', 'sq', 'sr', 'km', 'fi', 'hr', 'is', 'gl',
                   'id', 'jw', 'gu', 'kn', 'eu', 'hi', 'mr', 'da', 'az', 'en',
                   'tl', 'ms', 'ga')


def get_key(secret):
    '''Retrieves API key from file.'''
    filepath = abspath(secret)
    with open(filepath, 'rt') as key:
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


def load_json(file):
    path = abspath(file)
    with open(path, 'rt') as json_file:
        data = json.load(json_file)
        return data


def main():
    codes = load_json('language_codes.json')['data']['languages']
    for code in codes:
        print(code['language'], code['name'])


if __name__ == '__main__':
    main()
