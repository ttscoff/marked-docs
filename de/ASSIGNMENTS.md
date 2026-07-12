# Translation assignments — German (de)

Who is working on which section, so contributors don't translate the same files twice. Maintained by the German lead. Work as fork + PR against the German branch; the lead reviews and merges. Follow `SYNTAX.md` and `GLOSSARY.md`.

| Section (config.yaml `folder`) | Assigned to | Status |
|---|---|---|
| Getting_Started | Thomas (@fucx, lead) | done |
| Settings | Thomas (@fucx, lead) | done |
| Supported_Apps | Hilthart (@h3pdesign) | done |
| Reading_Features | Thomas Ungricht (@Thomas-U) | offered |
| Just_for_Writers | Hilthart (@h3pdesign) | in progress (5 pages already done by lead — see below, skip those) |
| Special_Features | Thomas (@fucx, lead) | in progress |
| Comparisons_FAQ | — | open |
| Troubleshooting | — | open |
| About_Markdown | — | open (Markdown_Dingus already done) |
| Credits | Thomas Ungricht (@Thomas-U) | done (license pages stay English) |

Status: *done* = translated and reviewed · *in progress* = being worked on · *offered* = proposed to a translator, awaiting their confirmation · *open* = unclaimed. Ping the lead to claim an open section.

### Already post-edited by the lead — do NOT redo

The lead has post-edited several high-traffic pages that fall inside other sections. They are finished on `main`; please skip them:

- **In Just_for_Writers:** Multi-File_Documents, MathJax, RTF_Support, PDF_Support, Working_With_DOCX
- **In Special_Features:** Custom_Styles, Writing_Custom_CSS, Custom_Processor, Special_Syntax, URL_Handler, Streaming_Preview
- **In About_Markdown:** Markdown_Dingus

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
