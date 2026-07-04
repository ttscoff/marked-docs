<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Zavarba ejtő igeragozás és fontos kifejezések kiemelése.

## Kulcsszavak kiemelése

A Megjelölt kulcsszókiemelés lehetővé teszi, hogy elkapja azokat a gyakori kifejezéseket, amelyeket érdemes elkerülni, alternatív kifejezéseket kereshet, vagy csak általános célból kiemelhet. Az egyes kategóriáknak megfelelő kulcsszavak listája a {% prefspane Proofing %} alatt szerkeszthető.

Engedélyezze a kiemelést az {% kbd shift cmd H %} gombbal a fogaskerék menüből ({% appmenu {{gear}}, Highlight Keywords %}), vagy nyissa meg a kulcsszófiókot a bal alsó sarokban található kiemelő ikon segítségével (a fogaskerék menü közelében). A fiók a {% kbd shift cmd K %} billentyűkóddal is kinyitható. A kiemelés automatikusan engedélyezve van a fiók kinyitásakor, és a fiók bal oldalán található kapcsolóval be- és kikapcsolható.

## A kulcsszófiók

![Kulcsszófiók][kwd]

[kwd]: images/screenshots/mainwindow-feature-keywords-crop.jpg @2x width=1089px height=503px class=center

A kiemelés engedélyezésekor megjelenő Kulcsszófiók gyors hozzáférést biztosít a kiemelési lehetőségekhez, beleértve az egyes kiemelési típusok engedélyezését és letiltását. A bal oldali színes címkék függőleges sora a szöveg kiemeléseivel korrelál. Ha egy címkére kattint, az adott kulcsszótípushoz tartozó kiemelések válthatók.

Minden címkétől balra található egy cél ikon. Erre kattintva elkezdődik a dokumentum görgetése a dokumentumsorrendben szereplő kiemelés következő példányához. A címke jobb oldalán egy szám látható, amely az adott típushoz tartozó kiemelések teljes számát mutatja.

A billentyűzet segítségével gyorsan navigálhat a kiemelések között. A `[` és `]` beírása először előre-hátra léptet az összes kiemelt helyen. Ha rákattint egy cél ikonra, a `[` és a `]` pont az ilyen típusú kiemelések navigációjára vált. A `{` (Shift-[) és a `}` (Shift-]) mindig az összes kiemelt helyen navigál, függetlenül az utoljára kattintott célponttól.

Ha rákattint egy kiemelt szóra vagy kifejezésre, az adott típus lesz a navigáció célpontja, és a `[` vagy `]` használatával navigál a dokumentumban erről a pontról.

## Kulcsszavak szerkesztése

![Lektorálási beállítások][proofprefs]

  [proofprefs]: images/screenshots/preferences-Proofing.jpg @2x width=689px height=1031px class=preferencepane

Alapértelmezés szerint a Marked a [Plain English Campaign](http://www.plainenglish.co.uk) túlzottan használt szavak és kifejezések listáját használja. Ezeket egyszerűen hozzáadhatja vagy kicserélheti a {% prefspane Proofing %} szerkesztésével. Minden mező szabad formátumú szöveg, és minden sor keresési kifejezésként értelmezhető. Használja a `*` karaktert egy kifejezés vagy szó elején az előző szöveghez, a `?` karaktert pedig egyetlen karakter helyettesítéséhez használja helyettesítő karakterként.

A reguláris kifejezések akkor használhatók, ha a kifejezést perjellel veszi körül:

    /\\S*?ly/

A fentiek megfelelnek minden „ly”-re végződő szónak kiemelés céljából. A Marked kulcsszókiemelésénél a reguláris kifejezések szintaxisa [ugyanaz, mint a JavaScript](http://www.regular-expressions.info/javascript.html).

## Ideiglenes kulcsszavak

A jegyzettömb szerkesztésével ideiglenes kulcsszavakat is hozzáadhat a Kulcsszófiókhoz. Csakúgy, mint az {% prefspane Proofing %} mezőkben, soronként egy kulcsszót vagy kifejezést ad meg, a reguláris kifejezések megengedettek (előre perjelekkel körülvéve). Az ideiglenes kulcsszavak szerkesztése után feltétlenül kattintson a „Frissítés” gombra (vagy nyomja meg a {% kbd cmd return  %} gombot), hogy mentse a változtatásokat, és kiemelve jelenjen meg a dokumentumban.

A reguláris kifejezések az ideiglenes kulcsszó mezőben is működnek, csak vegye körül a szöveget perjelekkel (`/my expression\b/`).

Az ideiglenes kulcsszavak olyan helyzetekre szolgálnak, amikor a kulcsszó sűrűsége fontos, és lehetővé teszik, hogy gyorsan megtekinthesse, hányszor használta a célszavakat, kiemelve azok helyét a dokumentumban. Az ideiglenes kulcsszavakra vonatkozó egyezések száma jól láthatóan megjelenik a fiókban.

Tekintse meg a ["Szóismétlés vizualizálása"][wordrep] parancsot is, hogy megtalálja a túlzottan használt szavakat a szövegben.

[wordrep]: Document_Statistics.html#visualizewordrepetition

## Passzív hang

A megjelölve rámutat a „passzív hang” használatára az angol szövegben. Ahogy [a Wikipédia definiálja][passzív]:

> a nyelvtani alany a főige témáját vagy páciensét fejezi ki – vagyis azt a személyt vagy dolgot, amely a cselekvésen megy keresztül, vagy amelynek állapota megváltozott.

A passzív hang nem gonosz, erről olvashatsz [Geoffrey K. Pullum nyelvész bejegyzéseiben][gkp]. A Marked passzív hangon mutat rá a szövegrészekre, de az érvényességükről a te döntésed.

[passive]: https://en.wikipedia.org/wiki/Passive_voice
[gkp]: http://languagelog.ldc.upenn.edu/nll/?cat=54

## Megkettőzött szavak

A kettős szavak (pl. "a") automatikusan narancssárga színnel vannak kiemelve, ha a kulcsszókiemelés engedélyezve van. Ez jelenleg nem konfigurálható, de korrektnek kell lennie lektoráláshoz.