<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A rugalmasság kulcsfontosságú.

## Fogaskerék menü [gear-menu]

![][4]

   [4]: images/gearmenu.jpg @2x width=740px height=235px class=center

A Gear menü a menüsorban található funkciók többségét, valamint néhány előnézet-specifikus funkciót kínál. Csak kattintson a fogaskerékre az ablak jobb alsó sarkában a funkciók eléréséhez.

## Maradj a tetején [keep-on-top]

![][5]

   [5]: images/KeepOnTopPin.jpg @2x width=740px height=345px class=center

A bal alsó sarokban található lakat ikon az Előnézet ablakot előrehozza, és ott tartja (lebegteti), amikor más alkalmazásokra vált. A {% prefspane General %}-ban beállíthat egy átlátszóságot az ablakon, amely lehetővé teszi az ablak elhalványulását más alkalmazások használatakor.

Ez a funkció az {% kbd shift-opt-cmd-f %} gombbal is átkapcsolható.

## Ablakszintű alapértelmezett beállítások [window-level-defaults]

A {% prefspane General %} részben az „Új ablakok tartása a tetején” funkcióval beállíthatja, hogy az új ablakok mindig a többi ablak felett maradjanak, és/vagy beállíthatja, hogy az ablakok a tetejére emelkedjenek, amikor a kapcsolódó dokumentumot frissítik. A frissítésre beállított Windows nem „lopja el a fókuszt” a szerkesztőből, csak akkor jelenik meg, ha aktívvá válik.

## Forrás megtekintése [view-source]

![][6]

   [6]: images/view_source.jpg @2x width=740px height=345px class=center

Az előnézeti és a forráskód nézet között a jobb felső sarokban található gombbal válthat. Ez a nézet U-val is váltható.

## Keresés [search]

![][7]

   [7]: images/SearchBarFull.jpg @2x width=818px height=195px class=center

A keresősáv a {% kbd cmd F %} gombbal érhető el, és lehetővé teszi, hogy az előnézetben keressen egy szóra vagy kifejezésre. A keresés után a {% kbd cmd G %} és {% kbd shift cmd G %} gombokkal navigálhat előre és hátra a további találatok között.

A keresősáv jobb oldalán található jelölőnégyzetek segítségével szűkítheti a keresést a kis- és nagybetűk érzékenysége, csak egész szavak és reguláris kifejezések szerint. A reguláris kifejezések keresése mellett a helyettesítő karakteres (*?) keresés mindig működik, még akkor is, ha a reguláris kifejezés ki van kapcsolva.

A keresett kifejezést vagy kifejezést perjelekkel is körülveheti, hogy automatikusan reguláris kifejezésként értelmezze (pl. „/term.+?\b/”).


Használja a keresési funkciót a könyvjelzővel kombinálva, hogy elmentse a helyeket, amikor megtalálja őket. Nyomja meg a Tab ({% kbd ⇥ %}) gombot a dokumentum fókuszálásához, majd nyomja meg a Shift-[1-9] billentyűt, hogy könyvjelzőt állítson be a számon. Visszaugorhat a könyvjelzőhöz, ha egyszerűen beírja a számot (a Shift billentyű nélkül), vagy a n/p billentyűkombinációval a dokumentumok sorrendjében navigálhat. Az N/P számsorrendben fog navigálni. A könyvjelzőkről, a tartalomjegyzékről, a minitérképről és a gyors fejléckeresésről lásd: [Dokumentumnavigáció](Document_Navigation.html). További lehetőségekért tekintse meg az [Előnézeti navigáció](Keyboard_Shortcuts.html#previewnavigation) részt, vagy írja be a "?" bármikor az Előnézetben.

> **Megjegyzés:** A keresés nem tördelhet az elemek között, ami azt jelenti, hogy a keresési karakterlánc nem folytatódhat a bekezdés és a címsor között, a listaelemek között stb.

A {% kbd ctrl shift 1 %}, {% kbd 2 %} és {% kbd 3 %} segítségével válthatja az „Egész szavak”, „Kis- és nagybetűk megkülönböztetése” és „Regex” jelölőnégyzetet.

### Speciális keresés ### [advanced-search]

Használhat helyettesítő karaktereket a nem regex keresésben. A `*` minden nem szóköz karaktersorozattal, a `?` pedig egyetlen karakterrel egyezik.

Ha a keresést a `*` karakterrel indítja el, az jQuery választó keresés lesz. Bármely jQuery választót használhatja, és az összes egyező elem kiemelésre kerül, és navigálható a {% kbd cmd G %} és a {% kbd shift cmd G %} jelekkel. Ha a szöveges keresés hatókörét egy bizonyos elemtípusra szeretné korlátozni, adja hozzá a keresett kifejezéseket dupla idézőjelbe a választó definíciója után:

    *h2 "Alice"

Ez a `*h2:contains(Alice)` megfelelője

## Dokumentumnavigáció (TOC, könyvjelzők, minitérkép) [document-navigation-toc-bookmarks-mini-map]

A [Dokumentumnavigáció](Document_Navigation.html) oldal tartalmazza a tartalomjegyzéket (beleértve a szűrő {% kbd Space %}-vel történő megnyitását), a gyorskeresést a {% kbd f %}-vel, a könyvjelzőket és a minitérképet.

## Navigáció billentyűzettel [keyboardnavigation]

Az előnézeti ablakban gyorsan lehet navigálni a billentyűparancsokkal. Használja a {% kbd j %} és {% kbd k %} billentyűket a fel és le mozgáshoz, és tartsa lenyomva a Shift ({% kbd J %}/{% kbd K %}) billentyűt a gyorsabb mozgáshoz. A {% kbd t %} és a {% kbd b %} a dokumentum tetejére és aljára kerül (ahogyan a {% kbd gg %} és {% kbd G %} is a Vim rajongók számára). A {% kbd u %} és a {% kbd d %} 1/2 oldalt felfelé és lefelé mozgat.

### Fejléc ugrás [header-jumping]

A vessző ({% kbd , %}) és a pont ({% kbd . %}) billentyű lenyomásával előre-hátra ugrik a dokumentum bármely fejlécében. A Shift ({% kbd shift  %}) lenyomva tartása csak az 1. és 2. szintű fejlécek között ugrik.


## Teljes képernyő [full-screen]

A teljes képernyős módot az Előnézet menüből vagy a {% kbd ctrl cmd F %} beírásával lehet váltani.

## Külső hivatkozásokra kattintva [clicking-external-links]

![][10]

[10]: images/linkpopover.png @2x width=706px height=213px class=center

A dokumentum előnézetében egy külső hivatkozásra kattintva megnyílik az alapértelmezett böngészőben. Ha rákattint és lenyomva tartja, a Marked felengedésekor három lehetőséget kínál: átmásolhatja a hivatkozás URL-jét a vágólapra, érvényesítheti a hivatkozást, vagy megnyithatja a hivatkozást az alapértelmezett böngészőben. Csak kattintson bárhová az előnézetben az ablak bezárásához. Ez a funkció letiltható a {% prefspane Preview %} ("Link popoverek engedélyezése") menüpontban.

Nézzen meg egy [áttekintő videót a YouTube-on](https://www.youtube.com/watch?v=nrt7YZPrnv0&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=1).

## Összecsukható címsorok ## [collapsibleheadlines]

Ha a „Címsorok panelek összecsukása” engedélyezve van a {% prefspane Preview %}-ban, a címsorokra kattintva összecsukja az adott címsor és a következő címsor közötti szakaszt ugyanazon a szinten. A szakaszon belüli alszakaszok el vannak rejtve. Opcionálisan ezt a viselkedést {% kbd cmd %} kattintásra korlátozhatja.

![][13]

[13]: images/headlines.jpg @2x width=740px height=287px class=center

Ha lenyomva tartja a {% kbd opt  %} billentyűt kattintáskor (vagy a {% kbd cmd %}-kattintáskor), kibontja/összecsukja az összes alárendelt részt a kattintott címsor alatt. A {% kbd shift  %} (Shift) billentyű lenyomva tartása kattintás közben az összes többi szakaszt összecsukja ugyanazon a szinten, és csak a kattintott rész látható.

Az összecsukott szakaszokat a cím jobb oldalán sárga kiemelés jelzi, és a kurzor jelzi, hogy mi történik, ha az elemre kattintanak.

Ha olyan szerkesztést hajt végre, amelynek láthatónak kell lennie, vagy ha olyan tartalomjegyzék-szakaszra kattintanak, amely jelenleg egy összecsukott szakaszon belül van, akkor a szükséges szülőrészek kibontásra kerülnek, hogy felfedje azt.

A dokumentum összes szakaszát összecsukhatja/kibonthatja egyszerre az „Összes szakasz összecsukása” ({% kbd opt cmd left  %}) és az „Összes szakasz kibontása” ({% kbd opt cmd right  %}) segítségével.

További részletekért tekintse meg a [Dokumentumnavigációs videót a YouTube-on](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

## Egyéni processzorjelzők/kapcsolók ## [custom-processor-indicatorstoggles]

![][jelzők]

[indicators]: images/processorindicators.png @2x width=874px height=255px class=center

Ha az egyéni processzor és/vagy előfeldolgozó engedélyezve van, jelzőfények jelennek meg az eszköztáron. Ezek segítségével megtekinthető, hogy a processzor be van-e kapcsolva az aktuális dokumentumhoz (a jelző kiemelve lesz), és rájuk kattintva váltható az egyéni előfeldolgozó és processzor használata.

## Görgessen a Szerkesztéshez [scrolltoedit]

A Marked „görgessen a szerkesztéshez” funkciója nyomon követi a legutóbbi és az utolsó frissítés közötti különbségeket, és megpróbálja megtalálni azt a pontot, ahol a legutóbbi módosításokat végrehajtotta. A Marked mindig ezt követi, és egy kis piros vonal jelenik meg az előnézetben, amely megmutatja az első észlelt változás helyét. A {% prefspane Preview %} oldalon bekapcsolhatja a „Görgetés az első szerkesztésig” funkciót, és amikor az előnézet frissül, finoman görgeti a nézetet az adott helyre.

Ha a „Görgetés az első szerkesztéshez” funkció ki van kapcsolva, az előnézetben bármikor megnyomhatja az „e” gombot, hogy az utoljára tárolt szerkesztési pontra lépjen.

## Automatikus görgetés [autoscroll]

Lásd a dedikált [Autoscroll](Autoscroll.html) oldalt. Ha az Autoscrollt teleprompterként használja, [a speciális szintaxis szüneteket szúrhat be](Special_Syntax.html#pauses).

## Nagyítás áttekintése [zoom-overview]

Lásd a [Nagyítás áttekintése](Zoom_Overview.html) oldalt ({% kbd z %} az előnézetben; működik a szóismétlésben is a {% kbd ctrl cmd w %}-al).

## Markdown referencia [markdown-reference]

![][11]

   [11]: images/markdown_reference.jpg @2x width=1148px height=267px class=center

Válassza a Markdown Reference lehetőséget a {% appmenu Help %} menüből, hogy megjelenítsen egy útmutatót, amely a többi ablak fölött lebeg. Ez hasznos azoknak, akik még tanulják a Markdown szintaxisát. Ezt a panelt a billentyűzeten keresztül nyithatja meg a {% kbd opt cmd M %} használatával.

## Globális billentyűparancsok [global-keyboard-shortcuts]

A {% prefspane General %}-ben kijelölhet egy egyéni billentyűkódot a Marked aktiválásához, és egyet, amellyel csak az elülső ablakot emelheti fel a szerkesztő elhagyása nélkül.