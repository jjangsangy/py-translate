# -*- coding: utf-8 -*-
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import os
import sys
from nose.tools import *

sys.path.insert(0, os.path.abspath('..'))

try:
    from languages import load_codes, language_codes
except ImportError:
    from translate import load_codes, language_codes

class TestLanguages(unittest.TestCase):

    def test_load(self):
        codes = load_codes('supported_translations.json')
        self.assertIsInstance(codes, dict)
        self.assertIsInstance(codes['ko'], list)

        ko_codes = {}
        for code in codes['ko']:
            ko_codes[code['language']] = code['name']

        self.assertEqual(ko_codes.get('en'), u'영어')

    def test_codes(self):
        table = language_codes('ko')
        self.assertEqual(table['en'], u'영어')


if __name__ == '__main__':
    unittest.main()
