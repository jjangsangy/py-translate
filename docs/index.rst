.. py-translate documentation master file, created by
   sphinx-quickstart on Wed Mar 26 13:21:22 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===========================================
py-translate
===========================================
**py-translate is a CLI Tool for Google Translate written in Python!**

------------------------------------------------------------------------

.. sidebar:: Current Supported Platforms

    Linux & Mac OS X

:Author:  Sang Han 2014
:License: `Apache Software License v2 <http://opensource.org/licenses/Apache-2.0>`_
:Version: v\ |version|

------------------------------------------------------------------------

Installation
------------
Clone the repository

.. code-block:: bash

    $ git clone https://github.com/jjangsangy/py-translate.git

Install with setup.py

.. code-block:: bash

    $ python setup.py install

Easy to Use Syntax
------------------

Unix Pipes
~~~~~~~~~~
.. code-block:: bash
    :emphasize-lines: 2, 5

    $ echo 'Hello World!' | translate zh-TW
    你好世界！

    $ echo 'Goodbye!' | translate ko
    안녕히 가세요!


Redirect from File
~~~~~~~~~~~
.. code-block:: bash
    :emphasize-lines: 3-

    $ translate zh-CN < "alice.txt"

    阿麗思道：「你不是說你要告訴你的歷史嗎？告訴我你為甚麼恨—那個—那些—C和D，」
    她末了兩個字母輕輕兒地說的，怕回來又得罪了牠。

    那老鼠對著阿麗思嘆了一口氣道，「唉﹗我的身世說來可真是又長又苦又委屈呀—」

    阿麗思聽了，瞧著那老鼠的尾巴說，「你這尾是曲啊﹗可是為甚麼又叫它苦呢﹗」
    她就一頭聽著那老鼠說話，一頭在在心上納悶，所以她聽的那老鼠講的「尾曲」
    的歷史是差不多像這個樣了的

Features
---------
- Simple command line parsing!
- Written in pure Python!
- Backwards compatable with Python 2.7
- Supports all language from Google Translate API
- Speed: Unix Pipes
- Native UTF-8 Support

API Documentation
-----------------
.. toctree::
    :maxdepth: 2

    usage
    requirements
    api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

