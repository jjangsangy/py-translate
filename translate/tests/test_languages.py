# -*- coding: utf-8 -*-
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import os
import sys

from ..languages import translation_table, print_table


class TestLanguages(unittest.TestCase):


    def test_translation_table(self):
        table = translation_table('en')
        self.assertDictEqual(
             table,
            {'af': 'Afrikaans',
             'ar': 'Arabic',
             'az': 'Azerbaijani',
             'be': 'Belarusian',
             'bg': 'Bulgarian',
             'bn': 'Bengali',
             'bs': 'Bosnian',
             'ca': 'Catalan',
             'ceb': 'Cebuano',
             'cs': 'Czech',
             'cy': 'Welsh',
             'da': 'Danish',
             'de': 'German',
             'el': 'Greek',
             'en': 'English',
             'eo': 'Esperanto',
             'es': 'Spanish',
             'et': 'Estonian',
             'eu': 'Basque',
             'fa': 'Persian',
             'fi': 'Finnish',
             'fr': 'French',
             'ga': 'Irish',
             'gl': 'Galician',
             'gu': 'Gujarati',
             'hi': 'Hindi',
             'hmn': 'Hmong',
             'hr': 'Croatian',
             'ht': 'Haitian Creole',
             'hu': 'Hungarian',
             'id': 'Indonesian',
             'is': 'Icelandic',
             'it': 'Italian',
             'iw': 'Hebrew',
             'ja': 'Japanese',
             'jw': 'Javanese',
             'ka': 'Georgian',
             'km': 'Khmer',
             'kn': 'Kannada',
             'ko': 'Korean',
             'la': 'Latin',
             'lo': 'Lao',
             'lt': 'Lithuanian',
             'lv': 'Latvian',
             'mk': 'Macedonian',
             'mr': 'Marathi',
             'ms': 'Malay',
             'mt': 'Maltese',
             'nl': 'Dutch',
             'no': 'Norwegian',
             'pl': 'Polish',
             'pt': 'Portuguese',
             'ro': 'Romanian',
             'ru': 'Russian',
             'sk': 'Slovak',
             'sl': 'Slovenian',
             'sq': 'Albanian',
             'sr': 'Serbian',
             'sv': 'Swedish',
             'sw': 'Swahili',
             'ta': 'Tamil',
             'te': 'Telugu',
             'th': 'Thai',
             'tl': 'Filipino',
             'tr': 'Turkish',
             'uk': 'Ukrainian',
             'ur': 'Urdu',
             'vi': 'Vietnamese',
             'yi': 'Yiddish',
             'zh': 'Chinese (Simplified)',
             'zh-TW': 'Chinese (Traditional)'})

    def test_codes(self):
        pass


if __name__ == '__main__':
    unittest.main()
