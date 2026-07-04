<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked automatikusan érzékeny `<picture>` elemeket tud létrehozni a helyi képekhez, ha a kísérő **sötét mód** és **retina** fájlok a hivatkozott kép mellett helyezkednek el. Ez ugyanazt az elnevezési konvenciót használja, mint az Apple DocC dokumentációs katalógusai, de működik **bármely Markdown vagy HTML dokumentumhoz**, normál képelérési úttal, amely fájlkiterjesztést tartalmaz.

Lásd még: [DocC támogatás](DocC_Support.html) a `.docc` csomagokon belüli bővítmény nélküli katalógushivatkozásokért.

## Képváltozatok engedélyezése

A {% prefspane Apps %} mezőben engedélyezze a **Sötét és @2x képváltozatok feloldása** lehetőséget (alapértelmezés szerint be van kapcsolva) a DocC beállítások alatt.

Ez a beállítás eltér a **Dokumentumkép-hivatkozások megoldása** beállítástól, amely csak a `.docc` katalógusokon belül érvényes. A projekttől függően használhatja az egyiket, mindkettőt vagy egyiket sem.

## Elnevezési konvenció

Helyezze el a változat fájljait **ugyanabban a mappában**, mint az elsődleges kép. A Marked négy kombinációt keres az alapnév alapján:

| Szerep | Példa fájlnév |
|------|------------------|
| Fény (1x) | `icon.png` |
| Sötét (1x) | `icon~dark.png` |
| Fény (2x) | `icon@2x.png` |
| Sötét (2x) | `icon~dark@2x.png` |

Az utótagok sorrendje rugalmas – a `icon@2x~dark.png` és a `icon~dark@2x.png` azonos módon kezelendő.

Támogatott kiterjesztések: `png`, `jpg`, `jpeg`, `gif`, `svg`, `webp` és `pdf`.

## Amit átírnak

A Marked beszkenneli a dokumentumot **az utolsó előnézeti megjelenítés előtt**:

- **Lejegyzés:** `![Alt text](images/icon.png)`
- **HTML:** `<img src="images/icon.png" alt="Alt text">`

Ha legalább **két** egyező változatfájl van a lemezen, a hivatkozás helyére egy `<picture>` blokk kerül. Elég egyetlen extra fájl – nincs szüksége mind a négy változatra.

Példa kimenet világos, sötét és @2x fájlok esetén:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/icon~dark.png 1x, images/icon~dark@2x.png 2x">
  <source srcset="images/icon.png 1x, images/icon@2x.png 2x">
  <img src="images/icon.png" alt="Alt text">
</picture>
```

Az előnézet (és a HTML-exportálás) ezután követi a felhasználó rendszermegjelenését a sötét változatoknál és az eszköz pixelsűrűségét a @2x eszközöknél.

## Ami kimaradt

A megjelölt **nem** írja át:

- Távoli URL-ek (`http://`, `https://`, `data:`)
- Hivatkozások, amelyek már egy `~dark` fájlra mutatnak
- `<img>` címkék már egy meglévő `<picture>` elemen belül
- Kiterjesztés nélküli nevek, például `![Diagram](diagram)` – a [DocC Support](DocC_Support.html) használata katalógus-stílusú hivatkozásokhoz

## Élő előnézet és fájlnézés

Változatok észlelésekor a Marked felveszi **minden létező változatfájlt** a figyelőlistájára a fő dokumentum mellé. A `icon~dark.png` külső szerkesztőben való mentése ugyanazt az élőkép újratöltését indítja el, mint a `icon.png` szerkesztése.

## Tippek

- Ha lehetséges, hivatkozzon a **light 1x** képre a forrásban (`icon.png`, nem `icon~dark.png`). Marked testvéreket fedez fel ezen az úton.
- Ha csak `@2x` eleme van, vegyen fel legalább egy másik változatot (általában `~dark`), különben a Megjelölt változat változatlanul hagyja a hivatkozást.
- A változatfelbontás a **dokumentumhoz viszonyított** elérési utat használja (vagy a beágyazott tartalmak esetén a mellékelt fájl mappáját), ugyanazokat az alapelérési szabályokat, mint a [Többfájlos dokumentumok](Multi-File_Documents.html).

## Kapcsolódó témák

- [DocC támogatás](DocC_Support.html) – kiterjesztések nélküli képnevek a `.docc` katalógusokban
- [Beállítások: Alkalmazások](Settings_Apps.html) – a DocC és a képváltozatok preferenciája
- [Előnézet](Previewing.html) – élő előnézet és fájlfrissítések