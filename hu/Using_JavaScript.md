<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked sok JavaScriptet használ az előnézetben kínált funkciók biztosításához. Emiatt számos bonyodalom adódhat, ha szkriptek szerepelnek a dokumentum törzsében.

## Külső szkriptek

A dokumentum tetején található „CSS-fejléc:” metaadatsor használatával külső szkripteket is beilleszthet. Ezek a szkriptek azonban nem a fejlécbe kerülnek beszúrásra, hanem a láblécbe, miután a jQuery és a Marked szkriptjei már betöltődnek. Ez a legtöbb esetben ideális. Továbbra is váratlan viselkedést tapasztalhat, mivel a Marked nem tudja kompenzálni az összes lehetséges szkript-ütközést. A DOM-módosítások különösen problematikusak lehetnek.

    CSS-fejléc: <script src="file.js"></script>

## Inline tartalmazza

Számos alkalmazás létezik arra, hogy a JavaScript megjelenjen a dokumentum törzsében, például grafikongenerátorok vagy más Canvas-eszközök. A konfigurációs beállításoktól és a használt processzortól függően ezek gyakran összezavarodnak. A megoldás az, hogy a szkriptet és az extra DOM-elemeket egy külső fájlba helyezi, és a Marked szintaxisát használja a ["nyers" include fájlok][szintaxis] esetén. Ezeket a fájlokat semmilyen módon nem dolgozzák fel; a tartalom a feldolgozás többi részének befejezése után kerül be a fájlba.

    Markdown szöveg.

    <<{fájl.html}

    További Markdown szöveg...

A Marked előnézetében futó JavaScripttel való kísérletezéshez és hibakereséshez csatolhatja a Safari Web Inspector alkalmazást az előnézeti ablakhoz a [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) lépései szerint.

[syntax]: Special_Syntax.html#includingunprocessedtextorhtml