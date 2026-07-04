<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Megjelölve lehetővé teszi egy dokumentum bizonyos attribútumainak MultiMarkdown metaadat formátumban történő beállítását (részletek lent). Ezekkel olyan jellemzőket és stílusokat határozhat meg, amelyek csak az adott dokumentumot érintik, az alapértelmezett beállítások módosítása nélkül.

A legtöbb MultiMarkdown fejlécet figyelmen kívül hagyja az előnézet, de a következők megengedettek, és hatással vannak a megjelenítésre. A végső kimenetben más metaadatokat is megadhat, a Megjelölve figyelmen kívül hagyja az alább nem szereplő kulcsokat. Ha HTML-ként menti, és *nem* tartalmaz sablont, a Marked az összes metaadatkulcsot a várt módon jeleníti meg.

## Metaadat formátum

A metaadatok a Markdown fájl tetején vagy közvetlenül a YAML-fejlécek után kerülnek bevitelre. Ezek egy kulcsból, majd kettőspontból, nem kötelező szóközökből vagy tabulátorokból és a következő értékből állnak:

	Példa metaadat: példakulcs

Több metaadat-bejegyzésnek a saját sorában kell lennie, de sortörés nélkül. Az utolsó metaadat-bejegyzést egy üres sornak kell követnie a dokumentumszöveg kezdete előtt.

	Először is: ez az első metaadat-bejegyzés
	Második: ez a második bejegyzés
	Harmadik: az utolsó metaadat-bejegyzés

	# A dokumentum szövegének eleje

## Megjelölt metaadatkulcsok

### Metaadatok elrejtése más processzorok számára [hidingmeta]

**Megjegyzés:** Ha egyéni processzort használ, vagy közvetlenül olyan forráshoz teszi közzé a Markdown-t, amely nem dolgozza fel ezeket a metaadatokat, továbbra is használhatja, ha HTML megjegyzésjelölőket ad hozzá a metaadatok elé és után. A MultiMarkdowntól és más processzoroktól eltérően a Marked ezeket a címkéket bárhol megtalálja a dokumentumban, és feldolgozza/eltávolítja őket a kimenetből. Így a fejlécben szereplők megadják a kívánt eredményeket a Megjelölve, de máshol nem jelennek meg:

	<!--
	Megjelölt stílus: Saját stílus
	Egyedi processzor: igaz
	-->

*Csak győződjön meg arról, hogy a metaadatkulcs a sor elején kezdődik szóközök és tabulátorok nélkül, és ne tegyen mást az érték utáni sorba.*

### Dokumentumonkénti stílusok

A "Megjelölt stílus:" gomb beállítja a dokumentum előnézeti stílusát. Az érték lehet egy alapértelmezett stílus neve, vagy bármely [Custom Style](Custom_Styles.html) neve vagy elérési útja, amelyet a beállításokban definiált. Ha ez a kulcs megtalálható, és megegyezik egy olyan stílussal, amelyről a Marked tud, akkor ezt a stílust fogja használni az előnézethez minden alkalommal, amikor az azt tartalmazó dokumentumot betölti.

**Példa**

	Jelzett stílus: előkelő polgár

### Idézetek nyelve

Alapértelmezés szerint a Marked angol stílusú idézőjeleket használ. Ezt dokumentumonként módosíthatja az "Idézetek nyelve:" billentyűvel. Az elérhető nyelvek a következők:

* holland
* angolul
* francia
* német
* guillemets
* svéd

**Példa**

	Idézetek Nyelv: francia

	Francia nyelvű "idézőjeleket" hoz létre.

### Alapfejléc szint

Az „Alapfejléc szintje:” billentyűvel beállíthatja azt a fejlécszintet, amelytől a Marked elkezd számolni. Ennek 1-6 számnak kell lennie, és módosítja a „#” fejlécek megjelenítési módját. Ha a fejlécszintet 3-ra állítja, akkor az általában első szintű fejléc (h1) harmadik szintű fejlécként (h3) jelenik meg, és a következő fejlécek a hierarchiában 2-vel feljebb tolódnak.

**Példa**

	Alapfejléc szint: 3

	# Ez a címsor h3-ként jelenik meg

	## Ez a cím egy h4 lesz

	Így jelenik meg:

	<h3>Ez a címsor h3-ként jelenik meg</h3>

	<h4>Ez a cím egy h4 lesz</h4>

### Egyedi processzorok

Az [Egyéni feldolgozó](Custom_Processor.html#preprocessor) részben részletezve engedélyezheti vagy letilthatja az egyéni processzort és egyéni előfeldolgozót metaadatok használatával:

    Egyedi processzor: igaz
    Egyéni előfeldolgozó: false

"igaz" vagy "hamis" kapcsolja be és ki az elő-/feldolgozót.

A "Processzor" értéke "multimarkdown" vagy "discount" állítható be az egyik vagy másik belső processzor használatára kényszerítéséhez. Ez a dokumentumonkénti beállítás nem módosítja a {% prefspane Processor %} alapértelmezett beállítását.

### Fejlécek/láblécek nyomtatása

A nyomtatási fejlécek és láblécek beállításait felülbírálhatja az {% prefspane Export %}-ben a következő billentyűkkel:

	fejléc nyomtatás balra:
	nyomtatási fejléc központ:
	fejléc nyomtatása jobbra:
	lábléc nyomtatása balra:
	lábléc középpontjának nyomtatása:
	lábléc nyomtatása jobbra:

Ide tartozhatnak [nyomtatási változók](Exporting.html#headersandfooters), például `%title`, `%page`, `%total` stb., valamint más metaadatokra való hivatkozások a `%md_[key without spaces]` használatával.

### Margók nyomtatása

A `Margins:` billentyűvel állítsa be az oldalmargókat a nyomtatáshoz és a lapozott PDF kimenethez. Az értékek pontokban vannak megadva; a `px`, `pt` és `em` utótagokat figyelmen kívül hagyja. Adjon meg két számot a függőleges és vízszintes margókhoz, vagy négy számot a felső, jobb, alsó és bal oldali margókhoz:

	Margók: 10 20
	Margók: 10, 20, 10, 20

A metaadat-margók felülírják a {% prefspane Export %} beállításokat és a PDF-exportálási panel margómezőit.

### JavaScript beszúrása

Ez a módszer a dokumentum `<head>` címkéjében szereplő adatokat határozza meg. A Marked figyelmen kívül hagyja ennek a kulcsnak a legtöbb értékét, kivéve a teljes dokumentum kimenetét, de tiszteletben tartja az így beépített parancsfájlokat. Az itt definiált szkriptcímkék nem lesznek a fejlécben, azonban a záró `</body>` címke elé kerülnek hozzá. A jQuery már be van töltve, és ezt bármely beinjektált szkriptben kihasználhatja.

**Példa**

	XHTML-fejléc: <script>(function($){$('#wrapper').fadeOut();})(jQuery);</script>

		-vagy-

	XHTML-fejléc: <script src="myfancyscript.js"></script>