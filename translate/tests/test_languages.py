# -*- coding: utf-8 -*-
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import os
import sys

from nose.tools import *

sys.path.insert(0, os.path.abspath('..'))

from ..languages import translation_table, print_table



class TestLanguages(unittest.TestCase):

    def test_load(self):
        pass

    def test_codes(self):
        pass


if __name__ == '__main__':
    unittest.main()
