# -*- coding: utf-8 -*-
import translate

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(path):
    '''Build a file path from *paths* and return the contents.'''
    with open(path) as f:
        return f.read()


description = '''A simple command line utility for translating text
    using Google Translate.'''
long_description = '\n\n'.join(
    [
        read('README.rst'),
        read('HISTORY.rst')
    ])

setup(
    name='py-translate',
    description=description,
    long_description=long_description,
    author='Sang Han',
    license=translate.__license__,
    url='https://github.com/jjangsangy/GTranslate',
    download_url='https://github.com/jjangsangy/GTranslate.git',
    author_email='jjangsangy@gmail.com',
    include_package_data=True,
    packages=['translate'],
    version=translate.__version__,
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            'translate = translate.__main__:main'
            ]
        },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Unix Shell',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
    ],
)
