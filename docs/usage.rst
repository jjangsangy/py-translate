Usage
-----
:samp:`translate [-h] [-V] [{source}] {dest}`

py-translate is a CLI Tool for Google Translate written in Python!

positional arguments::

-source         Source language to convert from
-dest           Destination language to convert into


optional arguments::

-h, --help     show this help message and exit
-V, --version  show program's version number and exit


Unix Pipes
~~~~~~~~~~~~
.. code-block:: bash

    $ echo 'Hello World!' | translate zh-TW
    你好世界！

    $ echo 'Goodbye!' | translate ko
    안녕히 가세요!


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

