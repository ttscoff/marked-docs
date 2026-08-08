<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Tekintse meg a [Markdown Dingus](x-marked-3://dingus?processor=discount) elemet, hogy kísérletezzen a Discount processzorral.

## Mi az a Discount GFM? [what-is-discount-gfm]

A Discount GFM (GitHub Flavored Markdown) egy C-alapú Markdown processzor, amely a GitHub kiterjesztett Markdown szintaxisát valósítja meg. Az eredeti Discount-könyvtáron alapul, de GitHub-specifikus funkciókkal, például táblázatokkal, feladatlistákkal, áthúzott szöveggel és automatikus URL-összekapcsolással bővítve.

## Főbb jellemzők [key-characteristics]

- **C-alapú teljesítmény**: Gyors, natív C implementáció az optimális teljesítmény érdekében
- **GitHub-kompatibilitás**: a GitHub Markdown-bővítményeit valósítja meg a maximális kompatibilitás érdekében
- **Könnyű**: Minimális függőség és kis helyigény
- **Bővíthető**: Támogatja a különböző Markdown-bővítményeket és egyéni beállításokat
- **HTML5 támogatás**: Modern HTML5 kimenetet generál megfelelő szemantikai jelöléssel

## Főbb különbségek a szabványos leértékeléshez képest [major-differences-from-standard-markdown]

### 1. **GitHub ízű leértékelési bővítmények** [1-github-flavored-markdown-extensions]

**Asztalok**

- Teljes támogatás a GitHub-stílusú táblákhoz igazítási lehetőségekkel
- Fejlécek, elválasztók és adatsorok megfelelő HTML-táblaszerkezettel
- Oszlopigazítás kettőspontokkal (`:`) az elválasztó sorokban

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Feladatlisták**

- A GitHub-stílusú jelölőnégyzetek támogatása a listákban
- Interaktív jelölőnégyzetek (HTML beviteli elemként jelennek meg)
- Mind a bejelölt, mind a nem bejelölt állapotok támogatottak

```markdown
- [x] Completed task
- [ ] Pending task
- [x] Another completed task
```

**Áthúzott szöveg**

- A dupla hullámvonalba (`~~`) foglalt szöveg áthúzott lesz
- HTML `<del>` címkéket használ a szemantikai jelöléshez
- Támogatja a több hullámvonalat a kiemelés érdekében

```markdown
~~This text is crossed out~~
~~Mistaken text that should be removed~~
```

### 2. **Továbbfejlesztett kódblokk támogatás** [2-enhanced-code-block-support]

**Kerített kódblokkok**

- Háromszoros backtick (```` ``` ````) kódblokkokhoz
- Nyelvi specifikáció a szintaxis kiemeléséhez
- Nincs szükség behúzásra (a szabványos Markdown-tól eltérően)

```markdown
```javascript
function hello() {
  console.log("Hello, World!");
}
```
```

**Automatic Language Detection**

- Support for many programming languages
- Proper syntax highlighting when supported
- Fallback to plain text for unsupported languages

### 3. **Automatic URL Linking** [3-automatic-url-linking]

**URL Autolinking**

- Automatic conversion of URLs to clickable links
- Support for http, https, and ftp protocols
- Email addresses automatically converted to mailto links

```markdown
Visit http://example.com for more information.
Contact us at user@example.com
```

**Smart Link Detection**

- Felismeri az URL-eket kifejezett jelölés nélkül
- Különféle URL formátumokat és protokollokat kezel
- Konfigurálható link biztonsági opciók

### 4. **Speciális listafunkciók** [4-advanced-list-features]

**Alfabetikus listák**

- Rendezett listák alfabetikus markerekkel (a, b, c stb.)
- Automatikus továbblépés az ábécén keresztül
- Megfelelő HTML `<ol type="a">` kimenet

```markdown
a. First item
b. Second item
c. Third item
```

**Továbbfejlesztett listafeldolgozás**

- A beágyazott listák jobb kezelése
- Javított térköz és behúzás
- Vegyes listatípusok támogatása

### 5. **Lábjegyzetek támogatása** [5-footnotes-support]

**Referencia stílusú lábjegyzetek**

- Automatikus lábjegyzetszámozás
- Hivatkozási hivatkozások `[^1]` szintaxissal
- Lábjegyzet-definíciók a dokumentum végén

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Automatikus lábjegyzet-feldolgozás**

- Megfelelő HTML lábjegyzet szerkezetet hoz létre
- Hivatkozások és definíciók közötti kapcsolatok
- Sorozatszámozás a dokumentumban

### 6. **HTML integráció** [6-html-integration]

**HTML5 támogatás**

- Teljes HTML5 címkefelismerés
- Megfelelő szemantikai jelölés generálása
- Modern HTML struktúra és attribútumok

**Nyers HTML-blokkok**

- HTML támogatása a Markdownon belül
- Megfelelő szökés és fertőtlenítés
- Integráció Markdown szintaxissal

### 7. **További kiemelési szabályok** [7-enhanced-emphasis-rules]

**Nyugodt hangsúly**

- Az aláhúzásjelek (`_`) nem hoznak létre hangsúlyt a szavak közepén
- Jobb a kód és a műszaki tartalom dokumentálására
- Megakadályozza a nem kívánt hangsúlyt az azonosítókban

```markdown
This is a variable_name that won't be emphasized.
This is _emphasized text_ that will be styled.
```

**Több kiemelési szint**

- A félkövér, dőlt és kombinált kiemelés támogatása
- Összhangban a szokásos Markdown hangsúlyszabályokkal
- Megfelelő HTML-kimenet `<strong>` és `<em>` címkékkel

### 8. **Tartalomjegyzék létrehozása** [8-table-of-contents-generation]

**Automatikus TOC**

- Tartalomjegyzéket generál címsorokból
- Címsorszinteken alapuló hierarchikus felépítés
- Konfigurálható TOC generálási lehetőségek

**Címsorazonosító generálása**

- Automatikus azonosító generálás a címsorokhoz
- Horgonylinkek az egyszerű navigáció érdekében
- Következetes azonosító formázás

## Kedvezményes GFM vs egyéb Markdown ízek [discount-gfm-vs-other-markdown-flavors]

| Funkció | Kedvezmény | CommonMark (GFM) | Kramdown | MultiMarkdown | Standard |
| ----------------- | ------------ | ---------- | -------- | ------------- | -------- |
| Táblázatok | Igen | Nem | Igen | Igen | Nem |
| Áthúzott | Igen | Nem | Nem | Igen | Nem |
| Feladatlisták | Igen | Nem | Nem | Igen | Nem |
| Bekerített kód | Igen | Igen | Igen | Igen | Nem |
| Matek | Nem | Nem | Igen | Igen | Nem |
| Lábjegyzetek | Igen | Nem | Igen | Igen | Nem |
| Definíciós listák | Nem | Nem | Igen | Igen | Nem |
| Rövidítések | Nem | Nem | Igen | Nem | Nem |
| Attribútumlisták | Nem | Nem | Igen | Nem | Nem |
| Kiterjesztések | Korlátozott | Nem | Igen | Igen | Nem |
| Tipográfia | Alapvető | Nem | Igen | Nem | Nem |
| Automatikus linkek | Igen | Nem | Nem | Nem | Nem |
| Alfabetikus listák | Igen | Nem | Nem | Nem | Nem |

## A kedvezményes GFM fő előnyei [key-advantages-of-discount-gfm]

1. **GitHub-kompatibilitás**: Tökéletes olyan tartalmakhoz, amelyeknek működniük kell a GitHubon
2. **Teljesítmény**: Gyors C-alapú megvalósítás
3. **Egyszerűség**: A GitHub alapvető funkcióira koncentrálva, bonyolultság nélkül
4. **Megbízhatóság**: Stabil, jól tesztelt megvalósítás
5. **Szabványoknak való megfelelés**: Követi a GitHub Markdown specifikációját
6. **Könnyű**: Minimális erőforrás-felhasználás és függőségek

## Általános használati esetek [common-use-cases]

**GitHub dokumentáció**

- README fájlok és projektdokumentáció
- GitHub oldalak és wikik
- Kérelemleírások kiadása és lekérése

**Technikai írás**

- Kóddokumentáció és oktatóanyagok
- API dokumentáció
- Műszaki adatok

**Tartalomkezelés**

- Blogbejegyzések és cikkek
- Dokumentációs weboldalak
- Tudásbázisok

**Együttműködő szerkesztés**

- Csapat dokumentáció
- Projekttervezési dokumentumok
- Az ülés jegyzetei és jegyzőkönyvei

## Konfigurációs lehetőségek [configuration-options]

A Discount GFM különféle konfigurációs lehetőségeket támogat:

- **Automatikus linkelés**: Automatikus URL-észlelés engedélyezése/letiltása
- **Lábjegyzetek**: A lábjegyzetek feldolgozásának vezérlése
- **Tartalomjegyzék**: TOC generálási beállítások
- **HTML Biztonság**: Linkellenőrzés és -fertőtlenítés
- **Szigorú mód**: Továbbfejlesztett elemzési szabályok
- **Smart Quotes**: Automatikus árajánlat átalakítás

## Megvalósítási részletek [implementation-details]

**Elemző beállításai**

- `kGHMarkdownAutoLink`: Automatikus URL-összekapcsolás engedélyezése
- `kGHMarkdownFootnotes`: Engedélyezze a lábjegyzetek feldolgozását
- `kGHMarkdownTOC`: Tartalomjegyzék generálás engedélyezése
- `kGHMarkdownSafeLinks`: A hivatkozások korlátozása a biztonságos protokollokra
- `kGHMarkdownNoHTMLTags`: A HTML címkefeldolgozás letiltása

**Kimeneti jellemzők**

- HTML5 szemantikai jelölés
- Megfelelő címsor-hierarchia
- Hozzáférhető táblázatszerkezetek
- Tiszta, érvényes HTML kimenet

## Bevált gyakorlatok [best-practices]

1. **Használja takarékosan a táblákat**: A táblák hatékonyak, de karbantartásuk bonyolult lehet
2. **Tőkeáttételi feladatlisták**: Kiválóan alkalmas projektmenedzsmenthez és dokumentációhoz
3. **Automatikus linkek használata**: Hagyja, hogy a processzor automatikusan kezelje az URL-átalakítást
4. **Struktúra címsorokkal**: Használjon megfelelő címsor-hierarchiát a jobb tartalomjegyzék létrehozása érdekében
5. **Teszt a GitHubon**: A GitHub megjelenítésével való kompatibilitás ellenőrzése

## Áttérés a Standard Markdownból [migration-from-standard-markdown]

A legtöbb szabványos Markdown változtatás nélkül működik a Discount GFM-mel. A GFM funkciók kihasználásához:

1. **Táblázatok hozzáadása**: Konvertálja az adatokat GitHub-stílusú táblázatformátumba
2. **Feladatlisták használata**: Cserélje ki a felsorolásjeleket jelölőnégyzetekkel, ahol szükséges
3. **Áthúzás engedélyezése**: Használja a `~~text~~` jelet az áthúzott tartalomhoz
4. **Használja ki az automatikus linkeket**: Távolítsa el a kézi linkjelölést az egyszerű URL-ek esetében
5. **Struktúracímsorok**: Biztosítsa a megfelelő címsor-hierarchiát a tartalomjegyzék generálásához

## Források [resources]

- [GitHub ízesítésű Markdown specifikáció] (https://github.github.com/gfm/)
- [Kedvezményes könyvtári dokumentáció](https://www.pell.portland.or.us/~orc/Code/discount/)
- [GitHub Markdown Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

---

*Ez a dokumentáció a Markedben megvalósított Discount GFM-re vonatkozik. A legfrissebb információkért mindig olvassa el a hivatalos GitHub Flavored Markdown specifikációt.*