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

Specify the output format by language code

.. code-block:: bash

   $ translate --langs zh-TW


.. hlist::
   :columns: 2

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

.. cssclass:: table-hover
.. csv-table::
   :name: Language Codes
   :header: Language, Code

   土耳其文,tr
   中文(繁體),zh-TW
   中文(簡體),zh
   丹麥文,da
   巴斯克文,eu
   日文,ja
   爪哇語,jw
   加里西亞文,gl
   加泰羅尼亞文,ca
   卡納達文,kn
   布爾文,af
   白俄羅斯語,be
   立陶宛文,lt
   冰島文,is
   匈牙利文,hu
   印尼文,id
   印度文,hi
   印度古哈拉地語,gu
   西班牙文,es
   克羅埃西亞文,hr
   希伯來文,iw
   希臘文,el
   亞塞拜然文,az
   孟加拉文,bn
   拉丁文,la
   拉脫維亞文,lv
   法文,fr
   波西尼亞,bs
   波斯語,fa
   波蘭文,pl
   芬蘭文,fi
   阿拉伯文,ar
   阿爾巴尼亞文,sq
   俄文,ru
   保加利亞文,bg
   威爾斯文,cy
   苗文,hmn
   英文,en
   挪威文,no
   泰文,th
   泰米爾文,ta
   泰盧固文,te
   海地克里奧文,ht
   烏克蘭文,uk
   烏爾都語,ur
   馬耳他文,mt
   馬來文,ms
   馬其頓文,mk
   馬拉地文,mr
   高棉文,km
   國際語文,eo
   宿霧文,ceb
   捷克文,cs
   荷蘭文,nl
   喬治亞文,ka
   斯瓦希里文,sw
   斯洛伐克文,sk
   斯洛維尼亞文,sl
   菲律賓文,tl
   越南文,vi
   塞爾維亞文,sr
   意第緒語,yi
   愛沙尼亞文,et
   愛爾蘭文,ga
   瑞典文,sv
   義大利文,it
   葡萄牙文,pt
   寮文,lo
   德文,de
   韓文,ko
   羅馬尼亞文,ro
