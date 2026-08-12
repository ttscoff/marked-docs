<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Marked funziona con molti editor e app di scrittura. Questa pagina copre le **impostazioni** condivise, l'**anteprima degli appunti**, i puntatori all'**anteprima in streaming** e le risorse di scripting. Guide dettagliate per le app più diffuse si trovano negli argomenti della guida dedicati (vedi la sezione **App supportate** nella barra laterale).

## Guide per app [per-app-guides]

Inizia con [Anteprima Live Markdown su Mac](Live_Markdown_Preview_on_Mac.html) per il flusso di lavoro complessivo. Se usi Obsidian, consulta [Anteprima Marked vs Obsidian](Marked_vs_Obsidian_Preview.html) per decidere quando Marked aggiunge valore insieme all'anteprima integrata di Obsidian.

| Argomento | Pagina di aiuto |
| :-- | :-- |
| **Bear** | [Bear](Bear.html) |
| **Curio** (anteprima in streaming) | [Curio](Curio.html) |
| ** Drafts** (anteprima in streaming + azioni) | [Drafts](Drafts.html) |
| **DEVONthink** (integrazione del menu Script) | [DEVONthink](DEVONthink.html) |
| **Visualizzazione cartelle** (nvALT, nvUltra, ecc.) | [Visione cartella](Folder_Watching.html) |
| ** Highland** | [Highland](Highland.html) |
| ** Hookmark** Risoluzione URL | [Hookmark](Hookmark.html) |
| **iA Writer** | [iA Writer](iA_Writer.html) |
| **iThoughtsX** `.itmz` mappe | [iPensieriX](iThoughtsX.html) |
| **MarsEdit** anteprima dal vivo | [MarsEdit](MarsEdit.html) |
| **MindNode** | [MindNode](MindNode.html) |
| **MultiMarkdown_Composer** | [MultiMarkdown_Composer](MultiMarkdown_Composer.html) |
| **nvUltra** | [nvUltra](nvUltra.html) |
| **Obsidian** | [Obsidian](Obsidian.html) |
| **OmniOutliner/OPML** | [OmniOutliner e OPML](OmniOutliner_and_OPML.html) |
| **RTF / RTFD** (Pagine, TextEdit, ecc.) | [Supporto RTF e RTFD](RTF_Support.html) |
| **PDF_Support** | [PDF_Support](PDF_Support.html) |
| **Scrivener 3** | [Supporto per Scrivener 3](Scrivener_Support.html) |
| **The_Archive** anteprima in streaming | [The_Archive](The_Archive.html) |
| Flusso di lavoro di esportazione di **Ulysses** | [Ulysses](Ulysses.html) |
| **Vim** (plugin contrassegnato con vim) | [Vim](Vim.html) |
| **VS_Code** (Apri nell'estensione contrassegnata) | [VS_Code](VS_Code.html) |
| **VoodooPad** | [VoodooPad](VoodooPad.html) |
| **Xcode Playgrounds** | [Xcode Playgrounds](Xcode_Playgrounds.html) |

## Impostazioni dell'applicazione [application-settings]

I> Diverse integrazioni espongono i commutatori all'interno di {% prefspane Apps %} e {% prefspane Preview %}.

![Impostazioni applicazione][appsettings]

Utilizza questi riquadri per le impostazioni predefinite dei collegamenti wiki, la consegna di Scrivener, le impostazioni degli appunti in streaming, le opzioni di incorporamento della mappa mentale per OPML/OmniOutliner, le integrazioni di Obsidian o altri processori che si basano su editor cooperativi.

## Anteprima degli appunti [clipboard-preview]

![][Menu Anteprima Appunti]

Markdown (o testo normale compatibile) negli appunti si apre con {% appmenu File, New, Clipboard Preview %} ({% kbd shift cmd V %}). Se gli appunti contengono **HTML o RTF**, Marked lo converte in un sorgente simile a Markdown prima dell'anteprima, incluso il rilevamento approssimativo dell'intestazione quando i paragrafi RTF utilizzano caratteri di grandi dimensioni del foglio di stile.

## Anteprima in streaming [streaming-preview]

Bear, Curio, Drafts, The Archive, nvALT, nvUltra e molti altri editor possono inserire Markdown in Marked durante la digitazione tramite **Anteprima streaming**. Vedi [Anteprima streaming](Streaming_Preview.html) per la configurazione e la risoluzione dei problemi.

## Script e pacchetto bonus [scripts-and-bonus-pack]

Le automazioni per BBEdit, TextMate, DEVONthink, Emacs, Vim e altre vengono fornite con il [Marked Bonus Pack] [bonus]. Installa o adatta questi script quando desideri macro della barra dei menu o dell'editor oltre alle integrazioni elencate sopra.


[appsettings]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane
[ClipboardPreviewMenu]: images/ClipboardPreviewMenu.jpg @2x width=600px height=198px class=center
[bonus]: https://github.com/kotfu/marked-bonus-pack