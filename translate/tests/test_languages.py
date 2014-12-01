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
    from translate import load_codes, code_map


class TestLanguages(unittest.TestCase):

    def test_load(self):
        pass

    def test_codes(self):
        pass


if __name__ == '__main__':
    unittest.main()
