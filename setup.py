# -*- coding: utf-8 -*-
import translate

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name=translate.__title__,
    description=readme,
    author=translate.__author__,
    license=translate.__license__,
    url='https://github.com/jjangsangy/GTranslate',
    download_url='https://github.com/jjangsangy/GTranslate.git',
    author_email='jjangsangy@gmail.com',
    version=translate.__version__,
    tests_require=['nose'],
    packages=['translate'],
    entry_points={
        'console_scripts': [
            'translate = translate.main:main'
            ]
        },
)
