try:
    import unittest2 as unittest
except ImportError:
    import unittest

from nose.tools import *
from translate import translator


class TestTranslator(unittest.TestCase):

    def typeassert(self):
        instance = translator('en', 'en', str())
        self.assertIsInstance(instance, dict)
        self.assertIsInstance(instance['sentences'], list)
        self.assertIsInstance(instance['sentences'][0], dict)
        self.assertIsInstance(instance['sentences'][0]['trans'], str)

    def test_love(self):
        love = translator('en', 'zh-TW', 'I love you')
        self.assertEqual(love['sentences'][0]['trans'], '我愛你')

if __name__ == '__main__':
    unittest.main()
