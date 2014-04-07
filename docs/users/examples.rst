.. _examples:

================================================
Examples
================================================

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

Arguments
~~~~~~~~~
Requires at least one command line argument for the destination language.
If no command line arguments are passed, an error message will be passed.

.. code-block:: bash

   $ echo 'No output language' | translate

.. describe::
   usage: translate [-h] [-v] [-l [code]] [source] dest
   translate: error: the following arguments are required: dest

See :ref:`usage` section for usage information

Language Codes
~~~~~~~~~~~~~~
Use the -l, or --langs option to see all the possible language codes.

.. code-block:: bash

   $ translate --langs

Here is a list of available languages and their language codes

.. cssclass:: table-hover
.. csv-table::
   :name: Language Codes
   :header: Language, Code

   Afrikaans,af
   Albanian,sq
   Arabic,ar
   Azerbaijani,az
   Basque,eu
   Belarusian,be
   Bengali,bn
   Bosnian,bs
   Bulgarian,bg
   Catalan,ca
   Cebuano,ceb
   Chinese (Simplified),    zh
   Chinese (Traditional),   zh-TW
   Croatian,hr
   Czech,cs
   Danish,da
   Dutch,nl
   English,en
   Esperanto,eo
   Estonian,et
   Filipino,tl
   Finnish,fi
   French,fr
   Galician,gl
   Georgian,ka
   German,de
   Greek,el
   Gujarati,gu
   Haitian,Creole          ht
   Hebrew,iw
   Hindi,hi
   Hmong,hmn
   Hungarian,hu
   Icelandic,is
   Indonesian,id
   Irish,ga
   Italian,it
   Japanese,ja
   Javanese,jw
   Kannada,kn
   Khmer,km
   Korean,ko
   Lao,lo
   Latin,la
   Latvian,lv
   Lithuanian,lt
   Macedonian,mk
   Malay,ms
   Maltese,mt
   Marathi,mr
   Norwegian,no
   Persian,fa
   Polish,pl
   Portuguese,pt
   Romanian,ro
   Russian,ru
   Serbian,sr
   Slovak,sk
   Slovenian,sl
   Spanish,es
   Swahili,sw
   Swedish,sv
   Tamil,ta
   Telugu,te
   Thai,th
   Turkish,tr
   Ukrainian,uk
   Urdu,ur
   Vietnamese,vi
   Welsh,cy
   Yiddish,yi
