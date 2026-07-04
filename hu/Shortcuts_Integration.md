<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Megjelölt natív **Parancsikonokat** tartalmaz (App Intents) a fájlok megnyitásához, az előnézeti stílusok megváltoztatásához és a dokumentumok exportálásához. Ezek a műveletek a Parancsikonok alkalmazásban jelennek meg, ha a **Megjelölt** kifejezésre keres, és **macOS 13 (Ventura)** vagy újabb rendszeren érhetők el.

A teljes objektummodellel rendelkező szkript alapú automatizáláshoz lásd: [AppleScript támogatás](AppleScript_Support.html). A héjból származó URL-alapú munkafolyamatokhoz lásd: [URL-kezelő](URL_Handler.html).

## Műveletek keresése

1. Nyissa meg a **Parancsikonok** alkalmazást.
2. Hozzon létre egy új parancsikont, vagy szerkesszen egy meglévőt.
3. Keresse meg a műveletkönyvtárban a **Megjelölt** kifejezést.

A műveletek a **Dokumentumok** és **Exportálás** csoportokba sorolhatók. A Marked olyan Siri-kifejezéseket is regisztrál, mint a „Fájl exportálása megjelölve” és „Megnyitás megjelölve” funkcióval a gyors parancsikonokhoz.

## A műveletek áttekintése

| Akció | Cél |
| --- | --- |
| **Fájl megnyitása megjelölt helyen** | Nyisson meg egy Markdown- vagy szövegfájlt egy előnézeti ablakban. |
| **Előnézeti stílus beállítása** | Módosítsa a megnyitott dokumentum előnézeti témáját (vagy először nyissa meg a fájlt). |
| **Fájl megnyitása és exportálása** | Nyisson meg egy fájlt, majd exportálja egy másik formátumba. |
| **Export dokumentum** | Megnyitott dokumentum exportálása (elülső ablak vagy egy adott fájl). |
| **Nyitott dokumentumok exportálása** | Exportáljon minden olyan dokumentumot, amely jelenleg a Megjelölt mappában van megnyitva. |

Minden exportálási művelet visszaadja az exportált fájlt (vagy fájlokat) Parancsikonok **Fájl** kimenetként, így átadhatja őket a következő lépésnek (Mail, Finder, másik alkalmazás).

## Nyissa meg a fájlt a Megjelölt helyen

**Paraméter:** **Fájl** – a megnyitandó dokumentum (a Finderből, a Share Sheet-ből vagy egy korábbi Parancsikon-lépésből).

Megjelölve megnyitja a fájlt egy előnézeti ablakban. Használja ezt, ha meg szeretné tekinteni az előnézetet vagy szerkeszteni szeretné a Marked alkalmazásban, mielőtt bármi mást tenne.

## Állítsa be az előnézeti stílust

**Paraméterek:**

- **Stílus** -- stílus előnézete egy választóból (ugyanazok a nevek, mint az előnézeti stílus menü és a Stíluskezelő).
- **Fájl** (nem kötelező) -- egy adott fájl. Ha kihagyja, a Marked az elülső dokumentumot használja. Ha a fájl még nincs megnyitva, a Marked először azt nyitja meg.

A stílus beállítása újratölti az előnézetet az adott témával (ugyanúgy, mint a stílus kiválasztása az előnézeti stílus menüből).

## Műveletek exportálása

Az exportálási műveletek ugyanazokkal az alapvető beállításokkal rendelkeznek:

| Paraméter | Leírás |
| --- | --- |
| **Formátum** | Markdown, HTML, oldalszámozott PDF, folyamatos PDF, EPUB, DOCX, ODT, RTF, RTFD, TextBundle, TextPack vagy OPML. |
| **Profil** (nem kötelező) | Mentett exportprofil innen: {% prefspane Export %}. |
| **Stílus** (opcionális) | Exportálás előtt alkalmazandó előnézeti stílus (teljes előnézeti újratöltés). |
| **Oldalméret** (opcionális) | Nyomtassa ki az oldalméret nevét, például `A4` vagy `Letter`. |
| **Margók** (nem kötelező) | Margó gyorsírás (lásd lent). |
| **Betűméret** (opcionális) | Az alap betűméret a PDF-exportálási pontokban, például `14` vagy `12pt`. |
| **Kimeneti fájl** / **Kimeneti mappa** (opcionális) | Cél útvonal. Ha kihagyja, a Marked a megfelelő kiterjesztéssel ír a forrásfájl mellé. |

**Jegyzetek**

- A **lapszámozott PDF** ugyanazt a nyomtatási elrendezési folyamatot használja, mint az {% appmenu File, Export As, Save PDF (Paginated) %}. Nem érhető el nyers HTML előnézeti dokumentumokhoz.
- A **HTML** exportálás a megjelenített előnézetet használja (amit a WebView-ban lát), nem pedig a nyers Markdown forrásfájlt.
- A **folyamatos PDF** rögzíti az aktuális előnézeti WebView elrendezést.
- A **Betűméret** lehetővé teszi ugyanazt az egyéni exportálási/nyomtatási betűméret beállítást a {% prefspane Export %}-től. Nem érinti a Fountain dokumentumokat.

### Nyissa meg és exportálja a fájlt

A legjobb a Finder munkafolyamatokhoz: válasszon ki egy Markdown fájlt, nyissa meg a Marked alkalmazásban, és exportálja egy lépésben.

**Paraméterek:** **Fájl** (kötelező), valamint a fenti exportálási lehetőségek.

Példa a felhasználásra: egy gyors művelet, amely fájlokat vesz a Finderből, és exportál **lapszámozott PDF-et** a kiválasztott profillal és stílussal.

### Dokumentum exportálása

Exportáljon egy dokumentumot, amely **már meg van nyitva** a Megjelölt helyen.

**Paraméterek:**

- **Fájl** (nem kötelező) -- egy adott megnyitott fájl. Ha kihagyja, a Marked exportálja az elülső dokumentumot.
- Exportálási beállítások és **Kimeneti fájl** a fentiek szerint.

Ezt akkor használja, ha a Megjelölt már fut, és a fájl újbóli megnyitása nélkül szeretné exportálni az aktuális előnézetet.

### Nyitott dokumentumok exportálása

**Minden** jelenleg megjelölt előnézeti dokumentum exportálása.

**Paraméterek:**

- **Formázás** és exportálási lehetőségek (profil, stílus, oldalméret, margók, betűméret).
- **Kimeneti mappa** (opcionális) - az exportált fájlok könyvtára. Ha kihagyja, minden fájl a forrásdokumentuma mellé kerül exportálásra.

Hasznos kötegelt exportáláshoz több fejezet vagy megjegyzés áttekintése után a Marked alkalmazásban.

## Margó gyorsírás

Ha a **Margins** be van állítva egy exportálási műveletnél, használjon 1-4 méretű karakterláncot. Mértékegységek: `in`, `cm`, `mm`, `pt` vagy `"` hüvelyk esetén. Az egység nélküli számot pontként kell kezelni.

| Érték | Jelentése |
| --- | --- |
| `1in` | Minden oldal |
| `1in 2in` | Felül és alul `1in`, balra és jobbra `2in` |
| `1in 2in 1in` | Felül `1in`, bal és jobb `2in`, lent `1in` |
| `1in 2in 1in 2in` | Felül, jobb, lent, bal |

Ez megegyezik az [AppleScript](AppleScript_Support.html#with-options-properties-record) exportrekordok `margins` kulcsával.

## Példa munkafolyamatokra

### Finder fájl PDF-be

1. **Fájl megnyitása és exportálása**
2. **Fájl** – bemenet a Share Sheet vagy a Finder gyorsműveletből.
3. **Formátum** -- Oldalszámozott PDF.
4. **Stílus** -- opcionális téma (például Amblin).
5. **Profil** -- opcionális mentett exportprofil.
6. **Kimeneti fájl** -- opcionális; hagyja üresen, hogy `filename.pdf`-t írjon a forrás mellé.

### Exportálja azt, ami a Megjelöltben nyitva van

1. **Export dokumentum**
2. Hagyja üresen a **Fájl** mezőt az elülső ablak használatához.
3. Válassza a **Formátum** lehetőséget és az opcionális profilt vagy stílust.

### Nyitott dokumentumok kötegelt exportálása

1. **Nyitott dokumentumok exportálása**
2. Válassza a **Formátum** lehetőséget (például EPUB).
3. Opcionálisan állítsa be a **Output Folder** beállítást, hogy az összes exportált anyagot egy könyvtárba gyűjtse.

### Stílus, majd exportálás (két lépés)

1. **Előnézeti stílus beállítása** -- válasszon stílust (opcionálisan célozzon meg egy adott **fájlt**).
2. **Dokumentum exportálása** -- ugyanaz a fájl vagy elülső dokumentum, a kívánt **formátummal**.

A **Stílust** közvetlenül is átadhatja egy exportálási műveletnél; A megjelölve alkalmazza a témát, és az exportálás előtt megvárja az előnézet újratöltését.

## Exportálási útvonalak és homokozó

- Ha a **Kimeneti fájl** vagy a **Kimeneti mappa** ki van hagyva, a Marked a forrásdokumentum mellé ír.
- A Megjelölt köztes mappákat hozhat létre, ha az exportálási útvonal **a megnyitott dokumentum mappájában** belül van.
- A dokumentum mappáján kívülre történő exportáláshoz írható elérési út szükséges, amelyhez a Megjelölt hozzáférhet (mentett dokumentum helye, biztonsági hatókörű könyvjelzők vagy a Megnyitás párbeszédpaneleken megadott mappák).

Ugyanezen sandbox-szabályokért lásd: [AppleScript támogatás](AppleScript_Support.html#export-paths-and-sandboxing).

## Legacy `convert_to` akció

Az AppleScript szótár továbbra is megjeleníti a **`convert_to`**-t a Markdown szöveg vagy fájlok konvertálásához nyitott előnézet nélkül. A natív parancsikonok fenti műveletei előnyösek: megfelelően megnyitják a dokumentumokat, megvárják az előnézeti betöltést, és támogatják a lapszámozott PDF-exportálást aszinkron módon.

Lásd: [Parancsikonok és `convert_to` az AppleScript támogatásban](AppleScript_Support.html#shortcuts-and-convert_to) a régebbi parancs részleteiért.

## Hibaelhárítás: A műveletek nem jelennek meg a parancsikonokban

Parancsikon indexek **egy** Megjelölt telepítési csomagonkénti azonosító (`com.brettterpstra.marked`). A **legmagasabb build számmal** (`CFBundleVersion`) rendelkező példányt részesíti előnyben, nem feltétlenül az Xcode-ban beépített alkalmazást.

Ha a Megjelölve nem jelenik meg az **Alkalmazások** alatt a Parancsikonok műveletkönyvtárában:

1. Soroljon fel minden másolatot a lemezen:
   ``` bash
   mdfind 'kMDItemCFBundleIdentifier == "com.brettterpstra.marked"'
   ```
2. Távolítsa el vagy nevezze át az elavult másolatokat (például egy régi `Marked.app`-t az Asztalon vagy a `/Applications`-ben, amelyet egy buildből másoltak **parancsikonok metaadatai nélkül).
3. Futtassa azt a buildet, amelyet használni szeretne a parancsikonoknak (Xcode **Run**, vagy nyissa meg közvetlenül a `.app`-t a DerivedData-ban).
4. Lépjen ki, és nyissa meg újra a **Parancsikonok** alkalmazást.

A parancsikonokat tartalmazó build a következőt tartalmazza: `Contents/Resources/Metadata.appintents`. Ellenőrizheti:

```bash
ls "/path/to/Marked.app/Contents/Resources/Metadata.appintents"
```

Indításkor a Marked naplózza a `[MKShortcuts] Registering App Intents`-t a Console.appban, amikor a regisztráció fut (macOS 13+).

## Hibakeresés

Engedélyezze a **Hibakeresési módot** a {% prefspane Advanced %}-ben. A megjelölt naplók exportálási lépései Info szinten a `[AppleScript]` előtaggal a Console.app alkalmazásban és a Marked naplónézőjében (az exportálási folyamat meg van osztva az AppleScripttel).

## Hibák

Gyakori üzenetek, amikor egy művelet sikertelen:

- Nem érhető el megjelölt dokumentum (nincs megnyitva és nincs megadva fájl).
- Ez a fájl nincs megnyitva a Megjelölt módban (használja a **Fájl megnyitása** vagy a **Fájl megnyitása és exportálása** lehetőséget).
- Ismeretlen exportprofil vagy előnézeti stílusnév.
- Időtúllépés várva az előnézet betöltésére vagy újratöltésére.
- Exportálási útvonalengedélyezési hibák vagy oldalszámozott PDF generálási hiba.