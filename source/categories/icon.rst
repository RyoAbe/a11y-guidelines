.. _category-icon:

アイコン
----------------------------

これらのガイドラインは、アイコンを対象にしたものです。

ここでアイコンとは、以下の目的で用いられている画像を指します：

-  オブジェクトの状態を表す
-  クリック可能なボタンやリンクを提供する

.. _icon-perceivable:

認知を可能にする
~~~~~~~~~~~~~~~~

.. _gl-icon-visible-label:

[MUST] テキスト情報の付与
^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [MUST] アイコンにはテキストのラベルを併せて表示し、それが難しい場合はアイコンの目的（表している状態、操作の結果）が分かるような代替テキストを付与する。
チェック内容
   .. include:: ../checks/inc/gl-icon-visible-label.rst

.. raw:: html

   <div><details>

意図
````

視覚障害者が画像の存在を認知し、内容を理解できるようにする。

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 1.1.1:

   *  |SC 1.1.1|
   *  |SC 1.1.1ja|

.. raw:: html

   </div></details>

.. _gl-icon-color-only:

[MUST] 複数の視覚的要素を用いた表現
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [MUST] アイコンに付与されているラベルが非表示のテキストの場合は、形状、サイズが同じで色だけが違う複数のアイコンを用いない。
チェック内容
   .. include:: ../checks/inc/gl-icon-color-only.rst

.. raw:: html

   <div><details>

意図
````

視覚障害者や色弱者が、コンテンツを利用できるようにする。

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 1.4.1:

   *  |SC 1.4.1|
   *  |SC 1.4.1ja|

.. raw:: html

   </div></details>

.. _gl-icon-consistent:

[MUST] アイコンの一貫性
^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [MUST] 同じ目的で用いられるアイコンには、サイト内で一貫性のある画像とテキストを用いる。
チェック内容
   .. include:: ../checks/inc/gl-icon-consistent.rst

.. raw:: html

   <div><details>

意図
````

予測可能性を上げ、混乱を防ぐ。

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 3.2.4:

   *  |SC 3.2.4|
   *  |SC 3.2.4ja|

.. raw:: html

   </div></details>

.. _gl-icon-contrast:

[MUST] コントラスト比の確保
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [MUST] 背景色とのコントラスト比を3:1以上にする。
チェック内容
   .. include:: ../checks/inc/gl-icon-contrast.rst

.. raw:: html

   <div><details>

意図
````

ロービジョン者が、コンテンツを利用できるようにする。

参考
````

*  :ref:`exp-contrast`
*  :ref:`exp-check-contrast`
*  |Vibes Color Contrast|

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 1.4.11:

   *  |SC 1.4.11|
   *  |SC 1.4.11ja|

.. raw:: html

   </div></details>

.. _gl-icon-target-size:

[SHOULD] 十分な大きさのクリック/タッチのターゲット
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ガイドライン
   [SHOULD] リンクが画像の場合、クリック/タッチのターゲット・サイズは充分に大きいものにする。

   -  デスクトップ向けWebでは最低24 x 24 CSS px、可能であれば44 x 44 CSS px以上
   -  モバイル向けは44 x 44 CSS px以上

チェック内容
   .. include:: ../checks/inc/gl-icon-target-size.rst

.. raw:: html

   <div><details>

意図
````

ロービジョン者、細かい手の動きが難しい肢体不自由者の、誤ったクリック/タッチ操作を防ぐ。

参考
````

*  :ref:`exp-target-size`

対応するWCAG 2.1の達成基準
````````````````````````````

*  SC 2.5.5:

   *  |SC 2.5.5|
   *  |SC 2.5.5ja|

.. raw:: html

   </div></details>
