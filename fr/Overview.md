# <%= @title %>

{% apponly div %}
*Pour la dernière version de cette documentation, visitez la [version en ligne][help].*
{% endapponly %}

**Assurez-vous de consulter la collection croissante de [vidéos tutorielles Marked](https://www.youtube.com/playlist?list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ).**

## Qu'est-ce que le Markdown ?

[daringfireball]: http://daringfireball.net/projects/markdown/basics
[mmd5]: https://fletcher.github.io/MultiMarkdown-5/
[mdguide]: https://www.markdownguide.org/
[help]: http://markedapp.com/help/

Markdown est un langage de balisage de base utilisant des symboles simples, vous permettant d'écrire du HTML (et d'exporter vers d'autres formats) avec une syntaxe simple comme `*italics*` et `**bold**`. Markdown a été créé par John Gruber et devient rapidement la norme de facto pour la publication sur le Web, la prise de notes et même la publication de livres. Il vous permet d'écrire sans un tas de barres d'outils et de manipulations de formatage, en mettant simplement des mots sur la page et en laissant vos processeurs (comme Marked) gérer le style et le formatage.

Marked fonctionne avec GitHub Flavored Markdown, CommonMark (GFM), Kramdown et MultiMarkdown, et peut convertir la syntaxe de plusieurs variantes pour un aperçu (il peut également être étendu pour fonctionner avec à peu près n'importe quel processeur dont vous avez besoin, y compris Textile, reStructuredText, Wikitext et plus). Je suppose que, puisque vous êtes ici, vous savez ce qu'est au moins un de ces langages de balisage. Sinon, vous devriez commencer par [Markdown Basics][daringfireball] de John Gruber, ou consultez [MarkdownGuide.org][mdguide]. Marked comprend un guide de syntaxe Markdown complet dans le menu d'aide.

Vous pouvez utiliser le [Markdown Dingus](x-marked-3://dingus) pour expérimenter les différentes versions de Markdown prises en charge par Marked.

## Qu'est-ce que Marked ?

Marked est une application d'aperçu Markdown en direct pour macOS, une application d'aperçu (Multi) Markdown indépendante de l'éditeur qui surveille les modifications d'un fichier, mettant à jour l'aperçu à chaque fois que vous enregistrez. En séparant et en automatisant les détails du formatage, il vous permet de vous concentrer davantage sur l'écriture et moins sur la présentation, tout en gardant un œil sur votre produit final.

Pour les flux de travail de configuration et les démarrages rapides spécifiques à l'éditeur, voir [Aperçu Live Markdown sur Mac](Live_Markdown_Preview_on_Mac.html). Pour un aperçu plus court du produit, visitez [markedapp.com/markdown-preview](https://markedapp.com/markdown-preview/).

Marked fonctionne avec n'importe quel fichier accessible localement, y compris les documents iCloud. Faites simplement glisser un document texte de la barre d'outils de n'importe quel éditeur vers Marked et il le restituera sous forme d'aperçu HTML et commencera à suivre les modifications, mettant à jour l'aperçu au fur et à mesure que vous écrivez. Il peut même compiler des [documents multi-fichiers](Multi-File_Documents.html) en utilisant une syntaxe de base « include », ou à partir des formats d'index Scrivener, Leanpub et mmd_merge.

Marked possède des fonctionnalités supplémentaires, notamment le nombre de mots et d'autres statistiques de documents, la possibilité de flotter au-dessus d'autres applications ou de s'atténuer en arrière-plan, et il peut afficher votre travail dans une variété de styles bien conçus. Il peut imprimer des documents PDF ou Word, des documents HTML complets (y compris des styles et des images) ou copier des données source HTML ou RTF dans votre presse-papiers en appuyant simplement sur une touche. Marked dispose également d'un dictionnaire AppleScript de base et d'un [gestionnaire d'URL](URL_Handler.html) qui facilitent son intégration dans votre flux de travail.

Oh oui, et cela fonctionne avec une tonne de vos applications préférées : des éditeurs de texte allant de Vim et Emacs à Sublime Text et TextMate, des éditeurs Markdown comme MultiMarkdown Composer, Byword et iA Writer, même des applications auxquelles vous ne vous attendez pas comme Ulysses, Scrivener, VoodooPad, MarsEdit, et plus encore.

## Exemples d'utilisation

Marked transforme n'importe quel éditeur de texte en un éditeur compatible Markdown. Votre aperçu est toujours disponible et il se met à jour au fur et à mesure que vous travaillez.

* Si votre éditeur préféré ne propose pas d'aperçu Markdown en direct, ouvrez le document sur lequel vous travaillez dans Marked et faites flotter la fenêtre sur le côté pour une expérience d'écriture Markdown complète.
* Aimez-vous écrire ou bloguer dans MacVim ou un autre éditeur basé sur un terminal ? Vous disposez désormais d'un aperçu Markdown synchronisé pendant que vous travaillez.
* Marked offre également des fonctionnalités d'affichage supérieures à tout aperçu Markdown existant et peut être utilisé à la place pour fournir le nombre complet de mots et les statistiques du document, des suggestions de rédaction et même mettre en évidence les erreurs dans votre formatage Markdown.
* Vous pouvez également utiliser Marked sans éditeur. Faites simplement glisser les fichiers Markdown vers l'icône pour les prévisualiser, les imprimer et les exporter au format source PDF, DOC, RTF ou HTML. Marked peut également **ouvrir les fichiers `.rtf` et `.rtfd`** en tant que documents sources ([Support RTF et RTFD](RTF_Support.html)).
* Dans les applications qui enregistrent automatiquement, vous constaterez que l'aperçu suit votre écriture sans aucune aide. Utilisez-le avec n'importe quel éditeur... ou *tous* vos éditeurs.
* Écrire un livre ? Marked peut compiler plusieurs fichiers pour un aperçu complet de votre travail, et même surveiller les modifications apportées aux fichiers inclus, en mettant à jour le document principal à chaque sauvegarde. Il peut même surveiller les modifications d'un dossier entier, basculant automatiquement l'aperçu vers le fichier que vous êtes en train de mettre à jour. Lorsque vous êtes prêt, vous pouvez publier aux formats EPUB, DOCX ou TextBundle.
* Vous travaillez avec une plateforme de codage d'IA ? Ouvrez un dossier de plan ou de documentation dans Marked et chaque fois qu'un fichier Markdown dans ce dossier change, Marked l'affichera, en faisant défiler automatiquement jusqu'au point de modification la plus récente. Marked affiche les diagrammes Mermaid et peut gérer toutes sortes de syntaxes étendues. Gardez une trace des plans et de la documentation pendant que vous travaillez, sans basculer entre les fichiers.
