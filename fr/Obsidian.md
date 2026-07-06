# <%= @title %>

Marked fonctionne avec les notes [Obsidian][obsidian-app] de deux manières : ouvrez un **dossier coffre-fort** pour un suivi automatique, ou utilisez le **plug-in communautaire** pour une synchronisation plus étroite.

L'aperçu intégré d'Obsidian est idéal lorsque vous ne quittez jamais l'application. Choisissez Marked lorsque vous souhaitez une exportation de qualité publication, une relecture avancée, des thèmes CSS personnalisés ou le même flux de travail de prévisualisation en direct sur plusieurs éditeurs. Voir [Marked vs Obsidian Preview](Marked_vs_Obsidian_Preview.html) pour une comparaison complète.

## Ouvrir un coffre-fort entier

Faites glisser le **dossier du coffre-fort** (le répertoire qui contient le dossier de configuration caché d'Obsidian à la racine du coffre-fort) sur Marked dans le Dock. Marked surveille cet arbre, conserve la note **la plus récemment modifiée** dans l'aperçu et se met à jour au fur et à mesure que vous enregistrez dans Obsidian.

Pour les valeurs par défaut spécifiques au coffre-fort (style, processeur, URL de base pour les images, etc.), ajoutez une [Règle personnalisée](http://support.markedapp.com) qui correspond aux chemins sous ce coffre-fort.

## Syntaxe des légendes d'Obsidian

Lorsque le processeur MultiMarkdown s'exécute, Marked convertit les **légendes courantes de style Obsidian** (le motif `> [!note]`) en balisage de bloc stylisé afin qu'elles correspondent au reste de votre aperçu.

## Plugin Obsidian de Marked 3

Le [plugin Marked 3 Obsidian][plugin] peut ouvrir la note actuelle ou l'ensemble du coffre-fort avec des commandes ou des raccourcis clavier afin que la fenêtre Marked suive ce que vous modifiez. Utilisez la palette de commandes (**⌘P**) et recherchez **Marked**, ou attribuez des raccourcis clavier dans les paramètres **Hotkeys** d'Obsidian.

### Installation à partir des plugins de la communauté

Dans Obsidian, ouvrez **Paramètres → Plugins communautaires**, parcourez ou recherchez **marked** et installez **Open in Marked**.

### Installer manuellement le plugin

Si vous préférez installer depuis GitHub :

1. Téléchargez `main.js` et `manifest.json` à partir de la [dernière version][plugin-releases] sur GitHub (ou créez-les à partir du référentiel [Marked3-obsidian][plugin]).
2. Dans votre coffre-fort, créez le dossier du plugin sous `plugins/` dans le répertoire de configuration d'Obsidian à la racine du coffre-fort. Le nom du dossier doit correspondre au plugin `id` dans `manifest.json` (voir le [plugin README][plugin] pour le chemin complet).
3. Copiez `main.js` et `manifest.json` dans ce dossier.
4. Dans Obsidian, ouvrez **Paramètres → Plugins communautaires**, désactivez le **Mode restreint** si nécessaire et activez **Ouvrir dans Marked**.

[obsidian-app]: https://obsidian.md/
[plugin]: https://github.com/ttscoff/Marked3-obsidian
[plugin-releases]: https://github.com/ttscoff/Marked3-obsidian/releases/latest
