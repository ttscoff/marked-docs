---
name: open-in-marked
description: >-
  Opens files and folders in Marked 3 on macOS, and changes Marked preferences,
  using the x-marked-3 URL scheme. Use when the user asks to preview a Markdown
  file or folder in Marked, open Marked Settings, or set a Marked preference
  with the pref or defaults URL.
---

# Open files in Marked

Marked 3 is a macOS previewer. Drive it with `open` and the `x-marked-3://` URL scheme. `x-marked://` is accepted too. Prefer `x-marked-3://`.

Percent-encode the path. Encode spaces as `%20`, and encode `?`, `&`, and `#`. A path may start with `~`. Marked expands that. The path must already exist. A missing file is ignored.

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
open "x-marked-3://open?file=~/Notes/Book"
```

A folder uses the same command as a file. Marked previews the folder when it recognizes it as a watched folder or text bundle.

Add `raise=1` to bring the window forward:

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md&raise=1"
```

Several files go in one `file` parameter, separated by commas. A comma separates paths only when it follows an extension (`.md,`) or the next path starts with `/` or `~`. That leaves commas inside a name like `report, draft.md` alone.

```bash
open "x-marked-3://open?file=/Users/me/a.md,/Users/me/b.md"
```

Other useful commands, same scheme:

| Command | What it does |
|---|---|
| `open?file=` | Open a file or folder |
| `refresh?file=` | Reload an open preview. No `file` refreshes the front window. `file=all` refreshes every window |
| `stream` | Open Streaming Preview |
| `help?page=Overview` | Open a help page. Underscores replace spaces |

`x-success` is an optional callback on any of these. Set it to another URL or a bundle id. Marked opens it after the command finishes.

## Open a Settings section

`pref` opens Settings. It does not change a value. The page name is matched loosely, ignoring case and hyphens. These names are exact:

`General`, `Preview`, `Style`, `Processor`, `Apps`, `Proofing`, `Export`, `Advanced`

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://pref/Style"
```

With no page, Settings opens to General.

`stylemanager` opens the Style pane and the Style Manager. `stylegallery` opens the style gallery.

## Change a preference

`defaults` writes keys on the running app. This is Marked, not the `defaults` command-line tool. Read the current key first so you set a name Marked already stores:

```bash
defaults read com.brettterpstra.marked
```

Older copies of the app stored preferences under `com.brettterpstra.marked2`. If `defaults read` on the first domain fails, try that one. The URL itself always writes into whichever copy is running.

```bash
open "x-marked-3://defaults?syntaxHighlight=0"
```

Rules:

- One URL may set several keys: `?syntaxHighlight=0&codeCanWrap=1`.
- A key is changed only when Marked already has a value for it. An unknown key is skipped. Do not invent key names.
- Booleans are `1` or `0`. Match the type already stored for that key.
- `folderPreviewExtensionsArray` and `outlineModeExtensions` take a comma-separated list of extensions with no dots: `md,txt,fountain`.
- `processor` is special. Use `multimarkdown` (or `mmd`), `discount` (or `gfm`), `commonmark` (or `cmark`), `kramdown`, or `apex`.
- After a change, Marked reloads open previews. Pass `refresh=0` to skip that.

```bash
open "x-marked-3://defaults?processor=apex&refresh=0"
```

Do not use `defaults` to flip a preference you have not read. If you only need the user to look at a setting, use `pref` instead.
