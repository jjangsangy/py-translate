# -*- coding: utf-8 -*-

import json
from os.path import dirname, abspath, join

__all__ = ['load_codes', 'language_codes']


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
    Prints out formatted language code pair for requested language.
    '''
    table = {}
    codes = load_codes('supported_translations.json')[lang]
    for code in codes:
        table[code['name']] = code['language']
        print(
            '{language:<8} {name:\u3000<20}'.format(
                name=code['name'],
                language=code['language'])
        )
    return table
