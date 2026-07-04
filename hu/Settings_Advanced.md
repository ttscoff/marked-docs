<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A {% prefspane Advanced %} opciói:

![Beállítások: Speciális][1]

[1]: images/screenshots/preferences-Advanced.jpg @2x width=689px height=1031px class=preferencepane-scroll

YAML és Pandoc Metadata
: - __Ignore:__ Pontosan olyannak hagyja, amilyen a dokumentumban van, hasznos, ha a processzor vagy az előfeldolgozó valóban a YAML-t használja.
: - __Eltávolítás renderelés előtt__: A YAML blokk le van szedve
: - __Treat as MMD metadata:__ A YAML vagy Pandoc metaadatblokkot MultiMarkdown formátumra konvertálja.

Távolítsa el a MultiMarkdown metaadat-fejléceket
: Ha ez engedélyezve van, a dokumentum tetején lévő MultiMarkdown metaadatok a megjelenítés előtt törlődnek.
: Ez akkor lehet hasznos, ha nem MultiMarkdown processzort használ, amely egyébként megjelenítené a metaadatokat a renderelt dokumentumban. A metaadatok továbbra is beolvasásra kerülnek az eltávolítás előtt, így a megjelölt szintaxis továbbra is felismerésre kerül.

Gyorsítótárban tárolt képek
: A Megjelölt alapértelmezés szerint nem gyorsítótárazza a képeket az előnézetben, mert figyeli a képek változásait, és azonnal frissíti őket. Ha olyan képeket használ, amelyekre web-URL-en keresztül hivatkoznak, bekapcsolhatja ezeknek a képeknek a gyorsítótárazását, hogy felgyorsítsa a megjelenítést lassabb kapcsolatokon.

Olvashatósági statisztikák elemzése
: Ha nem szeretné, hogy a [statisztika](Document_Statistics.html) kiszámítása történjen, ez letiltja ezt a feldolgozást. Ez bizonyos teljesítménynövekedést biztosít nagyon nagy dokumentumok esetén. A karakter-, szó- és mondatszámlálás továbbra is működik.

Használja a rendszerszintű Kereső pasztalapot
: Ez az opció lehetővé teszi a Megjelöltnek, hogy felvegye azt a keresőkifejezést, amelyet utoljára használt egy másik szerkesztőben, és a Megjelöltben keresett minden más alkalmazásokban is keresés lesz. Ennek letiltása önállóvá teszi a Marked keresési funkcióját.

Használja az {% kbd cmd E %} gombot a Keresés kijelöléssel funkcióhoz
: Alapértelmezés szerint a {% kbd cmd E %} megnyitja az alapértelmezett szerkesztőt. Ha ez az opció engedélyezve van, akkor a {% kbd cmd E %} a legtöbb szövegszerkesztő alkalmazáshoz hasonlóan működik, a kiválasztott szöveget használja a Kereséshez, és a Megnyitás a szerkesztőben a {% kbd opt cmd E %} gombbal indítható.

Hibakeresési mód
: Engedélyezi a hibakeresési naplózást. Használja ezt saját hibaelhárításához és egy probléma bejelentéséhez. A tevékenység megtekintéséhez válassza a __Súgó->Hibakeresési napló megnyitása__ lehetőséget.
: Az _All_ értékre állítva információs üzenetek, figyelmeztetések és hibaüzenetek jelennek meg. Azt is beállíthatja, hogy csak a hibákat vagy a hibákat és figyelmeztetéseket jelenítse meg.

Beállítások Biztonsági mentés
: A beállításokról biztonsági másolatot készíthet egy JSON-fájlba, amellyel visszaállíthatja a beállításokat, vagy áthelyezheti őket egy új gépre.