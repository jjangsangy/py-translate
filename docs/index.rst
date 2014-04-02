.. GTranslate documentation master file, created by
   sphinx-quickstart on Wed Mar 26 13:21:22 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===========================================
GTranslate
===========================================
**GTranslate is a CLI Tool for Google Translate written in Python!**

------------------------------------------------------------------------


:Author: Sang Han, 2014
:License: `Apache Software License v2 <http://opensource.org/licenses/Apache-2.0>`_
:Version: v\ |version|

Easy to Use Syntax
------------------
.. code-block:: bash

    $ echo 'Hello World!' | translate ko
    $ 안녕하세요！


Features
---------
- Simple command line parsing!
- Written in pure Python!
- Backwards compatable with Python 2.7
- Supports all language from Google Translate API
- Speed: Unix Pipes
- Native UTF-8 Support

Installation
------------
Clone the repository

.. code-block:: bash

    $ git clone https://github.com/jjangsangy/GTranslate.git

Install with setup.py

.. code-block:: bash

    $ python setup.py install

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

