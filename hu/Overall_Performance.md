<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked általános renderelési sebessége és teljesítménye nagymértékben változhat a beállításoktól és a dokumentumban található tartalom típusától függően. Számos tényező okozhat lassú megjelenítést vagy hosszú késéseket:

* **Time Machine.** Ha a Time Machine fut, és a rendszerben sok lemeztevékenység tapasztalható, előfordulhat, hogy a Marked lassabban reagál a dokumentum változásaira. A feldolgozási sebességet nem befolyásolja, csak a reakcióidőt.
* **Sok HTML-t tartalmazó Markdown-dokumentum megjelenítése.** Ennek feldolgozása mindig tovább tart. A Discount egy kicsit jobban kezeli, mint a MultiMarkdown, így ha ez szükséges, érdemes megfontolni az alapértelmezett processzor megváltoztatását (**Figyelmeztetés:** elveszíti a lábjegyzeteket és néhány egyéb MultiMarkdown funkciót).
* **A sok include-ot használva.** Legyen szó akár egy kódot tartalmazó fájlról, akár egy index-összevonási fájlról, a Markednek egy másodpercet vesz igénybe az összes elem felvétele. Ugyanez igaz a nagyméretű Scrivener dokumentumokra is. Nem sokat tehet ennek kijavítása érdekében, a Marked mindent megtesz, hogy lépést tartson a dokumentum felépítésének módjával.
* **A merevlemez állapota.** Ha a merevlemez majdnem megtelt, a Spotlight index sérült, vagy az engedélyeket egy ideje nem javították ki, előfordulhat, hogy a Marked nehezebben veszi fel az éppen figyelt fájl módosításait. A meghajtó optimalizálása az engedélyek javításával gyakran segít, és a Spotlight index újraépítése gyakran javítja a megjelölt problémákat.