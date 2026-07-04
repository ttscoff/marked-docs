<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Ha a [Markeds include syntax vagy IA Writer blokk szintaxisa][include]-on keresztül tartalmazott fájl CSV vagy TSV kiterjesztéssel rendelkezik, a Marked megpróbálja elemezni és MultiMarkdown táblává konvertálni. Ez a legtöbb szabványos formátummal működik, beleértve a vesszővel és tabulátorral elválasztott formátumokat, valamint a további elválasztókat és idézőformátumokat, amelyeket a rendszer automatikusan észlel.

A CSV-fájlok használatának egyik előnye a Markdown táblázatok írása helyett, hogy a cellákon belüli sortörések automatikusan `<br>` címkékké alakulnak. Ezt manuálisan kell megtenni, hogy a MultiMarkdown táblák írásakor sortörések is szerepeljenek, így ez további időmegtakarítást jelent.

Megjegyzendő, hogy van egy kiváló [TableFlip][] alkalmazás, amely sokkal egyszerűbbé teszi a táblázatok szerkesztését a dokumentumban. Érdemes megnézni, ha gyakran dolgozik táblázatos adatokkal.

A mellékelt CSV-fájlokat a rendszer figyeli a változásokra, így további szerkesztések végezhetők az eredeti CSV-fájlban, és a Megjelölt automatikusan frissíti az előnézetet mentéskor.

A konvertált táblázatok szerepelni fognak a Markdown exportban, így a Marked segítségével strukturált adatokat tartalmazó dokumentumokat lehet összeállítani és egyetlen fájlt exportálni.

[include]: Multi-File_Documents.html
[TableFlip]: http://tableflipapp.com/