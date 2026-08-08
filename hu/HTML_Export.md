<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A megjelölt HTML-t exportál az **élő előnézetből** --- ugyanaz a renderelt kimenet, amelyet a képernyőn lát. Használja a HTML-exportálást, ha egy részletet szeretne beilleszteni egy blogba vagy CMS-be, vagy egy önálló `.html` fájlra van szüksége beágyazott stílusokkal és képekkel, amelyeket bármely böngészőben vagy gazdagépen bárhol megnyithat.

A tipikus munkafolyamat az **előzetes előnézet, a második a HTML-exportálás**: nyissa meg vagy fordítsa le a dokumentumot a Marked alkalmazásban, válasszon témát, lektorálja az élő előnézetben, majd exportálja, amikor a jelölés megfelelőnek tűnik.

## A HTML beszerzésének két módja [two-ways-to-get-html]

### HTML (kódrészlet) másolása [copy-html-snippet]

**A HTML másolása** az előnézet HTML-forrását a vágólapra helyezi -- készen áll arra, hogy beillessze a WordPressbe, a Ghostba, a Squarespace-be, egy fórumba, egy e-mail-sablonba vagy bármely olyan alkalmazásba, amely elfogadja a HTML-töredékeket.

* Fogaskerék menü → **HTML másolás**, vagy {% kbd shift cmd C %} az előnézetre fókuszálva
* Másolja a **megjelenített törzs-HTML-t** (nem teljes dokumentum `<html>` burkolóval)
* Nem kötelező: engedélyezze a **Képek beágyazása HTML másolásakor** az {% prefspane Export %}-be, hogy Base64-kódolású helyi képeket `data:` URL-ként a beillesztett forrásban

A HTML másolása akkor ideális, ha a célhelynek már van saját stíluslapja, és csak a tartalomjelölésre van szüksége.

### HTML mentése (fájl) [save-html-file]

A **Save HTML** egy teljes `.html` fájlt ír a lemezre.

* Exportálás → **HTML mentése**, {% kbd cmd S %} vagy **HTML** az [Exportálási panelről](Exporting.html#drawer) ({% kbd shift cmd e %})
* Válassza ki a fájlnevet és a helyet a mentési párbeszédpanelen
* Konfigurálja az exportálási beállításokat a párbeszédablakban (lásd alább)

A HTML mentése ideális archiválásához, önálló fájlok megosztásához vagy az eredmény közvetlen böngészőben való megnyitásához.

## HTML beállítások mentése [save-html-options]

A HTML mentése párbeszédpanel exportálási profilválasztót és a következő beállításokat tartalmaz:

![Save HTML options][savehtml]

**Stílus szerepeltetése a kimenetben**

Ha be van jelölve, a Megjelölve beágyazza a kiválasztott előnézeti téma CSS-jét egy `<style>` blokkba az exportált fájlban. A jelölőnégyzet melletti stílusmenüből válasszon bármilyen beépített témát vagy [Custom Style](Custom_Styles.html)-t. A kimenet egy teljes HTML-dokumentum, `<!DOCTYPE html>`, `<head>` és egy `#wrapper` div karakterrel a tartalom körül --- megfelel az előnézeti képnek.

Ha nincs bejelölve, a Marked egy minimális HTML-dokumentumot ment el, amely csak a megjelenített tartalmat tartalmazza (nincs megjelölt téma CSS). Ezt akkor használja, ha a nyers HTML-t be szeretné illeszteni vagy importálni egy másik rendszerbe, amely saját stílust biztosít.

**Helyi képek beágyazása az önálló HTML-hez**

Ha a **Stílus szerepeltetése a kimenetben** engedélyezve van, a helyi képeket Base64 `data:` URL-ként is beágyazhatja a HTML-fájlba. Az eredmény egy olyan fájl, amelyet e-mailben elküldhet, feltölthet vagy tárolhat külön `images/` mappa nélkül.

* A helyi meghajtón található **relatív vagy abszolút elérési utak** által hivatkozott képekkel működik
* Kerülje a `file:///` URL-eket --- ezeket nem lehet megbízhatóan beágyazni
* A távoli képek (http/https) külső URL-ként maradnak, kivéve, ha először letölti őket
* A Base64 beágyazás nagy fájlokat tud előállítani; akkor használja, ha a hordozhatóság fontosabb, mint a fájlméret

**Include Syntax Highlighting JavaScript**

Ha a szintaktikai kiemelés engedélyezve van a {% prefspane Preview %}-ben, ez a beállítás hozzáadja a highlight.js CSS-t és a JavaScriptet a CDN-ből, így a kódblokkok megtartják színeiket az exportált fájlban. Az exportált HTML-nek internetkapcsolatra van szüksége a CDN-erőforrások betöltéséhez.

** Tartalmazza a MathJax vagy a KaTeX CDN linket**

Ha a [MathJax](MathJax.html) vagy a KaTeX engedélyezve van az előnézethez, akkor a megfelelő CDN-szkripteket belefoglalhatja a mentett HTML-kódba, hogy az egyenletek megjelenjenek a böngészőben. A szintaktikai kiemeléshez hasonlóan ehhez hálózati hozzáférésre van szükség a fájl megtekintésekor, hacsak nem saját maga tárolja a szkripteket.

**CriticMarkup exportálási típusa**

A [CriticMarkup](CriticMarkup.html)-kal rendelkező dokumentumok kiválaszthatják, hogy az exportálás szerkesztett szöveget, eredeti szöveget vagy teljes jelölést jelenítsen-e meg.

**Profil exportálása**

Válasszon ki egy mentett [Exportálási profilt](Exporting.html#export-profiles) a preferált HTML-exportálási beállítások (beágyazott stílusok, képek, szintaxiskiemelés, matematika) egy lépésben történő visszaállításához.

## Stílus kialakítása beépített és egyedi témákkal [styling-with-built-in-and-custom-themes]

Az **előnézeti stílus** elősegíti a HTML megjelenését, ha a **Stílus szerepeltetése a kimenetben** be van jelölve:

1. Válasszon egy stílust az előnézeti ablak stílusmenüjéből (vagy állítsa be az alapértelmezettet az {% prefspane Style %} alatt).
2. Tekintse át a tipográfiát, a címsorokat, a kódblokkokat és a képeket az élő előnézetben.
3. Mentse el a HTML-t az exportálási párbeszédpanelen kiválasztott stílussal.

Minden beépített Marked téma --- Swiss, GitHub, Manuscript és a többi --- beágyazható. Az [Egyéni stílusok](Custom_Styles.html) és a [Stíluskezelő](Custom_Styles.html) stílusok ugyanúgy működnek.

I> Előfordulhat, hogy egyes csak előnézeti CSS-ek (rögzített pozicionálás, nézetablak-trükkök, Sötét mód `@media screen` inverzió) nem fordítják le egy az egybe a Megjelölve kívül. Nyissa meg a mentett fájlt egy böngészőben, hogy ellenőrizze a közzététel előtt.

A szerzői útmutatásért lásd: [Egyéni CSS létrehozása](Writing_Custom_CSS.html).

## Metaadatok és MultiMarkdown fejlécek [metadata-and-multimarkdown-headers]

A forrásfájl tetején található MultiMarkdown metaadatok befolyásolhatják a HTML-exportálást:

* **`Title:`** --- a `<title>` elemhez használatos teljes HTML dokumentum mentésekor
* **`XHTML Header:`** / **`HTML Header:`** --- további címkéket szúr be az exportált `<head>`-be (szkriptek, linkcímkék, metacímkék)
* A többi metaadatkulcs feldolgozása a [Markdown processzor] szerint történik(Choosing_a_Processor.html)

Ha metaadatokat használ az exportálási beállításokhoz, de nem szeretné, hogy a kulcsok megjelenjenek más kimenetekben, csomagolja be őket HTML-megjegyzésekbe --- A Marked megkeresi és feldolgozza a megjegyzésekkel ellátott metaadatokat a dokumentumban bárhol. Lásd: [Dokumentumonkénti beállítások](Per-Document_Settings.html).

## Több fájlból álló dokumentumok [multi-file-documents]

Könyvekhez és fejezet-összeállításokhoz használja a [Többfájlos dokumentumok](Multi-File_Documents.html) lehetőséget. A Marked megtekinti az egyesített dokumentum előnézetét, és exportál egy HTML-fájlt a lefordított eredményből. A mellékelt fájlok HTML-megjegyzésekkel vannak megjelölve, amelyek a forrás elérési útját mutatják --- hasznosak lehetnek annak ellenőrzéséhez, hogy melyik fejezet melyik szakaszhoz járult hozzá.

## Beillesztés más alkalmazásokba [pasting-into-other-applications]

| Úticél | Javasolt megközelítés |
| :-- | :-- |
| Blog / CMS saját témával | **HTML másolás** (részlet, nincs beágyazott megjelölt CSS) |
| Statikus webhely vagy archívum | **Mentsd el a HTML-t** a **Stílus szerepeltetésével a kimenetben** |
| E-mail vagy fájlmegosztás (egy melléklet) | **HTML mentése** a **helyi képek beágyazásával** |
| WordPress, Ghost, Notion stb. | **HTML másolás**; engedélyezze a **Képek beágyazását HTML másolásakor**, ha a szerkesztő nem oldja fel a helyi elérési utakat |
| További szerkesztés kódszerkesztőben | **Mentse el a HTML-t** beágyazott stílus nélkül, vagy másolja ki a kódrészletet és csomagolja be kézzel |

A [Copy Rich Text](Exporting.html#rtfexportoptions) (fogaskerék menü) egy alternatíva, amikor a célalkalmazás formázott szöveget fogad el HTML-forrás helyett.

## Kapcsolódó témák [related-topics]

* [Exportálás](Exporting.html) --- panel, profilok és egyéb formátumok exportálása
* [EPUB Export](EPUB_Export.html) --- ebook kimenet beágyazott CSS-sel
* [Élő Markdown előnézet Macen](Live_Markdown_Preview_on_Mac.html) --- a munkafolyamat előnézete az exportálás előtt
* [Egyéni stílusok](Custom_Styles.html) és [Beállítások: Exportálás](Settings_Export.html)
* [HTML-specifikus beállítások](HTML_Specific_Settings.html) --- processzorbeállítások a HTML-kimenethez
* [AppleScript export](AppleScript_Support.html) --- automatizálja a HTML-másolást és mentést

[savehtml]: images/SaveHTML.png @2x width=740px height=229px 
r