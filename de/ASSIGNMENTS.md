# Translation assignments — German (de)

Who is working on which section, so contributors don't translate the same files twice. Maintained by the German lead. Work as fork + PR against the German branch; the lead reviews and merges. Follow `SYNTAX.md` and `GLOSSARY.md`.

| Section (config.yaml `folder`) | Assigned to | Status |
|---|---|---|
| Getting_Started | Thomas (@fucx, lead) | in progress |
| Settings | Thomas (@fucx, lead) | in progress |
| Supported_Apps | Hilthart (@h3pdesign) | assigned |
| Reading_Features | — | open |
| Just_for_Writers | — | open |
| Special_Features | — | open |
| Comparisons_FAQ | — | open |
| Troubleshooting | — | open |
| About_Markdown | — | open |
| Credits | — | open |

## Which files belong to a section?

Two ways to see it:

- **Rendered:** the published help at <https://markedapp.com/help/Overview> shows every section in the sidebar. The pages grouped under "Supported Apps" there are exactly your files.
- **Source of truth:** `config.yaml` defines each section's pages via the `file:` entries under its `folder`. A `file:` value is the English basename, so `file: Bear` means `Bear.md` at the content root, and its German translation lives at `de/Bear.md` (same filename). Note that a section's `folder` slug and its display title can differ (e.g. `folder: Special_Features` shows as "Advanced Features").

### Supported_Apps (24 files)

```
Additional_Application_Support.md   Highland.md                 OmniOutliner_and_OPML.md
Bear.md                             Hookmark.md                 Scrivener_Support.md
Curio.md                            iA_Writer.md                The_Archive.md
DEVONthink.md                       iThoughtsX.md               Ulysses.md
DocC_Support.md                     MarsEdit.md                 Vim.md
Drafts.md                           MindNode.md                 VoodooPad.md
Folder_Watching.md                  MultiMarkdown_Composer.md   VS_Code.md
                                    nvUltra.md                  Xcode_Playgrounds.md
                                    Obsidian.md
```

## Notes

- Each file already contains a machine-translated draft: review and correct, don't translate from scratch.
- Start with a small first PR to align on terminology and style, then batch the rest however suits you. Avoid one giant PR.
- Keep `{% … %}` tags, `.md`/`.html` filenames, and `#anchors` unchanged (see `SYNTAX.md`).
- Ping the lead to claim an open section before starting.
