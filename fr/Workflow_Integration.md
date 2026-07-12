# <%= @title %>

## AppleScript

Marked inclut un [dictionnaire AppleScript](AppleScript_Support.html) complet pour ouvrir des fichiers, contrôler l'aperçu (rechargement, défilement, mises en évidence, défilement automatique, Lecture rapide), lire les statistiques, définir les processeurs, copier du HTML ou du RTF, changer le style d'aperçu, et exporter vers Markdown, HTML, PDF, EPUB, DOCX, ODT, TextBundle, RTF et OPML. **La prévisualisation des titres / de la table des matières** via AppleScript est [documentée comme étant en cours de développement](AppleScript_Support.html#table-of-contents-work-in-progress) et n'est pas encore fiable.

Vous pouvez cibler l'application, une fenêtre spécifique, ou un document. Les commandes d'application incluent **open streaming preview**, **preview clipboard** et **close all**. Les commandes de document incluent **get statistics** et **print with profile**. Les commandes d'export acceptent un **profile** d'export facultatif, ou un enregistrement **`with`** pour des options telles que le **style**, la **pageSize** et les **margins** de l'aperçu. Par exemple :

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/path/to/output.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

Voir [Prise en charge d'AppleScript](AppleScript_Support.html) pour la liste des commandes, la notation abrégée des marges, les notes sur le bac à sable, et des astuces de débogage.

L'intégration AppleScript permet également à des applications telles que Tags.app de fonctionner directement au sein de Marked.

{% note %}
## Shortcuts

Marked includes native [Shortcuts actions](Shortcuts_Integration.html) on macOS 13 or later. Use **Open and Export File** for Finder-to-PDF workflows, **Export Document** for whatever is already open in Marked, or **Set Preview Style** to change themes before export. Export actions accept **profiles**, preview **styles**, and options such as **page size**, **margins**, and **font size** (same semantics as AppleScript `with` records).

[shortcuts]: Shortcuts_Integration.html
{% endnote %}

## Gestionnaire d'URL

Le [gestionnaire d'URL de Marked][urlhandler] permet une intégration étendue simplement en appelant des URL, que ce soit depuis AppleScript ou avec une simple commande `open` dans un script shell.

## Marked Bonus Pack

Le Marked Bonus Pack est une collection de scripts, de commandes et de services. Certains fonctionnent avec plusieurs éditeurs, d'autres sont spécifiques à certains éditeurs. Les services fonctionnent généralement avec tout éditeur disposant des capacités nécessaires. Le reste est organisé en dossiers selon l'application avec laquelle ils fonctionnent.

Vous pouvez télécharger le Bonus Pack et trouver les instructions d'installation et d'utilisation dans cet [article de la base de connaissances](http://support.markedapp.com/kb/how-to-tips-and-tricks/marked-bonus-pack-scripts-commands-and-bundles).

[urlhandler]: URL_Handler.html
[applescript]: AppleScript_Support.html
