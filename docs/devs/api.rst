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

Stream Caching
----------------

.. autofunction:: translate.source
.. autofunction:: translate.spool
.. autofunction:: translate.set_task
.. autofunction:: translate.write_stream
.. autofunction:: translate.accumulator


Multitasking
-------------

.. autofunction:: translate.set_task

Writer
-------

.. autofunction:: translate.write_stream


Language Code Generation
----------------------------

.. autofunction:: translate.translation_table
.. autofunction:: translate.print_table

.. glossary::

    translate
        Access to library is done primarily through the application called
        translate which will be installed and accessed through a directory
        under users $PATH envar.
