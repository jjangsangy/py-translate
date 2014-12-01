# -*- coding: utf-8 -*-
import sys
from argparse import ArgumentParser

from .__version__ import __version__, __build__
from .translator import (text_sink, spooler, source)

__all__ = []

description = '''A simple command line utility for translating text
    using Google Translate.'''

epilog = '''If only 1 positional argument is specified, it will be assumed
    to be dest and source will default to english.'''


def main():
    '''
    Main Entry point for translator and argument parser
    '''
    version = ''.join([__version__, __build__])

    # Language Code Parser
    langs = ArgumentParser(add_help=False)

    # Languages
    langs.add_argument(
        '-l', '--languages',
        nargs='?',
        default=False,
        const='en',
        metavar='code',
        help='List out available languages codes')

    codes = langs.parse_known_args()

    # Parse Languages
    if codes[0].languages:
        from .languages import print_table
        print_table(codes[0].languages)
        sys.exit(0)

    # Argument Parser
    parser = ArgumentParser(
        parents=[langs],
        prog='translate',
        description=description,
        epilog=epilog)

    # Version
    parser.add_argument(
        '-v', '--version', action='version',
        version="%s v%s" % ('translate', version))

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

    source(spooler(text_sink(args.source, args.dest)))

if __name__ == '__main__':
    sys.exit(main())
