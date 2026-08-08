<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Tekintse meg a [Markdown Dingus](x-marked-3://dingus?processor=commonmark)-t, hogy kísérletezzen a CommonMark (GFM) processzorral.


## Mi az a CommonMark? [what-is-commonmark]

A CommonMark a Markdown szigorúan meghatározott, nagymértékben kompatibilis megvalósítása. Azért hozták létre, hogy orvosolja John Gruber eredeti Markdown specifikációjában rejlő kétértelműségeket és következetlenségeket, amelyek különböző platformokon és eszközökön eltérő megvalósításokhoz vezettek.

## Miért létezik a CommonMark? [why-commonmark-exists]

John Gruber eredeti Markdown-specifikációja szándékosan kétértelmű volt számos területen, ami a különféle megvalósítások eltérő értelmezéseihez vezetett. Ez olyan problémákat okozott, hogy ugyanaz a Markdown-dokumentum eltérően jelenik meg a különböző platformokon (GitHub, StackOverflow, Reddit stb.).

A CommonMark a következőket kínálja:

- **Egyértelmű specifikációk** minden Markdown szintaxishoz
- **Átfogó tesztcsomag** a következetes viselkedés biztosítása érdekében
- **Törölje az elsőbbségi szabályokat** az ütköző szintaxis esetén
- **Részletes elemzési algoritmus**, amely következetesen megvalósítható

## Főbb különbségek a szabványos leértékeléshez képest [key-differences-from-standard-markdown]

### 1. **Szigorúbb elemzési szabályok** [1-stricter-parsing-rules]

A CommonMark következetesebb elemzési viselkedést kényszerít ki:

**Üres sorok a blokkelemek előtt**

- A CommonMark használatához üres sorok szükségesek a címsorok, idézőjelek és listák előtt
- A Standard Markdown gyakran lehetővé teszi ezeket üres sorok nélkül

```markdown
Text
# Heading
```

*CommonMark: Üres sort igényel a címsor előtt*

*Standard Markdown: gyakran üres sor nélkül is lehetővé teszi*

### 2. **Listaelem elemzése** [2-list-item-parsing]

**Behúzási követelmények**

- A CommonMark speciális szabályokat tartalmaz a listaelemek behúzására
- Az allistákat következetesen be kell húzni (általában 4 szóköz)
- A szabványos Markdown implementációk ettől eltérőek

```markdown
1. First item
   - Sublist item (4 spaces required in CommonMark)
2. Second item
```

**Lista folytatás**

- A CommonMark világos szabályokkal rendelkezik arra vonatkozóan, hogy a listaelemek mikor „lazák” vagy „szorosak”
- A laza listák `<p>` címkékbe csomagolják az elemeket, a szűk listák nem

### 3. **Kódblokk kezelése** [3-code-block-handling]

**Kerített kódblokkok**

- A CommonMark szabványosítja az elkerített kódblokk szintaxisát backtickekkel vagy tildákkal
- Konzisztens behúzást és záró jelzőket igényel


    ``` nyelv
    kód itt
    ```


**Behúzott kódblokkok**

- A CommonMark üres sorokat igényel a behúzott kódblokkok előtt
- A Standard Markdown gyakran lehetővé teszi üres sorok nélkül

### 4. **Link és képfeldolgozás** [4-link-and-image-processing]

**Hivatkozási hivatkozás elsőbbsége**

- A CommonMark világos szabályokkal rendelkezik, amelyeknél a referenciadefiníció élvez elsőbbséget
- Ugyanahhoz a hivatkozáshoz több definíciót is következetesen kezel a rendszer

```markdown
[link1]: /url1
[link1]: /url2
[link1]  <!-- Uses /url2 in CommonMark -->
```

**Link elemzési sorrend**

- A CommonMark a hivatkozásokat a kiemelés előtt dolgozza fel
- Ez befolyásolja a beágyazott szintaxis értelmezését

### 5. **Kiemelés és erős hangsúly** [5-emphasis-and-strong-emphasis]

**Beágyazott kiemelési szabályok**

- A CommonMark speciális algoritmusokkal rendelkezik a beágyazott `*` és `_` markerek kezelésére
- Megakadályozza az összetett kiemelési minták félreérthető elemzését

```markdown
*foo *bar* baz*  <!-- Clear precedence rules in CommonMark -->
```

**Határoló feldolgozás**

- A CommonMark "határoló verem" algoritmust használ a következetes hangsúlyelemzés érdekében
- A szabványos Markdown megvalósítások megközelítése eltérő

### 6. **HTML blokk feldolgozás** [6-html-block-processing]

**HTML blokkészlelés**

- A CommonMark 7 különböző típusú HTML-blokkot tartalmaz meghatározott szabályokkal
- Minden típusnak más-más követelményei vannak a kezdési/végi feltételekre

```html
<div>
This is an HTML block in CommonMark
</div>
```

### 7. **Vonaltörés kezelése** [7-line-break-handling]

**Hard Line Breaks**

- A CommonMark két szóközt igényel a sor végén a kemény törésekhez
- Az egysoros törések lágy törésekké válnak (HTML-ben figyelmen kívül hagyva)

```markdown
Line one
Line two  <!-- Two spaces before line break -->
```

### 8. **Entitás- és karakterhivatkozások** [8-entity-and-character-references]

**Numerikus karakterhivatkozások**

- A CommonMark támogatja a decimális és hexadecimális numerikus hivatkozásokat is
- A szabványos Markdown támogatás változó

```html
&#8212;  <!-- Decimal -->
&#x2014; <!-- Hexadecimal -->
```

## CommonMark elemzési algoritmus [commonmark-parsing-algorithm]

A CommonMark kétfázisú elemzési megközelítést alkalmaz:

### 1. fázis: Blokkstruktúra [phase-1-block-structure]

1. **Line Processing**: Minden sor blokkszintű markerek szempontjából elemzésre kerül
2. **Konténerblokkok**: A blokkidézetek, listák és egyéb tárolók azonosítva
3. **Leaf Blocks**: A címsorok, kódblokkok, bekezdések feldolgozása megtörténik
4. **Referencia hivatkozások**: A hivatkozásdefiníciókat későbbi felhasználás céljából összegyűjtjük

### 2. fázis: Inline szerkezet [phase-2-inline-structure]

1. **Inline Processing**: A blokkon belüli szöveg elemzése soron belüli elemekhez történik
2. **Kiemelés elemzése**: Határoló verem-algoritmust használ a következetes kiemelés érdekében
3. **Link feloldása**: A hivatkozási hivatkozások feloldása összegyűjtött definíciók segítségével történik
4. **Entitásfeldolgozás**: A karakterhivatkozások tényleges karakterekké alakulnak

## A CommonMark előnyei [benefits-of-commonmark]

1. **Kijósolható viselkedés**: Ugyanaz a bemenet mindig ugyanazt a kimenetet állítja elő
2. **Platformok közötti kompatibilitás**: Következetesen működik a különböző eszközökön
3. **Átfogó tesztelés**: A kiterjedt tesztkészlet biztosítja a megbízhatóságot
4. **Egyértelmű dokumentáció**: A részletes specifikáció kiküszöböli a találgatásokat
5. **Jövőbiztos**: Jól meghatározott bővítési pontok az új funkciókhoz

## Végrehajtási megjegyzések [implementation-notes]

A CommonMark célja:

- **A specifikációkkal kompatibilis**: Pontosan követi a hivatalos CommonMark specifikációt
- **Tesztvezérelt**: megfelel a hivatalos CommonMark tesztcsomagnak
- **Bővíthető**: A kompatibilitás megőrzése mellett további funkciókkal bővíthető
- **Gyors**: A teljesítmény érdekében optimalizált elemzési algoritmusok

## Források [resources]

- [CommonMark specifikáció](https://spec.commonmark.org/0.31.2/)
- [CommonMark Test Suite](https://github.com/commonmark/commonmark-spec)
- [CommonMark Dingus](https://spec.commonmark.org/dingus/) - Online tesztelőeszköz
- [CommonMark vitafórum](https://talk.commonmark.org/)

---

*Ez a dokumentáció a CommonMark 0.31.2-re (2024-01-28) vonatkozik. A legfrissebb információkért mindig olvassa el a hivatalos specifikációt.*