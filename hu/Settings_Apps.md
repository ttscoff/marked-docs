<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A {% prefspane Apps %} opciói:

(Lásd: [További alkalmazástámogatás](Additional_Application_Support.html))

![Beállítások: Alkalmazások][1]

[1]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Általános beállítások [general-settings]

Szövegszerkesztő
: Válasszon ki egy szövegszerkesztőt, amely az {% kbd cmd E %} beírásakor fogadja az aktuális dokumentumot.

Az új fájlok automatikus szerkesztése
: Az "Új fájl" parancs használatakor ez az opció automatikusan megnyitja a létrehozott fájlt a választott külső szerkesztőben.

A szöveges fájlokra mutató hivatkozásoknak a következő helyen kell megnyílniuk:
: Meghatározza a Marked viselkedését, amikor az előnézeti ablakban egy hivatkozásra kattintva helyi szövegfájlhoz vezet.

Képszerkesztő
: Válassza ki azt az alkalmazást, amely megnyílik, ha a helyi képre jobb gombbal kattint, és a „Kép szerkesztése” lehetőséget választja.

Képannotáció/jelölőszerkesztő
: Válasszon ki egy alkalmazást, amely megnyílik, ha a helyi képre jobb gombbal kattint, és a „Kép megjegyzése” van kiválasztva.

Ha nincs kiválasztva szerkesztő, a Marked megjeleníti a telepített alkalmazások menüjét, amikor szerkeszti vagy megjegyzéseket fűz. A menüben megtalálhatók a Mac számítógépen található általános Markdown, kép és annotációs eszközök, az **Egyéb…** opció, amellyel bármelyik alkalmazást kiválaszthatja az `/Applications` közül, és a **Mindig használja ezt az alkalmazást** (alapértelmezés szerint engedélyezve van), hogy elmentse választását alapértelmezettként. A kijelölés eltávolításához és a kiválasztóhoz való visszatéréshez használja a törlés gombot (körbe X-szel) a {% prefspane Apps %}-ben szereplő Válasszon vezérlőelemek mellett.

### Alkalmazás-specifikus beállítások [application-specific-settings]

Alapértelmezés szerint a megjegyzések és megjegyzések megjelenítése
: Ha be van jelölve, a Scrivener, Fountain, Word és CriticMarkup dokumentumokban készített megjegyzések kiemelve jelennek meg az előnézetben. Törölje a jelölést a teljes elrejtéshez. Ezek a {% appmenu Gear, Proofing ({{ctrl}}{{cmd}}C)%} menüből egy dokumentum olvasása közben is átkapcsolhatók.
: Ha a megjegyzések engedélyezve vannak, a megjegyzések és lábjegyzetek az oldalsávon jelennek meg. Ha egy megjegyzés fölé viszi az egeret, az arra mutat, hogy a megjegyzés hol található a dokumentumban.

#### DocC [docc]

[(Információ a DocC támogatásról)](DocC_Support.html)

DocC képhivatkozások feloldása
: A `.docc` dokumentációkatalógusban oldja meg a kiterjesztések nélküli `![](ImageName)` hivatkozásokat a `Resources` katalógus mappájában található képekre, beleértve a `~dark` és `@2x` változatokat.

Sötét és @2x képváltozatok feloldása
: A (`images/icon.png`) fájlkiterjesztésű helyi képeknél észleli a `~dark` és `@2x` kísérőfájlokat ugyanabban a mappában, és érzékeny `<picture>` jelölést bocsát ki. Bármilyen Markdown vagy HTML dokumentumban működik, nem csak a DocC katalógusokban. Lásd: [Képváltozatok](Image_Variants.html).

#### Hookmark [hookmark]

A hook:// URL-ek feloldása képekben és linkekben
: A megjelölt be tudja olvasni a Hookmark által létrehozott URL-eket, és feloldja azokat a lemezen lévő elérési útjukra.

#### Leanpub/GitBook [leanpubgitbook]

Leanpub támogatás engedélyezése
: A `Book.txt` nevű fájlokat indexfájlként értelmezi, és speciális Leanpub szintaxist kezel.

Engedélyezze a GitBook támogatást
: A `SUMMARY.md` nevű fájlokat indexfájlként értelmezi a GitBook dokumentációhoz.

#### Markdownifier [markdownifier]

Használjon beépített hivatkozásokat
: A Markdownifier által létrehozott Markdown dokumentumok inline hivatkozásokat használnak hivatkozási hivatkozások helyett.

#### MarsEdit [marsedit]

Bejegyzés címe Markdown fejlécként (h1)
: Használja a kiválasztott bejegyzés címét Markdown fejlécként.

A metaadatok megjelenítése táblázatként
: Ha engedélyezve van, a metaadatok, például a kategóriák és a címek Markdown táblázatként jelennek meg az előnézetben.

#### Mappák [folders]

Csak ezeket a bővítményeket tekintse meg
: Mappa megnyitásakor a Megjelölt a legutóbb módosított dokumentumot keresi, alapértelmezés szerint a következő kiterjesztéssel: `md`, `mmd` és `html`. Az itt található lista felülírja az alapértelmezettet.

#### Scrivener [scrivener]

[(Információ a Scrivener támogatásáról)](Scrivener_Support.html)

Tartalmazza a dokumentumok címét Markdown fejlécként
: Az oldalak és a beágyazott oldalak címének elemzése hierarchikus Markdown fejlécek létrehozásához.

Ha hiányzik, adja hozzá a fordítási metaadatokat (cím, szerző).
: Ha egy Scrivener projektnek nincs `metadata` dokumentuma vagy meglévő MultiMarkdown fejléce, fűzze hozzá a Címet és a Szerzőt a projekt fordítási beállításaiból (`Settings/compile.xml`).

Nyissa meg a .scriv fájlokat a Scrivenerben, amikor a Marked alkalmazásban van megnyitva
: Ha egy Scrivener dokumentumot a Marked alkalmazásban nyit meg, akkor automatikusan nyissa meg a Scrivenerben is.

#### Szó [word]

Változáskövetés átalakítása <-> CriticMarkup
: Ha engedélyezve van, a Word dokumentumok változáskövetése importáláskor CriticMarkup formátumba, a DOCX fájlok exportálásakor pedig a CriticMarkup Word változáskövetéssé.

#### Mind Maps/Outlines [MindMapsOutlines]

Beágyazás sellő gondolattérképként
: Minden jelölőnégyzet egy mellékelt formátumot vezérel. Ha **be** van kapcsolva, a mellékelt fájl Hableány gondolattérkép-diagrammá alakul (tidy-fa-layout). Ha **ki**, a Marked az adott formátum alternatíváját használja.
: **Mind maps** — iThoughts X (.itmz), MindManager (.mmap), FreeMind (.mm). Ha be van kapcsolva: Mermaid gondolattérkép. Ha ki van kapcsolva: az iThoughts beágyazza előnézeti képét; A MindManager és a FreeMind beágyazott Markdown listákká konvertál.
: **OPML fájlok** (.opml). Ha be van kapcsolva: Mermaid gondolattérkép. Ha ki: beágyazott Markdown lista.
: **OmniOutliner körvonalai** (.ooutline). Ha be van kapcsolva: Mermaid gondolattérkép. Ha ki van kapcsolva: beágyazott Markdown lista (vagy ellenőrző lista, ahol van).
: **Kerékpár körvonalai**. Ha be van kapcsolva: Mermaid gondolattérkép. Ha ki: beágyazott Markdown lista.