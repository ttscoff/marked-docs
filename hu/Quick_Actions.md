<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Gyors műveletek paletta egy kereshető parancsindító a Marked számára. Összegyűjti a főmenüsor és az előnézeti **fogaskerék menü** műveleteit, valamint azokat a csak előnézeti billentyűparancsokat, amelyek nem jelennek meg a menükben (például **Automatikus görgetés**). Használja, ha tudja, mit szeretne csinálni, de nem emlékszik, melyik menü tartalmazza.

## A Gyorsműveletek paletta megnyitása

Nyissa meg a palettát a {% kbd shift cmd P %} vagy az {% appmenu File, Quick Actions… %} gombbal. A panel lebegő ablakként jelenik meg az aktuális dokumentum felett.

Nyomja meg újra ugyanazt a parancsikont, vagy nyomja meg az **Escape** gombot a paletta bezárásához. Ha a paletta már nyitva van, akkor a menü **Gyorsműveletek…** parancsával is bezárja azt.

## A parancsikon testreszabása

Az alapértelmezett parancsikon a {% kbd shift cmd P %}. A módosításhoz nyissa meg a {% prefspane General %} elemet, és rögzítsen egy új kombinációt a **Akciópaletta megnyitása** alatt a **Parancsikonok** részben.

A **Megjelölt aktiválása** és **Első ablak felemelése** lehetőségekkel ellentétben a Gyorsműveletek parancsikon csak akkor működik, ha a Megjelölt az aktív alkalmazás. Frissíti a {% appmenu File, Quick Actions… %} menüparancsot, hogy megfeleljen a beállításnak.

## Keresés és szűrés

Írja be a panel tetején található keresőmezőt a parancsok valós idejű szűréséhez. A párosítás homályos és megbocsátó:

- A szórend nem számít (`view source` egyezik a **Forrásnézet váltása**)
- A kezdőbetűk jól működnek (`sv` megfelel a **Forrásnézet**)
- Az összecsukott egyezés szóközök nélkül találja meg a parancsokat (`akdoc` egyezés **Kérdezzen a dokumentumról**)

Minden eredmény a parancs nevét mutatja a bal oldalon, és a billentyűparancsát (ha elérhető) a jobb oldalon szürkén. Egyes parancsok navigációs útvonalat is mutatnak (például `Preview › Autoscroll`), ha a művelet egy almenüből vagy az előnézeti motorból származik.

## Mi jelenik meg a listában

A paletta a következőket tartalmazza:

- **Menüparancsok** a fő menüsorról, beleértve a dinamikus menüket, például a **Stílus**, **Előzmények** és a megnyitott **Ablak** lapokat
- **Fogaskerék menü** parancsok az előnézeti ablakból
- **Előnézeti billentyűparancsok** az előnézeti billentyűzettérképről (ugyanazok a parancsok, mint az előnézeti súgó HUD-ban), beleértve a navigációt, az automatikus görgetést, a könyvjelzőket, a keresést és más, csak előnézeti műveleteket

Ha ugyanaz a parancs több helyen is megjelenik, a Marked a legrövidebb menüútvonalat mutatja, és egyesíti a parancsikonok információit a duplikátumokból.

## Navigáció billentyűzettel

Navigáljon a Gyorsműveletek palettán teljes egészében a billentyűzetről:

- **↑/↓ nyílbillentyűk**: Lépés a szűrt listán
- **Return**: Futtassa a kiválasztott parancsot
- **Escape**: A paletta bezárása
- **⌘-billentyűparancsok**: Zárja be a palettát, és futtassa a megfelelő menüparancsot (például nyomja meg az {% kbd cmd U %} billentyűt a **Forrásnézet átváltása** futtatásához, ahelyett, hogy kijelölné a listában)

Az egyszerű gépelés (a Command billentyű nélkül) szűri a keresőmezőt. Csak előnézeti egygombos billentyűparancsok, például `s` az automatikus görgetéshez, szűrik a listát; nyomja meg a **Return** gombot a kiválasztott parancs futtatásához.

## Parancsok futtatása

A menüparancs kiválasztása ugyanúgy elküldi azt, mint a menüből történő kiválasztása, beleértve a dinamikus és a fogaskerék menüelemeket.

Az **előnézeti parancsikon** kiválasztása az aktív előnézetben futtatja a kapcsolódó műveletet (például az automatikus görgetés váltása vagy a következő fejlécre ugrás). Ezek a parancsok megnyitott dokumentumot igényelnek előnézettel; ha nem érhető el előnézet, a paletta továbbra is megnyílik, de a csak előnézeti műveleteknek nincs hatása.

A kapcsolódó fájlváltáshoz lásd: [Gyors megnyitás](Quick_Open.html). A teljes előnézeti billentyűzetreferenciaért lásd a [Billentyűparancsok](Keyboard_Shortcuts.html) részt, vagy nyomja meg a {% kbd h %} gombot az előnézetben a súgó HUD megjelenítéséhez.