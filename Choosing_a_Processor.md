# <%= @title %>

Marked can preview the same file with several built-in Markdown processors. Each one makes different tradeoffs between **writing workflow** (books, blogs, GitHub READMEs) and **output control** (IDs, classes, metadata). You choose the default in {% prefspane Processor %}; you can also override the processor per document.

This page summarizes how the four main processors differ. For full syntax details, see the reference pages under **Help → Markdown Reference** (e.g. [MultiMarkdown v5 Specification](MultiMarkdown_v5_Spec.html), [Kramdown Specification](Kramdown_Spec.html), [CommonMark Specification](CommonMark_Spec.html), [Discount GFM Specification](Discount_GFM_Spec.html)).

---

## MultiMarkdown (v5)

**Best for:** Long-form prose, academic or technical writing, and anything that relies on **metadata**, **citations**, and **MultiMarkdown-specific** features.

Marked ships with **MultiMarkdown 5** (see the [MultiMarkdown User's Guide](https://fletcher.github.io/MultiMarkdown-5/) for the upstream documentation).

### Strengths

- **Narrative and reference-heavy documents:** Footnotes, bibliography/citations, and tables are first-class.
- **Metadata:** Standard MultiMarkdown metadata blocks (`Key: Value` headers) plus **transclusion** and other MMD conveniences described in the v5 guide.
- **Metadata substitution:** Keys from metadata can be inserted in the body with `[%key]`-style replacement so titles, author strings, and similar values stay in sync with the header.
- **Tables, images, and cross-references:** Aligned with the features documented for MultiMarkdown 5.

### IDs and manual headings

- Heading IDs are **normalized** in a way that tends to produce **lowercase, concatenated** slugs (no spaces — words run together).
- For **manual header IDs**, MultiMarkdown uses the form: `## Headline Text [my-id]` (the bracketed identifier after the heading text).

### When to pick something else

If you need **GitHub-flavored** task lists and the exact behavior of GitHub’s current parser, prefer **CommonMark (GFM)**. If you need **fine-grained HTML classes/IDs** on arbitrary elements, consider **Kramdown**.

---

## Kramdown

**Best for:** Documents where you want **precise control over HTML output** — custom **classes**, **IDs**, and attributes, so your CSS can target specific blocks and spans.

The [kramdown syntax reference](https://kramdown.gettalong.org/syntax.html) is the authoritative guide.

### Strengths

- **Mostly compatible** with MultiMarkdown-style habits for everyday Markdown, while adding its own extensions.
- **Inline and block attribute lists (IALs):** Attach `{: #id .class key="value"}` to paragraphs, headers, code blocks, links, images, and more --- ideal for Jekyll-style sites and custom stylesheets.
- **Header IDs:** kramdown normalizes auto-generated header IDs to **lowercase, hyphen-separated** words (e.g. `my-section-title`). For **manual IDs**, use the `{#id}` form after the headline text — e.g. Setext: `My Section {#my-section}` then the underline, or ATX: `# My Section {#my-section}` (see kramdown’s [headers](https://kramdown.gettalong.org/syntax.html#headers) for exact placement and IAL rules).
- **Definition lists, footnotes, smart typography, math blocks:** Rich feature set for publishing pipelines that need more than "plain" Markdown.

### When to pick something else

If you rely on **MultiMarkdown-only** metadata substitution (`[%key]`) or MMD-specific citation workflows, **MultiMarkdown** may be a better fit. For **README and repo docs** that must match GitHub online, **CommonMark (GFM)** is usually closer.

---

## CommonMark (GitHub Flavored Markdown / cmark-gfm)

**Best for:** **README files**, **issue/PR descriptions**, and **project documentation** that should match **GitHub's current Markdown behavior** as closely as possible.

Marked uses a **GFM**-oriented engine (cmark-gfm). The formal spec is the [GitHub Flavored Markdown Spec](https://github.github.com/gfm/), built on [CommonMark](https://commonmark.org/).

### Strengths

- **Closest match to GitHub:** Tables, strikethrough, task list items, fenced code blocks with language tags, and autolinks behave like modern GitHub rendering.
- **Unambiguous parsing:** CommonMark defines block/inline precedence and list rules precisely — stricter in some edge cases than "classic" Markdown.pl behavior, but **more predictable** once you learn the rules.
- **Practical for wrapped text:** Paragraph and list rules are designed to behave well with hard-wrapped prose (see the spec's sections on lazy continuations and lists).

### Header IDs

Auto-generated heading anchors are typically **lowercase and hyphen-separated**, consistent with common GitHub-style slugging.

### When to pick something else

GFM does not replicate **MultiMarkdown metadata**, **kramdown IALs**, or **MMD citation** workflows. For books, theses, or heavy metadata, use **MultiMarkdown** or **Kramdown** as appropriate.

---

## Discount

**Best for:** A **fast, C-based** processor that tracks **classic Markdown** and an **older GitHub-flavored** feature set — useful when you want behavior closer to **original Markdown** plus tables, footnotes, and related extensions without the full CommonMark rule book.

Project home: [Discount](https://www.pell.portland.or.us/~orc/Code/discount/).

### Strengths

- **PHP Markdown Extra-style tables** and many extensions (footnotes, fenced code when enabled, etc. --- see Marked's [Discount GFM Specification](Discount_GFM_Spec.html) for what Marked enables).
- **Optional "GitHub" extras** in upstream Discount (e.g. checkbox lists when built with the right flags); Marked documents the combination it ships in the Discount spec page.
- **SmartyPants-style typography** and other conveniences described on the Discount site (though all included processors actually provide typography features).
- Philosophically close to **John Gruber's Markdown** plus practical extensions, rather than the full CommonMark test suite.

### When to pick something else

For **pixel-perfect parity with today's github.com**, prefer **CommonMark (GFM)**. For **MultiMarkdown metadata and citations**, use **MultiMarkdown**.

---

## Quick comparison

| Concern | MultiMarkdown | Kramdown | CommonMark (GFM) | Discount |
|--------|---------------|--------|------------------|----------|
| **Primary use** | Prose, papers, books | Styled HTML, Jekyll-like sites | READMEs, GitHub-like docs | Classic MD + extensions |
| **Citations / MMD metadata** | Strong | Via different syntax | No | No |
| **Manual heading ID style** | `## Title [id]` | `## Title {: #id }` (IAL) | Spec / GitHub slug rules | None |
| **Auto heading IDs** | Lowercase concatenated | Lowercase hyphenated | Lowercase hyphenated | Lowercase-hyphenated |
| **Extra attributes (classes/ids)** | Limited MMD mechanisms | **IALs** — very strong | Limited | Limited |

---

## See also

- [Settings: Processor](Settings_Processor.html) — default processor and related options
- [Markdown Dingus](Markdown_Dingus.html) — try processors side by side in Marked
- [Custom Processor](Custom_Processor.html) — plug in your own toolchain when needed
