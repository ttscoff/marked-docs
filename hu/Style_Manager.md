<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Stíluskezelő központosított felületet biztosít az összes adat kezeléséhez
beépített és egyedi stílusok. Teljes ellenőrzést biztosít a felett, hogy melyik
A stílusok a menükben, sorrendjükben, billentyűparancsokban és egyebekben jelennek meg.

## A Stíluskezelő megnyitása

A Stíluskezelő megnyitásához kattintson a **Stílusok kezelése…** gombra a {% prefspane Style %}
ablaktáblát, vagy használja az {% appmenu Style, Manage Styles (~@$m) %} lehetőséget. A CSS-fájlokat közvetlenül a beállítások ablakba is húzhatja --- Megjelölve
importálja őket, nyissa meg a Stíluskezelőt, és válassza ki az újonnan hozzáadott sort
te.

![Stíluskezelő][img-style-manager]

  [img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center

## A stílustáblázat

A Stíluskezelő az összes stílust egy rendezhető táblázatban jeleníti meg, amely keveredik
beépített és egyedi stílusok zökkenőmentesen. A táblázat minden sora több sort tartalmaz
oszlopok:

### Engedélyezve jelölőnégyzet

Az **Engedélyezve** jelölőnégyzet azonnal hozzáadja vagy eltávolítja a stílust a Stílusból
menüt, az Alapértelmezett stílus előugró ablakot és a billentyűparancsokat. Ha letilt egy stílust,
el van rejtve a menükben, de a Stíluskezelőben marad az egyszerű újraaktiválás érdekében.

Ha letiltja az aktuálisan aktív stílust, a Marked automatikusan átvált a
következő elérhető engedélyezett stílus.

### Név oszlop

A **Név** oszlopban megjelenik a stílus megjelenített neve. Ezt a nevet szerkesztheti
inline közvetlenül rákattintva; A változtatások továbbra is fennállnak, és minden menüre kiterjednek
ahol a stílus megjelenik. Ez különösen hasznos az egyéni stílusok esetében, ahol Ön
esetleg leíróbb nevet szeretne, mint a fájlnév.

A beépített stílusok zárolt nevekkel rendelkeznek, amelyeket nem lehet szerkeszteni. Testreszabásához a
beépített stílus nevét, először másolja le a szerkeszthető másolat létrehozásához.

### Forrás oszlop

A **Forrás** oszlop jelzi, honnan származik a stílus:

- **Beépített**: Stílusok, amelyek a Marked funkcióval vannak ellátva, és az alkalmazásban tárolódnak
  köteg
- **Egyéni**: A meghajtón lévő CSS-fájlokból hozzáadott stílusok
- **Duplikált**: Stílusok, amelyeket egy másik stílus sokszorosításával hoztak létre (akár beépített
  vagy egyéni)

### Műveletek oszlop

Minden sor tartalmaz egy **Műveletek** köteget az adott stílus kezeléséhez szükséges gombokkal:

**Szerkesztés**: Megnyitja a CSS-fájlt az alapértelmezett szerkesztőben. A beépített stílusok nem lehetnek
közvetlenül szerkesztett -- először meg kell másolnia őket, hogy szerkeszthető másolatot hozzon létre.

**Duplikáció**: Létrehoz egy másolatot a stílusról és egy új CSS-fájlt a lemezen. A
A duplikátum közvetlenül az eredeti stílus alatt jelenik meg a táblázatban. Ez van
a beépített stílusok testreszabásának ajánlott módja.

**Reveal**: Megjeleníti a CSS-fájlt a Finderben, megkönnyítve a fájl megtalálását
a hajtásod. Ez a gomb csak a fájl elérési úttal rendelkező egyéni stílusokhoz érhető el.

**Törlés**: Eltávolítja a stílust a Megjelölt közül. Egyedi stílusok esetén megadjuk
csak a hivatkozás eltávolítása (a CSS-fájl megtartása), vagy az áthelyezés lehetősége
a CSS-fájlt a kukába. A beépített stílusokat nem lehet törölni, de igen
letiltva.

**Visszaállítás**: A beépített stílusok esetén ez a gomb visszaállítja a stílust
alapértelmezett állapot, ha módosították. Ez a gomb csak a következőnél látható
beépített stílusok.

## Stílusok átrendezése

A sorok átrendezhetők húzással. Egyszerűen húzzon egy stílussort egy újba
helyet a táblázatban. Az itt beállított sorrend a következőket hajtja:

- A Stílus menü sorrendje a Marked menüiben
- Billentyűparancs-hozzárendelések (`⌘1`–`⌘9` az első kilenc engedélyezett stílushoz,
  `⌥⌘1`–`⌥⌘0` a következő tízre, és így tovább)

Húzza a stílusokat a kívánt billentyűkombinációkba
elfoglalni.

## Stílusok hozzáadása

Többféleképpen is hozzáadhat új egyéni stílusokat a Stíluskezelőhöz:

### Hozzáadás gomb

Kattintson az **Új stílus hozzáadása** gombra a fájlválasztó megnyitásához
ahol kiválaszthat egy vagy több CSS-fájlt importálni. A kiválasztott fájlok lesznek
hozzáadva a Stíluskezelőhöz, és alapértelmezés szerint engedélyezve van.

### Fogd és vidd

A CSS-fájlokat közvetlenül a Stíluskezelő ablakba húzhatja. Amikor húzod
fájlokat az ablak felett, egy fedvény jelenik meg az "Egyéni stílus hozzáadása" felirattal (vagy
„N egyéni stílus hozzáadása” több fájlhoz). Húzza el a fájlokat az importáláshoz.

A CSS-fájlokat a táblázat meghatározott helyeire is húzhatja – a cseppre
jelző mutatja, hogy hova kerül az új stílus beszúrása, lehetővé téve a vezérlést
importálás és pozicionálás egy műveletben.

A CSS-fájlok áthúzása a {% prefspane Style %} beállítások panelre szintén megteszi
importálja őket, és automatikusan nyissa meg a Stíluskezelőt.

## Élő előnézet

A Stíluskezelő jobb oldali ablaktáblája a kiválasztottak élő előnézetét jeleníti meg
stílusban. Az előnézet átfogó mintadokumentumot jelenít meg címsorokkal,
listák, táblázatok, kódblokkok, idézőjelek és egyéb gyakori Markdown elemek,
mind a kiválasztott stílus tényleges CSS-jével stílusozva.

Az előnézet a CSS-fájlt közvetlenül a lemezről használja, így az Ön által végzett módosítások
a külső szerkesztő azonnal frissül az előnézetben. Ez megkönnyíti a
valós időben láthatja a változtatásokat, miközben egyéni stílusokat fejleszt.

### Sötét mód előnézete

Az előnézet feletti jelölőnégyzet lehetővé teszi a világos és a sötét mód közötti váltást
előzetesek. Ez hasznos annak teszteléséhez, hogyan néznek ki a stílusok mindkét megjelenési módban,
különösen, ha olyan stílusokat hoz létre, amelyek alkalmazkodnak a rendszer megjelenéséhez.

## Billentyűparancsok

A Stíluskezelő a táblázat alatt egy jelmagyarázatot jelenít meg, amely bemutatja a billentyűzet használatát
parancsikonok hozzá vannak rendelve. Az első kilenc engedélyezett stílus megkapja a {% kbd cmd 1 %}-t
{% kbd cmd 9 %} ({% kbd cmd 0 %} fenntartva), a következő tíz {% kbd opt cmd 1 %}-t {% kbd opt cmd 0 %}-ig kap, és így tovább. A hozzárendelt billentyűparancsokat bármelyik Előnézet Stílus előugró menüjében láthatja.

## Letiltott stílusok szűrése

Az ablak alján található jelölőnégyzet lehetővé teszi a letiltott állapotok megjelenítését vagy elrejtését
stílusok. Ha nincs bejelölve, csak az engedélyezett stílusok jelennek meg, ami megkönnyíti a beállítást
összpontosítson és rendezze át aktív stílusait. Ha be van jelölve, az összes stílus (engedélyezett és letiltott)
megjelennek, lehetővé téve a teljes stílusgyűjtemény kezelését.

## Beépített stílusok visszaállítása

Az ablak alján található **Az összes beépített stílus visszaállítása** gomb
visszaállítja az összes beépített stílust az alapértelmezett állapotába. Ez hasznos, ha
letiltotta a beépített stílusokat, és szeretné újra engedélyezni őket, vagy ha vissza szeretné állítani őket
a beépített stílusokon végzett bármilyen módosítás.

## Tippek

- **Rendezés gyakoriság szerint**: Húzza a leggyakrabban használt stílusokat a tetejére, hogy megadja
  nekik a legegyszerűbb billentyűparancsok ({% kbd cmd 1 %}, {% kbd cmd 2 %} stb.)

- **Letiltás törlés helyett**: A nem használt stílusok törlése helyett,
  tiltsa le őket. Kimaradnak az útból, de szükség esetén elérhetőek maradnak
  őket később.

- **Kísérletezéshez használjon másodpéldányt**: Másoljon stílust, mielőtt szaktárgyat készítene
  megváltozik, így mindig visszatérhet az eredetihez.

- **Előnézet szerkesztés közben**: CSS szerkesztése közben tartsa nyitva a Stíluskezelőt
  fájlokat, hogy a módosítások valós időben frissüljenek az előnézeti panelen.

- **Kötegelt importálás**: Egyszerre több CSS-fájlt is kiválaszthat a
  Hozzáadás gombot, vagy húzzon több fájlt az összes importálásához egy műveletben.