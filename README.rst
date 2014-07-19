py-translate
=============

.. image:: https://travis-ci.org/jjangsangy/py-translate.svg?branch=master
    :target: https://travis-ci.org/jjangsangy/py-translate

.. image:: https://badge.fury.io/gh/jjangsangy%2Fpy-translate.svg
    :target: http://badge.fury.io/gh/jjangsangy%2Fpy-translate

.. image:: https://badge.fury.io/py/py-translate.svg
    :target: http://badge.fury.io/py/py-translate

py-translate is a CLI Tool for Google Translate written in Python!

.. image:: img/alice.gif
    :alt: alice
    :align: center

:Author: Sang Han, 2014
:License: Apache Software License v2
:Version: 0.1.5

The end goal is a simple application for translating text in the terminal.
Text can be generated interactively or programmatically
in the shell enviornment. Through command line arguments,
file descriptors or pipes generating translated output
that can be piped to a file or displayed on the terminal.

Features
---------
- Simple command line parsing!
- Written in pure Python!
- Backwards compatable with Python 2.7
- Supports for PyPy as target implementation
- Supports all language from Google Translate API
- The power of Unix pipes and filters
- Native UTF-8 Support

Installation
------------

From PyPI with pip (easy)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ pip install py-translate


From Source at Github
~~~~~~~~~~~~~~~~~~~~~

* Clone the repository

.. code-block:: bash

    $ git clone https://github.com/jjangsangy/py-translate.git

* Install with setup.py

.. code-block:: bash

    $ python setup.py install

Usage
-----
* Default will translate from english to target language

.. code-block:: bash

    $ translate zh-TW <<< "Hello World!"
    你好世界！

.. image:: img/helloworld.gif
    :alt: Hello
    :align: center

Examples
--------
* Just as easily specify a source language by providing it as first
  argument

.. code-block:: bash

   # Translate Hello from French to English
   $ translate fr en <<< 'Bonjour, comment allez-vous!' 
   Hello, how are you?

Redirect from File
~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    $ translate zh-TW < "alice.txt"

    阿麗思道：「你不是說你要告訴你的歷史嗎？告訴我你為甚麼恨—那個—那些—C和D，」
    她末了兩個字母輕輕兒地說的，怕回來又得罪了牠。

    那老鼠對著阿麗思嘆了一口氣道，「唉﹗我的身世說來可真是又長又苦又委屈呀—」

    阿麗思聽了，瞧著那老鼠的尾巴說，「你這尾是曲啊﹗可是為甚麼又叫它苦呢﹗」
    她就一頭聽著那老鼠說話，一頭在在心上納悶，所以她聽的那老鼠講的「尾曲」
    的歷史是差不多像這個樣了的

Chaining together Pipes
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

   # Translate Telephone!
   $ echo 'What is love?' | translate zh-TW | translate ko | translate fr | translate en
   What is love?

Be Creative!
~~~~~~~~~~~~
.. code-block:: bash

   # A "Here-String" Grocery List
   $ cat <<- GROCERY_LIST | translate ko
        Celery
        Milk
        Eggs
        Bread
        Cereal
   GROCERY_LIST

   셀러리
   우유
   달걀
   빵
   시리얼

Documentation
-------------

Documentation is available at https://py-translate.readthedocs.org/
