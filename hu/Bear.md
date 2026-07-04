<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A [Bear][bear] élő előnézetet küldhet közvetlenül a Markednek.

## Küldés a Beartől

A Bear programban válassza az **Előnézet megjelölve** lehetőséget a **Nézet** menüből (a szöveg Medve verziónként kissé eltérhet). A Marked TextBundle-t kap, így a beágyazott képek és elemek általában a szöveggel együtt utaznak.

Az abszolút elérési utakkal vagy `https` URL-ekkel hivatkozott képek is feloldódnak, amíg a Megjelölt el tudja érni őket.

## Mac App Store megjegyzés

Ha a Marked **Mac App Store** buildjét használja, és a macOS folyamatosan engedélyt kér a könyvtárak megnyitásához, amikor előnézetet készít a Bear alkalmazásból, [vegye fel a kapcsolatot a Marked ügyfélszolgálatával](http://support.markedapp.com) a közvetlen letöltésű kiadáshoz való ingyenes áttéréshez, amellyel elkerülhető az adott sandbox súrlódás.

## Címkék

A medve-stílusú címkék úgy jeleníthetők meg, ha a {% prefspane Processor %} alatt kapcsolja be a **#Text is tag** és a **Stíluscímkék** lehetőséget.

W> Ez a beállítás megzavarhatja a Megjelölt, ha a `#` után szabályos címsorokat ír szóközök nélkül.

## Fájlnevek és exportálás

Ha bekapcsolja a **Használja az első H1-et tartalékcímként** az {% prefspane Export %}-ben, ez a cím irányíthatja a fájlnevet és az `%title` helyőrzőt, amikor PDF-eket nyomtat vagy exportál a Marked alkalmazásból.

I> Egy előnézeti stílus, amely megközelíti Bear saját megjelenését [elérhető a markedapp.com/styles oldalon] (https://markedapp.com/styles/preview?style=bear).

A Bear streamelési előnézete a [Streaming előnézet](Streaming_Preview.html) oldalon és a [További alkalmazásintegrációk](Additional_Application_Support.html) oldalon található.

[bear]: https://bear.app/