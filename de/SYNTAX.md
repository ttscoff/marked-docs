# Syntax guide — German (de)

Practical conventions for the German docs. Read this and `GLOSSARY.md` before translating. Terms and style are aligned with the localized Marked app (`de.lproj`) so the docs match the UI.

## Common pitfalls (quick checklist)

Recurring things to watch when post-editing the machine-translated drafts:

1. **Reference-link definitions** (`[label]: url`) each on their own line — never collapse several onto one line, or all but the first break.
2. **Translate the link text, keep the target:** in `[text](Target.html)` and `[text][label]`, translate only the visible text; the filename and the `[label]` stay English.
3. **Dash:** the German parenthetical dash is `–` (en dash with spaces), not `---` or `—`.
4. **Block tags** (`{% apponly div %}`, `{% endapponly %}`, …) on their own line, no trailing spaces.
5. **Localize syntax example words, consistently:** `*kursiv*`, `**fett**` (not `*italics*` / `**bold**`).
6. **UI and technical terms → match the app and Apple:** e.g. „AppleScript-Wörterbuch" (not „-Verzeichnis"); menu paths exactly from the German app.
7. **Keep verb forms parallel:** „… ausgeben oder … kopieren", not „ausgegeben … kopieren".
8. **Basics:** Sie throughout; product names stay English (Marked, Markdown, MultiMarkdown, CommonMark …); German quotes „…"; ellipsis `…`.

## Tone and audience

- **Formality: Sie.** The German app UI uses formal address throughout; keep the docs consistent with it. Never switch to „du".
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

- **Quote the corrected string, not the shipped one.** When the prose cites a menu or option label, use the fixed wording from `ui-strings/de-ui-review.marked-l10n`, not the (still wrong) string in the currently installed app. Docs and the UI fixes ship together, so the docs follow the target wording (e.g. „Neue Dateien automatisch bearbeiten", not „Bearbeiten Sie neue Dateien automatisch").
- **Control labels → infinitive**, not a Sie-imperative. `Enable Leanpub support` → „Leanpub-Unterstützung aktivieren" (nicht „Aktivieren Sie …").
- **Descriptive tooltips → third person present**, matching the app. `Prints a horizontal line …` → „Druckt eine horizontale Linie …" (nicht „Drucken Sie …").
- **Genuine user instructions stay in Sie.** „Klicken Sie auf das Feld …", „Ziehen Sie ein Bild …" — where the reader really is told to act.
- **`{% appmenu %}` segments** must match the localized app menus exactly: `Ablage`, `Bearbeiten`, `Darstellung`, `Fenster`, `Hilfe`, `Einstellungen…`, `Exportieren…`, `Im Finder anzeigen`, … (verify against `MainMenu.strings`, incl. the ellipsis `…`).
- **`{% prefspane %}` / `{% kbd %}` / `{{cmd}}`:** leave tags unchanged (see root `README.md`).
- **Settings pane names in prose:** use the same wording as localized `Settings.strings`.

## Punctuation and typography

- Quotation marks: German „…" (`„` U+201E … `"` U+201C). Not straight `"..."`.
- Ellipsis: Unicode `…`, matching the app (nicht drei Punkte `...`).
- Dash: Halbgeviertstrich `–` for parentheticals, not the em dash `—`.
- Decimal/thousands: German conventions (1.000, 3,5).

## Links and filenames

- Keep `.md` / `.html` filenames identical to English (`Exporting.md`, not translated).
- Translate link **anchor text** only, never the target.
- Do not change `#anchor` IDs unless you add explicit heading IDs and update all references (ask the lead first).

## `config.yaml` for this locale

Per root `README.md`: translate section `title`, `folder` slugs, page `title`/`sidebar_title`, `description`, `keywords`, and `wiki_keywords`. **`file:` values stay English.** Rebuild `wiki_keywords` from the translated prose; do not copy English phrases.

## Review checklist (before opening a PR)

- [ ] `{% appmenu %}` paths verified against the localized app
- [ ] Control labels in infinitive, descriptive tooltips in third person
- [ ] „Überschrift" used for headings (never „Schlagzeile")
- [ ] Sie used consistently, German quotes „…" and ellipsis `…`
- [ ] `.md`/`.html` filenames and `{% … %}` tags unchanged
- [ ] Terms match `GLOSSARY.md`; new recurring terms added there
