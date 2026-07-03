# Syntax guide — Spanish (es)

Practical conventions for the Spanish docs. Read this and `GLOSSARY.md` before translating. Terms and style are aligned with the localized Marked app (`es.lproj`) so the docs match the UI.

## Common pitfalls (quick checklist)

Recurring things to watch when post-editing the machine-translated drafts:

1. **Reference-link definitions** (`[label]: url`) each on their own line — never collapse several onto one line, or all but the first break.
2. **Translate the link text, keep the target:** in `[text](Target.html)` and `[text][label]`, translate only the visible text; the filename and the `[label]` stay English.
3. **Block tags** (`{% apponly div %}`, `{% endapponly %}`, …) on their own line, no trailing spaces.
4. **Localize syntax example words, consistently:** `*cursiva*`, `**negrita**` (not English *italics* / **bold** in examples).
5. **UI and technical terms → match the app and Apple:** menu paths exactly from the Spanish app.
6. **Keep verb forms parallel** in lists and paired instructions.
7. **Basics:** product names stay English (Marked, Markdown, MultiMarkdown, CommonMark …); use Spanish quotation marks «…» where appropriate; ellipsis `…`.

## Tone and audience

- **Audience:** Mac users who write in Markdown; assume familiarity with menus and keyboard shortcuts.
- **Voice:** Follow macOS Spanish (Apple style). Avoid literal translations of English idioms; rephrase for natural Spanish.

## Product and technology names

| Term | Treatment |
|------|-----------|
| Marked | Keep as **Marked** |
| MultiMarkdown, CommonMark, CriticMarkup, MathJax, KaTeX, GitHub Flavored Markdown | Keep English |
| macOS, Finder, Dock, AppleScript | Keep English (Apple's localized UI keeps them) |
| App names (Scrivener, Obsidian, Bear, Drafts, …) | Keep English |

## UI strings and control style

- **`{% appmenu %}` segments** must match the localized app menus exactly: `Archivo`, `Edición`, `Vista previa`, `Ayuda`, `Ajustes…`, `Exportar…`, … (verify against `MainMenu.strings`, including the ellipsis `…`).
- **`{% prefspane %}` / `{% kbd %}` / `{{cmd}}`:** leave tags unchanged (see root `README.md`).
- **Settings pane names in prose:** use the same wording as localized `Settings.strings`.

## Links and filenames

- Keep `.md` / `.html` filenames identical to English (`Exporting.md`, not translated).
- Translate link **anchor text** only, never the target.

## `config.yaml` for this locale

Per root `README.md`: translate section `title`, `folder` slugs, page `title`/`sidebar_title`, `description`, `keywords`, and `wiki_keywords`. **`file:` values stay English.**

## Review checklist (before opening a PR)

- [ ] `{% appmenu %}` paths verified against the localized app
- [ ] Terms match `GLOSSARY.md`; new recurring terms added there
- [ ] `.md`/`.html` filenames and `{% … %}` tags unchanged
- [ ] `config.yaml` titles and keywords localized; `file:` keys unchanged
