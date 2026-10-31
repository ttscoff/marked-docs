# <%= @title %>

W> **Az Apex támogatása a Markedben béta állapotban van.** A viselkedés változhat, ahogy az integráció érik. Kérjük, jelentsd a problémákat, a váratlan megjelenítést vagy a hiányzó szintaxist a [support.markedapp.com](https://support.markedapp.com) oldalon.

Az Apex egy **egységesített Markdown-feldolgozó**: egyetlen motor, amely célja, hogy lefedje azokat a funkciókat, amelyek miatt az emberek általában a CommonMarkot, a GitHub Flavored Markdownt (GFM), a MultiMarkdownt vagy a Kramdownt választják --- anélkül, hogy lemondanának a többi változat előnyeiről.

A Markedben az **Apex (béta)** mindig az Apex **egységesített (unified)** módjában fut (az összes funkciócsoport egyszerre engedélyezve). A Markedben egyelőre nem választható külön Apex „CommonMark mód” vagy „Kramdown mód”; ez a lehetőség később még megjelenhet.

Nézd meg a [Markdown Dingust](x-marked-3://dingus?processor=apex), hogy kipróbáld az Apexet, vagy nyisd meg a {% appmenu Help, Markdown Reference %} elemet, és válaszd az **Apex** fület egy tömör gyorsreferenciáért.

---

## Miért létezik az Apex [why-apex-exists]

A Markdown „változatai” jó okokból fejlődtek külön utakon --- a GitHubnak feladatlistákra és táblázatokra volt szüksége, a MultiMarkdownnak lábjegyzetekre és metaadatokra, a Kramdownnak attribútumlistákra --- de ha valaki egy adott feldolgozó mellett dönt, azzal általában le kell mondania egy másik szintaxisáról.

Az Apex célja ezeknek a kiterjesztéseknek az **egyesítése**, hogy egyetlen dokumentum használhassa:

- A mindennapi CommonMark / GFM szokásokat (kódblokkok, feladatlisták, áthúzás, GFM táblázatok)
- A MultiMarkdown-stílusú lábjegyzeteket, rövidítéseket és metaadat-szokásokat
- A Kramdown-barát definíciós listákat, matematikai képleteket, és (haladó használatra) attribútumlistákat
- A Marked-specifikus kényelmi funkciókat, például a kiemeléseket (callout), a Critic Markupot és a tartalomjegyzék-jelölőket

A teljes forrásdokumentáció az [Apex wikin](https://github.com/ApexMarkdown/apex/wiki) érhető el. Ez az oldal azt mutatja be, amire a mindennapi használat során a Marked előnézetében szükséged lehet.

---

## Az Apex engedélyezése a Markedben [enabling-apex-in-marked]

1. Nyisd meg a {% prefspane Processor %} elemet.
2. Állítsd az **Alapértelmezett Markdown-feldolgozó** beállítást **Apex (béta)** értékre.
3. Vagy dokumentumonként felülbírálhatod metaadatokkal, például `Processor: apex` (aliasok: `apex-beta`, `unified`).

Az aliasok AppleScriptből, a Conductor „Run Processor” műveleteiből, egyéni feldolgozók stdout kimeneteiből (`APEX`), valamint `x-marked://` defaults URL-ekből is működnek.

T> Ebben a bétaverzióban a Marked továbbra is kibontja a saját fájlbefoglalásait (`<<[file]` és a kapcsolódó Marked include útvonalak), mielőtt az Apex lefutna. Az Apex natív include motorja a Markedben a sandboxolás miatt ki van kapcsolva. Használd a Marked include funkcióit úgy, ahogy eddig is.

---

## Alapszintaxis, amit az Apex hozzáad vagy egységesít [basic-syntax]

A szabványos Markdown (címsorok, kiemelések, hivatkozások, képek, listák, idézetblokkok, kód) a várt módon működik. Az alábbiak azok a kiegészítések, amelyekre az Apexre való átálláskor a legtöbbeknek szükségük van.

### Feladatlisták [task-lists]

```markdown
- [ ] Todo
- [x] Done
```

### Áthúzás [strikethrough]

```markdown
~~removed text~~
```

### Táblázatok [tables]

GFM-stílusú „pipe” táblázatok fejlécelválasztókkal és oszlopigazítással:

```markdown
| Left | Center | Right |
| :--- | :----: | ----: |
| a    | b      | c     |
```

A haladó táblázatfunkciók (sorösszevonás `^^`, oszlopösszevonás, feliratok, rácstáblázatok, CSV) a wikin vannak dokumentálva: [Táblázatok](https://github.com/ApexMarkdown/apex/wiki/Tables).

### Lábjegyzetek [footnotes]

Hivatkozás-stílusú:

```markdown
See the note[^1].

[^1]: Footnote text.
```

A MultiMarkdownból / Kramdownból ismert soron belüli stílusok is támogatottak. Részletek: [Szintaxis](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Definíciós listák [definition-lists]

```markdown
Apple
: A fruit.
: A computer company.
```

### Felső és alsó index [superscript-and-subscript]

```markdown
Text^super^ and H~2~O
```

### Matematika [math]

Soron belüli `$x^2$` és önálló (display) `$$...$$` (a Marked MathJax / KaTeX beállításai továbbra is szabályozzák az előnézet megjelenését).

### Kiemelések (callout) [callouts]

Obsidian / Bear-stílusú:

```markdown
> [!NOTE]
> Something worth highlighting.
```

Lásd még a Marked [Speciális szintaxis](Special_Syntax.html) oldalát, valamint az Apex [Kiemelések](https://github.com/ApexMarkdown/apex/wiki/Callouts) wikioldalát.

### Critic Markup [critic-markup]

```markdown
{++insertion++}
{--deletion--}
{==highlight==}
{>>comment<<}
```

Engedélyezd a Critic Markupot a Markedben a szokásos módon; az Apex képes megjeleníteni a critic szintaxist a feldolgozási folyamatban. Lásd: [CriticMarkup](CriticMarkup.html).

### Rövidítések [abbreviations]

```markdown
*[HTML]: HyperText Markup Language

The HTML spec is long.
```

### Emoji rövidkódok [emoji-shortcodes]

```markdown
Ship it :rocket:
```

### Metaadatok [metadata]

A YAML front matter, a MultiMarkdown-stílusú `Key: Value` fejlécek és a Pandoc címblokkok felismerésre kerülnek. Az értékeket `[%key]` formában szúrhatod be, ahol ez támogatott.

Konfigurációs részletek a wikin: [Konfiguráció](https://github.com/ApexMarkdown/apex/wiki/Configuration) és [Metaadat-átalakítások](https://github.com/ApexMarkdown/apex/wiki/Metadata-Transforms).

### Tartalomjegyzék-jelölők [table-of-contents-markers]

Az Apex felismeri a gyakori tartalomjegyzék-jelölőket, köztük:

- `<!--TOC-->`
- `{{TOC}}` vagy `{{TOC:2-4}}`
- Kramdown-stílusú `{:toc}`

Egy címsort a `{:.no_toc}` használatával zárhatsz ki, ahol az IAL elérhető. További információ: [Szintaxis](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Speciális jelölők [special-markers]

A Marked-specifikus HTML-megjegyzések, mint például a `<!--BREAK-->` (oldaltörés) és a `<!--PAUSE:N-->` (automatikus görgetés), továbbra is működnek az Apex előnézeteiben.

---

## Haladó témák (wiki) [advanced-topics-wiki]

Az olyan funkciókhoz, amelyek erőteljesek, de a mindennapi előnézet során ritkábban használtak, nézd meg az [Apex wikit](https://github.com/ApexMarkdown/apex/wiki):

| Téma | Wiki |
|------|------|
| Index generálás | [Indexek](https://github.com/ApexMarkdown/apex/wiki/Indices) |
| Hivatkozások / bibliográfia | [Hivatkozások](https://github.com/ApexMarkdown/apex/wiki/Citations) |
| Inline attribútumlisták, span-ek, fenced divek | [Inline attribútumlisták](https://github.com/ApexMarkdown/apex/wiki/Inline-Attribute-Lists) |
| Többfájlos dokumentumok és include-ok | [Többfájlos dokumentumok](https://github.com/ApexMarkdown/apex/wiki/Multi-File-Documents) |
| Címsor-azonosító formátumok | [Címsor-azonosítók](https://github.com/ApexMarkdown/apex/wiki/Header-IDs) |
| Többformátumú képek | [Többformátumú képek](https://github.com/ApexMarkdown/apex/wiki/Multi-Format-Images) |
| Kompatibilitási módok (CLI) | [Módok](https://github.com/ApexMarkdown/apex/wiki/Modes) |
| Beépülők és szűrők | [Beépülők](https://github.com/ApexMarkdown/apex/wiki/Plugins), [Szűrők](https://github.com/ApexMarkdown/apex/wiki/Filters) |
| Quarto / Pandoc / Jekyll | [Quarto mód](https://github.com/ApexMarkdown/apex/wiki/Quarto-Mode), [Pandoc integráció](https://github.com/ApexMarkdown/apex/wiki/Pandoc-Integration), [Jekyll](https://github.com/ApexMarkdown/apex/wiki/Using-Apex-with-Jekyll) |

---

## Lásd még [see-also]

- [A feldolgozó kiválasztása](Choosing_a_Processor.html) --- mikor érdemes a MultiMarkdownt, a CommonMarkot, a Kramdownt, a Discountot vagy az Apexet választani
- [Beállítások: Feldolgozó](Settings_Processor.html)
- [Markdown Dingus](Markdown_Dingus.html)
- [Az Apex wiki főoldala](https://github.com/ApexMarkdown/apex/wiki)
- Hibák bejelentése: [support.markedapp.com](https://support.markedapp.com)
