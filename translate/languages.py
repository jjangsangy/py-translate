# -*- coding: utf-8 -*-

import json
from os.path import dirname, abspath, join


def load_codes(file):
    '''
    Opens up file located under the etc directory conaining language
    codes and prints them out
    '''
    filepath = abspath(join(dirname(__file__), 'etc', file))
    with open(filepath, 'rt') as data:
        return json.load(data)


def language_codes(lang):
    '''
    Prints out the language codes available.
    '''
    codes = load_codes('supported_translations.json')[lang]
    for code in codes:
        print(code['language'], '\t', code['name'])
