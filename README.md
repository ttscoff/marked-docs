# Marked Help — source content for translators

This folder contains the **English source** for Marked's in-app and web help. Translations live in **locale subdirectories** (see layout below). Each locale has its own `config.yaml`, `SYNTAX.md`, and `GLOSSARY.md`.

**Translator repository:** This tree is maintained in the separate **`marked-docs`** Git repository for localization work. It mirrors `HelpDocs/content/` in the main Marked project; merged translations are pulled into Marked before help is built and shipped with the app.

The build pipeline converts Markdown to HTML using **Liquid-style tags** and **double-brace shortcuts**. Most tags stay **unchanged** in translated source; the build resolves localized labels from app string tables where applicable.

---

## Repository layout

```
content/
  README.md              ← this file (English instructions for all locales)
  config.yaml            ← English help index and metadata (master)
  Overview.md            ← English topic pages (same basename in every locale)
  Settings_General.md
  images/                ← English screenshots and shared assets
  _templates/            ← bootstrap templates (maintainers)

  de/
    config.yaml          ← German section titles, keywords, wiki_keywords
    SYNTAX.md            ← German syntax guide (lead translator)
    GLOSSARY.md          ← agreed term translations
    Overview.md          ← translated pages (add as you translate)
    images/              ← localized screenshots (mirror English paths)

  es/  fr/  it/  ja/  nl/  pt-BR/  zh-Hans/  zh-Hant/  hu/
    …                    ← same structure per locale

  ui-strings/            ← localized app UI strings (menus, settings, etc.)
    de-ui-review.marked-l10n
    es-ui-review.marked-l10n
    …                    ← one file per locale
```

Example localized screenshot path (mirrors English):

```
content/images/screenshots/preferences-Advanced.jpg     ← English
de/images/screenshots/preferences-Advanced.jpg            ← German UI capture
```

**English** topic files sit in the **content root**. Each locale directory holds that language's **`config.yaml`**, **`SYNTAX.md`**, **`GLOSSARY.md`**, translated **`.md` files**, and optionally **`images/`** for localized screenshots.

English **`images/`** at the content root is the default for all locales. When you re-capture UI in your language, store files under **your locale folder** using the **same relative path and filename** as English (see Images below).

---

## Workflow (Git)

1. **Assignment** — One lead translator per locale (`de/`, `ja/`, `zh-Hans/`, etc.), even if others contribute. The lead merges work, maintains `SYNTAX.md` and `GLOSSARY.md`, and reviews `config.yaml`.
2. **Branching** — Work in a dedicated branch (for example `translate/de` or `locale/hu`). Do not mix locales in one branch or one pull request.
3. **Scope** — Translate `.md` files into your locale folder. **Keep the same basename** as English (`Exporting.md`, not a translated filename). Cross-links depend on stable names.
4. **Starter files** — Each locale directory already contains `config.yaml`, `SYNTAX.md`, and `GLOSSARY.md`. Customize the latter two before bulk translation; localize `config.yaml` as you go (see below).
5. **Pull requests** — Open a PR when a section or milestone is ready. Note any resolved `{% note %}` blocks or glossary additions.
6. **Review** — Spot-check `{% appmenu %}` paths against the localized app and verify `wiki_keywords` do not collide across pages.

---

## Machine translation first

Most locales start from a **machine-translated draft**, not a blank page. Maintainers generate initial `.md` copies in each locale folder from the English source; your job is to **review and correct**, not translate from scratch.

**Leave alone (even in MT output):**

- All `{% ... %}` tag syntax — especially `{% prefspane General %}` pane IDs
- `{% kbd %}`, `{{cmd}}`, and other shortcut tokens
- Link targets (`Page.html`, `#anchors`, URLs)
- Image paths (`images/...`)
- Page `file` keys in `config.yaml`

**Fix carefully after MT:**

- **`{% appmenu %}` paths** — replace with exact menu strings from the localized app (`MainMenu.strings`, etc.)
- **Settings and UI terminology** — align with `Settings.strings`, `KBShortcuts.strings`, and your locale's `GLOSSARY.md`
- **`config.yaml`** — section titles, `folder` slugs, `keywords`, and `wiki_keywords` (rebuild keyword lists for your language; do not copy English phrases blindly)
- **Prose quality** — tone, idioms, and product-name conventions from your locale's `SYNTAX.md`

Treat MT as a **starting point**. A good first pass is: fix menus and Settings wording, then polish one section at a time.

---

## UI strings (`ui-strings/`)

The **`ui-strings/`** directory holds **`.marked-l10n`** files with the localized strings used throughout Marked's UI — menus, Settings, popups, keyboard shortcut references, statistics labels, tips, and related interface text.

| File pattern | Purpose |
|--------------|---------|
| `<locale>-ui-review.marked-l10n` | Review and edit existing translations for that locale |

These files are the **authoritative handoff** for UI wording. Help documentation should align with the terms in your locale's file (and your `GLOSSARY.md`).

### Changing UI strings

If you need to fix or update text that appears **in the app** (not just in help pages):

1. Edit the appropriate **`<locale>-ui-review.marked-l10n`** file in your locale branch.
2. Change only the **values** on each line (`"key" = "your translation";`). Keep keys unchanged.
3. Preserve placeholders (`%@`, `%ld`, `%1$@`, `\n`) and keyboard symbols.
4. Open a **pull request** with your edits for review.

**Brett** ([@ttscoff](https://github.com/ttscoff)), the Marked developer, merges approved changes into the app's **`.lproj`** string tables for each locale. Translators do not edit `.lproj` files directly in this repository.

When you submit a PR that touches `ui-strings/`, **mention @ttscoff** in the PR description or a comment so the changes can be incorporated into the app build.

---

## What to translate

| Translate | Leave unchanged |
|-----------|-----------------|
| Body text, headings, list items, table descriptions | All `{% ... %}` tag syntax (see below) |
| Link **text** in `[text](Page.html)` | Link **targets** (`Page.html`, `#anchors`, URLs) |
| Text inside `{% download %}` descriptions | Download URLs in `{% download %}` |
| Content inside `{% apponly %}...{% endapponly %}` blocks | `{% prefspane ... %}`, `{% kbd ... %}`, `{{cmd}}`, etc. |
| `I>`, `T>`, `W>`, `E>` blockquote lines (text after the prefix) | Code blocks and inline `` `code` `` unless clearly UI labels |
| Image **alt text** if present | Image **paths** in Markdown (`images/...`) — unchanged in source; localized files live under `<locale>/images/` |

### Images

Re-capturing screenshots in your language is **optional**. When you do, follow this layout:

1. **Mirror the English path** under your locale folder — same directories and **same filename** as in `content/images/`.
2. **Do not rename** image files (links in Markdown stay `images/screenshots/foo.jpg`).
3. **Provide `@2x` variants** when the English source includes them (e.g. `foo.jpg` and `foo@2x.jpg`).

| English | Localized (German example) |
|---------|----------------------------|
| `content/images/screenshots/preferences-Advanced.jpg` | `de/images/screenshots/preferences-Advanced.jpg` |
| `content/images/screenshots/preferences-Advanced@2x.jpg` | `de/images/screenshots/preferences-Advanced@2x.jpg` |

Markdown in translated pages still references `images/...` (same as English). **Do not change** image paths in `.md` files—only add the corresponding files under your locale's `images/` tree.

When capturing:

- Preserve the **intent** of the original (same UI area, same feature highlighted).
- Use the **localized app** (menus and settings in your language).
- Match **dimensions and cropping** to the English shot when possible so layout stays consistent.

---

## Localizing `config.yaml`

Each locale has its own **`config.yaml`** (copied from English with a header comment). The build uses it for the help **sidebar**, **search keywords**, **auto-linking**, and page metadata.

Work in **your locale folder** (`de/config.yaml`, not the root file).

### Translate

| Field | Example | Notes |
|-------|---------|-------|
| `Title` | Marked Help → Marked-Hilfe | Help bundle / site title |
| `MetaDescriptions` | Search, Ask, Changelog, Contents | Short UI strings for special pages |
| Section `title` | Getting Started | Sidebar group heading |
| Section `folder` | Getting_Started | URL/slug segment; translate meaning, keep `_` style |
| Page `title` | Opening Files | Primary page title |
| Page `sidebar_title` | RTF / RTFD | Optional shorter sidebar label |
| Page `description` | … | Search / SEO summary; translate fully |
| Page `keywords` | open, files, recent | Lowercase search terms for your locale |
| Page `wiki_keywords` | quick actions | Phrases that auto-link in help text (see below) |

### Do not change

| Field | Why |
|-------|-----|
| Page `file` | **Must match English** (`Opening_Files`, not translated). Points to `Opening_Files.md` in your locale folder. |
| `MDIndex` | Entry page basename (`Overview`) stays English. |
| `TargetProject`, `WebHelpBaseURL`, `Processor`, `Dependencies`, `Version` | Build / deploy settings (maintainers) |
| Commented-out pages | Leave structure; translate only if uncommented for your locale |

### Section `folder` vs page `file`

- **`folder`** — localized slug for grouping (appears in URLs/paths). Use ASCII letters, numbers, underscores. Example: `Getting_Started` → `Erste_Schritte`.
- **`file`** — **always the English basename** so `[Exporting](Exporting.html)` links work across locales and match the `.md` on disk.

### `keywords`

General search terms for the help index. Use words users in your locale would type. Lowercase, comma-separated in YAML lists. They do not auto-link in prose.

### `wiki_keywords` (auto-linking)

`wiki_keywords` drive **automatic wiki-style links** in rendered help: when that phrase appears in body text, it links to **one** help page.

Rules:

1. **One page per phrase** — Each `wiki_keyword` must appear in **only one** page's list across the entire `config.yaml`. Duplicates make linking ambiguous.
2. **Be specific** — Prefer multi-word phrases (`export as pdf`, `table of contents`) over single common words (`export`, `style`).
3. **Unambiguous** — Avoid terms that could refer to multiple topics. If two pages could match, narrow the phrase or skip auto-linking for that term.
4. **Match translated prose** — After you translate a page, add keywords that actually appear in your translated text (or that you expect writers to use consistently).
5. **Product names** — Usually omit from `wiki_keywords` unless the link target is specifically about that product integration.

Bad (too broad, likely duplicated):

```yaml
wiki_keywords: [export, settings, preview]
```

Good (specific, one target page):

```yaml
wiki_keywords: [export as pdf, paginated pdf, save html]
```

Review the English `config.yaml` for examples, then **rebuild your locale's lists from scratch** — do not copy English phrases that will not appear in translated text.

### `SYNTAX.md` and `GLOSSARY.md`

Each locale folder includes starter files:

- **`SYNTAX.md`** — Lead translator documents tone, punctuation, product-name rules, and locale-specific `{% appmenu %}` conventions.
- **`GLOSSARY.md`** — Table of agreed EN → locale terms; update when you settle on recurring vocabulary.

Fill these in **before** large-scale translation so contributors stay consistent.

---

## Liquid-style tags (`{% ... %}`)

Tags use spaces inside the braces: `{% tag arguments %}`.

**Default rule: leave every `{% tag %}` exactly as in English.** Only translate **plain Markdown text** around them. Exceptions are called out below.

### `{% prefspane PaneName %}` — leave unchanged

References a **Settings window pane**. The argument is an **English pane identifier**, not display text.

Valid pane names used in this documentation:

| Tag argument | Settings area |
|--------------|---------------|
| `General` | General settings |
| `Preview` | Preview settings |
| `Style` | Style settings |
| `Processor` | Processor settings |
| `Apps` | Apps settings |
| `Proofing` | Proofing settings |
| `Export` | Export settings |
| `Advanced` | Advanced settings |

Example (do not translate the tag):

```markdown
Open {% prefspane Advanced %} and enable **Debug Mode**.
```

At build time, this becomes a styled link like **Marked → Settings → Advanced pane**, with the **visible pane name taken from localized `Settings.strings`** in the app. The English identifier in the tag (`Advanced`) is used only as a lookup key (`x-marked-3://pref/advanced`).

Do **not** translate `General`, `Preview`, etc. inside `{% prefspane %}`.

---

### `{% appmenu Menu, Submenu, Item (shortcut) %}` — translate menu path only

Renders a stylized **menu path** (bold top-level menu, italic submenus). Menu names must match the **localized app menus** (`MainMenu.strings`, etc.), not a free translation.

**Syntax:**

```markdown
{% appmenu File, Open... %}
{% appmenu Help, Report an Issue %}
{% appmenu File, New, Clipboard Preview %}
{% appmenu {{gear}}, Proofing, Show Comments %}
{% appmenu File, Open... ({{cmd}}O) %}
{% appmenu Style, Manage Styles (~@$m) %}
```

| Part | Rule |
|------|------|
| First segment | Top-level menu name — translate to match the app |
| Segments after commas | Submenu titles in order — translate to match the app |
| `(shortcut)` at end | Optional; leave shortcut syntax unchanged (see `{% kbd %}`) |
| `{{gear}}` | Gear / preview menu icon placeholder — **leave as `{{gear}}`** |

**Examples**

English source:

```markdown
{% appmenu File, Quick Open %}
```

German (must match `de.lproj/MainMenu.strings`, not literal English):

```markdown
{% appmenu Ablage, Schnell öffnen %}
```

Use the **exact** menu strings from the localized app. If a menu item uses an ellipsis character (`…`), match the app (Unicode ellipsis vs three dots).

---

### `{% kbd ... %}` — leave unchanged

Renders keyboard shortcuts with proper modifier symbols (⌘, ⇧, etc.).

```markdown
{% kbd cmd S %}
{% kbd shift cmd O %}
{% kbd opt cmd E %}
{% kbd cmd shift [/] %}
{% kbd ctrl cmd C %}
{% kbd return %}
{% kbd h %}
```

Supported modifiers: `cmd`, `shift`, `opt`, `ctrl`, `fn`, and aliases (`command`, `option`, `control`, etc.).

Special keys: `return`, `tab`, `esc`, `del`, `gear`, arrow keys, `pgup`, `pgdn`, etc.

Also supports symbol form inside `{% appmenu %}` parentheses: `(@~k)` = Option-Command-K.

**Do not translate** `{% kbd %}` tags. macOS shortcut keys are the same across locales; only the **surrounding prose** is translated.

---

### `{{ ... }}` double-brace shortcuts — leave unchanged

Used mainly in `Keyboard_Shortcuts.md` tables and occasionally inside `{% appmenu %}`.

```markdown
{{cmd}}   {{opt}}   {{shift}}   {{ctrl}}   {{gear}}
{{cmd}}O  {{shift}}{{cmd}}P  {{opt}}{{cmd}}K
```

Same rule as `{% kbd %}`: leave token syntax unchanged; translate the **description column** in shortcut tables.

`{{toc}}` — if present, leave unchanged (auto table of contents).

---

### `{% download "url" "description" %}` — translate description only

```markdown
{% download "https://example.com/file.pkg" "Signed PKG installer. Double-click to install." %}
```

| Part | Rule |
|------|------|
| URL (first quoted string) | Unchanged |
| Description (second quoted string) | Translate |

The Download button label in HTML is generated separately and may be localized by the build pipeline.

---

### Block tags

#### `{% apponly div %}...{% endapponly %}` — translate inner content

Content appears **only in the in-app help browser**, not the public web help. Translate the Markdown inside the block; leave the tags unchanged.

#### `{% note %}...{% endnote %}` — author notes (usually omitted from output)

Used for internal TODOs and editor notes. These blocks are **stripped when help is built** and do not appear to readers.

- You may leave them as-is, delete them, or resolve TODOs and remove the block.
- Do not spend effort polishing text inside `{% note %}` unless asked.

#### `{% notes %}`, `{% comment %}`, `{% todo %}`, `{% fixme %}`

Author-only; stripped at build. Same guidance as `{% note %}`.

---

## Attributed blockquotes (not tags)

Single-line prefixes (not `{%` tags):

```markdown
I> Informational callout (renders as a tip-style blockquote).
T> Same as I> (tip).
W> Warning callout.
E> Error callout.
```

Translate the text **after** the prefix. Keep the prefix letter and `>` unchanged.

---

## Plain Markdown and links

### Internal links

```markdown
See [Exporting](Exporting.html) for details.
See [scroll to edit](Interface_Features.html#scrolltoedit).
```

- Keep `Exporting.html` and other filenames unchanged.
- Keep `#anchor` IDs unchanged unless you add explicit heading IDs and update all references (ask the lead before changing anchors).

### `x-marked-3://` URLs

Deep links into Marked (Settings panes, Dingus, etc.) are generated from tags or written literally. **Do not translate or modify** these URLs.

### Product and technology names

Usually keep in English unless your locale conventionally localizes them:

- **Keep:** Marked, MultiMarkdown, CommonMark, GitHub Flavored Markdown, CriticMarkup, MathJax, KaTeX, Scrivener, AppleScript, etc.
- **Translate:** generic UI words (Settings, Export, Preview) when they appear in **plain text**, not inside tags meant to stay English.

When in doubt, follow your locale's `SYNTAX.md`.

---

## Settings documentation files

Files such as `Settings_General.md`, `Settings_Preview.md`, etc. document one Settings pane each. They use many `{% prefspane %}` tags with **English pane keys** — leave those keys unchanged.

The **setting titles and descriptions** in the body (often definition-list style with `: `) should be translated to match localized `Settings.strings` in the app where possible.

---

## Keyboard Shortcuts page

`Keyboard_Shortcuts.md` is special:

- **Shortcut column:** `{{cmd}}`, `{{shift}}`, etc. — unchanged.
- **Description column:** translate to match localized `KBShortcuts.strings` / menu wording where applicable.

---

## Quick reference: translate or not?

| Construct | Translator action |
|-----------|-------------------|
| `{% prefspane General %}` | **Leave unchanged** (English pane ID) |
| `{% appmenu File, Export %}` | **Translate** menu path to match localized menus |
| `{% kbd shift cmd P %}` | **Leave unchanged** |
| `{{opt}}{{cmd}}K` | **Leave unchanged** |
| `{% download "url" "text" %}` | **Translate** `text` only |
| `{% apponly %}...{% endapponly %}` | **Translate** inner Markdown |
| `{% note %}...{% endnote %}` | Optional; stripped at build |
| `I>`, `W>`, `T>`, `E>` lines | **Translate** after prefix |
| `[link text](Page.html)` | **Translate** link text; keep URL |
| `` `code` `` / fenced blocks | Usually **unchanged** |
| `images/...` in Markdown | **Unchanged** in source; localized files at `<locale>/images/...` (same filename, `@2x` when English has it) |

---

## Questions

Open an issue or contact the Marked documentation maintainer if:

- A menu path in English does not exist in your localized app (menu restructuring).
- You need the exact localized string for an `{% appmenu %}` segment (check `MainMenu.strings`, `QuickPanels.strings`, or ask for an export).
- You are unsure whether a phrase is a product name or generic UI copy.

---

## Automation (maintainers)

English source uses **English pane IDs** in `{% prefspane %}`. The build pipeline will resolve visible labels from `en.lproj` / locale `Settings.strings` while keeping stable `x-marked-3://pref/...` links. Translators should not duplicate that logic in Markdown.

Locale help builds may also resolve `{% appmenu %}` from localized string tables in the future; until then, translators update menu paths by hand (see **Machine translation first** above).

To (re)create locale scaffolding:

```bash
python3 HelpDocs/content/scripts/bootstrap_locales.py
python3 HelpDocs/content/scripts/bootstrap_locales.py --locale de --force-config
```

Templates live in `content/_templates/`.
