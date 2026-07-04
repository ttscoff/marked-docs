<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Tekintse meg a [Markdown Dingus](x-marked-3://dingus?processor=multimarkdown) dokumentumot, hogy kísérletezzen a MultiMarkdown processzorral.

## Mi az a MultiMarkdown?

A MultiMarkdown egy kiterjesztett Markdown processzor, amelyet úgy terveztek, hogy a weboldal töredékei helyett teljes dokumentumokkal dolgozzon. Kibővíti az eredeti Markdown szintaxist olyan funkciókkal, amelyek lehetővé teszik a konvertálást többféle kimeneti formátumra, beleértve a HTML, LaTeX, PDF, ODF és Microsoft Word dokumentumokat.

## Főbb jellemzők

- **Dokumentumközpontú**: Teljes dokumentumokhoz tervezték, nem csak webrészletekhez
- **Több formátumú kimenet**: HTML, LaTeX, PDF, ODF, RTF és Word formátumba konvertál
- **Content Over Presentation**: A dokumentum szerkezetére és jelentésére összpontosít
- **Cross-Platform**: Bármilyen operációs rendszeren működik bármilyen szövegszerkesztővel
- **Bővíthető**: Gazdag szolgáltatáskészlet összetett dokumentumkövetelményekhez
- **5-ös verzió**: Teljes átírás jobb teljesítménnyel és megbízhatósággal

## Filozófia és tervezési célok

A MultiMarkdown azt az elvet követi, hogy **a tartalom fontosabb, mint a prezentáció**. A hangsúly a dokumentumok jelentésének ábrázolásán van (ez egy lista, azaz egy táblázat stb.), nem pedig a betűtípusok, színek vagy stílusok diktálásán.

A cél, hogy az emberek 80%-a által írt dokumentumok 80%-a használható legyen, így alkalmas legyen regények, szakdolgozatok, műszaki dokumentációk és a legtöbb egyéb írásos tartalom elkészítésére.

## Főbb szolgáltatások és bővítmények

### 1. **Metaadat-támogatás**

- Dokumentum metaadatok a fájlok tetején
- Cím, szerző, dátum és egyéni változók
- Automatikus felvétel a kimeneti fejlécekbe

```markdown
title: My Document
author: John Doe
date: 2024-01-15
custom: value

<!-- A blank line ends the metadata -->
Content
---

# Document Content
```

**Metaadat-változók**

- Használjon metaadat értékeket a dokumentumban
- Szintaxis: `[%variable_name]`
- Automatikus helyettesítés a feldolgozás során

```markdown
Title: [%title]
Author: [%author]
Date: [%date]
```

### 2. **Speciális táblázatok**

**Teljes asztali támogatás**

- Fejlécek, igazítás és összetett táblázatszerkezetek
- Táblázat feliratok és címkék támogatása
- Kereszthivatkozások táblázatokra

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |

Table: Sample Table with Alignment
```

**Asztal jellemzői**

- Oszlopigazítás kettőspontokkal
- A táblázat feliratai és címkéi
- kereszthivatkozások a `[Table 1]`-vel
- Komplex táblaszerkezetek támogatása

### 3. **Lábjegyzetek és idézetek**

**Lábjegyzetek**

- Hivatkozási stílusú lábjegyzetek `[^1]` szintaxissal
- Automatikus számozás és linkelés
- A szövegközi lábjegyzetek támogatása

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Idézettámogatás**

- Akadémiai idézetek formázása
- Bibliográfia generáció
- Különféle idézetstílusok támogatása

```
This is a statement that should be attributed to
its source[p. 23][#Doe:2006].
```

És a következő a hivatkozás leírása
használt az irodalomjegyzékben.

```
[#Doe:2006]: John Doe. *Some Big Fancy Book*.  Vanity Press, 2006.
```

A HTML-kimenetben az idézeteket nem lehet megkülönböztetni a lábjegyzetektől.

Nem kötelező helymeghatározót használni (pl. 23. oldal), és nincsenek speciális szabályok arra vonatkozóan, hogy mi használható helymeghatározóként, ha úgy dönt, hogy használja. Ha inkább kihagyja a lokátort, csak használjon üres szögletes zárójelet az idézet előtt:

```
This is a statement that should be attributed to its
source[][#Doe:2006].
```

Nincsenek szabályok az Ön által használt idézőkulcs-formátumra (pl. Doe:2006), de azt egy `#`-nek kell megelőznie, akárcsak a lábjegyzeteknél az `^` karaktert.

### 4. **Kereszthivatkozások**

**Automatikus kereszthivatkozások**

- Hivatkozás címsorokhoz, táblázatokhoz, ábrákhoz és egyenletekhez
- Automatikus címkegenerálás
- Egyedi címkék támogatása

```markdown
See [Table 1] for details.
Refer to [Section 2.1] for more information.

## Section 2.1 [section-2-1]
```

**Referencia típusok**

- Címsorok: `[Section 1]`, `[Heading Title]`
- Táblázatok: `[Table 1]`, `[Table: Caption]`
- Ábrák: `[Figure 1]`, `[Figure: Caption]`
- Egyenletek: `[Equation 1]`

### 5. **Definíciólisták**

**Kifejezés-meghatározás párok**

- Definíciós listák támogatása
- Több definíció kifejezésenként
- Megfelelő HTML `<dl>` kimenet

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

### 6. **Elkerített kódblokkok**

**Nyelvspecifikus kódblokkok**

- Háromszoros backtick nyelvi specifikációval
- Szintaxis kiemelés támogatása
- Automatikus nyelvérzékelés

```markdown
```python
def hello():
    print("Hello, World!")
```
```

**Code Block Features**

- Language specification for syntax highlighting
- Support for many programming languages
- Proper HTML ⟦14⟧ output

### 7. **Math Support**

**Mathematical Expressions**

- LaTeX-compatible math syntax
- Both inline and block math support
- Integration with LaTeX output

```markdown
Inline math: $E = mc^2$

Block math:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 8. **Kép- és linkattribútumok**

**Továbbfejlesztett linkek és képek**

- HTML attribútumok támogatása
- Szélesség, magasság, alternatív szöveg stb
- Jobb integráció a kimeneti formátumokkal

```markdown
[Link text]: url.html title="Link title" class="external"
```

### 9. **Transclusion**

**Fájlbefoglalás**

- Más fájlokat is beilleszthet a dokumentumokba
- Beágyazott támogatás
- Automatikus útfelbontás

```markdown
{{chapter1.md}}
{{../shared/intro.md}}
```

**Átvezetési jellemzők**

- Fájl beillesztése a következővel: `{{filename}}`
- Relatív és abszolút utak támogatása
- Beágyazott transzlusio támogatás
- Manifest generálása a mellékelt fájlok számára

### 10. **CriticMarkup integráció**

**Változáskövetés**

- A CriticMarkup szintaxis támogatása
- Kövesse nyomon a kiegészítéseket, törléseket és megjegyzéseket
- Együttműködő szerkesztési funkciók

```markdown
This is {>>deleted text<<} and this is {++added text++}.

This is a {~~deletion~>replacement~~}.
```

### 11. **Tartalomjegyzék**

**Automatikus tartalomjegyzék generálás**

- `{{TOC}}` helyőrző a tartalomjegyzékhez
- Címsorokon alapuló hierarchikus felépítés
- Testreszabható TOC generálás

```markdown
# Document Title

{{TOC}}

## Section 1
Content here...

## Section 2
More content...
```

### 12. **Rövidítések**

**HTML-stílusú rövidítések**

- Határozza meg az automatikus bővítés rövidítését
- Eszköztippek és magyarázatok támogatása
- Megfelelő HTML `<abbr>` kimenet

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

## MultiMarkdown v5 vs egyéb Markdown ízek

| Funkció | MultiMarkdown v5 | CommonMark (GFM) | Kedvezmény | Kramdown | Standard |
| ----------------- | ----------------- | ---------- | ------------ | -------- | -------- |
| Táblázatok | Igen | Nem | Igen | Igen | Nem |
| Áthúzott | Igen | Nem | Igen | Nem | Nem |
| Feladatlisták | Igen | Nem | Igen | Nem | Nem |
| Bekerített kód | Igen | Igen | Igen | Igen | Nem |
| Matek | Igen | Nem | Nem | Igen | Nem |
| Lábjegyzetek | Igen | Nem | Igen | Igen | Nem |
| Definíciós listák | Igen | Nem | Nem | Igen | Nem |
| Rövidítések | Igen | Nem | Nem | Igen | Nem |
| Attribútumlisták | Igen | Nem | Nem | Igen | Nem |
| Kiterjesztések | Igen | Nem | Korlátozott | Igen | Nem |
| Tipográfia | Igen | Nem | Alapvető | Igen | Nem |
| Automatikus linkek | Igen | Nem | Igen | Nem | Nem |
| Kereszthivatkozások | Igen | Nem | Nem | Nem | Nem |
| Idézetek | Igen | Nem | Nem | Nem | Nem |
| Transzklúzió | Igen | Nem | Nem | Nem | Nem |
| Metaadatok | Igen | Nem | Nem | Nem | Nem |

## A MultiMarkdown v5 legfontosabb előnyei

1. **Dokumentumközpontú**: Teljes dokumentumokhoz tervezték, nem csak webrészletekhez
2. **Több formátumú kimenet**: Konvertálás HTML, LaTeX, PDF, ODF, RTF és Word formátumba
3. **Akadémiai támogatás**: Idézetek, lábjegyzetek és kereszthivatkozások
4. **Professzionális szolgáltatások**: Metaadatok, áttétel és speciális formázás
5. **Cross-Platform**: Bármilyen operációs rendszeren működik
6. **Jövőbiztos**: Az egyszerű szöveges formátum biztosítja a hosszú távú kompatibilitást
7. **Bővíthető**: Gazdag szolgáltatáskészlet összetett dokumentumkövetelményekhez

## Általános használati esetek

**Akadémiai írás**

- Szakdolgozatok, disszertációk és kutatási dolgozatok
- Hivatkozáskezelés és bibliográfia generálása
- Kereszthivatkozások és lábjegyzetek

**Műszaki dokumentáció**

- API dokumentáció és felhasználói útmutatók
- Műszaki adatok és kézikönyvek
- Kóddokumentáció szintaktikai kiemeléssel

**Kiadás**

- Könyvek, cikkek és jelentések
- Több formátumú kimenet különböző platformokhoz
- Professzionális dokumentum formázás

**Tartalomkezelés**

- Dokumentációs weboldalak
- Tudásbázisok és wikik
- Együttműködő írási projektek

## Bevált gyakorlatok

1. **Metaadatok használata**: Használja ki a YAML előlapját a dokumentuminformációkhoz
2. **Struktúra címsorokkal**: Használjon megfelelő címsor-hierarchiát a tartalomjegyzék generálásához
3. **Használja ki a kereszthivatkozásokat**: Használjon automatikus linkelést a jobb navigáció érdekében
4. **Rendezés transzmisszióval**: A nagy dokumentumok felosztása kezelhető fájlokra
5. **Kimenet tesztelése**: Ellenőrizze a formázást a különböző kimeneti formátumok között
6. **Idézetek használata**: Alkalmazzon megfelelő tudományos idézési gyakorlatot

## Migráció más Markdown-ízekből

A legtöbb szabványos Markdown változtatás nélkül működik a MultiMarkdown-nal. Az MMD funkcióinak kihasználása:

1. **Metaadatok hozzáadása**: A dokumentuminformációkhoz tartalmazza a YAML előlapját
2. **Kereszthivatkozások használata**: Cserélje ki a kézi hivatkozásokat automatikus hivatkozásokra
3. **Idézetek megvalósítása**: Adjon hozzá megfelelő akadémiai hivatkozási formázást
4. **Struktúra áttétellel**: A nagy dokumentumok felosztása kisebb fájlokra
5. **Tőkeáttételi táblák**: Használjon fejlett táblázatfunkciókat az adatok megjelenítéséhez

## Források

- [MultiMarkdown felhasználói kézikönyv](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html)
- [MultiMarkdown szintaxis útmutató](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html#syntax)
- [MultiMarkdown GitHub Repository](https://github.com/fletcher/MultiMarkdown-5)
- [MultiMarkdown dokumentáció](https://fletcher.github.io/MultiMarkdown-5/)

---

*Ez a dokumentáció a MultiMarkdown v5.1.0-ra vonatkozik. A legfrissebb információkért mindig tekintse meg a hivatalos MultiMarkdown dokumentációt a [fletcher.github.io/MultiMarkdown-5] címen (https://fletcher.github.io/MultiMarkdown-5/).*