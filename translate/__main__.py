# -*- coding: utf-8 -*-
'''
Small command line utility for translating text streams
using Google Translate v2 API.
'''
from __future__ import print_function, unicode_literals

import json
import sys
from argparse import ArgumentParser
from functools import wraps

from .__version__ import __version__, __build__
from .translator import push_url, translator

def coroutine(func):
    '''Coroutine decorator primes first call to next'''
    @wraps(func)
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        try:
            cr.__next__()
        except AttributeError:
            cr.next()
        return cr
    return start


@coroutine
def text_sink(source, dest):
    '''Coroutine end-point. Outputs text stream into translator'''
    while True:
        line = (yield)
        # Placeholder
        translation = translator(source, dest, line)['sentences']
        for line in translation:
            print(line['trans'], end='')

# Make less http requests by chunking. Google maxes chunks around 2k
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
    Main Entry point for translator
    '''
    parser = ArgumentParser(
        description='''
            GTranslate is a CLI Tool for Google Translate written in Python! ''')
    parser.add_argument('-V', '--version',
                        action='version',
                        version="%s v%s" %(__package__, ''.join([__version__, __package__])))
    parser.add_argument('source',
                        help='''Source language to convert from''',
                        nargs='?',
                        default='en')
    parser.add_argument('dest',
                        help='''Destination language to convert into''')
    args = parser.parse_args()

    source(spooler(text_sink(args.source, args.dest)))

if __name__ == '__main__':
    sys.exit(main())
