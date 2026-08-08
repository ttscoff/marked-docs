# <%= @title %>

Marked understands [Apple DocC](https://www.swift.org/documentation/docc/) documentation catalogs (`.docc` bundles). When you preview Markdown that lives inside or beside a catalog, Marked can resolve **extensionless** image references to files in the catalog's `Resources` folder — including `~dark` and `@2x` variants.

For normal Markdown documents that use **paths with file extensions** (`images/icon.png`), see [Image Variants](Image_Variants.html). That feature works everywhere; DocC resolution is catalog-specific.

## Enabling DocC resolution [enabling-docc-resolution]

In {% prefspane Apps %}, enable **Resolve DocC image references** (on by default).

DocC detection runs when Marked finds a `.docc` catalog ancestor of the open document. No special URL scheme or Xcode integration is required — open the catalog's Markdown the same way you would any other file.

## Extensionless references [extensionless-references]

Inside a DocC catalog, authors typically reference images **without** a path or extension:

```markdown
![Order flow](OrderStateTransitions)
```

Marked resolves `OrderStateTransitions` to `Resources/OrderStateTransitions.png` (or another supported type) when that file exists in the catalog.

References that already include a path and extension — `images/chart.png` — are left to [Image Variants](Image_Variants.html) instead and are not rewritten by DocC resolution.

## Dark mode and Retina variants [dark-mode-and-retina-variants]

DocC catalogs often ship multiple files per image:

| Role | Example in `Resources/` |
|------|-------------------------|
| Light (1x) | `diagram.png` |
| Dark (1x) | `diagram~dark.png` |
| Light (2x) | `diagram@2x.png` |
| Dark (2x) | `diagram~dark@2x.png` |

When more than one variant exists, Marked emits the same responsive `<picture>` markup described in [Image Variants](Image_Variants.html). A single-file reference still resolves to a normal `<img>` or `![](Resources/...)` path.

## HTML and Markdown [html-and-markdown]

DocC resolution applies during Marked's include pass:

- **Markdown sources** — `![alt](ImageName)` references
- **HTML sources** — `<img src="ImageName">` without extension

Both are updated before preview rendering.

## File watching [file-watching]

Resolved images under the catalog `Resources` folder are added to Marked's watch list. Editing a variant file externally updates the preview without a manual refresh.

## Related topics [related-topics]

- [Image Variants](Image_Variants.html) — `~dark` and `@2x` detection for extension-based paths in any project
- [Xcode Playgrounds](Xcode_Playgrounds.html) — preview Swift playground commentary
- [Settings: Apps](Settings_Apps.html) — DocC and image variant preferences
