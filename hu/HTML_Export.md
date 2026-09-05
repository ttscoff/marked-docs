# <%= @title %>

A Marked a **élő előnézetből** exportál HTML-t --- ugyanabból a megjelenített kimenetből, amit a képernyőn látsz. Akkor használd a HTML-exportot, ha egy blogba vagy CMS-be beilleszthető részletre van szükséged, vagy egy önálló `.html` fájlra beágyazott stílusokkal és képekkel, amelyet bármelyik böngészőben megnyithatsz, vagy bárhol kiszolgálhatsz.

A megszokott munkafolyamat: **először előnézet, aztán HTML-export**: nyisd meg vagy fordítsd le a dokumentumot a Markedben, válassz egy témát, ellenőrizd az élő előnézetben, majd exportálj, amikor a jelölőnyelv megfelelőnek tűnik.

## Kétféleképpen szerezhetsz HTML-t [two-ways-to-get-html]

### HTML másolása (részlet) [copy-html-snippet]

A **HTML másolása** az előnézet HTML-forráskódját a vágólapra helyezi --- készen arra, hogy beilleszd WordPressbe, Ghostba, Squarespace-be, egy fórumba, egy e-mail sablonba, vagy bármely olyan alkalmazásba, amely HTML-részleteket fogad.

* Gear menü → **HTML másolása**, vagy {% kbd shift cmd C %} az előnézetre fókuszálva
* A **megjelenített törzs HTML-t** másolja (nem egy teljes dokumentumot `<html>` csomagolással)
* Opcionális: kapcsold be a **Képek beágyazása HTML másolásakor** funkciót itt: {% prefspane Export %}, hogy a helyi képeket Base64 kódolással `data:` URL-ként ágyazza be a beillesztett forráskódba

A HTML másolása akkor ideális, ha a célhely már rendelkezik saját stíluslappal, és csak a tartalmi jelölőnyelvre van szükséged.

### HTML mentése (fájl) [save-html-file]

A **HTML mentése** egy teljes `.html` fájlt ír a lemezre.

* Export → **HTML mentése**, {% kbd cmd S %}, vagy **HTML** az [Exportálás panelről](Exporting.html#drawer) ({% kbd shift cmd e %})
* Válaszd ki a fájlnevet és a helyet a mentési párbeszédpanelen
* Állítsd be az exportálási beállításokat a párbeszédpanel kiegészítőjében (lásd lent)

A HTML mentése akkor ideális, ha archiválsz, önálló fájlt osztasz meg, vagy közvetlenül böngészőben szeretnéd megnyitni az eredményt.

## HTML mentése beállítások [save-html-options]

A HTML mentése párbeszédpanel tartalmaz egy exportprofil-választót és a következő beállításokat:

![Save HTML options][savehtml]

**Stílus belefoglalása a kimenetbe**

Ha be van jelölve, a Marked beágyazza a kiválasztott előnézeti téma CSS-ét egy `<style>` blokkba az exportált fájlon belül. Válassz bármelyik beépített témát vagy [Egyéni stílust](Custom_Styles.html) a jelölőnégyzet melletti stílusmenüből. A kimenet egy teljes HTML-dokumentum `<!DOCTYPE html>`, `<head>` és a tartalmadat körülvevő `#wrapper` div elemmel --- pontosan úgy, ahogy az előnézetben láttad.

Ha nincs bejelölve, a Marked egy minimális HTML-dokumentumot ment, csak a megjelenített tartalommal (Marked-témájú CSS nélkül). Ezt akkor használd, ha nyers HTML-re van szükséged, amelyet beilleszthetsz vagy importálhatsz egy másik rendszerbe, amely saját stílust biztosít.

**Helyi képek beágyazása önálló HTML-hez**

Ha a **Stílus belefoglalása a kimenetbe** be van kapcsolva, a helyi képeket is beágyazhatod Base64-es `data:` URL-ként a HTML-fájlba. Az eredmény egyetlen fájl lesz, amelyet e-mailben elküldhetsz, feltölthetsz vagy kiszolgálhatsz külön `images/` mappa nélkül.

* Működik a helyi meghajtón **relatív vagy abszolút elérési úttal** hivatkozott képekkel
* Kerüld a `file:///` URL-eket --- ezek nem ágyazhatók be megbízhatóan
* A távoli (http/https) képek külső URL-ként maradnak, hacsak nem töltöd le őket előbb
* A Base64-es beágyazás nagy fájlokat eredményezhet; akkor használd, ha a hordozhatóság fontosabb a fájlméretnél

**Szintaxiskiemelő JavaScript belefoglalása**

Ha a szintaxiskiemelés be van kapcsolva itt: {% prefspane Preview %}, ez a beállítás hozzáadja a highlight.js CSS-t és JavaScriptet egy CDN-ről, hogy a kódblokkok megtartsák a színeiket az exportált fájlban. Az exportált HTML-nek internetkapcsolatra van szüksége a CDN-erőforrások betöltéséhez.

**MathJax vagy KaTeX CDN-hivatkozás belefoglalása**

Ha a [MathJax](MathJax.html) vagy a KaTeX be van kapcsolva az előnézethez, a mentett HTML-be belefoglalhatod a megfelelő CDN-szkripteket, hogy a képletek megjelenjenek egy böngészőben. A szintaxiskiemeléshez hasonlóan ehhez is hálózati hozzáférés szükséges a fájl megtekintésekor, hacsak nem magad üzemelteted a szkripteket.

**CriticMarkup exporttípus**

A [CriticMarkup](CriticMarkup.html)-ot tartalmazó dokumentumoknál kiválasztható, hogy az export a szerkesztett szöveget, az eredeti szöveget vagy a teljes jelölést mutassa.

**Exportprofil**

Válassz egy mentett [Exportprofilt](Exporting.html#export-profiles), hogy egy lépésben visszaállítsd a preferált HTML-exportbeállításokat (beágyazott stílusok, képek, szintaxiskiemelés, matematika).

## Stílusozás beépített és egyéni témákkal [styling-with-built-in-and-custom-themes]

Az **előnézeti stílus** vezérli a HTML megjelenését, amikor a **Stílus belefoglalása a kimenetbe** be van jelölve:

1. Válassz egy stílust az előnézeti ablak stílusmenüjéből (vagy állíts be egy alapértelmezettet itt: {% prefspane Style %}).
2. Ellenőrizd a tipográfiát, a címsorokat, a kódblokkokat és a képeket az élő előnézetben.
3. Mentsd a HTML-t ugyanazzal a stílussal, amelyet az exportpárbeszédpanelen kiválasztottál.

Minden beépített Marked-téma --- a Swiss, a GitHub, a Manuscript és a többi --- beágyazható. Az [Egyéni stílusok](Custom_Styles.html) és a [Stíluskezelőből](Custom_Styles.html) származó stílusok ugyanígy működnek.

A {% prefspane Style %} **kiegészítő CSS** szerepel a HTML-exportban, ha a stílusok be vannak ágyazva. Az exportált `<body>` megkapja a `mk-has-additional-css` osztályt, hogy a Marked átírt kiegészítő CSS-szelektorai illeszkedjenek. Lásd: [Egyéni CSS létrehozása](Writing_Custom_CSS.html#additional-css-settings).

I> Egyes csak előnézetre vonatkozó CSS-ek (fix pozicionálás, viewport-trükkök, Sötét mód `@media screen` invertálás) a Markeden kívül esetleg nem ültethetők át egy az egyben. Nyisd meg a mentett fájlt egy böngészőben, hogy ellenőrizd, mielőtt közzéteszed.

Szerkesztési útmutatásért lásd: [Egyéni CSS létrehozása](Writing_Custom_CSS.html).

## Metaadatok és MultiMarkdown fejlécek [metadata-and-multimarkdown-headers]

A forrásfájlod tetején lévő MultiMarkdown metaadatok befolyásolhatják a HTML-exportot:

* **`Title:`** --- a `<title>` elemhez használt, amikor egy teljes HTML-dokumentumot mentesz
* **`XHTML Header:`** / **`HTML Header:`** --- további címkéket illeszt az exportált `<head>`-ba (szkriptek, link címkék, meta címkék)
* A többi metaadatkulcsot a [Markdown-feldolgozód](Choosing_a_Processor.html) szerint dolgozza fel a program

Ha metaadatokat használsz exportbeállításokhoz, de nem szeretnéd, hogy a kulcsok láthatók legyenek más kimenetekben, csomagold őket HTML-megjegyzésekbe --- a Marked bárhol megtalálja és feldolgozza a megjegyzésbe rejtett metaadatokat a dokumentumban. Lásd: [Dokumentumonkénti beállítások](Per-Document_Settings.html).

## Több fájlból álló dokumentumok [multi-file-documents]

Könyvekhez és fejezetgyűjteményekhez használd a [Több fájlból álló dokumentumokat](Multi-File_Documents.html). A Marked az egyesített dokumentumot jeleníti meg előnézetben, és egyetlen HTML-fájlt exportál az összeállított eredményből. A beillesztett fájlokat HTML-megjegyzések jelzik, amelyek megmutatják a forrás elérési útját --- hasznos, ha ellenőrizni akarod, melyik fejezet melyik részhez adott hozzá tartalmat.

## Beillesztés más alkalmazásokba [pasting-into-other-applications]

| Célhely | Javasolt megközelítés |
| :-- | :-- |
| Blog / CMS saját témával | **HTML másolása** (részlet, beágyazott Marked CSS nélkül) |
| Statikus webhely vagy archívum | **HTML mentése** a **Stílus belefoglalása a kimenetbe** beállítással |
| E-mail vagy fájlmegosztás (egy melléklet) | **HTML mentése** a **Helyi képek beágyazása** beállítással |
| WordPress, Ghost, Notion stb. | **HTML másolása**; kapcsold be a **Képek beágyazása HTML másolásakor** funkciót, ha a szerkesztő nem oldja fel a helyi elérési utakat |
| További szerkesztés kódszerkesztőben | **HTML mentése** beágyazott stílus nélkül, vagy másold a részletet és csomagold be kézzel |

A [Formázott szöveg másolása](Exporting.html#rtfexportoptions) (gear menü) egy alternatíva, ha a célalkalmazás formázott szöveget fogad HTML-forrás helyett.

## Kapcsolódó témák [related-topics]

* [Exportálás](Exporting.html) --- exportpanel, profilok és egyéb formátumok
* [EPUB-export](EPUB_Export.html) --- e-könyv kimenet beágyazott CSS-sel
* [Élő Markdown-előnézet Macen](Live_Markdown_Preview_on_Mac.html) --- előnézeti munkafolyamat exportálás előtt
* [Egyéni stílusok](Custom_Styles.html) és [Beállítások: Export](Settings_Export.html)
* [HTML-specifikus beállítások](HTML_Specific_Settings.html) --- feldolgozási beállítások HTML-kimenethez
* [AppleScript-export](AppleScript_Support.html) --- HTML másolás és mentés automatizálása

[savehtml]: images/SaveHTML.png @2x width=740px height=229px
