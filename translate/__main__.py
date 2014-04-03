# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import sys
from argparse import ArgumentParser
from functools import wraps

from .__version__ import __version__, __build__
from .translator import translator

description = '''A simple command line utility for translating text
    using Google Translate.'''


def coroutine(func):
    '''Coroutine decorator primes first call to next'''
    @wraps(func)
    def initialization(*args, **kwargs):
        start = func(*args, **kwargs)
        try:
            start.__next__()
        except AttributeError:
            start.next()
        return start
    return initialization


@coroutine
def text_sink(source, dest):
    '''Coroutine end-point. Outputs text stream into translator'''
    while True:
        line = (yield)
        translation = translator(source, dest, line)['sentences']
        for line in translation:
            print(line['trans'], end='')


# Make less http requests by chunking.
# Google maxes chunks sizes around 2k characters
@coroutine
def spooler(iterable):
    '''Consumes text stream and spools into larger chunk for processing'''
    try:
        while True:
            wordcount, spool = 0, str()
            while wordcount < 1000:
                stream = (yield)
                spool += stream
                wordcount += len(stream)
            else:
                iterable.send(spool)
    finally:
        iterable.send(spool)
        sys.stdout.write('\n')


def source(target):
    '''Coroutine start point. Produces text stream and forwards to consumers'''
    for line in sys.stdin:
        target.send(line)
    target.close()


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
            ''.join(
                [
                    __version__,
                    __build__
                ]
                )
            )
        )

    # Source Language
    parser.add_argument(
        'source',
        help='''
            Source language to convert from
            ''',
        nargs='?',
        default='en'
        )

    # Destination Language
    parser.add_argument(
        'dest',
        help='''
            Destination language to convert into
            '''
        )

    # Parse Args
    args = parser.parse_args()

    # Run Main
    source(spooler(text_sink(args.source, args.dest)))

if __name__ == '__main__':
    sys.exit(main())
