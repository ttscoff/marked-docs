# <%= @title %>

A {% prefspane Style %} beállításai:

![Settings: Style][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Elrendezés és tipográfia [layout-and-typography]

Szöveg szélességének korlátozása az előnézetben
: A csúszka segítségével (pixelben) megadhatja az előnézet törzsének maximális szélességét.

Automatikus elválasztás bekezdésekben
: Engedélyezi a szavak automatikus elválasztását szótagolással.

Árvasorok megelőzése címsorokban és bekezdésekben
: Nem törhető szóközt kényszerít a címsorok és bekezdések utolsó két szava közé, hogy egyetlen szó se kerüljön új sorba.

Tipográfiailag helyes idézőjelek és írásjelek létrehozása
: A SmartyPants használata az intelligens idézőjelekhez, a hármaspont-átalakításhoz és más tipográfiai funkciókhoz (MultiMarkdown).

Lábjegyzetjelölők szögletes zárójelbe foglalása
: Ha be van jelölve, a lábjegyzetjelölők az alapértelmezett MultiMarkdown formázást használják ([1]). Kapcsolja ki a szögletes zárójelek eltávolításához.

Outline engedélyezése kiterjesztésekhez
: A felsorolt kiterjesztésű fájloknál automatikusan bekapcsolja az Outline módot.

APA stílus használata
: APA stílusú vázlatok használata az alapértelmezett decimális formátum helyett.

Szó szerinti (kód) blokkok stílusa versként
: Ha be van jelölve, a tabulátorral behúzott, keretezett vagy beillesztett kód versként jelenik meg kódblokk helyett (szintaxiskiemelés nélkül, a témától függő speciális stílussal).

Témák engedélyezése a szöveg tördelésére kódblokkokon belül
: Ha be van jelölve, a témák tördelhetik a szöveget a `pre>code` blokkokon belül. Ha nincs bejelölve, a vízszintes túlcsordulás mindig görgethető marad.

Kód mindig tördelése
: A kódblokkok tördelésének kikényszerítése a téma beállításaitól függetlenül (felülírja a téma tördelési viselkedését).

RTL szöveg felismerése és stílusa
: A dokumentum egyes elemeinek nyelvét felismeri, és ennek megfelelően jobbról balra íródó (RTL) stílust alkalmaz rájuk.

### Téma [theme]

Stílusok kezelése
: Megnyitja a [Stíluskezelő](Style_Manager.html) ablakot. Adjon hozzá CSS-fájlokat a meghajtójáról, hogy megjelenjenek a stílusválasztó menükben. Használja a `Add New Style` gombot, vagy húzza a CSS-fájlokat erre az ablakra. Húzással átrendezheti, a jelölőnégyzetekkel pedig ki- és bekapcsolhatja a stílusokat.

További témák
: Megnyitja az online témagalériát, ahol további stílusokat böngészhet és telepíthet.

Alapértelmezett stílus
: Az itt kiválasztott stílus töltődik be minden új ablakhoz, kivéve ha [a dokumentum metaadataiban dokumentumspecifikus stílus van megadva](Per-Document_Settings.html) (például „Marked Style: Grump").

CSS-módosítások követése
: Ha ez be van kapcsolva, a Marked figyeli az aktuális stílus lemezen történő változásait, ami segít az egyéni stílusok szerkesztésében és a webfejlesztésben.

További CSS
: Az itt megadott CSS minden téma normál stíluslapja után kerül hozzáfűzésre. Ez egy részleges átfedő réteg, nem pedig teljes témahelyettesítő.
: A Marked átírja a mezőben szereplő szelektorokat (például a nyomtatási szabályoknak a `body.mkprinting #wrapper …`-t kell használniuk). Nincs méret- vagy érvényességi korlátozás — lásd az [Egyéni CSS létrehozása](Writing_Custom_CSS.html#additional-css-settings) című részt.
: Ez minden dokumentumra és minden stílusra vonatkozik, beleértve a HTML-exportot is, ha a stílusok be vannak illesztve. Ha feltételek alapján szeretne egyéni CSS-t alkalmazni a dokumentumokra, használja az Egyéni szabályokat a {% prefspane Processor %} alatt.

### Szkriptek beillesztése [include-scripts]

Szintaxiskiemelés
: Bekapcsolja a highlight.js [szintaxiskiemelést](Syntax_Highlighting.html) a kódblokkokhoz. Válasszon témát a legördülő menüből.
: Ha a **Csak ha a nyelv meg van adva** be van jelölve, a szintaxiskiemelés csak azokra a keretezett kódblokkokra vonatkozik, amelyeknél meg van adva a nyelv.

MathJax engedélyezése
: Betölti a [MathJax](MathJax.html)-ot a MathML-egyenletek megjelenítéséhez. Válasszon a legördülő menüből **Helyi** (beépített) vagy **CDN** opciót.
: A **További csomagok** gombra kattintva egy panel nyílik meg, ahol további MathJax-csomagokat (például Physics és Chemistry) adhat hozzá.
: A **Speciális konfiguráció** gombra kattintva egy panel nyílik meg az egyéni MathJax-konfigurációhoz.

KaTeX engedélyezése
: Betölti a [KaTeX](MathJax.html#katex)-et a MathJax alternatívájaként. Csak az egyik választható a kettő közül.

Egyenletek számozása
: Ha alkalmazható, a Marked ábraszámokat ad a megjelenített egyenletekhez. A számozáshoz válasszon **Bal oldal** vagy **Jobb oldal** opciót. MathJax használata esetén választhatja a **Csak AMS** opciót, amely csak az AMS-egyenleteket számozza.

Mermaid
: Betölti a [mermaid.js](https://mermaid.js)-t egy CDN-ről a Markdown-stílusú diagramkészítés engedélyezéséhez. A Mermaid-diagramok minden dokumentumfrissítéskor történő megjelenítéséhez szükséges hook automatikusan bekerül.

Diagramok mozgatása és nagyítása
: Ha Mermaid-diagramok vannak jelen, engedélyezi a nagyítást a {% kbd cmd %}-görgetéssel, valamint a mozgatást kattintással és húzással.
