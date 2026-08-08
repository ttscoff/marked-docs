# <%= @title %>

Marked works with many editors and writing apps. This page covers shared **settings**, the **clipboard preview**, pointers to **streaming preview**, and scripting resources. Detailed guides for popular apps live in their own help topics (see the **Supported Apps** section in the sidebar).

## Per-app guides [per-app-guides]

Start with [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) for the overall workflow. If you use Obsidian, see [Marked vs Obsidian Preview](Marked_vs_Obsidian_Preview.html) to decide when Marked adds value alongside Obsidian's built-in preview.

| Topic | Help page |
| :-- | :-- |
| **Bear** | [Bear](Bear.html) |
| **Curio** (streaming preview) | [Curio](Curio.html) |
| **Drafts** (streaming preview + actions) | [Drafts](Drafts.html) |
| **DEVONthink** (Script menu integration) | [DEVONthink](DEVONthink.html) |
| **Folder watching** (nvALT, nvUltra, etc.) | [Folder Watching](Folder_Watching.html) |
| **Highland** | [Highland](Highland.html) |
| **Hookmark** URL resolution | [Hookmark](Hookmark.html) |
| **iA Writer** | [iA Writer](iA_Writer.html) |
| **iThoughtsX** `.itmz` maps | [iThoughtsX](iThoughtsX.html) |
| **MarsEdit** live preview | [MarsEdit](MarsEdit.html) |
| **MindNode** | [MindNode](MindNode.html) |
| **MultiMarkdown Composer** | [MultiMarkdown Composer](MultiMarkdown_Composer.html) |
| **nvUltra** | [nvUltra](nvUltra.html) |
| **Obsidian** vaults & callouts | [Obsidian](Obsidian.html) |
| **OmniOutliner / OPML** | [OmniOutliner and OPML](OmniOutliner_and_OPML.html) |
| **RTF / RTFD** (Pages, TextEdit, etc.) | [RTF and RTFD Support](RTF_Support.html) |
| **PDF** | [PDF Support](PDF_Support.html) |
| **Scrivener 3** | [Scrivener 3 Support](Scrivener_Support.html) |
| **The Archive** streaming preview | [The Archive](The_Archive.html) |
| **Ulysses** export workflow | [Ulysses](Ulysses.html) |
| **Vim** (vim-marked plugin) | [Vim](Vim.html) |
| **VS Code** (Open in Marked extension) | [VS Code](VS_Code.html) |
| **VoodooPad** | [VoodooPad](VoodooPad.html) |
| **Xcode playgrounds** | [Xcode Playgrounds](Xcode_Playgrounds.html) |

## Application settings [application-settings]

I> Several integrations expose toggles inside {% prefspane Apps %} and {% prefspane Preview %}.

![Application Settings][appsettings]

Use these panes for wiki-link defaults, Scrivener hand-off, streamed clipboard settings, Mind Map embedding options for OPML/OmniOutliner, Obsidian integrations, or other processors that rely on cooperative editors.

## Clipboard Preview [clipboard-preview]

![][ClipboardPreviewMenu]

Markdown (or compatible plain text) in the clipboard opens with {% appmenu File, New, Clipboard Preview %} ({% kbd shift cmd V %}). If the clipboard holds **HTML or RTF**, Marked converts it into Markdown-like source before preview&#8212;including rough heading detection when RTF paragraphs use large stylesheet font sizes.

## Streaming Preview [streaming-preview]

Bear, Curio, Drafts, The Archive, nvALT, nvUltra, and several other editors can push Markdown into Marked as you type via **Streaming Preview**. See [Streaming Preview](Streaming_Preview.html) for setup and troubleshooting.

## Scripts and Bonus Pack [scripts-and-bonus-pack]

Automations for BBEdit, TextMate, DEVONthink, Emacs, Vim, and more ship with the [Marked Bonus Pack][bonus]. Install or adapt those scripts when you want menu-bar or editor macros beyond the integrations listed above.


[appsettings]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane
[ClipboardPreviewMenu]: images/ClipboardPreviewMenu.jpg @2x width=600px height=198px class=center
[bonus]: https://github.com/kotfu/marked-bonus-pack
