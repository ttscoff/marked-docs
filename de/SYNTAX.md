# Syntax guide — German (de)

Lead translator: replace this file with your locale's conventions before bulk translation begins. Keep it short and practical; link to `GLOSSARY.md` for term choices.

## Tone and audience

- **Formality:** (formal / informal / technical-neutral)
- **Audience:** Mac users who write in Markdown; assume familiarity with menus and keyboard shortcuts.
- **Voice:** Match Apple's style for your locale where it fits; avoid overly literal translations of English idioms.

## Product and technology names

List what stays in English vs what you localize:

| Term | Treatment |
|------|-----------|
| Marked | Keep as **Marked** |
| MultiMarkdown, CommonMark, CriticMarkup, MathJax, … | (your rule) |
| macOS, AppleScript, Finder | (your rule) |

## UI strings

- **`{% appmenu %}` segments:** Must match localized `MainMenu.strings` / app menus exactly (including ellipsis `…`).
- **`{% prefspane %}` / `{% kbd %}`:** Leave tags unchanged; see root `README.md`.
- **Settings pane names in prose:** Use the same wording as localized `Settings.strings`.

## Punctuation and typography

- Quotation marks: (e.g. „…” German, «» French, "" Chinese)
- Ellipsis: Unicode `…` vs three dots — match the app
- Non-breaking spaces before `:;?!` if required by your locale

## Links and filenames

- Keep **`.md` / `.html` filenames** identical to English (`Exporting.md`, not translated).
- Translate link **anchor text** only.
- Do not change `#anchor` IDs unless you add explicit heading IDs and update all references.

## `config.yaml` for this locale

See root `README.md` — section titles, `folder` slugs, page `title`/`sidebar_title`, `description`, `keywords`, and `wiki_keywords` are translated here. **`file:` values stay English.**

## Review checklist

- [ ] `{% appmenu %}` paths verified against the localized app
- [ ] No duplicate `wiki_keywords` across pages (each phrase maps to one page only)
- [ ] Glossary updated for new recurring terms
- [ ] Screenshots (if any) use localized UI
