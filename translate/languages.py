# -*- coding: utf-8 -*-
from __future__ import print_function

import json
import operator

from os.path import dirname, abspath, join, isfile

__all__ = ['translation_table', 'print_table']


def translation_table(language, filepath='supported_translations.json'):
    '''
    Opens up file located under the etc directory containing language
    codes and prints them out.

    :param file: Path to location of json file
    :type file: str

    :return: language codes
    :rtype: dict
    '''
    fullpath = abspath(join(dirname(__file__), 'etc', filepath))

    if not isfile(fullpath):
        raise IOError('File does not exist at {0}'.format(fullpath))

    with open(fullpath, 'rt') as fp:
        raw_data = json.load(fp).get(language, None)
        assert(raw_data is not None)

    return dict((code['language'], code['name']) for code in raw_data)


def print_table(language):
    '''
    Generates a formatted table of language codes
    '''
    table = translation_table(language)

    for code, name in sorted(table.items(), key=operator.itemgetter(0)):
        print(u'{language:<8} {name:\u3000<20}'.format(
            name=name, language=code
        ))

    return None
