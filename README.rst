py-translate
============

|Documentation| |github| |travis| |pypi|

A simple translation command line utility

.. figure:: https://raw.githubusercontent.com/jjangsangy/py-translate/master/img/alice.gif
   :alt: Translate Lewis Carroll: Alice in Wonderland

   Translate Lewis Carroll: Alice in Wonderland

--------------

The end goal is a simple application for translating text in the
terminal. Text can be generated interactively or programmatically in the
shell environment. Through command line arguments, file descriptors or
pipes generating translated output that can be piped to a file or
displayed on the terminal.

Features
--------

-  Fast and easy to install, easy to use
-  Implemented in ``Python 3.4``, backwards compatible to ``2.7``
-  Even supports ``PyPy`` and ``PyPy 3k``
-  Supports translation from any language
-  Highly composable interface, the power of Unix pipes and filters.
-  Simple API and documentation

Installation
------------

From PyPI with pip (easy)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block sh

    $ pip install py-translate

From Source at Github
~~~~~~~~~~~~~~~~~~~~~

-  Clone the repository

.. code-block sh

    $ git clone https://github.com/jjangsangy/py-translate.git

-  Install with setup.py

.. code-block sh

    $ python setup.py install

Usage
-----

``translate [-h] [-l [code]] [-v] source dest``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Arguments
~~~~~~~~~

+------------------+---------------------------------------------------------+
| **Positional**   |                                                         |
+==================+=========================================================+
| dest             | Destination language code                               |
+------------------+---------------------------------------------------------+
| source           | Source language code                                    |
+------------------+---------------------------------------------------------+
| **Optional**     |                                                         |
+------------------+---------------------------------------------------------+
| -h, --help       | Show this help message and exit                         |
+------------------+---------------------------------------------------------+
| -l *[code]*      | Enumerate the name of country and language code pair.   |
+------------------+---------------------------------------------------------+
|                  | [*Optionally specify output language format*\ ]         |
+------------------+---------------------------------------------------------+
| -v, --version    | Show program’s version number and exit                  |
+------------------+---------------------------------------------------------+

Examples
--------

-  Default will translate from english to target language

.. code-block sh

    $ translate zh-TW <<< 'Hello World!'
    你好世界！

.. figure:: https://raw.githubusercontent.com/jjangsangy/py-translate/master/img/helloworld.gif
   :alt: Hello World

   Hello World

-  Just as easily specify a source language by providing it as first
   argument

.. code-block sh

    # Translate Hello from French to English
    $ translate fr en <<< 'Bonjour, comment allez-vous!'
    Hello, how are you?

Redirect from File
~~~~~~~~~~~~~~~~~~

.. code-block sh

    $ translate zh-TW < 'alice.txt'

    阿麗思道：「你不是說你要告訴你的歷史嗎？告訴我你為甚麼恨—那個—那些—C和D，」
    她末了兩個字母輕輕兒地說的，怕回來又得罪了牠。

    那老鼠對著阿麗思嘆了一口氣道，「唉﹗我的身世說來可真是又長又苦又委屈呀—」

    阿麗思聽了，瞧著那老鼠的尾巴說，「你這尾是曲啊﹗可是為甚麼又叫它苦呢﹗」
    她就一頭聽著那老鼠說話，一頭在在心上納悶，所以她聽的那老鼠講的「尾曲」
    的歷史是差不多像這個樣了的
    ....

Chaining together Pipes
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block sh

    # Multiple Chaining
    $ echo 'What is love?' | translate zh-TW | translate zh-TW ko | translate ko fr | translate fr en
    What is love?

Be Creative!
~~~~~~~~~~~~

.. code-block sh

    # Grocery List
    $ cat << BUY | translate ko
    Celery
    Milk
    Eggs
    Bread
    Cereal
    BUY

    셀러리
    우유
    달걀
    빵
    시리얼

Documentation
-------------

Find the latest documentation http://pythonhosted.org//py-translate/

.. |Documentation| image:: https://readthedocs.org/projects/py-translate/badge/?version=master
   :target: https://readthedocs.org/projects/py-translate/?badge=master

.. |github| image:: https://badge.fury.io/gh/jjangsangy%2Fpy-translate.svg
   :target: http://badge.fury.io/gh/jjangsangy%2Fpy-translate

.. |travis| image:: https://travis-ci.org/jjangsangy/py-translate.svg?branch=master
   :target: https://travis-ci.org/jjangsangy/py-translate

.. |pypi| image:: https://badge.fury.io/py/py-translate.svg
   :target: http://badge.fury.io/py/py-translate
