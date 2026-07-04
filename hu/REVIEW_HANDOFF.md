# Marked Help — review handoff (hu)

**Locale:** Hungarian (`hu`)  
**Generated:** 2026-07-04  
**Status:** Machine-translated drafts — human review required

This package is ready for post-editing. Work in the `hu/` folder on a
`translate/hu` (or `locale/hu`) branch; open one pull request per locale.

---

## What you received

| Item | Location |
|------|----------|
| Topic pages (MT drafts) | `hu/*.md` (117 files) |
| Help index metadata | `hu/config.yaml` |
| Style guide | `hu/SYNTAX.md` |
| Term glossary | `hu/GLOSSARY.md` |
| Menu path reference | `hu/APPMENU.md` |
| App UI strings (read-only reference) | `ui-strings/hu-ui-review.marked-l10n` |
| Screenshot folder (optional) | `hu/images/` (mirror English paths) |

- **English master:** `content/` at repo root (do not edit for locale work)
- **MT banner:** 115 pages still contain `<!-- MT-DRAFT: machine translation; human review required -->` — remove it when a page is reviewed

---

## Read first (30 minutes)

1. Root [`README.md`](../README.md) — tags, links, workflow
2. [`SYNTAX.md`](SYNTAX.md) — Spanish tone, pitfalls, checklist
3. [`GLOSSARY.md`](GLOSSARY.md) — agreed EN → Hungarian terms
4. [`APPMENU.md`](APPMENU.md) — `{% appmenu %}` paths vs the localized app
5. [`ui-strings/hu-ui-review.marked-l10n`](../ui-strings/hu-ui-review.marked-l10n) — Settings/menus wording to match

---

## Review priorities

### Priority 1 — high-traffic pages

Fix menus and Settings terminology first, then polish prose:

- `Overview.md`, `Live_Markdown_Preview_on_Mac.md`, `Opening_Files.md`
- `Settings_General.md`, `Settings_Preview.md`, `Settings_Export.md`, `Settings_Proofing.md`
- `Keyboard_Shortcuts.md`, `Exporting.md`, `Document_Navigation.md`

### Priority 2 — `config.yaml`

Edit in place under `hu/config.yaml`:

- `Title`, `MetaDescriptions`, section `title`, `folder` slugs
- Page `title`, `sidebar_title`, `description`
- `keywords` and `wiki_keywords` — rewrite for Spanish search; do not copy English phrases blindly
- **Never change** `file:` keys (English basenames) or build paths (`TargetProject`, `WebHelpBaseURL`, …)

### Priority 3 — integration pages

Editor/app pages (`VS_Code.md`, `Obsidian.md`, `Scrivener_Support.md`, …) — verify product names stay English.

### Priority 4 — spec / reference pages

Syntax spec pages (`CommonMark_Spec.md`, `Kramdown_Spec.md`, …) — keep code blocks intact; translate descriptions only.

---

## Leave unchanged

| Keep as-is | Examples |
|------------|----------|
| Topic filenames | `Exporting.md`, not translated names |
| Link targets | `Page.html`, `#anchors`, `https://…`, `x-marked-3://…` |
| Liquid tags | `{% prefspane General %}`, `{% kbd shift cmd P %}` |
| Shortcut tokens | `{{cmd}}`, `{{opt}}`, `{{shift}}` |
| `config.yaml` `file:` keys | `Overview`, `Settings_General`, … |
| Image paths in Markdown | `images/screenshots/…` |

---

## Fix carefully after MT

1. **`{% appmenu File, Export %}`** — each segment must match `MainMenu.strings` (see `APPMENU.md`)
2. **Settings panes in prose** — align with localized `Settings.strings` / `Preferences.strings`
3. **Reference links** — one `[label]: url` definition per line
4. **Syntax examples** — use Spanish demo words (`*cursiva*`, `**negrita**`) where the English source uses *italics* / **bold**
5. **`wiki_keywords`** — short phrases users might type; must not collide across pages (see root README)

---

## Suggested section order

### Kezdő lépések (`Kezdő lépések/`)

- [✓] **Áttekintés** — `Overview.md`
- [✓] **Élő Markdown előnézet Macen** — `Live_Markdown_Preview_on_Mac.md`
- [✓] **Újdonságok** — `Whats_New.md`
- [✓] **Fájlok megnyitása** — `Opening_Files.md`
- [✓] **A böngészőbővítmények használata** — `Using_the_Browser_Extensions.md`
- [✓] **Gyors nyitás** — `Quick_Open.md`
- [✓] **Gyors műveletek** — `Quick_Actions.md`
- [✓] **Processzor kiválasztása** — `Choosing_a_Processor.md`
- [✓] **Előnézet** — `Previewing.md`
- [✓] **Interfész jellemzők** — `Interface_Features.md`
- [✓] **Exportálás** — `Exporting.md`

### Összehasonlítások és GYIK (`Összehasonlítások_GYIK/`)

- [✓] **Marked vs Obsidian Preview** — `Marked_vs_Obsidian_Preview.md`
- [✓] **Markdown előnézeti GYIK** — `Markdown_Preview_FAQ.md`

### Olvasási funkciók (`Reading_Features/`)

- [✓] **Dokumentumnavigáció** — `Document_Navigation.md`
- [✓] **Wiki Navigáció** — `Wiki_Navigation.md`
- [✓] **Nagyítás áttekintése** — `Zoom_Overview.md`
- [✓] **Automatikus görgetés** — `Autoscroll.md`
- [✓] **Gyorsolvasás** — `Speed_Reading.md`
- [✓] **Kérdezzen a dokumentumról** — `AI_Ask_About_Document.md`

### Írás jellemzői (`Just_for_Writers/`)

- [✓] **Elrendezés és tipográfia** — `Layout_and_Typography.md`
- [✓] **Dokumentumstatisztika** — `Document_Statistics.md`
- [✓] **Több fájlból álló dokumentumok** — `Multi-File_Documents.md`
- [✓] **Szökőkút forgatókönyvíróknak** — `Fountain_for_Screenwriters.md`
- [✓] **Kulcsszókiemelés** — `Keyword_Highlighting.md`
- [✓] **Helyesírás és nyelvtan** — `Spelling_Grammar.md`
- [✓] **CriticMarkup** — `CriticMarkup.md`
- [✓] **MathJax** — `MathJax.md`
- [—] **Dolgozik a DOCX-szel** — `Working_with_DOCX.md`
- [✓] **HTML exportálás** — `HTML_Export.md`
- [✓] **EPUB exportálás** — `EPUB_Export.md`
- [✓] **RTF és RTFD támogatás** — `RTF_Support.md`
- [✓] **PDF importálás és exportálás** — `PDF_Support.md`
- [✓] **Képváltozatok** — `Image_Variants.md`
- [✓] **Link érvényesítése** — `Link_Validation.md`
- [✓] **Megjegyzések és megjegyzések** — `Comments_and_Annotations.md`
- [✓] **Funkciók kódolók számára** — `Features_For_Coders.md`
- [✓] **Ügynöki kódolással jelölt használata** — `Using_Marked_with_Agentic_Coding.md`

### Támogatott alkalmazások (`Támogatott_alkalmazások/`)

- [✓] **Medve** — `Bear.md`
- [✓] **Ritka műalkotás** — `Curio.md`
- [✓] **DEVONgondolkozz** — `DEVONthink.md`
- [✓] **Dámajáték** — `Drafts.md`
- [✓] **Mappafigyelés** — `Folder_Watching.md`
- [✓] **Felvidéki** — `Highland.md`
- [✓] **Hookmark** — `Hookmark.md`
- [✓] **iA író** — `iA_Writer.md`
- [✓] **iThoughtsX** — `iThoughtsX.md`
- [✓] **MarsEdit** — `MarsEdit.md`
- [✓] **MindNode** — `MindNode.md`
- [✓] **MultiMarkdown zeneszerző** — `MultiMarkdown_Composer.md`
- [✓] **nvUltra** — `nvUltra.md`
- [✓] **Obszidián** — `Obsidian.md`
- [✓] **OmniOutliner és OPML** — `OmniOutliner_and_OPML.md`
- [✓] **Scrivener 3 támogatás** — `Scrivener_Support.md`
- [✓] **Az archívum** — `The_Archive.md`
- [✓] **Ulysses** — `Ulysses.md`
- [✓] **Vim** — `Vim.md`
- [✓] **VS kód** — `VS_Code.md`
- [✓] **VoodooPad** — `VoodooPad.md`
- [✓] **Xcode játszóterek** — `Xcode_Playgrounds.md`
- [✓] **DocC támogatás** — `DocC_Support.md`
- [✓] **További alkalmazásintegrációk** — `Additional_Application_Support.md`

### Speciális funkciók (`Special_Features/`)

- [✓] **Egyedi stílusok** — `Custom_Styles.md`
- [✓] **Egyedi stílusok létrehozása** — `Writing_Custom_CSS.md`
- [✓] **Egyedi stílusgenerátor** — `Custom_Style_Generator.md`
- [✓] **Stíluskezelő** — `Style_Manager.md`
- [✓] **Stíluslopó** — `Style_Stealer.md`
- [✓] **Markdownifier** — `Markdownifier.md`
- [✓] **Egyedi processzor** — `Custom_Processor.md`
- [✓] **Sandbox korlátozások** — `Sandbox_Restrictions.md`
- [✓] **Dokumentumonkénti beállítások** — `Per-Document_Settings.md`
- [✓] **Megjelölve speciális szintaxis** — `Special_Syntax.md`
- [✓] **Táblázatok létrehozása CSV-fájlok használatával** — `Creating_Tables_using_CSV_files.md`
- [✓] **Gondolattérképek és körvonalak beágyazása** — `Embedding_Mind_Maps_and_Outlines.md`
- [✓] **Billentyűparancsok** — `Keyboard_Shortcuts.md`
- [✓] **Munkafolyamat-integráció** — `Workflow_Integration.md`
- [✓] **URL-kezelő** — `URL_Handler.md`
- [✓] **AppleScript támogatás** — `AppleScript_Support.md`
- [✓] **Command Line Utility** — `Command_Line_Utility.md`
- [✓] **Streaming előnézet** — `Streaming_Preview.md`
- [✓] **HTML-specifikus beállítások** — `HTML_Specific_Settings.md`
- [✓] **JavaScript beágyazása** — `Embedding_Scripts.md`
- [—] **JavaScript API dokumentumok** — `.md`

### Beállítások elemre (`Beállítások elemre/`)

- [✓] **Beállítások: Általános** — `Settings_General.md`
- [✓] **Beállítások: Előnézet** — `Settings_Preview.md`
- [✓] **Beállítások: Stílus** — `Settings_Style.md`
- [✓] **Beállítások: Processzor** — `Settings_Processor.md`
- [✓] **Beállítások: Alkalmazások** — `Settings_Apps.md`
- [✓] **Beállítások: Proofing** — `Settings_Proofing.md`
- [✓] **Beállítások: Exportálás** — `Settings_Export.md`
- [✓] **Beállítások: Speciális** — `Settings_Advanced.md`

### Hibaelhárítás (`Hibaelhárítás/`)

- [✓] **Az előnézet nem frissül** — `Preview_doesn_t_update_when_file_is_saved.md`
- [✓] **Teljes teljesítmény** — `Overall_Performance.md`
- [✓] **Hibakeresés** — `Troubleshooting.md`
- [✓] **További segítség** — `Additional_Help.md`

### A Markdownról (`About_Markdown/`)

- [✓] **Processzor kiválasztása** — `Processor_Selection.md`
- [✓] **Markdown áttekintése** — `Markdown_Tutorial.md`
- [✓] **Markdown Dingus** — `Markdown_Dingus.md`
- [✓] **MultiMarkdown v5 specifikáció** — `MultiMarkdown_v5_Spec.md`
- [✓] **CommonMark specifikáció** — `CommonMark_Spec.md`
- [✓] **Kramdown specifikáció** — `Kramdown_Spec.md`
- [✓] **Akciós GFM specifikáció** — `Discount_GFM_Spec.md`

### Kredit (`Kredit/`)

- [✓] **Kredit** — `Credits.md`
- [✓] **MultiMarkdown licenc** — `MultiMarkdown_License.md`
- [✓] **Kedvezményes licenc** — `Discount_License.md`
- [✓] **Kramdown licenc** — `Kramdown_License.md`
- [✓] **CommonMark licenc** — `CommonMark_License.md`
- [✓] **pdf22md licenc** — `PDF22MD_License.md`

---

## Before you open a PR

- [ ] `{% appmenu %}` paths checked against the localized Marked app
- [ ] Terms match `GLOSSARY.md`; new recurring terms added there
- [ ] `config.yaml` keywords/wiki_keywords reviewed for this locale
- [ ] Link targets and `{% … %}` tags unchanged
- [ ] MT banner removed from pages you finished reviewing
- [ ] Branch contains **only** `hu/` (and `ui-strings/` if UI wording changed)

Mention **@ttscoff** in the PR if you also edited `ui-strings/` (app string merge is separate from help).

---

## Maintainer commands (reference)

```bash
python3 HelpDocs/content/scripts/bootstrap_locales.py hu
python3 HelpDocs/content/scripts/machine_translate_help.py --locale hu
python3 HelpDocs/content/scripts/generate_help_review_handoff.py hu
```
