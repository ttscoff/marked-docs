# <%= @title %>

Marked fonctionne avec de nombreux éditeurs et applications d'écriture. Cette page couvre les **paramètres** partagés, l'**aperçu du presse-papiers**, des renvois vers l'**aperçu en continu**, ainsi que des ressources de script. Les guides détaillés pour les applications populaires se trouvent dans leurs propres rubriques d'aide (voir la section **Applications prises en charge** dans la barre latérale).

## Guides par application

Commencez par [Aperçu Markdown en direct sur Mac](Live_Markdown_Preview_on_Mac.html) pour une vue d'ensemble du fonctionnement. Si vous utilisez Obsidian, consultez [Marked face à l'aperçu intégré d'Obsidian](Marked_vs_Obsidian_Preview.html) pour décider quand Marked ajoute de la valeur par rapport à l'aperçu intégré d'Obsidian.

| Sujet | Page d'aide |
| :-- | :-- |
| **Bear** | [Bear](Bear.html) |
| **Curio** (aperçu en continu) | [Curio](Curio.html) |
| **Drafts** (aperçu en continu + actions) | [Drafts](Drafts.html) |
| **DEVONthink** (intégration au menu Scripts) | [DEVONthink](DEVONthink.html) |
| **Surveillance de dossiers** (nvALT, nvUltra, etc.) | [Surveillance de dossiers](Folder_Watching.html) |
| **Highland** | [Highland](Highland.html) |
| **Résolution des URL Hookmark** | [Hookmark](Hookmark.html) |
| **iA Writer** | [iA Writer](iA_Writer.html) |
| **iThoughtsX** cartes `.itmz` | [iThoughtsX](iThoughtsX.html) |
| **MarsEdit** aperçu en direct | [MarsEdit](MarsEdit.html) |
| **MindNode** | [MindNode](MindNode.html) |
| **MultiMarkdown Composer** | [MultiMarkdown Composer](MultiMarkdown_Composer.html) |
| **nvUltra** | [nvUltra](nvUltra.html) |
| Coffres et légendes **Obsidian** | [Obsidian](Obsidian.html) |
| **OmniOutliner / OPML** | [OmniOutliner et OPML](OmniOutliner_and_OPML.html) |
| **RTF / RTFD** (Pages, TextEdit, etc.) | [Prise en charge de RTF et RTFD](RTF_Support.html) |
| **PDF** | [Prise en charge de PDF](PDF_Support.html) |
| **Scrivener 3** | [Prise en charge de Scrivener 3](Scrivener_Support.html) |
| **The Archive** aperçu en continu | [The Archive](The_Archive.html) |
| **Ulysses** flux d'export | [Ulysses](Ulysses.html) |
| **Vim** (plugin vim-marked) | [Vim](Vim.html) |
| **VS Code** (extension Open in Marked) | [VS Code](VS_Code.html) |
| **VoodooPad** | [VoodooPad](VoodooPad.html) |
| **Xcode Playgrounds** | [Xcode Playgrounds](Xcode_Playgrounds.html) |

## Paramètres de l'application

I> Plusieurs intégrations exposent des bascules à l'intérieur de {% prefspane Apps %} et {% prefspane Preview %}.

![Paramètres de l'application][appsettings]

Utilisez ces volets pour les valeurs par défaut des liens wiki, le transfert vers Scrivener, les paramètres du presse-papiers en continu, les options d'intégration de cartes mentales pour OPML/OmniOutliner, les intégrations Obsidian, ou d'autres processeurs qui dépendent d'éditeurs coopératifs.

## Aperçu du presse-papiers

![][ClipboardPreviewMenu]

Le Markdown (ou le texte brut compatible) dans le presse-papiers s'ouvre avec {% appmenu File, New, Clipboard Preview %} ({% kbd shift cmd V %}). Si le presse-papiers contient **HTML ou RTF**, Marked le convertit en source de type Markdown avant l'aperçu, y compris la détection de titre approximatif lorsque les paragraphes RTF utilisent de grandes tailles de police de feuille de style.

## Aperçu en continu

Bear, Curio, Drafts, The Archive, nvALT, nvUltra et plusieurs autres éditeurs peuvent envoyer du Markdown vers Marked au fil de la frappe grâce à l'**aperçu en continu**. Voir [Aperçu en continu](Streaming_Preview.html) pour la configuration et le dépannage.

## Scripts et Bonus Pack

Des automatisations pour BBEdit, TextMate, DEVONthink, Emacs, Vim et d'autres sont fournies avec le [Marked Bonus Pack][bonus]. Installez ou adaptez ces scripts si vous voulez des macros de barre de menus ou d'éditeur au-delà des intégrations listées ci-dessus.


[appsettings]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane
[ClipboardPreviewMenu]: images/ClipboardPreviewMenu.jpg @2x width=600px height=198px class=center
[bonus]: https://github.com/kotfu/marked-bonus-pack
