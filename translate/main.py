#!/usr/bin/env python3
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

try:
    from urllib.request import quote, build_opener, urlopen, Request
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import quote, build_opener, urlopen, Request
    from urllib import urlencode



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


def push_url(site):
    'Decorator for functions that return complete urls for HTTP request.'
    @wraps(site)
    def connection(*args, **kwargs):
        # Declare the header and create the Request object.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:27.0) Gecko/20100101 Firefox/27.0'}
        url = site(*args, **kwargs)
        request = Request(url, headers=headers)
        # Make HTTP Request
        req = urlopen(request)
        req_stream = req.read().decode('UTF-8')
        req.close()
        return json.loads(req_stream)

    return connection


@push_url
def translator(source, target, phrase):
    'Assembles the URL for the GET request'
    base = 'http://translate.google.com/translate_a/t'
    params = urlencode({
            'client': 'webapp',
            'ie': 'UTF-8',
            'oe': 'UTF-8',
            'sl': source,
            'tl': target,
            'q': phrase
        })
    url = '?'.join([base, params])
    return url


def main():
    '''
    Main Entry point for translator
    '''
    parser = ArgumentParser(
        description='''
            GTranslate is a CLI Tool for Google Translate written in Python! ''')
    parser.add_argument('-V', '--version',
                        action='version',
                        version="%s v%s" %('translate', '0.0.0'))
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
