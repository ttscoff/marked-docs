<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Quick Open gyors hozzáférést biztosít a megnyitott dokumentumokhoz és a legutóbbi fájlokhoz.

## Gyors megnyitás [opening-quick-open]

A Gyors megnyitás panelt a {% kbd shift cmd O %} gombbal vagy az {% appmenu File, Quick Open %} menüből érheti el. A panel lebegő ablakként jelenik meg az aktuális dokumentum felett, lehetővé téve a gyors váltást a megnyitott dokumentumok vagy a legutóbbi fájlok között.

![Quick Open Panel][qo]

[qo]: images/quick-open-800.jpg @2x width=800

## Dokumentumrészek [document-sections]

A Gyors megnyitás panel áttekinthető szakaszokba rendezi a dokumentumokat:

### Nyissa meg a dokumentumokat [open-documents]

A lista tetején az összes jelenleg megnyitott dokumentum látható. A dokumentumokat az ablakuk alapján vizuálisan csoportosítják:

- **Füllel ellátott ablakok**: A füles ablakokban lévő dokumentumok alcíme az „Ablak X lappal” felirattal, jelezve, hogy hány lap van az adott ablakcsoportban
- **Önálló ablakok**: Az egyes ablakokban lévő dokumentumok alcíme az „Ablak”

Minden megnyitott dokumentum a következőket jeleníti meg:
- A dokumentum fájlneve fő címként
- Az ablak csoportosítási információi alcímként
- Egy dokumentum ikon

### Legutóbbi dokumentumok [recent-documents]

A megnyitott dokumentumok alatt a "Legutóbbi dokumentumok" elválasztó választja el a listát. A legutóbbi dokumentumok szakasz legfeljebb 10 legutóbb megnyitott fájlt jelenít meg, amelyek jelenleg nincsenek megnyitva. Minden legutóbbi dokumentum a következőket jeleníti meg:

- A dokumentum fájlneve fő címként
- "Legutóbbi" alcímként
- Egy dokumentum ikon

### Nyissa meg az Egyéb lehetőséget [open-other]

A lista alján található "Másik megnyitása..." lehetőség lehetővé teszi a szabványos macOS-fájlválasztó megnyitását bármely fájl kiválasztásához. Ez az opció a következőket jeleníti meg:

- "Open Other…" főcímként
- "Fájl vagy mappa megnyitása" feliratként
- Egy mappa ikon

## Keresés és szűrés [search-and-filter]

Írja be a panel tetején található keresőmezőt a lista valós idejű szűréséhez. A keresés a következővel egyezik:

- Dokumentum fájlnevek
- Teljes fájl elérési utak

Gépelés közben a lista azonnal frissül, és csak a megfelelő dokumentumokat jeleníti meg. A "Másik megnyitása..." lehetőség mindig látható marad a szűrt eredmények alján.

## Navigáció billentyűzettel [keyboard-navigation]

Navigáljon a Gyors megnyitás panelen a billentyűzet segítségével:

- **↑/↓ nyílbillentyűk**: Lépés fel és le a listában
- **Vissza**: A kiválasztott dokumentum vagy opció megnyitása
- **Kilépés**: Zárja be a Gyorsnyitás panelt
- **Parancs (⌘)**: Tartsa lenyomva a fájl elérési útjainak megjelenítéséhez (lásd lent)

## Fájlútvonalak megtekintése [viewing-file-paths]

Tartsa lenyomva a **Command (⌘)** billentyűt, miközben a Gyors megnyitás panel nyitva van, hogy megtekinthesse az egyes dokumentumok teljes fájlútvonalát a feliratterületen. A kezdőkönyvtár elérési útjai a `~` rövidítéssel jelennek meg (pl. `~/Documents/file.md`). Engedje fel a Command billentyűt, hogy visszatérjen a normál nézethez, amely az ablakok csoportosítását vagy a "Legutóbbi" információkat mutatja.

Ez különösen akkor hasznos, ha több azonos nevű fájl van nyitva, vagy ha ellenőrizni kell egy dokumentum pontos helyét.

## Dokumentumok megnyitása [opening-documents]

- **Nyitott dokumentumok**: Ha egy megnyitott dokumentumot kiválaszt, az ablaka az előtérbe kerül, és átvált a dokumentum lapjára, ha füles ablakban van.
- **Legutóbbi dokumentumok**: Ha egy legutóbbi dokumentumot választ ki, az új ablakban nyílik meg, vagy lapként jelenik meg (a „Dokumentumok megnyitása lapokon” beállításától függően a {% prefspane General %}-ben)
- **Open Other...**: Ha ezt a lehetőséget választja, megnyílik a szabványos macOS fájlválasztó párbeszédpanel