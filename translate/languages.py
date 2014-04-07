# -*- coding: utf-8 -*-

import json
from os.path import dirname, abspath, join


def load_languages(file):
    '''
    Opens up file located under the etc directory conaining language
    codes and prints them out
    '''
    filepath = abspath(join(dirname(__file__), 'etc', file))
    with open(filepath, 'rt') as data:
        return json.load(data)['data']['languages']


def language_codes():
    '''
    Prints out the language codes available.
    '''
    codes = load_languages('language_codes.json')
    for code in codes:
        print(code['language'], '\t', code['name'])
