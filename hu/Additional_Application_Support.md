<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked számos szerkesztővel és íróalkalmazással működik. Ez az oldal a megosztott **beállításokat**, a **vágólap előnézetét**, a **streaming előnézetre** mutató mutatókat és a parancsfájl-erőforrásokat tartalmazza. A népszerű alkalmazások részletes útmutatói a saját súgótémájukban találhatók (lásd az oldalsáv **Támogatott alkalmazások** szakaszát).

## Alkalmazásonkénti útmutatók [per-app-guides]

Kezdje a [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) elemmel az általános munkafolyamathoz. Ha Obsidian-t használ, tekintse meg a [Marked vs Obsidian Preview](Marked_vs_Obsidian_Preview.html) részt annak eldöntéséhez, hogy a Marked mikor ad hozzá értéket az Obsidian beépített előnézetéhez.

| Téma | Súgó oldal |
| :-- | :-- |
| **Medve** | [Medve](Bear.html) |
| **Curio** (streaming előnézet) | [Curio](Curio.html) |
| **Piszkozatok** (streaming előnézet + műveletek) | [Piszkozatok](Drafts.html) |
| **DEVONthink** (Script menü integráció) | [DEVONthink](DEVONthink.html) |
| **Mappafigyelés** (nvALT, nvUltra stb.) | [Mappafigyelés](Folder_Watching.html) |
| **Felföld** | [Felföld](Highland.html) |
| **Hookmark** URL felbontás | [Hookmark](Hookmark.html) |
| **iA Writer** | [iA Writer](iA_Writer.html) |
| **iThoughtsX** `.itmz` térképek | [iThoughtsX](iThoughtsX.html) |
| **MarsEdit** élő előnézet | [MarsEdit](MarsEdit.html) |
| **MindNode** | [MindNode](MindNode.html) |
| **MultiMarkdown Composer** | [MultiMarkdown Composer](MultiMarkdown_Composer.html) |
| **nvUltra** | [nvUltra](nvUltra.html) |
| **Obszidián** boltívek és feliratok | [Obszidián](Obsidian.html) |
| **OmniOutliner / OPML** | [OmniOutliner és OPML](OmniOutliner_and_OPML.html) |
| **RTF / RTFD** (Oldalak, TextEdit stb.) | [RTF és RTFD támogatás](RTF_Support.html) |
| **PDF** | [PDF támogatás](PDF_Support.html) |
| **Scrivener 3** | [Scrivener 3 támogatás](Scrivener_Support.html) |
| **The Archive** streaming előnézet | [Az archívum](The_Archive.html) |
| **Ulysses** export munkafolyamat | [Ulysses](Ulysses.html) |
| **Vim** (vim-jelölésű bővítmény) | [Vim](Vim.html) |
| **VS Code** (Megjelölt bővítményben nyitva) | [VS kód](VS_Code.html) |
| **VoodooPad** | [VoodooPad](VoodooPad.html) |
| **Xcode játszóterek** | [Xcode Playgrounds](Xcode_Playgrounds.html) |

## Alkalmazásbeállítások [application-settings]

I> Számos integráció kapcsolót tesz elérhetővé a {% prefspane Apps %} és az {% prefspane Preview %} között.

![Alkalmazásbeállítások][alkalmazásbeállítások]

Használja ezeket a paneleket a wikilink alapértelmezéseihez, a Scrivener átadáshoz, a streamelt vágólap beállításaihoz, az OPML/OmniOutliner Mind Map beágyazási opcióihoz, az Obsidian integrációkhoz vagy más olyan processzorokhoz, amelyek együttműködő szerkesztőkre támaszkodnak.

## Vágólap előnézete [clipboard-preview]

![][ClipboardPreviewMenu]

A Markdown (vagy kompatibilis egyszerű szöveg) a vágólapon a {% appmenu File, New, Clipboard Preview %} ({% kbd shift cmd V %}) gombbal nyílik meg. Ha a vágólap **HTML-t vagy RTF-et** tartalmaz, a Marked azt Markdown-szerű forrásba konvertálja az előnézet előtt – beleértve a durva fejlécészlelést, amikor az RTF bekezdések nagy stíluslap-betűméreteket használnak.

## Streaming előnézet [streaming-preview]

A Bear, a Curio, a Drafts, az Archive, az nvALT, az nvUltra és számos más szerkesztő a **Streaming előnézet** segítségével beírhatja a Markdownt a Markedbe, miközben gépel. A beállításhoz és a hibaelhárításhoz lásd: [Streaming előnézet](Streaming_Preview.html).

## Szkriptek és bónuszcsomag [scripts-and-bonus-pack]

A BBEdit, a TextMate, a DEVONthink, az Emacs, a Vim és más alkalmazások automatizálása a [Marked Bonus Pack][bónusz] csomaggal érkezik. Telepítse vagy módosítsa ezeket a szkripteket, ha menüsor- vagy szerkesztőmakrókat szeretne a fent felsorolt ​​integrációkon túl.


[appsettings]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane
[ClipboardPreviewMenu]: images/ClipboardPreviewMenu.jpg @2x width=600px height=198px class=center
[bonus]: https://github.com/kotfu/marked-bonus-pack