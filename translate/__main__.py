# -*- coding: utf-8 -*-
"""
Copyright: Sang Han 2014

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
from argparse import ArgumentParser

from .__version__ import __version__, __build__
from .translator import chunk, spool, source, set_task
from .languages import print_table, translation_table

__all__ = []

def command_line():

    description = 'A simple command line utility for translating text using Google Translate.'
    epilog      = ' '.join(sorted(translation_table('en').keys()))
    version     = ' '.join([__version__, __build__])

    codes = ArgumentParser(add_help=False)
    codes.add_argument(
        '-l',
        nargs='?',
        default=False,
        const='en',
        metavar='code',
        dest='code',
        help='Enumerate the name of country and language code pair. Optionally specify output language'
    )

    language,_ = codes.parse_known_args()
    if language.code:
        print_table(language.code)
        sys.exit(0)

    # Main Parser
    parser = ArgumentParser(
        parents=[codes],
        prog='translate',
        description=description,
        epilog=epilog
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version="%s v%s" % ('translate', version)
    )

    # Source and Target Language
    parser.add_argument(
        'source',
        help='Source language code',
    )
    parser.add_argument(
        'dest',
        help='Destination language code'
    )

    return parser.parse_args()


def main():
    '''
    Main Entry point for translator and argument parser
    '''
    args = command_line()
    source(spool(chunk(set_task(args.source, args.dest))))

    return

if __name__ == '__main__':
    sys.exit(main())
