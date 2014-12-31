py-translate
============

|Documentation| |github| |travis| |pypi| |Wheel|

A Translation Tool for Humans

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

-  Made for Python 3 but still works on Python 2
-  Fast and easy to install, easy to use
-  Supports translation from any language
-  Highly composable interface, the power of Unix pipes and filters.
-  Simple API and documentation

Installation
------------

From PyPI with pip (easy)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    $ pip install py-translate

From Source at Github
~~~~~~~~~~~~~~~~~~~~~

-  Clone the repository

.. code:: sh

    $ git clone https://github.com/jjangsangy/py-translate.git

-  Install with setup.py

.. code:: sh

    $ python setup.py install

Usage
-----

``translate [--flags] [source] dest``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Arguments
~~~~~~~~~

+------------------+-------------------------------------------------------+
| **Positional**   |                                                       |
+==================+=======================================================+
| dest             | Destination language code                             |
+------------------+-------------------------------------------------------+
| source           | Source language code                                  |
+------------------+-------------------------------------------------------+
| **Optional**     |                                                       |
+------------------+-------------------------------------------------------+
| -h,--help        | Show this help message and exit                       |
+------------------+-------------------------------------------------------+
| -v, --version    | Show program’s version number and exit                |
+------------------+-------------------------------------------------------+
| -l,--list [code] | Enumerate the name of country and language code pair. |
+------------------+-------------------------------------------------------+
|                  | [ Optionally specify output language format ]         |
+------------------+-------------------------------------------------------+
| --translit       | Print out the transliteration of the text             |
+------------------+-------------------------------------------------------+

Examples
--------

Hello World from English to Traditional Chinese

.. code:: sh

    $ translate en zh-TW <<< 'Hello World!'
    你好世界！

.. figure:: https://raw.githubusercontent.com/jjangsangy/py-translate/master/img/helloworld.gif
   :alt: Hello World

   Hello World

-  Just as easily specify a source language by providing it as first
   argument

.. code:: sh

    # Translate Hello from French to English
    $ translate fr en <<< 'Bonjour, comment allez-vous!'
    Hello, how are you?

Smart Language Detection
~~~~~~~~~~~~~~~~~~~~~~~~

Omitting the source language will try to detect it based on the text
content

.. code:: sh

    $ translate fr <<< 'I think therefore I am'
    Je pense donc je suis

Romanified Transliteration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    $ translate --translit en ko <<< 'Want to fight!'
    ssaugo sip-eo!

    $ translate --translit en zh-TW <<< 'Kidding, we should be friends'
    Kāiwánxiào, wǒmen yīnggāi shì péngyǒu

Redirect from File
~~~~~~~~~~~~~~~~~~

.. code:: sh

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

.. code:: sh

    # Multiple Chaining
    $ echo 'What is love?' | translate en zh-TW | translate zh-TW ko | translate ko fr | translate fr en
    What is love?

Be Creative!
~~~~~~~~~~~~

.. code:: sh

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

Support
-------

Here’s a list of Python platforms that are officially supported.

-  Python 3.4
-  Python 3.3
-  Python 3.2
-  Python 2.7
-  Python 2.6
-  PyPy 2 (Latest)
-  PyPy 3 (latest)

Documentation
-------------

Find the latest documentation http://pythonhosted.org/py-translate/

Contribute
----------

1. Fork us on `Github <https://github.com/jjangsangy/py-translate>`__.

2. Find a bug? Implemented a new feature? Send a pull request to get it
   merged and published.

3. Feel free to send an e-mail to the code maintainer for questions or
   help regarding the codebase.
   `jjangsangy@gmail.com <jjangsangy@gmail.com>`__


.. |Documentation| image:: https://readthedocs.org/projects/py-translate/badge/?version=master
   :target: https://readthedocs.org/projects/py-translate/?badge=master

.. |github| image:: https://badge.fury.io/gh/jjangsangy%2Fpy-translate.svg
   :target: http://badge.fury.io/gh/jjangsangy%2Fpy-translate

.. |travis| image:: https://travis-ci.org/jjangsangy/py-translate.svg?branch=master
   :target: https://travis-ci.org/jjangsangy/py-translate

.. |pypi| image:: https://badge.fury.io/py/py-translate.svg
   :target: http://badge.fury.io/py/py-translate

.. |Wheel| image:: https://pypip.in/wheel/py-translate/badge.svg
   :target: https://pypi.python.org/pypi/py-translate/
