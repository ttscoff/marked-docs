# Marked Help — review handoff (pt-BR)

**Locale:** Brazilian Portuguese (`pt-BR`)  
**Generated:** 2026-07-03  
**Status:** Machine-translated drafts — human review required

This package is ready for post-editing. Work in the `pt-BR/` folder on a
`translate/pt-BR` (or `locale/pt-BR`) branch; open one pull request per locale.

---

## What you received

| Item | Location |
|------|----------|
| Topic pages (MT drafts) | `pt-BR/*.md` (2 files) |
| Help index metadata | `pt-BR/config.yaml` |
| Style guide | `pt-BR/SYNTAX.md` |
| Term glossary | `pt-BR/GLOSSARY.md` |
| Menu path reference | `pt-BR/APPMENU.md` |
| App UI strings (read-only reference) | `ui-strings/pt-BR-ui-review.marked-l10n` |
| Screenshot folder (optional) | `pt-BR/images/` (mirror English paths) |

- **English master:** `content/` at repo root (do not edit for locale work)
- **MT banner:** 0 pages still contain `<!-- MT-DRAFT: machine translation; human review required -->` — remove it when a page is reviewed

**Missing pages (115):** `AI_Ask_About_Document.md`, `Additional_Application_Support.md`, `Additional_Help.md`, `Additional_Javascript.md`, `AppleScript_Support.md`, `Autoscroll.md`, `Bear.md`, `Choosing_a_Processor.md`, `Command_Line_Utility.md`, `Comments_and_Annotations.md`, `CommonMark_License.md`, `CommonMark_Spec.md`
… and 103 more

---

## Read first (30 minutes)

1. Root [`README.md`](../README.md) — tags, links, workflow
2. [`SYNTAX.md`](SYNTAX.md) — Spanish tone, pitfalls, checklist
3. [`GLOSSARY.md`](GLOSSARY.md) — agreed EN → Brazilian Portuguese terms
4. [`APPMENU.md`](APPMENU.md) — `{% appmenu %}` paths vs the localized app
5. [`ui-strings/pt-BR-ui-review.marked-l10n`](../ui-strings/pt-BR-ui-review.marked-l10n) — Settings/menus wording to match

---

## Review priorities

### Priority 1 — high-traffic pages

Fix menus and Settings terminology first, then polish prose:

- `Overview.md`, `Live_Markdown_Preview_on_Mac.md`, `Opening_Files.md`
- `Settings_General.md`, `Settings_Preview.md`, `Settings_Export.md`, `Settings_Proofing.md`
- `Keyboard_Shortcuts.md`, `Exporting.md`, `Document_Navigation.md`

### Priority 2 — `config.yaml`

Edit in place under `pt-BR/config.yaml`:

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

### Getting Started (`Getting_Started/`)

- [—] **Overview** — `Overview.md`
- [—] **Live Markdown Preview on Mac** — `Live_Markdown_Preview_on_Mac.md`
- [—] **What's New** — `Whats_New.md`
- [—] **Opening Files** — `Opening_Files.md`
- [—] **Using the Browser Extensions** — `Using_the_Browser_Extensions.md`
- [—] **Quick Open** — `Quick_Open.md`
- [—] **Quick Actions** — `Quick_Actions.md`
- [—] **Choosing a Processor** — `Choosing_a_Processor.md`
- [—] **Previewing** — `Previewing.md`
- [—] **Interface Features** — `Interface_Features.md`
- [—] **Exporting** — `Exporting.md`

### Comparisons & FAQ (`Comparisons_FAQ/`)

- [—] **Marked vs Obsidian Preview** — `Marked_vs_Obsidian_Preview.md`
- [—] **Markdown Preview FAQ** — `Markdown_Preview_FAQ.md`

### Reading Features (`Reading_Features/`)

- [—] **Document Navigation** — `Document_Navigation.md`
- [—] **Wiki Navigation** — `Wiki_Navigation.md`
- [—] **Zoom Overview** — `Zoom_Overview.md`
- [—] **Autoscroll** — `Autoscroll.md`
- [—] **Speed Reading** — `Speed_Reading.md`
- [—] **Ask About Document** — `AI_Ask_About_Document.md`

### Writing Features (`Just_for_Writers/`)

- [—] **Layout and Typography** — `Layout_and_Typography.md`
- [—] **Document Statistics** — `Document_Statistics.md`
- [—] **Multi-file Documents** — `Multi-File_Documents.md`
- [—] **Fountain for Screenwriters** — `Fountain_for_Screenwriters.md`
- [—] **Keyword Highlighting** — `Keyword_Highlighting.md`
- [—] **Spelling and Grammar** — `Spelling_Grammar.md`
- [—] **CriticMarkup** — `CriticMarkup.md`
- [—] **MathJax** — `MathJax.md`
- [—] **Working with DOCX** — `Working_with_DOCX.md`
- [—] **HTML Export** — `HTML_Export.md`
- [—] **EPUB Export** — `EPUB_Export.md`
- [—] **RTF and RTFD Support** — `RTF_Support.md`
- [—] **PDF Import and Export** — `PDF_Support.md`
- [—] **Image Variants** — `Image_Variants.md`
- [—] **Link Validation** — `Link_Validation.md`
- [—] **Comments and Annotations** — `Comments_and_Annotations.md`
- [—] **Features for Coders** — `Features_For_Coders.md`
- [—] **Using Marked with Agentic Coding** — `Using_Marked_with_Agentic_Coding.md`

### Supported Apps (`Supported_Apps/`)

- [—] **Bear** — `Bear.md`
- [—] **Curio** — `Curio.md`
- [—] **DEVONthink** — `DEVONthink.md`
- [—] **Drafts** — `Drafts.md`
- [—] **Folder Watching** — `Folder_Watching.md`
- [—] **Highland** — `Highland.md`
- [—] **Hookmark** — `Hookmark.md`
- [—] **iA Writer** — `iA_Writer.md`
- [—] **iThoughtsX** — `iThoughtsX.md`
- [—] **MarsEdit** — `MarsEdit.md`
- [—] **MindNode** — `MindNode.md`
- [—] **MultiMarkdown Composer** — `MultiMarkdown_Composer.md`
- [—] **nvUltra** — `nvUltra.md`
- [—] **Obsidian** — `Obsidian.md`
- [—] **OmniOutliner and OPML** — `OmniOutliner_and_OPML.md`
- [—] **Scrivener 3 Support** — `Scrivener_Support.md`
- [—] **The Archive** — `The_Archive.md`
- [—] **Ulysses** — `Ulysses.md`
- [—] **Vim** — `Vim.md`
- [—] **VS Code** — `VS_Code.md`
- [—] **VoodooPad** — `VoodooPad.md`
- [—] **Xcode Playgrounds** — `Xcode_Playgrounds.md`
- [—] **DocC Support** — `DocC_Support.md`
- [—] **Additional app integrations** — `Additional_Application_Support.md`

### Advanced Features (`Special_Features/`)

- [—] **Custom Styles** — `Custom_Styles.md`
- [—] **Creating Custom Styles** — `Writing_Custom_CSS.md`
- [—] **Custom Style Generator** — `Custom_Style_Generator.md`
- [—] **Style Manager** — `Style_Manager.md`
- [—] **Style Stealer** — `Style_Stealer.md`
- [—] **Markdownifier** — `Markdownifier.md`
- [—] **Custom Processor** — `Custom_Processor.md`
- [—] **Sandbox Restrictions** — `Sandbox_Restrictions.md`
- [—] **Per-Document Settings** — `Per-Document_Settings.md`
- [—] **Marked Special Syntax** — `Special_Syntax.md`
- [—] **Creating Tables Using CSV Files** — `Creating_Tables_using_CSV_files.md`
- [—] **Embedding Mind Maps and Outlines** — `Embedding_Mind_Maps_and_Outlines.md`
- [—] **Keyboard Shortcuts** — `Keyboard_Shortcuts.md`
- [—] **Workflow Integration** — `Workflow_Integration.md`
- [—] **URL Handler** — `URL_Handler.md`
- [—] **AppleScript Support** — `AppleScript_Support.md`
- [—] **Command Line Utility** — `Command_Line_Utility.md`
- [—] **Streaming Preview** — `Streaming_Preview.md`
- [—] **HTML Specific Settings** — `HTML_Specific_Settings.md`
- [—] **Embedding JavaScript** — `Embedding_Scripts.md`
- [—] **JavaScript API Docs** — `.md`

### Settings (`Settings/`)

- [—] **Settings: General** — `Settings_General.md`
- [—] **Settings: Preview** — `Settings_Preview.md`
- [—] **Settings: Style** — `Settings_Style.md`
- [—] **Settings: Processor** — `Settings_Processor.md`
- [—] **Settings: Applications** — `Settings_Apps.md`
- [—] **Settings: Proofing** — `Settings_Proofing.md`
- [—] **Settings: Export** — `Settings_Export.md`
- [—] **Settings: Advanced** — `Settings_Advanced.md`

### Troubleshooting (`Troubleshooting/`)

- [—] **Preview Not Updating** — `Preview_doesn_t_update_when_file_is_saved.md`
- [—] **Overall Performance** — `Overall_Performance.md`
- [—] **Debugging** — `Troubleshooting.md`
- [—] **Additional Help** — `Additional_Help.md`

### About Markdown (`About_Markdown/`)

- [—] **Processor Selection** — `Processor_Selection.md`
- [—] **Markdown Overview** — `Markdown_Tutorial.md`
- [—] **Markdown Dingus** — `Markdown_Dingus.md`
- [—] **MultiMarkdown v5 Specification** — `MultiMarkdown_v5_Spec.md`
- [—] **CommonMark Specification** — `CommonMark_Spec.md`
- [—] **Kramdown Specification** — `Kramdown_Spec.md`
- [—] **Discount GFM Specification** — `Discount_GFM_Spec.md`

### Credits (`Credits/`)

- [—] **Credits** — `Credits.md`
- [—] **MultiMarkdown License** — `MultiMarkdown_License.md`
- [—] **Discount License** — `Discount_License.md`
- [—] **Kramdown License** — `Kramdown_License.md`
- [—] **CommonMark License** — `CommonMark_License.md`
- [—] **pdf22md License** — `PDF22MD_License.md`

---

## Before you open a PR

- [ ] `{% appmenu %}` paths checked against the localized Marked app
- [ ] Terms match `GLOSSARY.md`; new recurring terms added there
- [ ] `config.yaml` keywords/wiki_keywords reviewed for this locale
- [ ] Link targets and `{% … %}` tags unchanged
- [ ] MT banner removed from pages you finished reviewing
- [ ] Branch contains **only** `pt-BR/` (and `ui-strings/` if UI wording changed)

Mention **@ttscoff** in the PR if you also edited `ui-strings/` (app string merge is separate from help).

---

## Maintainer commands (reference)

```bash
python3 HelpDocs/content/scripts/bootstrap_locales.py pt-BR
python3 HelpDocs/content/scripts/machine_translate_help.py --locale pt-BR
python3 HelpDocs/content/scripts/generate_help_review_handoff.py pt-BR
```
