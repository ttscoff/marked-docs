<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Megjelölt megérti az [Apple DocC](https://www.swift.org/documentation/docc/) dokumentációkatalógusait (`.docc` csomagokat). A katalóguson belül vagy mellett található Markdown előnézetének megtekintésekor a Marked fel tudja oldani a **kiterjesztés nélküli** képhivatkozásokat a katalógus `Resources` mappájában található fájlokra – beleértve a `~dark` és `@2x` változatokat is.

A **fájlkiterjesztésű útvonalakat** (`images/icon.png`) használó normál Markdown dokumentumokhoz lásd: [Képváltozatok](Image_Variants.html). Ez a funkció mindenhol működik; A DocC felbontás katalógus-specifikus.

## DocC felbontás engedélyezése

A {% prefspane Apps %} mezőben engedélyezze a **Dokumentumkép-hivatkozások feloldása** lehetőséget (alapértelmezés szerint be van kapcsolva).

A DocC-észlelés akkor fut le, amikor a Marked megtalálja a megnyitott dokumentum `.docc` katalógus-elődjét. Nincs szükség speciális URL-sémára vagy Xcode-integrációra – nyissa meg a katalógus Markdown elemét ugyanúgy, mint bármely más fájlt.

## Kiterjesztés nélküli hivatkozások

A DocC-katalógusban a szerzők általában képekre hivatkoznak **elérési út vagy kiterjesztés nélkül:

```markdown
![Order flow](OrderStateTransitions)
```

A Marked a `OrderStateTransitions`-től `Resources/OrderStateTransitions.png`-ig (vagy más támogatott típusig) felel meg, ha az adott fájl létezik a katalógusban.

Azok a hivatkozások, amelyek már tartalmaznak elérési utat és kiterjesztést – `images/chart.png` – helyette az [Image Variants](Image_Variants.html)-re maradnak, és a DocC felbontás nem írja át őket.

## Sötét mód és Retina változatok

A DocC katalógusok gyakran több fájlt is szállítanak képenként:

| Szerep | Példa itt: `Resources/` |
|------|--------------------------|
| Fény (1x) | `diagram.png` |
| Sötét (1x) | `diagram~dark.png` |
| Fény (2x) | `diagram@2x.png` |
| Sötét (2x) | `diagram~dark@2x.png` |

Ha egynél több változat létezik, a Marked ugyanazt a reszponzív `<picture>` jelölést bocsát ki, amelyet a [Képváltozatok](Image_Variants.html) részben leírtak. Az egyfájlos hivatkozás továbbra is normál `<img>` vagy `![](Resources/...)` elérési útra oldódik fel.

## HTML és Markdown

A DocC felbontás a Marked bekerülési engedélye alatt érvényes:

- **Jelölési források** — `![alt](ImageName)` hivatkozás
- **HTML-források** - `<img src="ImageName">` kiterjesztés nélkül

Mindkettő frissül az előnézeti megjelenítés előtt.

## Fájlnézés

A katalógus `Resources` mappa alatt lévő megoldott képek hozzáadódnak a Marked figyelőlistájához. Egy változatfájl külső szerkesztése manuális frissítés nélkül frissíti az előnézetet.

## Kapcsolódó témák

- [Image Variants](Image_Variants.html) — `~dark` és `@2x` észlelés a kiterjesztés alapú elérési utakhoz bármely projektben
- [Xcode Playgrounds](Xcode_Playgrounds.html) – Swift játszótér kommentár előnézete
- [Beállítások: Alkalmazások](Settings_Apps.html) — DocC és képváltozatok beállításai