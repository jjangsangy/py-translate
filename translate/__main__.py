# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

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
    # Argument Parser
    parser = ArgumentParser(description=description)

    # Version
    parser.add_argument(
        '--version',
        action='version',
        version="%s v%s" % (
            'translate',
            ''.join([__version__, __build__])))

    # Source Language
    parser.add_argument('source', help='Source language to convert from',
                        nargs='?', default='en')

    # Destination Language
    parser.add_argument('dest', help='Destination language to convert into')

    # Parse Args
    args = parser.parse_args()

    # Run Main
    source(spooler(text_sink(args.source, args.dest)))

if __name__ == '__main__':
    sys.exit(main())
