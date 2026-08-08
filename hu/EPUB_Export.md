<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked teljesen kompatibilis EPUB-fájlokat exportál a Markdown előnézetéből --- ugyanazokkal a beépített és egyéni témákkal díszítve, mint a képernyőn, és olvasható az **Apple Books**, **Kobo** és más szabványos EPUB-olvasókban.

A tipikus munkafolyamat az **előzetes előnézet, majd az EPUB exportálása**: nyissa meg vagy fordítsa le a dokumentumot a Marked alkalmazásban, válasszon témát, lektorálja az élő előnézetben, majd exportálja, amikor a könyv készen áll.

## EPUB exportálása [exporting-an-epub]

Nyissa meg az [Exportálási panelt](Exporting.html#drawer) ({% kbd shift cmd e %}), vagy használja a **Mentés másként** lehetőséget a fogaskerék menüben, és válassza az **EPUB** lehetőséget.

Az EPUB mentési párbeszédpanelen a következőket állíthatja be:

* **Cím** --- alapértelmezés szerint a MultiMarkdown metaadatok vagy a fájlnév
* **Szerző** --- az alapértelmezett macOS-felhasználónév; az utoljára megadott szerzőt a rendszer megjegyzi a következő exportnál
* **Dátum** --- ISO formátum; időmegtakarítással szerkeszthető
* **Borítókép** --- opcionális PNG vagy JPG; A Megjelölt alapértelmezett borító előnézetet generál, ha nincs beállítva

A Marked helyi képeket ágyaz be az EPUB-ba, és távoli képeket tölthet le, így a kész fájl önálló. Az exportált EPUB-fájlokat a rendszer jól formázott XHTML-ként érvényesíti a mentés előtt, és olyan fájlokat állít elő, amelyek megfelelnek az EPUB-szabványoknak a terjesztés és a hozzáférhetőség tekintetében.

Lásd: [Profilok exportálása](Exporting.html#export-profiles) az EPUB metaadatok mentéséhez és a beállítások exportálásához az ismételt felhasználáshoz.

## Stílus kialakítása beépített témákkal [styling-with-built-in-themes]

A dokumentummeghajtók EPUB megjelenéséhez kiválasztott **előnézeti stílus**. Minden beépített Marked téma --- Swiss, GitHub, Manuscript és a többi --- alkalmazható EPUB-exportálásra.

1. Válasszon egy stílust az Előnézet ablak stílus menüjéből (vagy állítsa be az alapértelmezettet az {% prefspane Style %} pontban).
2. Tekintse át a tipográfiát, a címsorokat, a kódblokkokat és a képeket az élő előnézetben.
3. Exportálás EPUB-ba --- A Marked a téma CSS-jét az EPUB-csomagba köti.

A Marked az export-specifikus CSS-t is alkalmazza az előnézeti téma tetején, így az olyan elemek, mint a lábjegyzetek, táblázatok és a szintaxis által kiemelt kódblokkok megfelelően jelennek meg az e-olvasókban. A vázlatmódú dokumentumok vázlatra optimalizált exportstílusokat használnak; [Leanpub](Multi-File_Documents.html) `Book.txt` indexek automatikusan Leanpub-orientált exportstílust használnak.

I> Az EPUB-olvasók figyelmen kívül hagynak néhány csak webes CSS-t (rögzített pozicionálás, nézetablakos trükkök stb.). A Marked előnézetében látható a cél, de az e-olvasó elrendezési motorjai leegyszerűsíthetik a térközt és a betűtípusokat. Közzététel előtt tesztelje az Apple Booksban vagy a célolvasóban.

## Stílus kialakítása egyéni témákkal [styling-with-custom-themes]

Az [Egyéni stílusok](Custom_Styles.html) ugyanúgy működnek az EPUB esetében, mint az előnézetnél és a PDF-nél:

* Adjon hozzá CSS-fájlokat a {% prefspane Style %} vagy a [Style Manager](Custom_Styles.html) alatt.
* Exportálás előtt válassza ki az egyéni témát.
* A Megjelölve beágyazza a stíluslapot az exportált EPUB-fájlba.

Tippek az EPUB-barát egyéni CSS-hez:

* Legyen gördülékeny az elrendezés --- használjon relatív mértékegységeket és `max-width: 100%`-t a képeken (a `#wrapper img { max-width: 100%; }` jó kiindulópont).
* Kerülje a `@media print` szabályokat az e-könyvek stílusához; Az EPUB a fő képernyőstílusokat, valamint a Marked exportálási stíluslapját használja.
* [Sötét mód](Previewing.html) inverzió az előnézetben `@media screen` lekérdezéseket használ; a legtöbb EPUB-olvasó a világos stíluslapot használja, hacsak az olvasóalkalmazás nem alkalmaz saját sötét témát.
* A Stílusbeállítások [További CSS](Custom_Styles.html) használatával az összes témát egyszerre módosíthatja (például egységes törzsbetűméret az exportálás során).

A szerzői útmutatásért lásd: [Egyéni CSS létrehozása](Writing_Custom_CSS.html).

## Szintaxis kiemelés és matematika [syntax-highlighting-and-math]

Ha a **A szintaktikai kiemelés szerepeltetése az exportálásban** engedélyezve van a {% prefspane Export %}-ban, akkor a kódblokkoló exportálás az előnézettel megegyező szintaktikai színekkel történik. A [MathJax](MathJax.html) segítségével előállított matematikai adatok az e-olvasók támogatásának megfelelően szerepelnek az EPUB-ban.

## Metaadatok a forrásfájlban [metadata-in-your-source-file]

A mentési párbeszédpanel helyett beállíthatja az EPUB metaadatokat a dokumentumban. A Markdown-fájl tetején (vagy a Scrivener metaadat-oldalán) használjon MultiMarkdown-stílusú billentyűket:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

`cover image` a dokumentumhoz viszonyított elérési utat vagy abszolút elérési utat fogad el. A PNG és a JPG támogatott. A párbeszédpanel-értékek felülírják vagy kitöltik a hiányzó metaadatokat az exportáláskor.

## Több fájlból álló könyvek [multi-file-books]

Hosszabb munkák esetén fordítson fejezeteket [Multi-File Documents](Multi-File_Documents.html) --- indexfájlokkal, Scrivener-exportálással, Leanpub `Book.txt` vagy GitBook-stílusú indexekkel. A megjelölt figyeli a mellékelt fájlokat, megtekinti a teljes könyv előnézetét, és exportál egy EPUB-fájlt az összeállított HTML-ből.

Az összeállított dokumentum címsorai EPUB [tartalomjegyzék](Document_Navigation.html) néven alakulnak az Apple Books és más olvasók navigációjához.

## Olvasás és publikálás [reading-and-publishing]

Az exportált EPUB-fájlok közvetlenül az **Apple Books** alkalmazásban nyílnak meg (kattintson duplán a fájlra, vagy használja a **Fájl → Hozzáadás a könyvtárhoz** lehetőséget). A Kobo, Thorium, Calibre és a legtöbb EPUB 3-kompatibilis alkalmazásban is működnek.

### Apple Books [apple-books]

Húzzon egy exportált `.epub`-t a Könyvek alkalmazásba, vagy adja hozzá a **Fájl → Importálás** menüpontban. Egyéni tipográfia és borítóképek a Megjelölt témában keresztülvihetők. Használja az Apple Books alkalmazást Macen, iPaden vagy iPhone-on az elrendezés ellenőrzéséhez a megosztás előtt.

### Kindle Direct Publishing (KDP) [kindle-direct-publishing-kdp]

Az EPUB a [Kindle Direct Publishing] (https://kdp.amazon.com/) által elfogadott feltöltési formátum. Exportáljon a Marked alkalmazásból, és töltse fel a `.epub` fájlt; Az Amazon átalakítja Kindle szállításra. A KDP a [DOCX](Working_With_DOCX.html)-t is elfogadja. Az aktuális követelményekért tekintse meg az Amazon [támogatott e-könyv-formátumait] (https://kdp.amazon.com/en_US/help/topic/G200634390).

**MOBI nem szükséges** új KDP-címeknél. A megjelölt nem exportál MOBI-t.

Választható: a feltöltés előtt tekintse meg a Kindle elrendezés előnézetét az Amazon ingyenes [Kindle Previewerével] (https://kdp.amazon.com/help/topic/G202131170).

## Kapcsolódó [related]

* [HTML Export](HTML_Export.html) --- önálló HTML beágyazott stílusokkal és képekkel
* [Exportálás](Exporting.html) --- panel, profilok és egyéb formátumok exportálása
* [Élő Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) --- a munkafolyamat előnézete az exportálás előtt
* [Egyéni stílusok](Custom_Styles.html) és [Egyéni stílusgenerátor](Custom_Style_Generator.html)
* [Többfájlos dokumentumok](Multi-File_Documents.html) --- könyvek és fejezetek indexei
* [AppleScript export](AppleScript_Support.html) --- EPUB exportálás automatizálása