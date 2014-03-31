.. GTranslate documentation master file, created by
   sphinx-quickstart on Wed Mar 26 13:21:22 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GTranslate's documentation!
======================================

Requirements
------------
The following tools are needed to build the documentation:

sphinx

The documentation gets built using ``make``, and comes in several flavors.

``make html`` - build the API and narrative documentation web pages, this
is the the default ``make`` target, so running just ``make`` is equivalent to
``make html``.

``make html_noapi`` - same as above, but without running the auto-generated
API docs. When you are working on the narrative documentation, the most time
consuming portion  of the build process is the processing and rending of the
API documentation. This build target skips that.

``make pdf`` will compile a pdf from the documentation.

You can run ``make help`` to see information on all possible make targets.


API Documentation
-----------------
.. toctree::
    :maxdepth: 2

    api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

