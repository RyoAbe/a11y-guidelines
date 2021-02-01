.. _category-dynamic-content:

動的コンテンツ
------------------------------------

これらのガイドラインは、動的コンテンツに関するものです。

動的コンテンツとは、自動的、またはユーザーの操作を受けて変化するものです。そのような変化には、表示されているものの変更に加えて、ページ遷移なども含まれる場合があります。

.. _dynamic-content-behavior-on-interaction:

ユーザーの操作に伴う挙動
~~~~~~~~~~~~~~~~~~~~~~~~

.. _gl-dynamic-content-maintain-dom-tree:

[MUST] 適切なDOMツリーを維持する
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [MUST] ユーザーの操作によってコンテンツが増減するようなページでは、どの状態においても、最初から順に読み進めた場合にコンテンツの意味が正しく伝わるような順序にDOMツリーを維持する。
チェック内容
   .. include:: ../checks/inc/gl-dynamic-content-maintain-dom-tree.rst

.. raw:: html

   <div><details>

意図
````

スクリーン・リーダーなどの支援技術のユーザーが、コンテンツを正しく理解できるようにする。

-  動的に追加されるコンテンツがDOMツリーの適切な位置に挿入されることで、スクリーン・リーダーのユーザーがそのコンテンツの存在を認知し、内容を理解することができる。
-  モーダル・ダイアログ、開閉するメニュー、アコーディオンなどで注意が必要。

参考
````

*  :ref:`exp-dynamic-content-maintain-dom-tree`


対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 1.3.2:

   *  |SC 1.3.2|
   *  |SC 1.3.2ja|

.. raw:: html

   </div></details>

.. _gl-dynamic-content-focus:

[MUST] OnFocus/OffFocus時の挙動
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [MUST] OnFocus, OffFocusが以下のような変化を発生させないようにする。

   -  ページ遷移
   -  フォーム送信
   -  モーダル・ダイアログの表示

チェック内容
   .. include:: ../checks/inc/gl-dynamic-content-focus.rst

.. raw:: html

   <div><details>

意図
````

視覚障害、認知障害があるユーザーが予期できない挙動を発生させない。

参考
````

*  :ref:`exp-tab-order-check`

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 3.2.1:

   *  |SC 3.2.1|
   *  |SC 3.2.1ja|

.. raw:: html

   </div></details>

.. _gl-dynamic-content-hover-magnify:

[MUST] ホバーで表示されるコンテンツの拡大
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [MUST] ホバーで表示されるコンテンツについて、ポインターをホバーで表示されたコンテンツ上に移動しても、コンテンツが消えないようにすることで、そのコンテンツを拡大表示して利用することを可能にする。
チェック内容
   .. include:: ../checks/inc/gl-dynamic-content-hover-magnify.rst

.. raw:: html

   <div><details>

意図
````

拡大表示を利用しているロービジョン者が、ホバーで表示される内容を利用できるようにする。

参考
````

*  :ref:`exp-dynamic-content-hover`

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 1.4.13:

   *  |SC 1.4.13|
   *  |SC 1.4.13ja|

.. raw:: html

   </div></details>

.. _gl-dynamic-content-hover:

[SHOULD] ホバーで表示されるコンテンツの非表示
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [SHOULD] ホバーで表示されるコンテンツについて、以下のすべてを満たす。

   -  ポインターを移動させることなく、ホバーで表示されたコンテンツを非表示にできる。（Escキーで消える、など）
   -  ホバー状態ではなくなった場合、ユーザーが非表示にする操作を行った場合、内容が無効になった場合にのみ、ホバーで表示されたコンテンツを非表示にする。

チェック内容
   .. include:: ../checks/inc/gl-dynamic-content-hover.rst

.. raw:: html

   <div><details>

意図
````

拡大表示を利用しているロービジョン者が、ホバーで表示される内容を利用できるようにする。

参考
````

*  :ref:`exp-dynamic-content-hover`

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 1.4.13:

   *  |SC 1.4.13|
   *  |SC 1.4.13ja|

.. raw:: html

   </div></details>

.. _dynamic-content-status:

ステータス・メッセージ
~~~~~~~~~~~~~~~~~~~~~~~~

.. _gl-dynamic-content-status:

[MUST] ステータス・メッセージの適切なマークアップ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [MUST] ステータス・メッセージについて、以下のすべてを満たす。

   -  スクリーン・リーダーに自動的に読み上げられるようにする。
   -  ステータス・メッセージであることが分かるように適切なマークアップをする。

チェック内容
   .. include:: ../checks/inc/gl-dynamic-content-status.rst

.. raw:: html

   <div><details>

意図
````

視覚障害者が、ステータス・メッセージを遅滞なく確認できるようにする。

参考
````

*  :ref:`exp-dynamic-content-status`

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 4.1.3:

   *  |SC 4.1.3|
   *  |SC 4.1.3ja|

.. raw:: html

   </div></details>


.. _dynamic-content-auto-updated:

自動的に変化するコンテンツ
~~~~~~~~~~~~~~~~~~~~~~~~~~

参考： :ref:`exp-dynamic-content-auto-updated`

.. _gl-dynamic-content-pause-movement:

[MUST] 点滅、スクロールを伴うコンテンツ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [MUST] 同じページ上に、自動的に開始し5秒以上継続する、点滅やスクロールを伴うコンテンツと、他のコンテンツを一緒に配置しない。
   そのようなコンテンツを作る場合は、ユーザーが一時停止、停止、または非表示にすることができるようにする。
チェック内容
   .. include:: ../checks/inc/gl-dynamic-content-pause-movement.rst

.. raw:: html

   <div><details>

意図
````

ロービジョン者や認知障害者が、集中を阻害されないようにする。

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 2.2.2:

   *  |SC 2.2.2|
   *  |SC 2.2.2ja|

.. raw:: html

   </div></details>

.. _gl-dynamic-content-pause-refresh:

[MUST] 自動更新されるコンテンツ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [MUST] 予め設定された間隔で自動的に内容が更新されたり非表示になったりするコンテンツを作らない。
   そのようなコンテンツを作る場合は、ユーザーが一時停止、停止、非表示にすることができるか、更新頻度を調整できるようにする。
チェック内容
   .. include:: ../checks/inc/gl-dynamic-content-pause-refresh.rst

.. raw:: html

   <div><details>

意図
````

ロービジョン者や認知障害者が、集中を阻害されないようにする。

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 2.2.2:

   *  |SC 2.2.2|
   *  |SC 2.2.2ja|

.. raw:: html

   </div></details>

.. _gl-dynamic-content-no-flashing:

[MUST] 閃光を放つコンテンツ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [MUST] どの1秒間においても3回を超える閃光を放つものがないようにする。
チェック内容
   .. include:: ../checks/inc/gl-dynamic-content-no-flashing.rst

.. raw:: html

   <div><details>

意図
````

光感受性の発作を防ぐ。

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 2.3.1:

   *  |SC 2.3.1|
   *  |SC 2.3.1ja|

*  SC 2.3.2:

   *  |SC 2.3.2|
   *  |SC 2.3.2ja|

.. raw:: html

   </div></details>

.. _gl-dynamic-content-no-interrupt:

[SHOULD] 割り込み表示
^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [SHOULD] 緊急性が高い情報を提示する場合を除いて、プッシュ通知や自動更新などによる割り込みを発生させない。
チェック内容
   .. include:: ../checks/inc/gl-dynamic-content-no-interrupt.rst

.. raw:: html

   <div><details>

意図
````

ロービジョン者や認知障害者が、集中を阻害されないようにする。

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 2.2.4:

   *  |SC 2.2.4|
   *  |SC 2.2.4ja|

.. raw:: html

   </div></details>
