# <%= @title %>

Marked werkt met veel editors en schrijf-apps. Deze pagina behandelt gedeelde **instellingen**, het **klembordvoorbeeld**, verwijzingen naar **streamingvoorbeeld** en scriptbronnen. Gedetailleerde handleidingen voor populaire apps zijn te vinden in hun eigen Help-onderwerpen (zie het gedeelte **Ondersteunde apps** in de zijbalk).

## Gidsen per app [per-app-guides]

Begin met [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) voor de algehele workflow. Als je Obsidian gebruikt, zie [Marked vs Obsidian Preview](Marked_vs_Obsidian_Preview.html) om te beslissen wanneer Marked waarde toevoegt naast de ingebouwde preview van Obsidian.

| Onderwerp | Helppagina |
| :-- | :-- |
| **Beer** | [Bear](Bear.html) |
| **Curio** (streamingvoorbeeld) | [Curio](Curio.html) |
| **Concepten** (streamingvoorbeeld + acties) | [Drafts](Drafts.html) |
| **DEVONthink** (integratie van scriptmenu's) | [DEVONthink](DEVONthink.html) |
| **Mappen bekijken** (nvALT, nvUltra, etc.) | [Folder Watching](Folder_Watching.html) |
| **Hoogland** | [Highland](Highland.html) |
| **Hookmark** URL-resolutie | [Hookmark](Hookmark.html) |
| **iA-schrijver** | [iA Writer](iA_Writer.html) |
| **iThoughtsX** `.itmz` kaarten | [iThoughtsX](iThoughtsX.html) |
| **MarsEdit** livevoorbeeld | [MarsEdit](MarsEdit.html) |
| **MindNode** | [MindNode](MindNode.html) |
| **MultiMarkdown Componist** | [MultiMarkdown Composer](MultiMarkdown_Composer.html) |
| **nvUltra** | [nvUltra](nvUltra.html) |
| **Obsidian** kluizen en toelichtingen | [Obsidian](Obsidian.html) |
| **OmniOutliner / OPML** | [OmniOutliner and OPML](OmniOutliner_and_OPML.html) |
| **RTF / RTFD** (Pagina's, Teksteditor, enz.) | [RTF and RTFD Support](RTF_Support.html) |
| **PDF** | [PDF Support](PDF_Support.html) |
| **Scrivener 3** | [Scrivener 3 Support](Scrivener_Support.html) |
| **Het Archief** streamingvoorbeeld | [The Archive](The_Archive.html) |
| **Ulysses** exportworkflow | [Ulysses](Ulysses.html) |
| **Vim** (vim-gemarkeerde plug-in) | [Vim](Vim.html) |
| **VS-code** (openen in Marked extensie) | [VS Code](VS_Code.html) |
| **VoodooPad** | [VoodooPad](VoodooPad.html) |
| **Xcode-speeltuinen** | [Xcode Playgrounds](Xcode_Playgrounds.html) |

## Applicatie-instellingen [application-settings]

I> Verschillende integraties maken schakelaars zichtbaar binnen {% prefspane Apps %} en {% prefspane Preview %}.

![Application Settings][appsettings]

Gebruik deze vensters voor standaardinstellingen voor wikilinks, Scrivener hand-off, gestreamde klembordinstellingen, opties voor het insluiten van mindmaps voor OPML/OmniOutliner, Obsidian-integraties of andere processors die afhankelijk zijn van coöperatieve editors.

## Klembordvoorbeeld [clipboard-preview]

![][ClipboardPreviewMenu]

Markdown (of compatibele platte tekst) op het klembord wordt geopend met {% appmenu File, New, Clipboard Preview %} ({% kbd shift cmd V %}). Als het klembord **HTML of RTF** bevat, converteert Marked deze naar een Markdown-achtige bron vóór de voorbeeldweergave, inclusief ruwe kopdetectie wanneer RTF alinea's grote stylesheet-lettergroottes gebruiken.

## Streamingvoorbeeld [streaming-preview]

Bear, Curio, Drafts, The Archive, nvALT, nvUltra en verschillende andere editors kunnen Markdown in Marked pushen terwijl je typt via **Streaming Preview**. Zie [Streaming Preview](Streaming_Preview.html) voor installatie en probleemoplossing.

## Scripts en bonuspakket [scripts-and-bonus-pack]

Automatiseringen voor BBEdit, TextMate, DEVONthink, Emacs, Vim en meer worden geleverd met de [Marked Bonus Pack][bonus]. Installeer of pas deze scripts aan als u menubalk- of editormacro's wilt die verder gaan dan de hierboven genoemde integraties.


[appsettings]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane
[ClipboardPreviewMenu]: images/ClipboardPreviewMenu.jpg @2x width=600px height=198px class=center
[bonus]: https://github.com/kotfu/marked-bonus-pack