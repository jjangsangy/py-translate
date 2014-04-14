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
    Returns a dict corresponding to the language codes available for source lang
    '''
    table = {}
    codes = load_codes('supported_translations.json')[lang]
    for code in codes:
        table[code['language']] = code['name']
    return table

def print_table(lang):
    '''
    Generates a formatted table of language codes
    '''
    table = {}
    codes = load_codes('supported_translations.json')[lang]
    for code in codes:
        print(
            '{language:<8} {name:\u3000<20}'.format(
                name=code['name'],
                language=code['language'])
        )
    return
