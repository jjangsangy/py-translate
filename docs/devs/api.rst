.. _api:

Python API
=============

.. codeauthor:: Sang Han <jjangsangy@gmail.com>

Translator Co-Routine
-----------------------

.. autofunction:: translate.translator
.. autofunction:: translate.coroutine

HTTP Delegation
----------------

.. autofunction:: translate.push_url

String Cache
----------------

.. autofunction:: translate.source
.. autofunction:: translate.spooler
.. autofunction:: translate.text_sink


Language Code Generation
----------------------------

.. autofunction:: translate.load_codes
.. autofunction:: translate.language_codes

.. glossary::

    translate
        Access to library is done primarily through the application called
        translate which will be installed and accessed through a directory
        under users $PATH envar.
