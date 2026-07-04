<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A megjelölt közvetlenül megnyithatja a PDF dokumentumokat (`.pdf`). Húzzon egy fájlt a Megjelölt elemre, vagy használja a {% appmenu File, Open... ({{cmd}}O) %} gombot. A dokumentumot Markdown formátumba konvertálja az előnézet és az exportálás céljából.

A PDF-importálás a **kisebb, szöveges PDF-ek** (diák, cikkek, rövid jelentések) esetén működik a legjobban. A nagyméretű kézikönyvek, könyvek és beolvasott dokumentumok támogatottak, de gyakran lassan vagy tökéletlenül konvertálhatók – lásd alább a **Korlátozások** részt.

A Marked továbbra is egy **előnézeti** eszköz: nem szerkesztheti a PDF-et a Markedben. Használja az {% kbd cmd E %} gombot a PDF megnyitásához az **Előnézetben** (vagy a rendszer alapértelmezett beállításában), és a Megjelölve frissíti, ha a fájl megváltozik a lemezen.

## Hogyan működik az átalakítás

A PDF-importálás a [pdf22md](https://github.com/twardoch/pdf22md) könyvtárat használja (MIT-licenc; lásd: [pdf22md licenc](PDF22MD_License.html)). A Marked a háttérben futtatja a konverziót, miközben egy rövid **Konvertálás** értesítést jelenít meg.

Az átalakító:

- Kivonat **szöveg** digitális PDF-ekből a PDFKit segítségével
- **Vision OCR** használata azokon az oldalakon, ahol hiányzik a beágyazott szöveg (gyakori a beolvasásoknál)
- Ha lehetséges, a betűméret alapján észleli a **címsorokat**
- A **képeket** egy `assets` mappába menti a generált Markdown mellett

A megjelölve **nem** teszi lehetővé a pdf22md opcionális mesterséges intelligencia-tisztítását az alkalmazásban. A konvertálás minősége a PDF létrehozásának módjától függ.

## Gyorsítótár és élő előnézet

Az átalakított Markdown és a képek a Marked's Watchers gyorsítótárban (`~/Library/Caches/Marked/Watchers/PDF/`) tárolódnak. Az eredeti PDF elérési út marad a dokumentum forrása a fájlmegtekintéshez.

Amikor menti vagy lecseréli a PDF-fájlt egy másik alkalmazásban, a Marked észleli a változást, és automatikusan újrakonvertálja (ugyanaz az egyesített újratöltési viselkedés, mint az [RTF](RTF_Support.html) és a [Scrivener](Scrivener_Support.html)).

## Exportálás és egyéb funkciók

Az átalakítás után a Marked a dokumentumot más lefordított forrásokhoz hasonlóan kezeli: az exportálás, a statisztika és a legtöbb előnézeti funkció a generált Markdown ellen fut. Képútvonalak az előnézeti pontban a gyorsítótárazott eszközöknél az exportálásig.

## Korlátozások

Állítsa be elvárásait ennek megfelelően – a PDF-to-Markdown hasznos, nem tökéletes.

**Ami jól működik**

- **Vektor- és szövegalapú PDF-ek** valódi beágyazott szöveggel (Wordból, Pagesből, InDesignból stb. exportálva)
- **Közepes terjedelmű** – általában néhány tucat oldal ésszerű időn belül konvertálódik, jó szerkezettel

**Mi a megbízhatatlan**

- **OCR (beolvasott PDF-ek)** – A látás kitölti a hiányzó szöveget, de a pontosság gyakran gyenge egy dedikált OCR-eszközhöz képest; gépelési hibákra, törött szavakra és kihagyott oszlopokra számíthat
- **Táblázatok** — az elrendezést a szöveg pozíciói alapján lehet kitalálni; Az egyesített cellák, egymásba ágyazott táblák és összetett rácsok ritkán maradnak fenn tiszta Markdown táblákként
- **Képelhelyezés** – az ábrák `assets/`-ig kerülnek kibontásra, de az igazítás, a feliratok és a szövegkörnyékezés nem őrzi meg megbízhatóan a képeket

**Méret és teljesítmény**

- **A nagyméretű PDF-fájlok** (felhasználói útmutatók, tankönyvek, hosszú kézikönyvek) **nagyon hosszú ideig** konvertálhatók, jelentős memóriát igényelhetnek, vagy nem hoznak létre hasznos leértékelést. A megjelölt érzékeny marad, amíg a konverzió a háttérben fut, de nincs garancia arra, hogy az 500 oldalas kézikönyv sikeresen befejeződik
- Ha a konverzió kevés tartalommal vagy tartalom nélkül fejeződik be, a Megjelölt hibaüzenetet jelenít meg, ahelyett, hogy üres előnézetet hagyna

**Egyéb korlátozások**

- A **Jelszóval védett PDF-fájlok** nem támogatottak a v1-ben
- **A beágyazott PDF-képek a Markdown-ban** (`![]()`, amely `.pdf` fájlra hivatkozik) nem kapcsolódnak a PDF-importáláshoz – csak a `.pdf` megnyitása váltja ki a konverziót, mivel a fő dokumentum

Word-dokumentumokhoz használja a [DOCX-kezelés](Working_with_DOCX.html) parancsot. Rich Text esetén használja az [RTF- és RTFD-támogatás](RTF_Support.html)-t.

## Kapcsolódó témák

- [Fájlok megnyitása](Opening_Files.html) – fogd és vidd, Legutóbbi megnyitása, vágólap
- [Exportálás](Exporting.html) – HTML, PDF, DOCX és Markdown mentése az előnézetből
- [pdf22md licenc](PDF22MD_License.html) – harmadik féltől származó MIT licenc szövege