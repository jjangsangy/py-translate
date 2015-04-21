# -*- coding: utf-8 -*-
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import os
import sys

from ..translator import translator

class TestTranslator(unittest.TestCase):

    def test_love(self):
        love = translator('en', 'zh-TW', 'I love you')[0].pop()
        self.assertTrue(love)


if __name__ == '__main__':
    unittest.main()
