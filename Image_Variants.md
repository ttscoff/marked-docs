# <%= @title %>

Marked can automatically build responsive `<picture>` elements for local images when companion **dark mode** and **Retina** files sit next to the image you reference. This uses the same naming conventions as Apple's DocC documentation catalogs, but works for **any Markdown or HTML document** with normal image paths that include a file extension.

See also [DocC Support](DocC_Support.html) for extensionless catalog references inside `.docc` bundles.

## Enabling image variants [enabling-image-variants]

In {% prefspane Apps %}, enable **Resolve dark and @2x image variants** (on by default) under DocC settings.

This preference is separate from **Resolve DocC image references**, which only applies inside `.docc` catalogs. You can use one, both, or neither depending on your project.

## Naming convention [naming-convention]

Place variant files in the **same folder** as the primary image. Marked looks for four combinations based on the base name:

| Role | Example filename |
|------|------------------|
| Light (1x) | `icon.png` |
| Dark (1x) | `icon~dark.png` |
| Light (2x) | `icon@2x.png` |
| Dark (2x) | `icon~dark@2x.png` |

Suffix order is flexible — `icon@2x~dark.png` and `icon~dark@2x.png` are treated the same way.

Supported extensions: `png`, `jpg`, `jpeg`, `gif`, `svg`, `webp`, and `pdf`.

## What gets rewritten [what-gets-rewritten]

Marked scans your document **before** final preview rendering:

- **Markdown:** `![Alt text](images/icon.png)`
- **HTML:** `<img src="images/icon.png" alt="Alt text">`

If at least **two** matching variant files exist on disk, the reference is replaced with a `<picture>` block. A single extra file is enough — you do not need all four variants.

Example output when light, dark, and @2x files are present:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/icon~dark.png 1x, images/icon~dark@2x.png 2x">
  <source srcset="images/icon.png 1x, images/icon@2x.png 2x">
  <img src="images/icon.png" alt="Alt text">
</picture>
```

The preview (and HTML export) then follows the user's system appearance for dark variants and device pixel density for @2x assets.

## What is skipped [what-is-skipped]

Marked does **not** rewrite:

- Remote URLs (`http://`, `https://`, `data:`)
- References that already point at a `~dark` file
- `<img>` tags already inside an existing `<picture>` element
- Extensionless names like `![Diagram](diagram)` — use [DocC Support](DocC_Support.html) for catalog-style references

## Live preview and file watching [live-preview-and-file-watching]

When variants are detected, Marked adds **every existing variant file** to its watch list alongside the main document. Saving `icon~dark.png` in an external editor triggers the same live image reload as editing `icon.png`.

## Tips [tips]

- Reference the **light 1x** image in your source when possible (`icon.png`, not `icon~dark.png`). Marked discovers siblings from that path.
- If you only have `@2x` assets, include at least one other variant (typically `~dark`) or Marked will leave the reference unchanged.
- Variant resolution uses paths **relative to the document** (or the included file's folder for nested includes), the same base path rules as [Multi-file Documents](Multi-File_Documents.html).

## Related topics [related-topics]

- [DocC Support](DocC_Support.html) — extensionless image names inside `.docc` catalogs
- [Settings: Apps](Settings_Apps.html) — preference toggles for DocC and image variants
- [Previewing](Previewing.html) — live preview and file updates
