<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked tartalmaz egy AppleScript szótárt az előnézet, az export és a munkafolyamat-integráció automatizálásához. Megnyithatja a dokumentumokat, vezérelheti az előnézetet (újratöltés, görgetés, kiemelések, automatikus görgetés, gyorsolvasás), statisztikákat olvashat, processzorokat és stílusokat módosíthat, HTML vagy RTF fájlokat másolhat a vágólapra, és exportálhat a {% appmenu File, Export %} menüben elérhető legtöbb formátumba. **A címsorok / tartalomjegyzék előnézete az AppleScript segítségével folyamatban van** (lásd alább).

Az URL-alapú automatizáláshoz (shell szkriptek, `open` parancsok és visszahívások) tekintse meg az [URL Handler](URL_Handler.html) részt. Az AppleScript és az URL-kezelő kiegészíti egymást: használja az AppleScriptet, ha egy adott dokumentumot vagy ablakot kell megcéloznia, és URL-eket, ha egy egyszerű `open 'x-marked://...'` hívás elegendő.

## A szótár megtekintése

A **Script Editor** programban válassza a **Fájl → Szótár megnyitása…** lehetőséget, és válassza a Megjelölt lehetőséget. A szótár felsorolja az **alkalmazás**, **dokumentum** és **ablak** objektumok parancsait, valamint a Marked suite exportparancsait.

MacOS rendszeren a **Script Editor** segítségével böngészhet a szkriptdefiníciók között.

## Célzás megjelölve

A szabványos telepítéshez:

```applescript
tell application "Marked"
	-- commands here
end tell
```

## Dokumentumok és ablakok

**Alkalmazás**

- `documents` -- előnézeti dokumentumok megnyitása (rendezett lista).
- `windows` -- előnézeti ablakok.

**Dokumentum**

- `name` -- megjelenített név.
- `path` -- a fájl elérési útja, amikor a dokumentumot lemezre menti.
- `modified` -- vannak-e a dokumentumban nem mentett szerkesztői változások.
- `processor` -- Markdown processzor ehhez az előnézethez (olvasás/írás). Érvényes nevek: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. A `processor` beállítás dokumentumonkénti felülírást alkalmaz, és újra betölti az előnézetet; nem változtatja meg az {% prefspane Processor %} globális alapértelmezését.
- `preprocessor` -- előfeldolgozó ehhez az előnézethez (olvasás/írás). A `true` vagy a `false` gombbal engedélyezheti vagy letilthatja az egyéni előfeldolgozót, vagy adott esetben az előfeldolgozó nevét.
- `source text` -- nyers Markdown forrás (csak olvasható).
- `critic markup mode` -- hogy a CriticMarkup feldolgozás engedélyezve van-e (olvasás/írás). A módosítás után újra betöltődik az előnézet.
- `is autoscrolling` -- aktív-e az automatikus görgetés (csak olvasható).
- `is speed reading` -- aktív-e a gyorsolvasási mód (csak olvasható).
- Előnézeti, olvasói, statisztikai és exportálási parancsok (lásd alább).

**ablak**

- `document` -- az ablakban látható `MarkdownDocument`.
- `style` -- aktuális előnézeti stílus neve (olvasás/írás). A `style` beállítása újratölti az előnézetet a kiválasztott témával (ugyanúgy, mint a stílus kiválasztása az előnézeti stílus menüből).
- `close`, `save`, `print` -- szabványos ablakparancsok.
- Ugyanazok az előnézeti, olvasói, statisztikai és export parancsok, mint a dokumentumokon (tovább az ablak dokumentumába).

Egy adott előnézet exportálásakor előnyben részesítse a `tell document 1` vagy a `tell window 1's document` értéket. Az alkalmazás exportálási parancsai a kulcsablakot vagy az aktuális dokumentumot használják, ha nincs megadva vevő.

### Példa: elérési út megnyitása és olvasása

```applescript
tell application "Marked"
	open POSIX file "/Users/you/Documents/report.md"
	set docPath to path of document 1
end tell
```

### Példa: az előnézeti stílus módosítása

```applescript
tell application "Marked"
	tell window 1
		set style to "Amblin"
	end tell
end tell
```

A stílusnevek megegyeznek az előnézeti stílusmenüvel (megjelenítési név, CSS-erőforrás neve, például `swiss` vagy belső azonosító). A Stíluskezelőben hozzáadott egyéni stílusok támogatottak.

Használja a **`get preview style names`**-t az alkalmazásobjektumban az engedélyezett stílusmegjelenítési nevek felsorolásához.

### Példa: processzor és forrásszöveg

```applescript
tell application "Marked"
	tell document 1
		set processor to "Kramdown"
		set md to source text
		set critic markup mode to true
	end tell
end tell
```

## Alkalmazásparancsok

Ezek a parancsok az **alkalmazás** objektumra vonatkoznak (nem egy adott dokumentumra).

| Parancs | Leírás |
| --- | --- |
| `open streaming preview` | Nyisson meg egy [streaming vágólap előnézete](Streaming_Preview.html) ablakot. |
| `preview clipboard` | Nyissa meg a [vágólap előnézetét](Opening_Files.html) az aktuális vágólap tartalmából (ugyanaz, mint a {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}). |
| `close all` | Zárja be az összes megnyitott előnézeti dokumentumot (nincs mentési felszólítás; A Megjelölt nem szerkeszti a forrásfájlokat). |
| `get available processors` | Processzornevek listázása: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. |
| `get preview style names` | Az engedélyezett előnézeti stílus megjelenítési nevek listázása. |
| `get_available_formats` | A támogatott `convert_to` formátumnevek listája. |
| `get_available_profiles` | Sorolja fel az exportprofil neveket (ugyanaz, mint az `profiles` tulajdonság). |

Hozd a Marked előtérbe a szabványos AppleScript **`activate`** paranccsal:

```applescript
tell application "Marked"
	activate
	open streaming preview
end tell
```

## Előnézeti vezérlő

Elérhető **dokumentumban** és **ablakban**. Ezek többségéhez egy betöltött előnézeti WebView szükséges.

| Parancs | Paraméterek | Leírás |
| --- | --- | --- |
| `refresh preview` | — | Töltse be újra az előnézetet a forrásfájlból (ugyanaz, mint a {% appmenu Preview, Refresh %}). |
| `reveal in finder` | — | Jelenítse meg a dokumentumfájlt a Finderben. |
| `show highlights` | — | Kulcsszókiemelés engedélyezése (kerülje a szavakat, alternatívákat, passzív hangot, egyéni listákat). |
| `full screen` | opcionális `enabled` logikai | Lépjen be, lépjen ki, vagy váltson a teljes képernyős előnézeti módba. |
| `scroll to heading` | `title` vagy `id` | Görgessen egy címsorhoz a látható címszöveg vagy a DOM `id` segítségével. |
| `scroll to position` | `percent` vagy `line` | Görgetés a dokumentum magasságának százaléka vagy hozzávetőleges sorszám szerint. |
| `copy html` | — | Másolja az előnézeti HTML-kódot a vágólapra (fogaskerék menü vagy {% kbd shift cmd C %}; lásd: [HTML másolása](Exporting.html#copyhtml)). |
| `copy rtf` | — | A formázott szöveg másolása a vágólapra. |

```applescript
tell application "Marked"
	tell document 1
		refresh preview
		show highlights
		scroll to heading id "introduction"
		scroll to position percent 50
		full screen with enabled true
	end tell
end tell
```

## Automatikus görgetés és gyorsolvasás

| Parancs | Leírás |
| --- | --- |
| `autoscroll` | Indítsa el az automatikus görgetést. Az opcionális `wpm` egész szám beállítja a szavakat percenként a kezdés előtt. |
| `stop autoscroll` | Állítsa le az automatikus görgetést. |
| `pause autoscroll` | Az automatikus görgetés szüneteltetése vagy folytatása. |
| `speed read` | Indítsa el vagy kapcsolja be a [gyorsolvasás](Speed_Reading.html)-t. |
| `stop speed read` | Állítsa le a sebességolvasást. |
| `pause speed read` | A gyorsolvasás szüneteltetése vagy folytatása. |

Ellenőrizze az állapotot a `is autoscrolling` és `is speed reading` dokumentumtulajdonságokkal.

```applescript
tell application "Marked"
	tell document 1
		autoscroll with wpm 250
		-- or: speed read
	end tell
end tell
```

## Statisztika

**`get statistics`** egy `statistics_record` értéket ad vissza az aktuális Markdown forrásból (nem a statisztikai fiókban látható formázott karakterláncokból) számított számértékekkel.

| Ingatlan | Leírás |
| --- | --- |
| `word_count` | Szószám |
| `sentence_count` | Mondatszám |
| `character_count` | Karakterszám |
| `paragraph_count` | Bekezdések száma |
| `average_words_per_sentence` | Szavak átlagos száma mondatonként |
| `average_syllables_per_word` | Átlagos szótagok száma szónként |
| `complex_word_percentage` | Összetett szó százalék |
| `reading_ease` | Flesch könnyű olvasás |
| `fog_index` | Fegyverzési köd index |
| `grade_level` | Flesch–Kincaid fokozat |
| `gulpease` | Gulpease index (olasz olvashatóság; `0` ha nem alkalmazható) |
| `gulpease_band` | Gulpease zenekar `1`–`4` (adott esetben) |
| `reading_time_minutes` | Olvasási idő **250 WPM** mellett |

```applescript
tell application "Marked"
	set stats to get statistics of document 1
	set wc to stats's word_count
	set fog to stats's fog_index
end tell
```

## Tartalomjegyzék (folyamatban lévő munka)

{% note %}
**WIP – még nem megbízható.** A szótár tartalmaz egy **`headings`** tulajdonságot és **`headings`** parancsot a beágyazott előnézeti címsorok (`heading_item` rekordok) olvasásához. Ez az automatizálás **nem működik megfelelően** a jelenlegi buildekben (üres eredmények, kényszerítési hibák vagy „nincs eredmény”). Egy későbbi kiadásban javítják. Addig előnyben részesítse a **`scroll to heading`**-t ismert címmel vagy azonosítóval.
{% endnote %}

**Tervezett viselkedés** (ha kész): beágyazott `heading_item` rekord az **előnézet** (`h1`–`h6`) címsoraiból, nem pedig a nyers jelölésből.

| Ingatlan | Leírás |
| --- | --- |
| `title` | Címsor szövege |
| `id` | DOM `id` attribútum (üres karakterlánc, ha nincs jelen) |
| `level` | Címsor szintje `1`–`6` |
| `children` | `heading_item` rekord beágyazott listája |

**`headings`** (dokumentumtulajdonság) – minden szint. **`headings levels {2, 3}`** (parancs) — opcionális szűrő: csak az iránymélységek (nem tartomány).

```applescript
-- Planned; do not rely on this yet
tell application "Marked"
	set toc to headings of document 1
	set filtered to headings levels {2, 3} of document 1
end tell
```

Használja a `id` értékeket **`scroll to heading id "..."`**-val, ha a címsorok automatizálása stabil.

## Nyomtatás profillal

**`print with profile`** ideiglenesen alkalmazza az exportprofil nyomtatási beállításait, majd kinyomtatja a dokumentumot (ugyanaz a beállításcsomag, mint a {% prefspane Export %} exportprofiljai).

```applescript
tell application "Marked"
	tell document 1
		print with profile "Print Letter"
	end tell
end tell
```

A profilnevek megkülönböztetik a kis- és nagybetűket. Nyomtatás után a Marked visszaállítja a korábban aktív exportálási profilt.

## Profilok exportálása

Az exportprofilok az exportálási/nyomtatási beállítások kötegeit tárolják (margók, fejlécek, tartalomjegyzék-beállítások és hasonló beállítások a {% prefspane Export %}-től).

**Profilnevek olvasása**

```applescript
tell application "Marked"
	set profileList to profiles
	-- or: get_available_profiles
end tell
```

**Exportálás profillal**

```applescript
tell application "Marked"
	tell document 1
		export html to "/Users/you/Desktop/report.html" with profile "My Profile"
	end tell
end tell
```

A profilnevek megkülönböztetik a kis- és nagybetűket, és pontosan meg kell egyeznie a mentett profillal.

## Parancsok exportálása

Az exportálási parancsok az **alkalmazás**, **dokumentum** és **ablak** objektumokon érhetők el. Minden parancshoz szükség van egy **`to`** paraméterre a kimeneti útvonallal (POSIX elérési út karakterlánc vagy `file` objektum).

| Parancs | Kimenet |
| --- | --- |
| `export markdown` | Markdown (.md) |
| `export html` | HTML |
| `export paginated pdf` | Oldalszámozott PDF (nyomtatási elrendezés) |
| `export continuous pdf` | Folyamatos görgetéses PDF |
| `export epub` | EPUB |
| `export docx` | Microsoft Word (.docx) |
| `export odt` | OpenDocument szöveg |
| `export textbundle` | TextBundle |
| `export rtf` | RTF |
| `export opml` | OPML |

**Jegyzetek**

- A lapozott PDF ugyanazt a HTML-PDF folyamatot használja, mint a {% appmenu File, Export As, Save PDF (Paginated) %}. Nem érhető el nyers HTML előnézeti dokumentumokhoz.
- A HTML-exportálás a **megjelenített előnézetet** használja (amit a WebView-ban lát), nem pedig a nyers Markdown-forrásfájlt.
- A folyamatos PDF rögzíti az aktuális előnézeti WebView elrendezést.

### Alapvető export

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Desktop/report.pdf"
	end tell
end tell
```

### Exportálási útvonalak és homokozó

- Használjon teljes POSIX elérési utat a célfájlhoz.
- A Megjelölt képes közbenső mappákat létrehozni, ha az exportálási útvonal **a megnyitott dokumentum mappájában** belül van (például a `.../MyProject/build/output.pdf` címre exportál a `.../MyProject/chapter.md` előnézete közben).
- A dokumentum mappáján kívülre történő exportáláshoz írható elérési út szükséges, amelyhez a Megjelölt hozzáférhet (mentett dokumentum helye, biztonsági hatókörű könyvjelzők vagy a Megnyitás párbeszédpaneleken megadott mappák). Ha az elérési út nem írható, a parancs az exportálás megkezdése előtt hibát ad vissza.

## `with` opciók (tulajdonságrekord)

A `with profile` helyett a **`with`** vagy **`with properties`** használatával adhatja át az opciók rekordját:

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in", fontSize:"14"}
```

Az AppleScript közvetlenül felismeri ezeket a kulcsokat (exportálás előtt leképezik őket):

| Kulcs | Leírás | Példa |
| --- | --- | --- |
| `style` | Exportálás előtt alkalmazandó előnézeti stílus (teljes előnézet újratöltése) | `"Amblin"`, `"Swiss"` |
| `pageSize` | Oldalméret név nyomtatása | `"A4"`, `"Letter"` |
| `margins` | Nyomtatási margók (lásd lent) | `"1in"`, `"1in 2in"` |
| `fontSize` | Az exportálási/nyomtatási alap betűméret felülbírálása pontokban (oldalszámozott és folyamatos PDF) | `"14"`, `"12pt"` |

A `fontSize` lehetővé teszi ugyanazt az **Egyéni betűméret exportáláshoz/nyomtatáshoz** opciót a {% prefspane Export %}-től. Nem érinti a Fountain dokumentumokat, amelyek rögzített forgatókönyv-méretet használnak.

Ha az `style` szerepel, a Marked alkalmazza a témát, megvárja, amíg az előnézet befejeződik az újratöltés után, majd exportálja. Nincs szükség külön `set style` lépésre.

A rekord többi kulcsa megegyezhet a profilokból származó **exportálási preferencia** nevekkel (ugyanazok a kulcsok, amelyek a {% prefspane Export %}-ben vannak tárolva, például `printBackgrounds`, `printTOC`, `topPrintMargin`). Ezeket az értékeket ideiglenesen alkalmazzák az exportra.

Az ütköző forrásokat nem kombinálhatja hanyagul: ha `with profile`-t használ, először töltse be azt a profilt; ha `with` rekordot használ, a rekordban lévő profilkulcsok felülírják az exportálás aktuális beállításait.

### Margó gyorsírás

A `margins` érték egy karakterlánc, amely egy-négy mérést tartalmaz. Mértékegységek: `in`, `cm`, `mm`, `pt` vagy `"` hüvelyk esetén. Az egység nélküli számot pontként kell kezelni.

| Értékek | Jelentése |
| --- | --- |
| `1in` | Minden oldal |
| `1in 2in` | Felül és alul `1in`, balra és jobbra `2in` |
| `1in 2in 1in` | Felül `1in`, bal és jobb `2in`, lent `1in` |
| `1in 2in 1in 2in` | Felül, jobb, lent, bal |

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in 2in"}
export paginated pdf to "/path/out.pdf" with {style:"Amblin", margins:"1in 2in 1in 2in"}
```

### Kombinált példa

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Documents/MyBook/build/book.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

## `convert_to`

Az alkalmazásobjektum a régi parancsfájl-parancsokat is megjeleníti:

- **`convert_to`** – a Markdown szöveg vagy a fájl elérési útja konvertálása formátumba (`html`, `pdf`, `epub`, `docx`, `rtf` és mások), opcionálisan a {% prefspane Processor %}.18 és 180⟧.18 segítségével
- **`get_available_formats`** - listázza a támogatott konverziós formátumok neveit.
- **`get_available_profiles`** -- exportálási profilnevek listája (ugyanaz, mint a `profiles` tulajdonság).

A `convert_to` továbbra is elérhető a régebbi munkafolyamatokhoz és csak az AppleScript-automatizáláshoz.

## Hibakeresés

Engedélyezze a **Hibakeresési módot** a {% prefspane Advanced %} alatt (vagy a Beállításokban a hibakeresési beállításokat). A Marked ezután naplózza az AppleScript-exportálási lépéseket Info szinten a `[AppleScript]` előtaggal a Console.appban és a Marked naplónézőjében.

Hasznos naplósorok oldalszámozott PDF-exportálás nyomon követéséhez:

- `paginated PDF: fetching preview HTML`
- `HTMLToPDFGenerator: loadHTMLString`
- `HTMLToPDFGenerator: didFinishLoadForFrame`
- `paginated PDF: generator finished`

A hosszú exportálások (különösen az oldalszámozott PDF-fájlok) felfüggesztik az AppleScript-eseményt a befejezésig, így az ügyfelek nem lépnek túl az exportálás közben.

## Hibák

A sikertelen exportálás beállítja a parancsfájl-hiba karakterláncát a parancsban (látható a Script Editorban és a `on error` kezelőkben). Gyakori üzenetek:

- Exportálási útvonal megadása kötelező.
- Az exportálási könyvtár nem létezik (a dokumentummappán kívül).
- Nem lehet exportálási könyvtárat létrehozni, vagy engedélyhiba történt a fájl írása közben.
- Ismeretlen előnézeti stílusnév.
- Időtúllépés várva az előnézetre a stílusmódosítás utáni újratöltésre.
- A lapozott PDF-exportálás időtúllépést szenvedett vagy meghiúsult az oldalak generálásakor.

## Integráció más eszközökkel

Az alkalmazások használhatják a Marked AppleScript felületét a dokumentumok metaadatainak olvasásához. A Parancsikonok alkalmazáshoz lásd: [Shortcuts Integration](Shortcuts_Integration.html). Shell-vezérelt munkafolyamatok, mappafigyelők és szerkesztő-visszahívások esetén az [URL-kezelő](URL_Handler.html) gyakran egyszerűbb. A [Marked Bonus Pack](Workflow_Integration.html#marked-bonus-pack) további szkripteket és szolgáltatásokat tartalmaz.