<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked URL-kezelője további szkriptelési és munkafolyamat-képességeket biztosít. Felvehet egy URL-t egy másik alkalmazás jegyzeteibe, például, amely kattintásra megnyit egy fájlt a Megjelölt mappában. Több műveletet is végrehajthat az alábbiak szerint.

## Az URL-séma [the-url-scheme]

A Marked URL-sémája `x-marked`, olyan opciókkal hívható meg, mint a `x-marked://open?file=/Users/username/Desktop/report.md`.

Kifejezetten megcélozhatja a Marked 3-at a `x-marked-3` használatával a `x-marked` helyett. A metódusok és paraméterek pontosan megegyeznek az `x-marked` paraméterrel, de csak a Marked 3 válaszol a `x-marked-3`-re.

## Hívás a parancssorból/szkriptekből [calling-from-the-command-linescripts]

Az URL-kezelő parancssorból vagy szkriptből hívható a macOS [`open` parancs](http://brettterpstra.com/2014/08/06/shell-tricks-the-os-x-open-command/) segítségével:

	nyissa meg az "x-marked://open?file=filename.md" fájlt
	nyissa meg az "x-marked://refresh?file=filename.md" fájlt

### Hívás a háttérben [calling-in-the-background]

Meghívhatja a `open` parancsot a `-g` jelzővel, hogy az eredményt a háttérben, fókuszváltás nélkül hajtsa végre. A parancs végrehajtása a háttérben, és az ablak felemelése a fókusz ellopása nélkül:

	open -g 'x-marked://open?file=filename.md&raise=true'

## Választható paraméterek [optional-parameters]

### x-siker [x-success]

Bármely parancs megadhat egy **x-success** lekérdezési paramétert. Állítsa be a parancs végrehajtása után meghívandó URL-t. Például: `x-marked://open/?file=filename.md&x-success=ithoughts:`. Megadhat egy csomagazonosítót is (például `com.googlecode.iterm`) olyan alkalmazás megnyitásához, amely nem rendelkezik URL-sémával.

### emelni [raise]

A **emelés** paraméter bármely paranccsal átadható, amely elfogad egy `file` paramétert, vagy minden ablakra hatással van. A művelet végrehajtása után az érintett ablak(ok) az összes többi ablak (minden alkalmazás) fölé emelkednek, mielőtt visszatérnek vagy visszahívást hajtanak végre.

	"x-marked://refresh?file=filename.md&raise=true"

### gyorsolvasás [speedread]

A **speedread** paraméter átadható URL-kezelő parancsokkal, amelyek megnyitják az előnézeti dokumentumot (`open`, `paste`, `preview` és `stream`). Állítsa be a `speedread=1` beállítást, hogy a Speed ​​Read automatikusan elinduljon, amint a cél előnézet készen áll.

Példák:

	x-marked://open?file=/Users/username/Desktop/report.md&speedread=1

	x-marked://preview?text=Some%20text&speedread=1

	x-marked://paste?speedread=1

# Elérhető parancsok [available-commands]

A következő parancsok érhetők el a `x-marked` URL-kezelő számára.

## addstyle [addstyle]

Adjon hozzá új egyéni stílust a Megjelölthez.

##### Paraméterek: [parameters]

**css**: URL-kódolású CSS-szöveg egyéni stílusba írható. Kötelező, hacsak nem adunk át egy **file** paramétert.

**fájl**: A CSS-fájl teljes elérési útja (POSIX), amelyet a Marked-hez kell hozzáadni. Kötelező, hacsak nem adunk át egy **css** paramétert.

**név**: A létrehozandó stílus neve.

A **css** paraméterrel ez mind a fájlnév, mind a menüelem neve lesz a lemezre írásakor, a ".css" hozzáadásával. Kötelező a **css** paraméterhez, és nem kötelező a **file** esetén (a fájlnév úgy lesz használva, mintha a név paraméter üres lenne).

	x-marked://addstyle?name=Saját+új+stílus&css=...

	x-marked://addstyle?file=/Users/myuser/Custom+Styles/Unicorn.css

Ha nevet ad meg a fájl paraméterben, akkor a menüelem ezt a nevet kapja a fájlnév helyett. Ha ugyanazt a nevet használja újra egy másik elérési úttal, akkor a menüelem az új elérési úttal frissül, ahelyett, hogy hozzáadna egy másik, azonos nevű elemet.

## alapértelmezett [defaults]

Felhasználói beállítások megadása. Elfogadja a kulcsok és értékek listáját lekérdezési paraméterként. Csak a meglévő kulcsok lesznek beállítva. Ha a beállítás módosítása frissítést igényel, az összes ablak automatikusan frissül, kivéve, ha a `refresh=0` áthalad.

Logikai értékek esetén használjon 1-et igaz, 0-t hamishoz.

##### Paraméterek: [parameters-2]

**frissítés** _(opcionális)_: ha 0-ra van állítva, a megnyitott előnézeti ablakok automatikus frissítése le van tiltva

* Alapértelmezett: 1 (igaz)

##### Példa: [example]

x-marked://defaults?syntaxHighlight=1&includeMathJax=0

A `defaults` módszert többnyire úgy tervezték, hogy a fejlesztő hivatkozásokat tudjon hozzáadni olyan ezoterikus funkciókhoz, amelyek egyébként nem lennének elérhetőek a Beállításokban. Előfordulhat azonban, hogy van néhány szabványos beállítás, amelyet az automatizálás során váltani szeretne. Néhány gyakori beállítás, amelyet az automatizálás során ellenőrizni szeretne:

szintaxisKiemelés
: a szintaxiskiemelés engedélyezése vagy letiltása

tartalmazza a MathJaxot
: a belső MathJax kezelés engedélyezése vagy letiltása

processzor
: állítsa `multimarkdown` vagy `mmd` értékre, ha a processzort MultiMarkdownra szeretné módosítani, `discount` vagy `gfm` értékre a Discount processzor használatához

h1IsPageBreak, h2IsPageBreak, breakBeforeFootnotes
: Automatikus oldaltörések az exportálásnál az 1. és 2. fejlécszint és lábjegyzetek előtt.


## dingus [dingus]

Nyissa meg a Markdown Dingust a különböző Markdown processzorok teszteléséhez.

	x-jellel:://dingus

##### Paraméterek: [parameters-3]

**processzor** (opcionális): adja meg, hogy melyik processzort válassza ki alapértelmezés szerint. Érvényes értékek:

- `multimarkdown` - MultiMarkdown processzor
- `commonmark` - CommonMark (GFM) processzor
- `discount` vagy `discount (gfm)` - Kedvezményes processzor
- `kramdown` - Kramdown processzor

Példák:

- `x-marked://dingus?processor=kramdown` - Megnyílik a Kramdown kiválasztásával
- `x-marked://dingus?processor=commonmark` - Megnyílik a CommonMark (GFM) kiválasztásával

*Megjegyzés:* Megnyílik a Markdown Dingus ablak, amely lehetővé teszi a különböző Markdown processzorok (MultiMarkdown, CommonMark (GFM), Discount és Kramdown) egymás melletti tesztelését és összehasonlítását. Tökéletes a Markdown szintaxissal való kísérletezéshez és a processzorok közötti különbségek megértéséhez.

## stíluslopás / lopás [stylestealer-steal]

Nyissa meg a Style Stealer HUD-ot. Hasznos, ha CSS-t szeretne rögzíteni egy élő oldalról, vagy manuális tartalomkivonási munkamenetet szeretne futtatni anélkül, hogy a felhasználói felületen keresztül elindítaná.

	Szinonimák: x-jelölt://stylestealer … , x-marked://steal …

##### Paraméterek: [parameters-4]

**url** _(nem kötelező)_: A Style Stealer ablakban előre kitöltendő URL. Ha kihagyja, a HUD üresen nyílik meg.

Példák:

- `x-marked://stylestealer?url=https%3A%2F%2Fmarkedapp.com`
- `x-marked://steal/https:%2F%2Fexample.com`

## importurl / markdownify [importurl-markdownify]

Nyissa meg az "URL importálása" (Content Extractor) ablakot, hogy manuálisan futtathassa a Markdownifier folyamatot. Ez **nem** hajtja végre automatikusan a kicsomagolást – ezt az alábbi `extract` parancs kezeli.

	Szinonimák: x-marked://importurl … , x-marked://markdownify…

##### Paraméterek: [parameters-5]

**url** _(nem kötelező)_: Előre kitölti az URL importálása mezőt. Ha kihagyja, az ablak egy üres mezővel nyílik meg, amely a hivatkozás beillesztésére vár.
**html** _(nem kötelező, csak markdownify)_: Ha a `x-marked://markdownify`-en van megadva, ennek URL-kódolású nyers HTML-nek kell lennie. A Marked a Vágólap előnézetével megegyező szabályok szerint konvertálja a HTML-kódot Markdown formátumba, és megnyitja egy átmeneti dokumentumban, mintha beillesztette volna a HTML-kódot a vágólap előnézeti ablakába.

Példák:

- `x-marked://importurl?url=https%3A%2F%2Fexample.com%2Farticle`
- `x-marked://markdownify/https:%2F%2Fnews.ycombinator.com`

## csináld [do]

Futtasson JavaScript parancsot egy dokumentumablakban. A Marked teljes JavaScript API-ja [itt dokumentálva](https://markedapp.com/help/jsapi/).

##### Paraméterek: [parameters-6]

**js** _(kötelező)_: JavaScript parancsot tartalmazó lekérdezési karakterlánc

* Elfogadja az elérési út paramétereit, amelyek a fájlok nevére hivatkoznak, vagy az "összes"
* A / által felosztott útvonalak több fájlban is keresnek
* A részleges fájlnevek illeszkednek a legjobban

		x-marked://do/filename1/filename2?js=...
		x-marked://do/all?js=...

**file**: vesszővel elválasztott útvonalakat/fájlneveket tartalmazó lekérdezési paraméter

	x-marked://do?file=filename1,filename2&js=...

A legelső ablakban fog működni, ha nincs megadva fájlnév (vagy nincs megadva az "összes")

## segítség [help]

Nyissa meg a Megjelölt belső súgórendszert, adott esetben adjon meg egy témát. Ez elsősorban belső használatra szolgál, de URL-en keresztül érhető el. Egy adott szakaszhoz tartozó URL-cím másolható, ha jobb gombbal kattint a címsortól jobbra található könyvjelző ikonra, és kiválasztja a __Hivatkozás másolása__ lehetőséget. A **Marked 3** alkalmazáson belüli súgó és keresés a `x-marked-3` sémát használja ezekhez a hivatkozásokhoz, így a macOS megnyitja őket Marked 3-ban, amikor a Marked 2 is telepítve van; az alábbi példák ezt az űrlapot használják.

##### dingus [dingus-2]

Nyissa meg a Markdown Dingust a különböző Markdown processzorok teszteléséhez.

	x-jellel:://dingus

######## Paraméterek:

**processzor** (opcionális): adja meg, hogy melyik processzort válassza ki alapértelmezés szerint. Érvényes értékek:

- `multimarkdown` - MultiMarkdown processzor
- `commonmark` - CommonMark (GFM) processzor
- `discount` vagy `discount (gfm)` - Kedvezményes processzor
- `kramdown` - Kramdown processzor

Példák:

- `x-marked://dingus?processor=kramdown` - Megnyílik a Kramdown kiválasztásával
- `x-marked://dingus?processor=commonmark` - Megnyílik a CommonMark (GFM) kiválasztásával

*Megjegyzés:* Megnyílik a Markdown Dingus ablak, amely lehetővé teszi a különböző Markdown processzorok (MultiMarkdown, CommonMark (GFM), Discount és Kramdown) egymás melletti tesztelését és összehasonlítását. Tökéletes a Markdown szintaxissal való kísérletezéshez és a processzorok közötti különbségek megértéséhez.

##### Paraméterek: [parameters-7]

**oldal** _(nem kötelező)_: Egy meglévő oldal pontos címe, opcionális horgonykivonattal

	x-marked-3://help?page=Document_Statistics

A szóközöket aláhúzásjelek helyettesítik, a Megjelölt súgófájl elnevezési konvenciója szerint. A horgony megadásakor kettőspont (:) használható a hash (#) helyett.

A cél megadható egyedül elérési úton (lekérdezési karakterlánc nélkül):

	x-marked-3://help/Keyword_Highlighting:editingkeywords


## kivonat [extract]

Csomagoljon ki tartalmat egy webes URL-ből, és nyissa meg új dokumentumként a Marked alkalmazásban.

	x-marked://extract?url=https://example.com

##### Paraméterek: [parameters-8]

**url** _(kötelező)_: A web URL-címe, ahonnan tartalom kinyerhető. `http://` vagy `https://` karakterekkel kell kezdődnie

**ablak** _(nem kötelező)_: Az ablak neve

**id** _(nem kötelező)_: Névtér azonosító

**alap** _(nem kötelező)_: Alap URL a relatív linkekhez

**emelés** _(opcionális)_: Állítsa `true` értékre az ablak felemeléséhez kinyitás után

**manuális** _(opcionális)_: Állítsa `true` értékre a Style Stealer manuális kibontási ablakának megnyitásához az automatikus kibontás helyett.

- Amikor `manual=true`, a Marked megnyitja a Stíluslopót, előre kitölti az URL mezőt (ha van), letilt minden automatikus Megnyitás párbeszédpanelt, és lehetővé teszi a stílusok/tartalom interaktív kiválasztását és kibontását a mentés előtt.
- Ha kihagyja vagy `false`, a Marked futtatja az automatikus kivonatot (Markdownifier), és az eredményt közvetlenül új ideiglenes dokumentumként nyitja meg.

##### Példák: [examples]

	x-marked://extract?url=https://news.ycombinator.com

	x-marked://extract?url=https://github.com&window=GitHub&raise=true

	x-marked://extract?url=https://example.com/article&manual=true

	x-marked://extract?url=https://blog.example.com/post-title

*Megjegyzés:* Ez a parancs a Marked tartalomkivonó szolgáltatását használja a weboldalak lekérésére, a tiszta tartalom kibontására az olvashatóság segítségével, a Markdown formátumba konvertálására, és az eredmény megnyitására egy új ideiglenes dokumentumban. A kivont tartalom metaadatokat (cím, forrás URL, dátum) tartalmaz, és tiszta Markdown formátumú. Tökéletes webtartalom gyors rögzítésére és szerkesztésére.

## nyitva [open]

Megnyitja a megadott dokumentumot a Megjelölve.

	x-marked://open?file=/Users/username/Desktop/report.md

##### Paraméterek: [parameters-9]

**fájl** *(kötelező)*: A megnyitandó dokumentum teljes POSIX elérési útja vagy az elérési utak vesszővel elválasztott listája

**speedread** *(opcionális)*: Állítsa `1` értékre a Speed Read automatikus elindításához a megnyitás után.

Az `open` olyan elérési utat is elfogad, amelynek összetevői egyetlen URL-be kerülnek

	x-jelölt://open/~/nvALT2.2

Ha a megadott fájl elérési útja nem létezik vagy nem nyitható meg, a Marked továbbra is előtérbe kerül. A *file* paraméter nélkül vagy üres értékkel futtatva egyszerűen megnyílik a Marked.

A Marked akkor is megnyitja a fájlokat, ha csak a fájl elérési útját hívja meg az URL-kezelő, pl. `x-marked:///Users/username/Desktop/report.md`.

## paszta [paste]

Hozzon létre egy új dokumentumot a vágólap jelenlegi tartalmából.

	x-jel:://paste

##### Paraméterek: [parameters-10]

**speedread** *(opcionális)*: Állítsa `1` értékre a Gyorsolvasás automatikus elindításához a vágólap előnézetének megnyitása után.

*Megjegyzés:* Ez ideiglenes dokumentumot hoz létre a "Vágólap előnézete" paranccsal. A vágólapon lévő bármely szöveg hozzáadódik egy új, üres dokumentumhoz, amely ezután megnyílik a Megjelölt mappában. Ha mentés nélkül zárja be, a rendszer eldobja.

## előnézet [preview]

Meghatározott szöveg előnézete egy új dokumentumban.

	x-marked://preview?text=Some%20text%20to%20%2A%2Apreview%2A%2A%0A

##### Paraméterek: [parameters-11]

**szöveg** *(kötelező)*: Az előnézetbe beszúrandó szöveg. A százalékos kódolású szöveg kódolatlan lesz a dokumentum megtekintése előtt.

**speedread** *(opcionális)*: Állítsa `1` értékre a gyorsolvasás automatikus elindításához az előnézeti szöveg megnyitása után.

## folyam [stream]

Nyissa meg a streaming vágólap előnézeti ablakát.

	x-jellel:://stream

##### Paraméterek: [parameters-12]

**speedread** *(opcionális)*: Állítsa `1` értékre a Speed Read automatikus elindításához a streaming előnézetének megnyitása után.

*Megjegyzés:* Ez ideiglenes dokumentumot hoz létre a "Vágólap előnézete" paranccsal. Az átadott szöveg hozzáadódik egy új, üres dokumentumhoz, amely ezután megnyílik a Megjelölve. Ha mentés nélkül zárja be, a rendszer eldobja.

## frissítés [refresh]

Egy dokumentum előnézetének vagy az összes megnyitott előnézetnek frissítése.

##### Paraméterek: [parameters-13]

**file**: vesszővel elválasztott elérési utakat/fájlneveket tartalmazó lekérdezési paraméter (a fájloknak jelenleg meg kell lenniük a Marked alatt). `file` paraméter vagy `?file=all` nélküli hívás esetén az összes nyitott ablak frissül.

A *file* paraméter lehet részleges is, a Marked minden nyitott ablakot frissít a *fájlnévben* részleges egyezéssel (nem a teljes elérési úttal). Az "összes" megadása az összes ablakot frissíti.

	x-jellel /refresh

	x-marked://refresh?file=/Users/username/Desktop/report.md

	x-marked://refresh?file=report.md

Ha nem `file` paraméterrel hívjuk meg, de az url-ben megadott dokumentumútvonalak vannak, akkor a / által felosztott elérési utak több fájlban is keresni fognak, és a részleges fájlnevek adják meg a legjobb egyezést.

	x-marked://refresh/filename1/filename2

## stílus [style]

Állítsa be egy vagy több dokumentum előnézeti stílusát (CSS).

##### Paraméterek: [parameters-14]

**css** _(kötelező)_: egy stílus nevét vagy elérési útját tartalmazó lekérdezési karakterlánc. A stílusoknak alapértelmezettként vagy manuálisan hozzáadott egyéni stílusként kell szerepelniük a Marked stílusmenüjében.

* Elfogadja az elérési út paramétereit, amelyek a fájlok nevére hivatkoznak, vagy az "összes"
* A / által felosztott útvonalak több fájlban is keresnek
* A részleges fájlnevek illeszkednek a legjobban

		x-marked://stílus/fájlnév1/fájlnév2?css=...
		x-marked://style/all?css=...

**file**: vesszővel elválasztott útvonalakat/fájlneveket tartalmazó lekérdezési paraméter

	x-marked://style?file=filename1,filename2&css=...

Ez a módszer a legelső ablakban fog működni, ha nincs megadva fájlnév (vagy az "összes" nem adható meg).