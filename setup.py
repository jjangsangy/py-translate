# -*- coding: utf-8 -*-
"""
py-translate
============
A simple translation command line utility

:copyright: (c) 2014 Sang Han
"""
from translate import __version__, __license__
from setuptools import setup

setup(
    name='py-translate',
    description=(
        'A simple translation command line utility'
    ),
    long_description='\n'.join(
        [
            open('README.rst').read(),
            open('HISTORY.rst').read(),
        ]
    ),
    author='Sang Han',
    license=__license__,
    url='https://github.com/jjangsangy/py-translate',
    author_email='jjangsangy@gmail.com',
    include_package_data=True,
    packages=['translate'],
    version=__version__,
    install_requires=['argparse'],
    tests_require=['nose'],
    zip_safe=False,
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
