<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A {% prefspane Export %} opciói:

(További információért lásd: [Exportálás](Exporting.html))

![Beállítások: Exportálás][1]

[1]: images/screenshots/preferences-Export.jpg @2x width=920px height=1031px class=preferencepane-scroll

### Profil exportálása [export-profile]

Profil exportálása
: Válasszon ki egy mentett profilt a felugró menüből. A profilok az exportálási beállítások teljes készletét tárolják a munkafolyamatok közötti gyors váltáshoz (például a nyomtatott PDF vagy a webes HTML). Lásd: [Profilok exportálása](Exporting.html#export-profiles).

Új
: Új profil létrehozása az aktuális beállításokból.

Kezelése
: Nyissa meg a profilkezelőt a profilok átnevezéséhez, másolásához vagy törléséhez.

### Nyomtatás/PDF [printpdf]

A hivatkozások/kiemelések letiltása PDF exportálásakor vagy nyomtatáskor
: Nyomtatáskor eltávolítja a formázást (aláhúzás és színes) a hivatkozásokról.

Adja meg az URL-t szöveges megjegyzésként
: PDF nyomtatásakor vagy exportálásakor a hivatkozás URL-címe a hivatkozott szöveg után jelenik meg.

Cserélje le a vízszintes szabályokat oldaltörésekkel
: A dokumentum vízszintes szabályait oldaltörésekké alakítja (ez ráadásul a lábjegyzeteket is új oldalra kényszeríti).

Képek beágyazása HTML másolásakor
: Ha engedélyezve van, a HTML vágólapra másolása megkeresi a helyi képeket, és a Base64 kódolja azokat, hogy adat URL-ként szerepeljen a forráskódban.

Nyomtasson háttérszíneket és képeket
: Alapértelmezés szerint a Marked fehér háttérrel nyomtat/exportál. Ha egyéni témákból szeretne háttérszíneket és képeket használni, engedélyezze ezt a lehetőséget.

Akadályozza meg az árva címsorokat
: Ez a beállítás megakadályozza, hogy a következő szakasz címsorai megjelenjenek az oldal alján, anélkül, hogy a tartalom megjelenne.

Első H1 kizárása
: Ha H1-eket használ oldaltörésként, figyelmen kívül hagyja a dokumentum első első szintű címsorát.

Használja az első H1-et tartalék címként
: Ha olyan alkalmazásokat használ, mint a Bear vagy a streaming előnézet, ez az opció lehetővé teszi a fájlnév felülírását a dokumentum első H1-jének tartalmával. Ha a "title" metaadatai meg vannak adva, az mindig elsőbbséget élvez.

Előtte oldaltöréseket adjon hozzá
: 1/2 szintű fejléceket használjon szakaszelválasztóként, mindig új oldalon kezdje. Válassza a "Lábjegyzetek" lehetőséget, ha mindig egy oldaltörést szeretne hozzáadni a lábjegyzetek elé a dokumentumban.

Oldaltörések jelzése az előnézetben
: Világos szaggatott vonal megjelenítése, ahol a töréseket <!\--BREAK\--> szintaxissal szúrja be, vagy az Exportálási beállításokban ellenőrizze az automatikus törés opciókat.

Egyedi betűméret az exportáláshoz/nyomtatáshoz
: Ha be van állítva, az összes szöveg a kiválasztott pontbeállítás alapján lesz méretezve (alapértelmezés szerint 10 pontos).

Margók
: Nyomtatási margók meghatározása (pontokban megadva) a felső, az alsó, a bal és a jobb oldalon.

Tartalomjegyzék nyomtatása
: Automatikus tartalomjegyzék hozzáadása a nyomtatáshoz/PDF-hez.

Oldalszünet után
: Automatikusan új oldalra törés a beszúrt tartalomjegyzék után.

Tartalomjegyzék szintjelzők
: A legördülő menük segítségével állítsa be a listaelem-jelölőt a tartalomjegyzék minden egyes behúzási szintjéhez.

### Fejlécek és láblécek [headers-and-footers]

Konfigurálja a betűtípust, a logót, a fejléc/lábléc mezőket, a dátum- és időformátumokat, az első oldalra való felvételt, az oldalszámozási eltolást és a szegélyeket. A mezők helyőrzői a következők: `%title`, `%logo`, `%page`, `%total`, `%date`, `%time`, `%h1`, `%h2` és mások.

Lásd: [Fejlécek és láblécek](Exporting.html#headers-and-footers) az [Exportálás](Exporting.html) helyen a helyőrző hivatkozásokért és példákért. A `%date` és `%time` formátumkódokról lásd a [Dátum- és időformátumok](Exporting.html#dateandtimeformats) részt.

Szerepel az első oldalon
: Ha a fejléc és/vagy lábléc nincs bejelölve, az első oldal nem a megadott típust nyomtatja ki.

Dátumformátum
: strftime stílusú formátumú karakterlánc a `%date`-hez a fejlécekben és a láblécekben. Lásd: [Dátum- és időformátumok](Exporting.html#dateandtimeformats).

Időformátum
: strftime stílusú formátum karakterlánc a `%time` számára a fejlécekben és a láblécekben. Lásd: [Dátum- és időformátumok](Exporting.html#dateandtimeformats).

Oldalszámozás eltolása
: Az oldalszámok kezdő számának beállítására szolgál. Ha például az első oldalon van egy tartalomjegyzék, és azt szeretné, hogy a számozás a második oldalon kezdődjön, állítsa az eltolást -1-re. A 2. oldal mostantól az 1. oldal lesz, és az összes oldal ennek megfelelően módosul.

Határ
: Nyomtasson vízszintes vonalat a fejléc alá és/vagy a lábléc fölé.

Alapértelmezett formátumok visszaállítása
: A dátum- és időformátum karakterláncainak visszaállítása a Marked alapértelmezett értékére (`%m-%d-%Y` és `%I:%M %p`). Lásd: [Dátum- és időformátumok](Exporting.html#dateandtimeformats).