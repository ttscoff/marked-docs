# <%= @title %>

Numbers matter just as much as words.

## Preview formulas with MathJax

![][1]

   [1]: images/mathjax.jpg @2x width=713px height=512px class=center

By turning on MathJax in the {% prefspane Style %}, the necessary scripts and CSS will be included in the preview. Then MultiMarkdown math syntax can be used in your Markdown document and the results will be displayed.

Example MMD MathJax syntax:

    \\\\[ {e}^{i\pi } 1=0 \\\\]

If you choose to include MathJax in an exported HTML file, a CDN link will be used instead of the embedded MathJax code. This requires an Internet connection to view the rendered MathML.

## MathJax source: Local vs CDN

When MathJax is enabled, Marked can load it from either:

- **Local**: a copy of MathJax v3 bundled inside the app (faster to load, works offline).
- **CDN**: the official MathJax v3 CDN (always up to date, no app bundle impact).

The **MathJax Source** popup in {% prefspane Style %} lets you choose:

- **Local** – uses the ES5 `tex-chtml.js` component from the app bundle.
- **CDN** – loads the same component from the CDN. This requires an Internet connection.

Exported HTML files always reference MathJax from a CDN, regardless of the preview source, so they remain self-contained and small.

## Equation numbering

You can enable equation numbering in {% prefspane Style %}. This works with both MathJax and KaTeX, but is implemented differently internally. For MathJax v3, Marked maps your settings to the appropriate MathJax configuration so that:

- “Number equations” controls whether any numbers are shown.
- The “side” option controls whether numbers appear on the left or right.
- The “AMS only” option restricts numbering to AMS-style equations.

These options correspond to MathJax’s `tex.tags` and `tex.tagSide` settings under the hood.

## Additional packages

MathJax v3 is modular. Marked always enables the core TeX/AMS packages, and you can optionally turn on extra ones in {% prefspane Style %}:

- **Physics** (`physics`) – physics notation and conveniences.
- **Chemistry** (`mhchem`) – chemistry equations.
- **Bra–ket** (`braket`) – Dirac bra–ket notation.
- **Bold symbols** (`boldsymbol`) – bold math symbols.

Click **Additional Packages…** to open a small checklist where you can turn these packages on or off. Changes take effect the next time Marked renders math in the preview.

## MathJax advanced configuration

You can apply additional custom configurations on top of Marked’s defaults by adding a valid JSON object in the **Advanced Configuration** field. This field is merged into the MathJax v3 configuration object (`window.MathJax`) before MathJax loads. It can contain [any options supported by MathJax v3](https://docs.mathjax.org/en/latest/options/), for example:

    {
        "tex": {
            "inlineMath": [["$","$"],["\\\\(","\\\\)"]],
            "displayMath": [["$$","$$"],["\\\\[","\\\\]"]],
            "macros": {
                "tr": "{\\\\scriptscriptstyle\\\\mathrm{T}}"
            },
            "packages": { "[+]": ["physics"] }
        }
    }

This example adjusts TeX delimiters, adds a `\tr` macro, and enables the `physics` package in addition to the default set. With these settings, all of the following renders properly:

    Inline formula using parens, \\\\({x}^{2} {y}^{2}=1\\\\), or with dollar signs, ${x}^{2} {y}^{2}=1$.

    Display with escaped brackets:

    \\\\[ {e}^{i\pi } 333=0 \label{testme} \\\\]

    Or with double dollar signs:

    $${x}_{1,2}=\\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a}$$

![][2]

   [2]: images/mathjax2.jpg @2x width=837px height=260px class=center

The additional configuration extends the existing object, so only the properties specified will be overridden. Unspecified options will remain at the default for the current preset.

Note that using the MultiMarkdown processor with non-standard delimiters, characters inside the expression are parsed, so symbols like `*` and `^` will cause typographic changes that will break the MathJax processor. The best solution in these cases is to use the Discount processor in [Processor settings](x-marked-3://pref/processor).

Marked performs a bit of magic when either MathJax or KaTeX are enabled, converting math syntax to ensure its as compatible as possible with the current processor (MultiMarkdown or Discount). This should be great in all circumstances, but if you find it causing issues, [contact support](https://support.markedapp.com/questions/add)!


## KaTeX

[katex]: https://katex.org/

[KaTeX][] is available as an alternative to MathJax. It's lighter weight and therefore faster to load, which can be great on documents with a large number of formulae. It doesn't have as many features, though, and some equations that work with MathJax (or LaTeX) may not be supported.

## Automatic Equation Numbering [numbering]

You can enable equation numbering in {% prefspane Style %}. This works with both MathJax and KaTeX. You can select whether numbers appear on the left or right side of the equation.

### In MathJax

In MathJax, this uses the setting:

    {
      TeX: { equationNumbers: { autoNumber: "all" } }
    }

If you want to only number AMS equations, select "AMS only" to the right of the "side" dropdown menu.

### In KaTeX

KaTeX doesn't offer equation numbering. To simulate this in Marked, CSS is used, and all display equations are numbered.

## Export Issues

Rich Text formats will not handle equations (either by MathJax or KaTeX). They will be hidden in the output document as trying to include the special fonts results in a bigger mess than you'd imagine... This is something I hope to fix at some point, but a shortcoming for right now.

