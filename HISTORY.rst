=================
Release History
=================

1.0.2 (2015-01-02)
------------------
- Happy New Year
- Created quick benchmarking suite
- Optimized thread utilization
- Bug fixes and better IO performance

1.0.1 (2014-12-30)
------------------
- More efficient task processing using `map` over `submit`.
- Seperated IO in coroutine exception blocks.
- Bug Fixes and Improvements.

1.0.0 (2014-12-18)
------------------
- Bug fix with lines longer than 1000 chars
- Fixed another unicode bug
- Improved Python 2/3 Compatability
- Implemented text transliteration where available
- Implemented simple File IO
- Better utilization of thread pools using futures module.
- Vendorized dependencies
- Swapped transport API from urllib2 with Requests
- SSL/TLS integration for secure web requests


0.2.3 (2014-12-08)
-------------------
- Bug fix with double output


0.2.2 (2014-12-07)
-------------------

- Bug fixes
- Decreased package size
- Split `translator.py` into two seperate modules


0.2.1 (2014-12-04)
------------------
- Added Output Buffer Streaming
- Utilized Cooperative Multitasking for Coroutines
- Updated Documentation on API

0.2.0 (2014-11-30)
------------------

- Bug fixes
- Implmented concurrency based on Asyncronous threads and coroutines
- Up to 10x performance speedup

0.1.6 (2014-11-30)
-------------------

- Bug Fixes
- Re-implmenenting concurrency models
- Python 3 is now the base implemntation


0.1.5 (2014-07-18)
-------------------

- Language Code Generator Fix

0.1.4 (2014-07-05)
--------------------

- General Bug Fixes
- Speed Improvements
- Length of multibyte characters correctly represented by spooler
- Better support for utf-8.

0.1.3 (2014-04-07)
-------------------

- Implemented language discovery arg
- Bug Fixes

0.1.2 (2014-04-04)
-------------------

- Documentation reorganization

**Bug Fixes**

- Fixed unicode encode/decode errors

0.1.1 (2014-04-03)
--------------------

- PyPy-c v2.2 now support

**Bug Fixes**

- Quick fix PyPI distribution (huge package sizes)
- MANIFEST.in now does it job
- Assorted fixes with methods and scope

0.1.0 (2014-04-02)
--------------------

- GTranslate is taken on PyPI.
- Name changed to py-translate
- Distributed through PyPI and Wheel
- More documentation and autoparsing for module functions
- Separated into logical modules in a package rather than one executable `__main__.py`

0.0.0 (2014-03-31)
--------------------

- Support for Python 2.7 and 3.x
- Sphinx Documentation hosted
- Travis CI build passed!
- Source released on Github
