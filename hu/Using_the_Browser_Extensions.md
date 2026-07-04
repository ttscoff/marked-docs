<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked olyan böngészőbővítményeket tartalmaz, amelyek segítségével oldalak URL-jeit vagy kiválasztott tartalmat közvetlenül a Marked 3-ba küldhet.

## Telepítés

Töltse le és telepítse innen: [https://markedapp.com/extensions](https://markedapp.com/extensions):

- Firefox / Zen
- Króm / Brave / Edge
- Safari (csomagban)

## Hogyan működik a bővítmény

Ha egy kiterjesztés gombra kattint, megnyílik egy egyéni URL, amelyet a Marked 3 kezel az `x-marked-3://markdownify` séma szerint.

### `Markdownify URL`

A kiterjesztés előugró ablakában kattintson a **`Markdownify URL`** elemre az aktuális oldal URL-jének elküldéséhez a Megjelölt oldalra.

### `Markdownify Selection`

A kiterjesztés előugró ablakában kattintson a **`Markdownify Selection`** elemre, ha kiválasztotta az oldalon.

A Marked megkapja az aktuális kijelölés HTML-kódját, és azt Markdown-ba konvertálja.

### Szakasz kiválasztása (blokkválasztási mód)

![][1]

[1]: images/marked-3-chrome-1.jpg width=1280px height=800px class=center

Kattintson a **Select Section** elemre, hogy belépjen a „szakaszkiválasztási módba”:

- Vigye az egérmutatót az oldal fölé a kiválasztható blokkelemek kiemeléséhez.
- Kattintson egy blokkra, hogy azonnal elküldje a Megjelöltnek (egyszeri küldés).
- Cmd-kattintás blokkok több blokk kiválasztásához (Cmd-kattintás ismételt blokk eltávolításához).
- Nyomja meg a Vissza gombot az aktuálisan kiválasztott blokkok elküldéséhez.
- Nyomja meg az Esc gombot a szakaszkiválasztási mód törléséhez.

A kiválasztás során a felugró ablakban nagyítási vezérlők is találhatók, amelyek segítségével kis vagy sűrű szakaszokra kattinthat:

![][2]

[2]: images/marked-3-chrome-2.jpg width=1280px height=800px class=center

- `-` kicsinyít
- **Magassághoz igazítás** nagyít, hogy az oldal illeszkedjen a nézetablak magasságához
- `+` nagyítás