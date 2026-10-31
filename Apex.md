# <%= @title %>

W> **Apex support in Marked is in beta.** Behavior may change as the integration matures. Please report problems, unexpected rendering, or missing syntax at [support.markedapp.com](https://support.markedapp.com).

Apex is a **unified Markdown processor**: one engine that aims to cover the features people usually pick CommonMark, GitHub Flavored Markdown (GFM), MultiMarkdown, or Kramdown for --- without abandoning the other flavors.

In Marked, **Apex (beta)** always runs in Apex's **unified** mode (all of those feature families enabled together). You do not pick a separate Apex "CommonMark mode" or "Kramdown mode" inside Marked yet; that may come later.

Check out the [Markdown Dingus](x-marked-3://dingus?processor=apex) to experiment with Apex, or open {% appmenu Help, Markdown Reference %} and choose the **Apex** tab for a compact cheat sheet.

---

## Why Apex exists [why-apex-exists]

Markdown "flavors" diverged for good reasons --- GitHub needed task lists and tables, MultiMarkdown needed footnotes and metadata, Kramdown needed attribute lists --- but picking one processor usually means giving up another's syntax.

Apex's goal is to **consolidate** those extensions so a single document can use:

- Everyday CommonMark / GFM habits (fenced code, task lists, strikethrough, GFM tables)
- MultiMarkdown-style footnotes, abbreviations, and metadata habits
- Kramdown-friendly definition lists, math, and (for advanced use) attribute lists
- Marked-oriented conveniences such as callouts, Critic Markup, and TOC markers

Full upstream documentation lives on the [Apex wiki](https://github.com/ApexMarkdown/apex/wiki). This page covers what you need day to day in Marked's preview.

---

## Enabling Apex in Marked [enabling-apex-in-marked]

1. Open {% prefspane Processor %}.
2. Set **Default Markdown processor** to **Apex (beta)**.
3. Or override per document with metadata such as `Processor: apex` (aliases: `apex-beta`, `unified`).

Aliases also work from AppleScript, Conductor "Run Processor" actions, custom processor stdout (`APEX`), and `x-marked://` defaults URLs.

T> In this beta, Marked still expands its own file includes (`<<[file]`, and related Marked include paths) before Apex runs. Apex's native include engine is left off in Marked for sandboxing. Use Marked's include features as you already do.

---

## Basic syntax Apex adds or unifies [basic-syntax]

Standard Markdown (headings, emphasis, links, images, lists, blockquotes, code) works as you'd expect. The items below are the extras people most often need when switching to Apex.

### Task lists [task-lists]

```markdown
- [ ] Todo
- [x] Done
```

### Strikethrough [strikethrough]

```markdown
~~removed text~~
```

### Tables [tables]

GFM pipe tables with header separators and column alignment:

```markdown
| Left | Center | Right |
| :--- | :----: | ----: |
| a    | b      | c     |
```

Advanced table features (rowspan `^^`, colspan, captions, grid tables, CSV) are documented on the wiki: [Tables](https://github.com/ApexMarkdown/apex/wiki/Tables).

### Footnotes [footnotes]

Reference-style:

```markdown
See the note[^1].

[^1]: Footnote text.
```

Inline styles familiar from MultiMarkdown / Kramdown are also supported. Details: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Definition lists [definition-lists]

```markdown
Apple
: A fruit.
: A computer company.
```

### Superscript and subscript [superscript-and-subscript]

```markdown
Text^super^ and H~2~O
```

### Math [math]

Inline `$x^2$` and display `$$...$$` (Marked's MathJax / KaTeX prefs still control preview chrome).

### Callouts [callouts]

Obsidian / Bear-style:

```markdown
> [!NOTE]
> Something worth highlighting.
```

Also see Marked's [Special Syntax](Special_Syntax.html) and the Apex [Callouts](https://github.com/ApexMarkdown/apex/wiki/Callouts) wiki page.

### Critic Markup [critic-markup]

```markdown
{++insertion++}
{--deletion--}
{==highlight==}
{>>comment<<}
```

Enable Critic Markup in Marked as usual; Apex can render critic syntax in the processor pipeline. See [CriticMarkup](CriticMarkup.html).

### Abbreviations [abbreviations]

```markdown
*[HTML]: HyperText Markup Language

The HTML spec is long.
```

### Emoji shortcodes [emoji-shortcodes]

```markdown
Ship it :rocket:
```

### Metadata [metadata]

YAML front matter, MultiMarkdown-style `Key: Value` headers, and Pandoc title blocks are recognized. Insert values with `[%key]` where supported.

Configuration details: [Configuration](https://github.com/ApexMarkdown/apex/wiki/Configuration) and [Metadata Transforms](https://github.com/ApexMarkdown/apex/wiki/Metadata-Transforms) on the wiki.

### Table of contents markers [table-of-contents-markers]

Apex understands common TOC markers, including:

- `<!--TOC-->`
- `{{TOC}}` or `{{TOC:2-4}}`
- Kramdown-style `{:toc}`

Exclude a heading with `{:.no_toc}` where IAL is available. More: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Special markers [special-markers]

Marked-oriented HTML comments such as `<!--BREAK-->` (page break) and `<!--PAUSE:N-->` (autoscroll) continue to work with Apex previews.

---

## Advanced topics (wiki) [advanced-topics-wiki]

Use the [Apex wiki](https://github.com/ApexMarkdown/apex/wiki) for features that are powerful but less common in everyday preview:

| Topic | Wiki |
|------|------|
| Index generation | [Indices](https://github.com/ApexMarkdown/apex/wiki/Indices) |
| Citations / bibliography | [Citations](https://github.com/ApexMarkdown/apex/wiki/Citations) |
| Inline Attribute Lists, spans, fenced divs | [Inline Attribute Lists](https://github.com/ApexMarkdown/apex/wiki/Inline-Attribute-Lists) |
| Multi-file documents & includes | [Multi-File Documents](https://github.com/ApexMarkdown/apex/wiki/Multi-File-Documents) |
| Header ID formats | [Header IDs](https://github.com/ApexMarkdown/apex/wiki/Header-IDs) |
| Multi-format images | [Multi-Format Images](https://github.com/ApexMarkdown/apex/wiki/Multi-Format-Images) |
| Compatibility modes (CLI) | [Modes](https://github.com/ApexMarkdown/apex/wiki/Modes) |
| Plugins & filters | [Plugins](https://github.com/ApexMarkdown/apex/wiki/Plugins), [Filters](https://github.com/ApexMarkdown/apex/wiki/Filters) |
| Quarto / Pandoc / Jekyll | [Quarto Mode](https://github.com/ApexMarkdown/apex/wiki/Quarto-Mode), [Pandoc Integration](https://github.com/ApexMarkdown/apex/wiki/Pandoc-Integration), [Jekyll](https://github.com/ApexMarkdown/apex/wiki/Using-Apex-with-Jekyll) |

---

## See also [see-also]

- [Choosing a Processor](Choosing_a_Processor.html) --- when to pick MultiMarkdown, CommonMark, Kramdown, Discount, or Apex
- [Settings: Processor](Settings_Processor.html)
- [Markdown Dingus](Markdown_Dingus.html)
- [Apex wiki home](https://github.com/ApexMarkdown/apex/wiki)
- Report issues: [support.markedapp.com](https://support.markedapp.com)
