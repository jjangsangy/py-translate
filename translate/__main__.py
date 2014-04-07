# -*- coding: utf-8 -*-
import sys
from argparse import ArgumentParser

from .__version__ import __version__, __build__
from .translator import (text_sink, spooler, source)

__all__ = []

description = '''A simple command line utility for translating text
    using Google Translate.'''


def main():
    '''
    Main Entry point for translator and argument parser
    '''
    version = ''.join([__version__, __build__])

    # Argument Parser
    parser = ArgumentParser(prog='translate', description=description)

    # Version
    parser.add_argument(
        '-v', '--version', action='version',
        version="%s v%s" % ('translate', version))

    # Languages
    parser.add_argument(
        '-l', '--languages',
        nargs='?',
        default=False,
        const='en',
        metavar='lang',
        help='List out available languages codes')

    # Parse Languages
    langs = parser.parse_known_args()
    if langs[0].languages:
        from .languages import language_codes
        language_codes(langs[0].languages)
        sys.exit(0)


    # Source Language
    parser.add_argument(
        'source',
        help='Source language code',
        nargs='?',
        default='en')

    # Destination Language
    parser.add_argument(
        'dest',
        help='Destination language code')

    args = parser.parse_args()
    print(args)

    source(spooler(text_sink(args.source, args.dest)))

if __name__ == '__main__':
    sys.exit(main())
