# Syntax guide — {LOCALE_LABEL} ({LOCALE})

Practical conventions for the {LOCALE_LABEL} docs. Read this and `GLOSSARY.md` before translating. Terms and style are aligned with the localized Marked app (`{LOCALE}.lproj`) so the docs match the UI.

## Common pitfalls (quick checklist)

Recurring things to watch when post-editing the machine-translated drafts:

1. **Reference-link definitions** (`[label]: url`) each on their own line — never collapse several onto one line, or all but the first break.
2. **Translate the link text, keep the target:** in `[text](Target.html)` and `[text][label]`, translate only the visible text; the filename and the `[label]` stay English.
3. **Block tags** (`{% apponly div %}`, `{% endapponly %}`, …) on their own line, no trailing spaces.
4. **Localize syntax example words, consistently:** translate words inside `*…*` / `**…**` examples in the docs (not the asterisks).
5. **UI and technical terms → match the app and Apple:** menu paths exactly from the localized app (`MainMenu.strings`).
6. **Keep verb forms parallel** in lists and paired instructions.
7. **Basics:** product names stay English (Marked, Markdown, MultiMarkdown, CommonMark …); follow your locale's typography rules in `GLOSSARY.md`.

## Tone and audience

- **Audience:** Mac users who write in Markdown; assume familiarity with menus and keyboard shortcuts.
- **Voice:** Follow macOS {LOCALE_LABEL} (Apple style). Avoid literal translations of English idioms; rephrase for natural {LOCALE_LABEL}.

## Product and technology names

| Term | Treatment |
|------|-----------|
| Marked | Keep as **Marked** |
| MultiMarkdown, CommonMark, CriticMarkup, MathJax, KaTeX, GitHub Flavored Markdown | Keep English |
| macOS, Finder, Dock, AppleScript | Keep English (Apple's localized UI keeps them) |
| App names (Scrivener, Obsidian, Bear, Drafts, …) | Keep English |

## UI strings and control style

- **`{% appmenu %}` segments** must match the localized app menus exactly (verify against `MainMenu.strings`, including the ellipsis `…`).
- **`{% prefspane %}` / `{% kbd %}` / `{{cmd}}`:** leave tags unchanged (see root `README.md`).
- **Settings pane names in prose:** use the same wording as localized `Settings.strings` / `Preferences.strings`.

## Links and filenames

- Keep `.md` / `.html` filenames identical to English (`Exporting.md`, not translated).
- Translate link **anchor text** only, never the target.
- Do not change `#anchor` IDs unless you add explicit heading IDs and update all references (ask the lead first).

## `config.yaml` for this locale

Per root `README.md`: translate section `title`, `folder` slugs, page `title`/`sidebar_title`, `description`, `keywords`, and `wiki_keywords`. **`file:` values stay English.** Rebuild `wiki_keywords` from the translated prose; do not copy English phrases blindly.

## Review checklist (before opening a PR)

- [ ] `{% appmenu %}` paths verified against the localized app
- [ ] Terms match `GLOSSARY.md`; new recurring terms added there
- [ ] `.md`/`.html` filenames and `{% … %}` tags unchanged
- [ ] `config.yaml` titles and keywords localized; `file:` keys unchanged
