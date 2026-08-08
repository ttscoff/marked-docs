<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Ez az oldal leírja, hogyan mozoghat a hosszú előnézetek között: a [Tartalomjegyzék](#tartalomjegyzék), [gyorskeresés](#gyorskeresés), [könyvjelzők](#bookmarks-and-mini-map) és a [Mini térkép](#minimap). A mindenhol érvényes görgetési billentyűparancsokhoz (például {% kbd j %}/{% kbd k %}) tekintse meg a [Billentyűzet navigáció](Interface_Features.html#keyboardnavigation) részt az [Interfész jellemzői](Interface_Features.html) alatt.

## Tartalomjegyzék [table-of-contents]

![][8]

   [8]: images/tableofcontentsbutton.jpg @2x width=740px height=238px class=center

Ha a dokumentumban fejlécek találhatók, egy lista gomb jelenik meg az eszköztáron. Kattintson rá a tartalomjegyzék kibontásához; kattintson egy címsorra, hogy az előnézet adott részéhez ugorjon. A {% kbd j %}/{% kbd k %} (le/fel) gombbal lépkedhet a listában, a {% kbd Enter %} vagy {% kbd o %} gombbal pedig a kiemelt fejlécre ugorhat.

**Szűrősáv:** Ha a tartalomjegyzék nyitva van, nyomja meg a {% kbd Space %} (szóköz) billentyűt az előre gépelés mező megnyitásához. Írja be a címsor nevének tetszőleges részét (A Jelölve TextMate-stílusú egyezést használ – például beírhatja minden szó első betűjét), majd nyomja meg a Tab ({% kbd ⇥ %}) vagy a lefelé mutató nyilat ({% kbd ↓ %}) a szűrt listán való mozgáshoz.

A {% kbd cmd T %} gomb megnyomásával a tartalomjegyzék is megnyitható (vagy bezárható).

Ha a ["Headlines Collapse Sections"](Interface_Features.html#collapsibleheadlines) engedélyezve van a {% prefspane General %}-ben, a Command billentyű lenyomva tartása, miközben egy elemre kattint a Tartalomjegyzékben, összecsukja vagy kibontja az adott szakaszt, szükség szerint megjelenítve a szülő szakaszokat.

Teljes képernyős módban a tartalomjegyzék rögzített oldalsávként jelenik meg előugró menü helyett. Ha ezt az elrendezést egy normál ablakos előnézetben szeretné használni, használja a teljes képernyős kapcsolót a TOC panel jobb alsó sarkában.

![Teljes képernyő váltása][12]

   [12]: images/tableofcontentsfullscreentoggle.jpg @2x width=740px height=238px class=center


A billentyűk tömörített listáját lásd: [Billentyűparancsok](Keyboard_Shortcuts.html#TableofContentsNavigation).

Lásd még a [Dokumentumnavigációs videót a YouTube-on](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

### Teljes képernyős mód a tartalomjegyzékhez [full-screen-mode-for-the-table-of-contents]

Ha a Megjelölt előnézeti ablak teljes képernyős, a Tartalomjegyzék rögzítve maradhat a bal oldalon az állandó navigáció érdekében. Továbbra is a {% kbd cmd T %}-vel vált; Ha a tartalomjegyzéken kívülre kattint, gyakran nem veti el azt ebben az elrendezésben.

Normál ablakban kattintson a TOC panel alján található ikonra, hogy oldalsávként rögzítse; kattintson az oldalsáv tetején lévő ikonra az előugró módba való visszatéréshez.

### A TOC megjelenési helyének testreszabása [customizing-where-the-toc-appears]

A tartalomjegyzék a [speciális szintaxis](Special_Syntax.html#tableofcontents) `<!--TOC-->` használatával beszúrható az exportált dokumentumba.

Az `max#` (például `<!--TOC max2-->`) hozzáadásával korlátozhatja, hogy hány címsorszint jelenjen meg.

## Gyors keresés [fast-search]

A **Gyors navigáció** a tartalomjegyzéket egyesíti a fókuszált szűrővel, így minimális gépeléssel ugorhat:

- Nyomja meg az előnézetben a {% kbd f %} gombot a tartalomjegyzék megnyitásához a **szűrőmezővel** (ugyanaz, mint a tartalomjegyzék megnyitása, majd a {% kbd Space %} megnyomása, további lépés nélkül).
- Írja be a címsor bármely részét; a lista a találatokra szűr.
- Ha csak egy címsor marad, a Return ({% kbd ↩ %}) megnyomásával egyenesen arra ugrik.
- Ha több címsor maradt, nyomja meg a Tab ({% kbd ⇥ %}) billentyűt a szűrőmező elhagyásához, mozgassa a {% kbd j %}/{% kbd k %} vagy a nyílbillentyűket, majd nyomja meg a {% kbd o %} vagy a Return ({% kbd ↩ %}) billentyűt a címsorra lépéshez és a tartalomjegyzék bezárásához.
- A Tab ismét visszaállítja a fókuszt a keresőmezőre.

> **Emlékeztető parancsikonra:** A tartalomjegyzék megnyitása és a {% kbd Space %} gomb megnyomása megnyitja a szűrősávot – akkor hasznos, ha a tartalomjegyzék már látható.

(A korábbi dokumentumok ezt "Fast Switcher"-nek nevezték; ez ugyanaz a funkció.)

## Könyvjelzők és minitérkép [bookmarks-and-mini-map]

Használja a {% appmenu Gear %} előnézeti menüt, és a {% kbd Tab %} ({% kbd ⇥ %}) elemet állítsa a dokumentumra a [search](Interface_Features.html#search) mellé a könyvjelzők elhelyezéséhez és újbóli megtekintéséhez lapozás közben.

### Könyvjelzők beállítása [setting-bookmarks]

Állítsa be a könyvjelzőket görgetési pozícióba a {% kbd shift 1 %}--{% kbd shift 9 %} használatával, és ugorjon vissza a {% kbd 1 %}--{% kbd 9 %} használatával. Használja a {% kbd n %} és {% kbd p %} karaktereket a következő/előző **dokumentumsorrendben**; {% kbd shift n %} és {% kbd shift p %} a következő/előző **numerikus** sorrendben.

A Stílus vagy az oldalméret módosítása áthelyezheti azt a helyet, ahol a könyvjelző megjelenik. A könyvjelzők ideiglenes áttekintési segédletként szolgálnak: nem maradnak fenn a dokumentum-munkamenetek között, de túlélik az előnézeti frissítéseket és szerkesztéseket.

**Címsor könyvjelzői:** Tartsa lenyomva az Option gombot, és nyomja meg a {% kbd opt 1 %}--{% kbd opt 9 %} gombot a nézetablak tetejéhez (vagy a teteje előtti utolsó címsor) lévő címsor könyvjelzővé tételéhez.

**Következő szabad hely:** {% kbd cmd D %} (vagy {% kbd \`\` %} bejelölés vim-felhasználók esetén) könyvjelzőt ad a következő elérhető számozott helyhez.

Nyomja meg a {% kbd 0 %} gombot a könyvjelzősáv kibontásához (a címsorok címei, ha elérhetők). Ha a [Mini térkép](#minimap) engedélyezve van, a {% kbd 0 %} egyidejűleg megjeleníti. Nyomja meg ismét az Escape vagy a {% kbd 0 %} billentyűt az összecsukáshoz.

Nyomja meg kétszer a {% kbd x %} gombot ({% kbd xx %}) az összes könyvjelző törléséhez.

Vannak [további előnézeti parancsikonok](Keyboard_Shortcuts.html); Nyomja meg a {% kbd h %} gombot az előnézetben a heads-up listához, vagy a {% kbd opt cmd K %} gombot a teljes hivatkozásért.

### Mini térkép [minimap]

Ha a Mini Map engedélyezve van a {% prefspane Preview %} beállításokban, a {% kbd 0 %} megnyitja a teljes dokumentum méretezett bélyegképét a könyvjelzősáv mentén. Kattintson a térkép tetszőleges részére a teljes előnézet görgetéséhez. A mentett könyvjelzők vízszintes vonalakként jelennek meg számokkal (és adott esetben címsorokkal).

Tartsa lenyomva a **Command** billentyűt, és mozgassa a Mini térképet a nagyított nagyítóhoz; tartsa lenyomva az **Option** gombot, és húzással görgessen, mintha a görgetősávot húzná.

A térkép újragenerálódik, amikor az ablak mérete vagy elrendezése megváltozik. Nagyon hosszú dokumentumok esetén a {% kbd 0 %} egyszeri megnyomása eltarthat egy ideig; A Jelölve elkerüli a Mini Map automatikus létrehozását a kezdeti betöltéskor, amíg Ön nem kéri.

Nyomja meg a {% kbd 0 %} vagy az Escape billentyűt a minitérkép bezárásához.

**Teljesítményre vonatkozó megjegyzés:** A térkép generálása rövid időre szüneteltetheti a hatalmas dokumentumok előnézetét; ez csak akkor fut, ha a térkép látható vagy átméretezés után.

### Nagyítás áttekintése (kapcsolódó) [zoom-overview-related]

A minitérkép nélküli szöveges léptékű áttekintésért lásd: [Nagyítás áttekintése](Zoom_Overview.html) ({% kbd z %}).