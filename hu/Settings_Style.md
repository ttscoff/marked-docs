<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A {% prefspane Style %} opciói:

![Beállítások: Stílus][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Elrendezés és tipográfia

Korlátozza a szöveg szélességét az Előnézetben
: Állítsa be az előnézet törzsének maximális szélességét a csúszkával (pixelben).

Automatikus elválasztás a bekezdésekben
: A szavak automatikus elválasztásának engedélyezése.

Akadályozza meg az özvegyek megjelenését a címsorokban és a bekezdésekben
: Nem törő szóközt kényszerít a címsorok és bekezdések utolsó két szava közé, hogy megakadályozza az egyes szavak új sorba tördelését.

Nyomdailag helyes idézőjelek és írásjelek létrehozása
: A SmartyPants használata intelligens idézőjelekhez, ellipszisek konvertálásához és egyéb tipográfiai funkciókhoz (MultiMarkdown).

A lábjegyzetek jelölőit szögletes zárójelben helyezze el
: Ha be van jelölve, használja az alapértelmezett MultiMarkdown formázást a lábjegyzetjelölőkhöz ([1]). Törölje a jelet a szögletes zárójelek eltávolításához.

Az Outline engedélyezése a bővítményekhez
: A Vázlat mód automatikus bekapcsolása a felsorolt kiterjesztésű fájloknál.

Használja az APA stílust
: Használjon APA-stílusú körvonalakat az alapértelmezett decimális formátum helyett.

Stílus szó szerinti (kód) blokkok költészet
: Ha be van jelölve, a tabulátoros behúzású, bekerített vagy beépített kód költészetként jelenik meg kódblokk helyett (nincs szintaktikai kiemelés, és speciális stílus a témától függően).

Engedélyezze a témáknak, hogy szöveget kódblokkokba burkoljanak
: Ha be van jelölve, a témák `pre>code` blokkon belüli tördelést okozhatnak. Ha nincs bejelölve, a vízszintes túlcsordulás mindig gördül.

Mindig csomagolja be a kódot
: Kényszeríti a kódblokkok tördelését a témabeállításoktól függetlenül (felülbírálja a téma tördelési viselkedését).

RTL-szöveg észlelése és stílusa
: Nyelv érzékelése elemenként a dokumentumban és a stílusnak megfelelően jobbról balra.

### Téma

Stílusok kezelése
: Megnyitja a [Style Manager](Style_Manager.html) ablakot. Adjon hozzá CSS-fájlokat a meghajtóról, hogy megjelenjenek a Stílusválasztó menükben. Használja az `Add New Style` gombot, vagy húzza a CSS-fájlokat ebbe az ablakba. Húzza át az átrendezéshez, és használja a jelölőnégyzeteket a stílusok engedélyezéséhez vagy letiltásához.

További témák
: Nyissa meg az online témagalériát további stílusok böngészéséhez és telepítéséhez.

Alapértelmezett stílus
: Az itt kiválasztott stílus minden új ablakhoz betöltődik, kivéve, ha [dokumentum-specifikus stílus szerepel a metaadatokban](Per-Document_Settings.html) (pl. "Megjelölt stílus: Grump").

Kövesse nyomon a CSS-módosításokat
: Ha ez be van kapcsolva, a Marked figyeli az aktuális stílust a lemezmódosításokhoz, segítve az egyéni stílusszerkesztést és a webfejlesztést.

További CSS
: Az ide hozzáadott CSS a normál stíluslap után fog megjelenni az összes témával. Többek között a belső stílusok szerkesztése nélkül is felülírhatja a beállításokat.
: Ez minden dokumentumra és minden stílusra vonatkozik. Ha egyéni CSS-t szeretne alkalmazni a dokumentumokra a feltételek alapján, használja az Egyéni szabályokat az {% prefspane Processor %} alatt.

### Szkriptek szerepeltetése

Szintaxis kiemelés
: A highlight.js [szintaxiskiemelés](Syntax_Highlighting.html) bekapcsolása kódblokkokhoz. Válasszon ki egy témát a legördülő menüből.
: Ha a **Csak ha a nyelv megadva** be van jelölve, a szintaktikai kiemelés csak a megadott nyelvű elkerített kódblokkokra vonatkozik.

Engedélyezze a MathJaxot
: A [MathJax](MathJax.html) betöltése a MathML egyenletek megjelenítéséhez. Válassza a **Helyi** (csomagolt) vagy a **CDN** lehetőséget a legördülő menüből.
: **További csomagok** megnyit egy lapot, ahol további MathJax-csomagokat is tartalmazhat (például fizika és kémia).
: A **Speciális konfiguráció** megnyit egy lapot az egyéni MathJax konfigurációhoz.

Engedélyezze a KaTeX-et
: A [KaTeX](Mathjax.html#katex) betöltése a MathJax alternatívájaként. Csak az egyik vagy a másik választható.

Számegyenletek
: Ha alkalmazható, a Marked számokat ad hozzá a renderelt egyenletekhez. A számozáshoz válassza a **Bal oldal** vagy a **Jobb oldal** lehetőséget. Ha MathJaxot használ, válassza a **Csak AMS** lehetőséget, ha csak az AMS-egyenleteket szeretné számozni.

Sellő
: Betölti a [mermaid.js](https://mermaid.js) fájlt egy CDN-ről a Markdown-stílusú diagramkészítés engedélyezéséhez. A Mermaid diagramok megjelenítéséhez szükséges horgot minden dokumentumfrissítéskor automatikusan tartalmazza.

Pásztázási és nagyítási diagramok
: Ha vannak sellődiagramok, engedélyezze a nagyítást a {% kbd cmd %} gombos görgetéssel és pásztázással kattintással és húzással.