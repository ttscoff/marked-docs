# <%= @title %>

[VoodooPad][vp] regroupe chaque page dans un unique fichier de base de données. Glissez le `.vpdoc` sur Marked pour prévisualiser la page actuellement au premier plan dans VoodooPad ; utilisez {% kbd cmd S %} dans VoodooPad chaque fois que vous avez besoin que Marked recharge depuis le disque.

Marked surveille le document sur le disque et remplace l'aperçu lorsque vous changez de page dans VoodooPad.

## Images intégrées [embedded-images]

Lorsque vous référencez des images en Markdown ou en HTML et que le binaire se trouve **à l'intérieur** de la base de données VoodooPad, Marked peut l'extraire pour l'aperçu. Les images qui ne sont que des **alias** (fichiers glissés par référence) ne sont pas stockées dans le bundle : pointez vers celles-ci avec des chemins absolus ou des chemins relatifs au `.vpdoc` sur le disque, afin que Marked puisse les résoudre.

[vp]: https://www.voodoopad.com/
