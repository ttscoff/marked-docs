<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Tekintse meg a [Markdown Dingus](x-marked-3://dingus?processor=kramdown)-t, hogy kísérletezzen a Kramdown processzorral.

## Mi az a Kramdown?

A Kramdown egy gyors, tiszta Ruby Markdown-szuperset konverter, amely kiterjeszti az eredeti Markdown szintaxist olyan funkciókkal, mint a Maruku, a PHP Markdown Extra és a Pandoc. Szigorú szintaxist biztosít határozott szabályokkal, miközben fenntartja a kompatibilitást a legtöbb Markdown dokumentummal.

## Főbb jellemzők

- **Gyors és tiszta Ruby**: Teljesen Ruby nyelven íródott a teljesítmény és a hordozhatóság érdekében
- **Szigorú szintaxis**: Határozott szabályokat és egyértelmű előírásokat biztosít
- **Továbbfejlesztett funkciók**: Sok olyan bővítményt tartalmaz, amelyek nem találhatók meg a szabványos Markdownban
- **Jekyll Integration**: Alapértelmezett Markdown processzor a Jekyll statikus helygenerátorhoz
- **Átfogó**: Támogatja a blokkszintű és a span szintű elemeket is kiterjedt testreszabással

## Főbb különbségek a szabványos leértékeléshez képest

### 1. **Továbbfejlesztett blokkszintű elemek**

**Definíciós listák**

- A Kramdown támogatja a definíciós listákat (nem a szabványos Markdownban)
- Az `:` karaktert használja a kifejezések és a definíciók elkülönítésére

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

**Asztalok**

- Teljes táblázattámogatás fejlécekkel, igazítással és formázással
- Átfogóbb, mint az alap Markdown tábla szintaxisa

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Matek blokkok**

- Matematikai kifejezések támogatása LaTeX szintaxis használatával
- Inline és blokk matematikai támogatás

```markdown
Inline math: $E = mc^2$

Block math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 2. **Speciális szövegjelölés**

**Lábjegyzetek**

- Teljes lábjegyzet támogatás automatikus számozással
- Hivatkozási stílusú lábjegyzetek `[^1]` szintaxissal

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Rövidítések**

- HTML-stílusú rövidítések támogatása
- A meghatározott rövidítések automatikus bővítése

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

**Tipográfiai szimbólumok**

- A gyakori tipográfiai karakterek automatikus átalakítása
- Intelligens idézetek, kötőjelek, ellipszisek stb.

```markdown
"Smart quotes" and -- em dashes -- and ... ellipses
Even << guillemets >>
```

### 3. **Attribútumlisták és bővítmények**

**Attribútumlista-definíciók (ALD-k)**

- Újrafelhasználható attribútumkészletek meghatározása
- Azonosítók, osztályok és egyéni attribútumok támogatása

```markdown
{:ref-name: #myid .my-class title="My Title"}

A paragraph with attributes.
{: #para-one .highlight}
```

**Inline attribútumlisták (IAL)**

- Attribútumok csatolása meghatározott elemekhez
- Mind blokk szintű, mind span szintű támogatás

```markdown
This *is*{:.underline} some ⟦3⟧{:#id}{:.class}.
A [link](test.html){:rel='something'} and some **tools**{:.tools}.
```

**Bővítmények**

- Egyedi bővítőrendszer a további funkciókhoz
- Beépített bővítmények a megjegyzésekhez és opciókhoz

```markdown
{::comment}
This text is completely ignored by kramdown.
{:/comment}

{::options key="val" /}
```

### 4. **Továbbfejlesztett kódblokk támogatás**

**Nyelv specifikáció**

- Automatikus szintaxis kiemelés elkerített kódblokkokhoz
- Számos programozási nyelv támogatása

    ``` rubin
    def hello
      "Hello, World!"
    vége
    ```

**Normál kódblokkok**

- A behúzott kódblokkok jobb kezelése
- Jobb integráció más blokk elemekkel

### 5. **Szigorúbb elemzési szabályok**

**Vonal burkolása**

- Kemény csomagolt tartalom támogatása (lusta szintaxis)
- Egyértelmű szabályok arra vonatkozóan, hogy mikor engedélyezett a vonaltörlés
- Olvashatóság miatt nem ajánlott, de kompatibilitás miatt támogatott

**Fülkezelés**

- Feltételezi, hogy a tabulátorok a négy többszörösét jelentik
- A tabulátorok csak a sorok elején engedélyezettek behúzáshoz
- Nem szabad szóközt előzni

**Blokkhatárok**

- Egyértelmű szabályok arra vonatkozóan, hogy az elemeknek mikor kell kezdődnie/végeznie a blokkhatárokon
- Konzisztens viselkedés a különböző elemtípusok között

### 6. **Speciális link- és képtámogatás**

**Automatikus linkek**

- Továbbfejlesztett automatikus linkérzékelés
- Az URL-ek és e-mail címek jobb kezelése

**Referencia linkek**

- Továbbfejlesztett hivatkozási hivatkozás feldolgozás
- Jobb konfliktusmegoldás több definícióhoz

**Képtulajdonságok**

- Képattribútumok támogatása IAL-okon keresztül
- Szélesség, magasság, alternatív szöveg és egyéb HTML-attribútumok

```markdown
![Alt text](image.jpg){:width="300" height="200" class="responsive"}
```

### 7. **HTML integráció**

**HTML blokkok**

- A HTML jobb kezelése a Markdownon belül
- HTML attribútumok és feldolgozás támogatása
- Rugalmasabb, mint a szokásos Markdown HTML-kezelés

**HTML átnyúlik**

- Inline HTML attribútum támogatással
- Jobb integráció a Markdown szintaxissal

### 8. **Matematikai kifejezések**

**Inline Math**

- `$...$` szintaxis a soron belüli matematikai kifejezésekhez
- LaTeX-kompatibilis szintaxis

**Matek blokkolása**

- `$$...$$` szintaxis blokk matematikai kifejezésekhez
- Komplex egyenletek és képletek támogatása

## Kramdown vs egyéb Markdown ízek

| Funkció | Kramdown | CommonMark (GFM) | GitHub ízesítésű | MultiMarkdown | Standard |
| ----------------- | -------- | ---------- | ---------------- | ------------- | -------- |
| Áthúzott | Nem | Igen | Nem | Nem | Nem |
| Feladatlisták | Nem | Nem | Igen | Igen | Nem |
| Bekerített kód | Igen | Igen | Igen | Igen | Nem |
| Matek | Igen | Nem | Igen | Igen | Nem |
| Lábjegyzetek | Igen | Igen | Igen | Igen | Nem |
| Definíciós listák | Igen | Nem | Nem | Igen | Nem |
| Rövidítések | Igen | Nem | Nem | Nem | Nem |
| Attribútumlisták | Igen | Nem | Nem | Nem | Nem |
| Tipográfia | Igen | Nem | Nem | Igen | Nem |

## A Kramdown legfontosabb előnyei

1. **Átfogó szolgáltatáskészlet**: Sok olyan bővítményt tartalmaz, amelyek más megvalósításokban nem találhatók meg
2. **Jekyll integráció**: Zökkenőmentes integráció a Jekyll statikus helygenerátorral
3. **Ruby ökoszisztéma**: Pure Ruby implementáció jó Ruby szerszámozási támogatással
4. **Bővíthetőség**: Egyedi bővítőrendszer a további funkciókhoz
5. **Attribútumtámogatás**: Gazdag attribútumrendszer a HTML-kimenet testreszabásához
6. **Matematikai támogatás**: A LaTeX matematikai kifejezések beépített támogatása
7. **Szigorú elemzés**: Világos, egyértelmű elemzési szabályok

## Általános használati esetek

**Jekyll webhelyek**

- Alapértelmezett processzor a Jekyll statikus webhely generálásához
- Kiváló dokumentációs és blogoldalak számára

**Műszaki dokumentáció**

- Tudományos és műszaki írások matematikai támogatása
- Attribútumlisták a speciális HTML testreszabáshoz

**Akadémiai írás**

- Lábjegyzet támogatás az idézetek és hivatkozások számára
- Matematikai kifejezések képletekhez és egyenletekhez

**Tartalomkezelés**

- Bővítmények az egyéni funkciókhoz
- Attribútumlisták a metaadatokhoz és a stílushoz

## Források

- [Kramdown szintaxis dokumentációja](https://kramdown.gettalong.org/syntax.html)
- [Kramdown Converter dokumentáció](https://kramdown.gettalong.org/converter.html)
- [Jekyll integrációs útmutató](https://jekyllrb.com/docs/configuration/markdown/)
- [Kramdown GitHub Repository](https://github.com/gettalong/kramdown)

## Áttérés a Standard Markdownból

A legtöbb szabványos Markdown dokumentum módosítás nélkül működik a Kramdownnal. A Kramdown szolgáltatásainak kihasználásához:

1. **Definíciólisták hozzáadása**: Szószedetek és kifejezéslisták konvertálása
2. **Attribútumlisták használata**: Adjon hozzá azonosítókat, osztályokat és egyéni attribútumokat
3. **Lábjegyzetek megvalósítása**: A zárójeles hivatkozások konvertálása

## Bevált gyakorlatok

1. **Kerülje a lusta szintaxist**: Ne hagyatkozzon a kemény csomagolásra az olvashatóság érdekében
2. **Attribútumlisták használata**: Használja ki az IAL-t a stílus és a metaadatok létrehozásához
3. **Konzisztens behúzás**: Ha lehetséges, használjon szóközt a tabulátorok helyett

---

*Ez a dokumentáció a Kramdown 2.5.1-re vonatkozik. A legfrissebb információkért mindig olvassa el a hivatalos dokumentációt a [kramdown.gettalong.org] címen (https://kramdown.gettalong.org/).*