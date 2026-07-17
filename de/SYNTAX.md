# Syntax guide — German (de)

Practical conventions for the German docs. Read this and `GLOSSARY.md` before translating. Terms and style are aligned with the localized Marked app (`de.lproj`) so the docs match the UI.

## Common pitfalls (quick checklist)

Recurring things to watch when post-editing the machine-translated drafts:

1. **Reference-link definitions** (`[label]: url`) each on their own line — never collapse several onto one line, or all but the first break.
2. **Translate the link text, keep the target:** in `[text](Target.html)` and `[text][label]`, translate the visible text; the filename and the `[label]` stay English. Exception: product, format, and feature names stay English even as link text — see *Links and filenames*.
3. **Dash:** the German parenthetical dash is `–` (en dash with spaces), not `---` or `—`.
4. **Block tags** (`{% apponly div %}`, `{% endapponly %}`, …) on their own line, no trailing spaces.
5. **Localize syntax example words, consistently:** `*kursiv*`, `**fett**` (not `*italics*` / `**bold**`).
6. **UI and technical terms → match the app and Apple:** e.g. „AppleScript-Wörterbuch“ (not „-Verzeichnis“); menu paths exactly from the German app.
7. **Keep verb forms parallel:** „… ausgeben oder … kopieren“, not „ausgegeben … kopieren“.
8. **Basics:** Sie throughout; product names stay English (Marked, Markdown, MultiMarkdown, CommonMark …); German quotes „…“; ellipsis `…`.

## Tone and audience

- **Formality: Sie.** The German app UI uses formal address throughout; keep the docs consistent with it. Never switch to „du“.
- **Audience:** Mac users who write in Markdown; assume familiarity with menus and keyboard shortcuts.
- **Voice:** Follow macOS German (Apple style). Avoid literal translations of English idioms; rephrase for natural German.

## Product and technology names

| Term | Treatment |
|------|-----------|
| Marked | Keep as **Marked** |
| MultiMarkdown, CommonMark, CriticMarkup, MathJax, KaTeX, GitHub Flavored Markdown | Keep English |
| macOS, Finder, Dock, AppleScript | Keep English (Apple's German UI keeps them) |
| App names (Scrivener, Obsidian, Bear, Drafts, …) | Keep English |

## UI strings and control style

This is where the German UI localization was weakest; keep the docs on the corrected style:

- **Quote the corrected string, not the shipped one.** When the prose cites a menu or option label, use the fixed wording from `ui-strings/de-ui-review.marked-l10n`, not the (still wrong) string in the currently installed app. Docs and the UI fixes ship together, so the docs follow the target wording (e.g. „Neue Dateien automatisch bearbeiten“, not „Bearbeiten Sie neue Dateien automatisch“).
- **Control labels → infinitive**, not a Sie-imperative. `Enable Leanpub support` → „Leanpub-Unterstützung aktivieren“ (nicht „Aktivieren Sie …“).
- **Descriptive tooltips → third person present**, matching the app. `Prints a horizontal line …` → „Druckt eine horizontale Linie …“ (nicht „Drucken Sie …“).
- **Genuine user instructions stay in Sie.** „Klicken Sie auf das Feld …“, „Ziehen Sie ein Bild …“ — where the reader really is told to act.
- **`{% appmenu %}` segments** must match the localized app menus exactly: `Ablage`, `Bearbeiten`, `Darstellung`, `Fenster`, `Hilfe`, `Einstellungen…`, `Exportieren…`, `Im Finder anzeigen`, … (verify against `MainMenu.strings`, incl. the ellipsis `…`).
- **`{% prefspane %}` / `{% kbd %}` / `{{cmd}}`:** leave tags unchanged (see root `README.md`).
- **Preposition before `{% prefspane %}`:** at build time the tag renders as a breadcrumb link (e.g. „Marked → Einstellungen → Stil“), so it cannot fuse with „im/in dem“. Write „unter {% prefspane X %}“, not „im {% prefspane X %}“ — the English „in the … pane“ does not carry over.
- **Settings pane names in prose:** use the same wording as localized `Settings.strings`.

## Punctuation and typography

- Quotation marks: German „…“ (`„` U+201E … `“` U+201C). Not straight `"..."`.
- Ellipsis: Unicode `…`, matching the app (nicht drei Punkte `...`).
- Dash: Halbgeviertstrich `–` for parentheticals, not the em dash `—`.
- Decimal/thousands: German conventions (1.000, 3,5).

## Links and filenames

- Keep `.md` / `.html` filenames identical to English (`Exporting.md`, not translated).
- Translate link **anchor text** only, never the target.
- **Link text: German for descriptive titles, English for names.** Translate page-title link text to German (`[Opening Files]` → „[Dateien öffnen]“, `[Exporting]` → „[Export]“, `[Working With DOCX]` → „[Arbeiten mit DOCX]“). But keep product, format, and feature names English even as link text: `[RTF]`, `[DOCX]`, `[Scrivener]`, `[MathJax]`, `[Fountain]`, `[Autoscroll]`, `[Speed Reading]`, `[pdf22md]`.
- Do not change `#anchor` IDs unless you add explicit heading IDs and update all references (ask the lead first).
- **Cross-page anchors break when you translate a heading.** A link like `Exporting.html#headers-and-footers` targets a heading whose slug is derived from the *English* text; translating that heading („## Kopf- und Fußzeilen“) changes the slug and the inbound link dies — in every language. Fix by pinning the English anchor on the translated heading with an explicit ID: `## Kopf- und Fußzeilen [headers-and-footers]`. Before translating a page's headings, check who links into its sections (`grep -rn "ThisPage.html#"`), and pin every incoming anchor.

## Code blocks and examples

The rule of thumb: anything the reader **types** stays English, anything the reader **reads** becomes German.

- **Commands, options, keys, and values are literal — never translate them.** The machine translation broke this repeatedly, because inside a damaged fence it no longer recognized the text as code: `cat notes.md` → „Katzennotizen.md“, `pbpaste | markdown` → „pbpaste | Abschlag“, `head -20` → „Kopf -20“, `processor=multimarkdown` → „Prozessor=Multimarkdown“, `mk --dojs "…" all` → „alle“. The same holds for AppleScript commands (`open streaming preview`, `get statistics`), `with` record keys (`style`, `pageSize`, `margins`), metadata keys, CSS values (`pre`, `pre-wrap`, `inherit`), and JSON keys (`macros`, `equationNumbers`).
- **Comments inside code blocks are prose — translate them.** `# Open a file` → „# Datei öffnen“. They are read, not executed, so translating them breaks nothing and helps the reader. Infinitive, like control labels.
- **Illustrative example content is prose — translate it.** Where an example shows Markdown the reader would see rendered, translate it: `mk --preview "## Hello\n\nThis is **markdown** text!"` → „## Hallo\n\nDies ist **Markdown**-Text!“. Placeholder values too: `Example metadata: example value` → „Beispiel-Metadatum: Beispielwert“.
- **Indentation marks literal code too, and it goes missing the same way.** A four-space or tab indent makes a code block just as a fence does, and the machine translation dropped it in places, with the same consequence: the block stops being code and its contents get translated. In `Fountain_for_Screenwriters` the opening `[scrippet]` lost its indent while the closing tag kept it. In `Keyword_Highlighting` the regex `/\\S*?ly/` lost its indent and was then translated to `/\\Listig/`, because `S*?ly` looks like „sly“. Neither shows up in a fence count, so compare indented lines too: `grep -cE '^(    |\t)\S' Page.md de/Page.md` must match.
- **Check the fences before you post-edit.** In several files the machine translation turned ```` ```bash ```` into „Bash and the closing ```` ``` ```` into „, which silently un-codes the whole block — it renders as body text, `#` comments become headings, and the commands inside were then translated too. Compare against the English original before you touch the prose: `grep -c '^```' Page.md de/Page.md` must match, and `grep -n '^„' de/Page.md` must not land on a fence.

## `config.yaml` for this locale

Per root `README.md`: translate section `title`, `folder` slugs, page `title`/`sidebar_title`, `description`, `keywords`, and `wiki_keywords`. **`file:` values stay English.** Rebuild `wiki_keywords` from the translated prose; do not copy English phrases.

## Review checklist (before opening a PR)

- [ ] `{% appmenu %}` paths verified against the localized app
- [ ] Control labels in infinitive, descriptive tooltips in third person
- [ ] „Überschrift“ used for headings (never „Schlagzeile“)
- [ ] Sie used consistently, German quotes „…“ and ellipsis `…`
- [ ] `.md`/`.html` filenames and `{% … %}` tags unchanged
- [ ] Code-fence count matches the English original, no `„` where a ``` belongs
- [ ] Indented-line count matches the English original (indentation marks literal code too)
- [ ] Commands, keys, and values in code blocks identical to English; comments and example content German
- [ ] Link text German for descriptive titles, English for product/format/feature names
- [ ] Cross-page anchor targets pinned with explicit `[id]` where the heading was translated
- [ ] Terms match `GLOSSARY.md`; new recurring terms added there
