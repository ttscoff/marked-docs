<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A {% prefspane Preview %} opciói:

![Beállítások: Előnézet][1]

[1]: images/screenshots/preferences-Preview.jpg @2x width=714px height=1031px class=preferencepane-scroll

### Tekintse meg a viselkedést [preview-behavior]

Mini térképes navigáció engedélyezése
: A dokumentum vizuális térképének létrehozása, amely megjelenik a „0” lenyomásakor. Rövid késéseket okozhat nagyméretű dokumentumok előállítása során.

A címsorok összecsukják a szakaszokat
: Ha egy címsorelemre kattint, az összecsukódik az elem és a következő címsor között.

{% kbd cmd %}-kattintás szükséges
: Ha ez be van jelölve, a címsorok csak akkor fognak összecsukódni/kinyílni, ha a Command billentyű lenyomva tartásával kattintanak rájuk.

Szinkronizálja az előnézetet és a forrás görgetését
: Ha a szerkesztője támogatja, tartsa görgetve az előnézetet, hogy megfeleljen a forrásdokumentum megfelelő helyének.

Szinkronizálja a gyorsolvasást görgetési pozícióval
: Tartsa a [Speed Reading](Speed_Reading.html) fedvényt az előnézeti görgetés pozíciójához igazítva. Ezt a Gyorsolvasási fedvényen is átkapcsolhatja.

### Görgessen a szerkesztéshez [scroll-to-edit]

Görgessen a szerkesztéshez
: Az előnézet frissítésekor a Marked meg tudja határozni az első pontot, ahol a dokumentum megváltozott, és automatikusan rágörget. Ez szinkronban tartja az előnézetet a szerkesztett dokumentum jelenlegi helyével. A legutóbbi szerkesztési jelölő az első különbség a dokumentumban az utolsó frissítés óta. A „fordított különbségi sorrend” engedélyezése ehelyett a dokumentum utolsó eltérését (fentről lefelé) tekinti a legutóbbi szerkesztésnek.

A legutóbbi szerkesztési jelző megjelenítése
: Egy kis piros jelölő jelenik meg az első észlelt szerkesztés helyén. Kapcsolja ki, hogy láthatatlan legyen. (Szerkesztéshez **Görgessen** szükséges.)

Az összes különbségjelző megjelenítése
: Ha ez be van kapcsolva, az utolsó frissítés és az aktuális tartalom közötti összes különbség kiemelve lesz az ereszcsatornában. A szerkesztések között a <kbd>e</kbd> (előre) és a {% kbd shift E %} (hátra) gombokkal a nézet közepéig görgetve navigálhat.

Fordított különbségi sorrend
: Ha ez engedélyezve van, a különbségek fordított sorrendben jelennek meg (alulról felfelé). Ez befolyásolja a navigációt, így az <kbd>e</kbd> felfelé, a {% kbd shift E %} pedig lefelé navigál. A „legutóbbi szerkesztés” lesz az utolsó különbség a dokumentumban.

### További funkciók [additional-features]

A tartalomjegyzék követi a görgetés pozícióját
: A tartalomjegyzék kiemeli az aktuális részt.

Felugró statisztika a szöveg kiválasztásához
: A kiválasztott szöveg szószámláló előugró ablakának megjelenítése, amikor kijelölés történik.

Link popover engedélyezése
: Előugró menü megjelenítése, amikor a külső hivatkozásokra kattintanak, és lenyomják őket, mielőtt elengedik.

Az URL-ek automatikus ellenőrzése frissítéskor
: URL-ek érvényesítése a dokumentum betöltésekor és frissítésekor. Csak akkor jeleníti meg az eredményeket, ha hibák vannak.
: Ez a [link validation](Link_Validation.html) minden alkalommal lefut, amikor a dokumentum frissül (ha jelentős számú hivatkozással rendelkezik, ez lassú folyamat lehet, és kerülni kell).

### Wiki linkelés [wiki-linking]

Konvertálni [[Wiki linkek]]
: Engedélyezze Marked [wiki navigációját](Wiki_Navigation.html) az `[[wiki link]]` szintaxishoz.

Alapértelmezett kiterjesztés
: A Megjelölt fájlnév-kiterjesztés olyan wikihivatkozások feloldásakor használatos, amelyek nem tartalmaznak kiterjesztést (például `md`).

### Megjelenés [appearance]

Sötét mód
: Az összes ablak megjelenítése "Nagy kontraszt" módban, sötét krómozással, és ha elérhető, az aktuális stílus fordított változatával (egyéni stílusokra esetleg nem vonatkozik).

Match System Setting
: Sötét mód automatikus váltása, amikor a macOS Dark Mode rendszerszinten be- vagy kikapcsolva van.

A teljes elérési út megjelenítése az ablak címében
: Ha engedélyezve van, a Megjelölve az ablak címében megjeleníti az aktuális dokumentum teljes elérési útját.