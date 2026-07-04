<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Kövesse nyomon, ahogy ír.

## Szószám és dokumentumstatisztika

![][1]

   [1]: images/WordCount.jpg @2x width=840px height=61px class=center

A szószám az alsó állapotsorban található, és az állapotsor alatti {% prefspane General %} gombbal engedélyezhető és letiltható. További statisztikákat tekinthet meg a fogaskerék menü előnézeti vagy forrásablakban, a szószámra kattintva vagy az Option-Command-S ({% kbd opt cmd S %}) beírásával. Tartsa lenyomva az Option ({% kbd opt  %}) billentyűt kattintás közben az Olvashatósági statisztikák megjelenítéséhez, és tartsa lenyomva az Option-Command ({% kbd opt cmd %}) billentyűt a Speciális statisztikák panel megnyitásához.

Ha szöveg van kiválasztva, a szószám kijelző és a bekezdés/mondatok/karakter előugró ablak csak a kijelölésre vonatkozó információkkal frissül.

## A kiválasztás szószáma

![Szószám előugró ablak a szövegkiválasztásnál][2]

   [2]: images/wordcountforselection.jpg @2x width=749px height=144px class=center

Ha az előnézetben szöveget jelöl ki, az ablak alján látható szószám csak a kiválasztott szövegre vonatkozó statisztikákat jeleníti meg.

Ha a „Szószám megjelenítése a kijelöléshez” engedélyezve van a {% prefspane Preview %}-ben, egy kis előugró ablak jelenik meg a kurzor mellett, hogy megjelenítse a kiválasztott szöveg szó-/sor-/karakterszámát. Ezt egyszerűen az egér elmozdításával lehet elvetni a felugró ablaktól.

A zoom funkció praktikus a nagyobb szövegrészek gyors kiválasztásához és számlálásához. A kicsinyítéshez és a kiválasztáshoz írja be az {% kbd z %} parancsot.

## Olvashatósági statisztika

![Olvashatósági statisztika sáv][3]

   [3]: images/screenshots/mainwindow-feature-stats-lower-crop.jpg @2x width=1089px height=111px class=center

A Flesch/Kincaid és a Fog Index további statisztikái a {% kbd opt shift cmd S %} segítségével érhetők el.

### Olvashatósági információ

**Flesch Reading Ease:** a magasabb pontszámok azt jelzik, hogy az anyag könnyebben olvasható; az alacsonyabb számok a nehezebben olvasható részeket jelölik.

**90,0--100,0**: átlagos 11 éves diák
**60,0--70,0**: 13-15 éves diákok
**0,0--30,0**: egyetemet végzettek

**Flesch-Kincaid fokozat:** a szöveg megértéséhez általában szükséges oktatási évek száma.

**Gunning Köd index:** az angol írás olvashatóságát méri. Az index azt becsüli meg, hogy hány évnyi formális oktatás szükséges a szöveg első olvasatbeli megértéséhez. A 12-es ködindexhez egy amerikai középiskolás (18 év körüli) olvasási szint szükséges.

## Speciális statisztikák

![Speciális statisztikák előugró ablak][adv]

[adv]: images/screenshots/mainwindow-feature-stats-info-crop.jpg @2x width=800px height=800px class=center

Ha a fogaskerék menüből kiválasztja a Speciális statisztikákat ---- vagy megnyomja a {% kbd cmd I %} --- gombot, egy olyan panel legördül, amely fejlettebb dokumentumstatisztikát tartalmaz, beleértve az átlagos szó- és mondathosszt, valamint az átlagos szóbonyolultságot.

### Lebegő speciális statisztikák

![Lebegő információs ablak][lebegő]

[floating]: images/floatinginfo.jpg @2x width=999px height=522px class=center

A {% kbd shift cmd I %} gomb megnyomásával megnyílik egy lebegő panel, amely az összes részletes statisztikát és olvashatósági információt tartalmazza. Ez a panel továbbra is az élvonalban maradhat, amikor a szerkesztőre vált, így minden mentéskor láthatja a statisztikák frissítését, függetlenül attól, hogy az előnézet látható-e vagy sem. A `<` ikon megnyomásával visszakerül az előtérbe a hozzá tartozó Megjelölt előnézet. Ha lenyomva tartja az opciót, és ugyanarra a gombra kattint, akkor megnyílik a Markdown fájl az alapértelmezett szövegszerkesztőben (a {% prefspane Apps %}-ben van beállítva).

### Word Targets

Ha írás közben meghatározott szószámot ír elő, hozzáadhat egy „cél:” metaadat-kulcsot a dokumentum tetejéhez, és a Marked nyomon követi az előrehaladást, és megjeleníti a teljesítésjelzőt a Részletes statisztikák panelen ({% kbd cmd I %}) és a Lebegő statisztikákban ({% kbd shift cmd I %}).

![][célszószám]

[targetwordcount]: images/wordtargets.jpg @2x width=740px height=191px class=center


## Képzeld el a szóismétlést

Ha a fogaskerék menüből kiválasztja a Szóismétlődés megjelenítése lehetőséget (vagy megnyomja a {% kbd ctrl cmd W %} gombot), akkor egy speciális nézetre vált, amely eltávolítja a nem szöveges elemeket, és kiemeli a dokumentumban ismétlődő szavakat. Az ismétlődő szavak halványrózsaszínnel vannak kiemelve, és ha a kiemelt szó fölé viszi az egérmutatót, a megfelelő szavakat az egész dokumentumban világosabbá teszik. Ha rákattint egy kiemelt szóra, a háttér elsötétül, és a kiemelést „ragasztja” a további áttekintéshez.

![Szóismétlés][4]

[4]: images/screenshots/mainwindow-word-repetition.jpg @2x width=1369px height=1084px

Ebben a módban is használhatja a "zoom" funkciót ("z" gépelje be), amely lehetővé teszi, hogy kiemeljen egy ismétlődő szót, majd gyorsan beolvassa a teljes dokumentumot, hogy megnézze, hol koncentrálódnak az ismétlések.

A szavakat a "töve" alapján hasonlítják össze, ami azt jelenti, hogy a "rész", "rész" és "részek" ismétlődő szavaknak minősülnek. Ez figyelembe veszi a szótagokat és a ragozást az ismétlési sűrűség ellenőrzésekor.

**Hatály**

Az ismétlési ellenőrzés hatóköre a dokumentum alsó eszköztárában módosítható, és beállítható Dokumentum vagy Bekezdés értékre. A dokumentum mód az alapértelmezett; A Bekezdés kiválasztása csak az ismétlődéseket számolja az egyes szövegblokkon belül. Az ismétlések továbbra is a teljes dokumentumban kiemelve lesznek, de csak akkor számítanak be, ha egy szó egy bekezdésben többször is előfordul.

**A szavak figyelmen kívül hagyása**

Ideiglenesen kizárhat egy szót és annak mindenféle ragozását és többes számozását, ha a kiemelt szóra kattint az Opció gombbal. Az ideiglenesen figyelmen kívül hagyott szavak az előnézet jobb alsó sarkában jelennek meg. Ha rákattint egy szóra a figyelmen kívül hagyott szavak listájában, az visszaáll a vizualizációba.

A szavak végleges figyelmen kívül hagyásához szerkeszthet egy listát az Ismétlések figyelmen kívül hagyása lap {% prefspane Proofing %} pontjában. A listába soronként egyenként hozzáadott szavak (vagy szótövek) mindig figyelmen kívül maradnak. Ha automatikusan szeretne hozzáadni egy szót ehhez a listához, nyomja meg az Option-Shift-kattintást a szóismétlési vizualizációban.

**Kilépés a szóismétlési módból**

A szóismétlési nézetet bezárhatja az alsó eszköztár hatókörválasztója melletti Bezárás ikonnal vagy az escape billentyű lenyomásával.