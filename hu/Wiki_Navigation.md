<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked tartalmaz egy wiki navigációs rendszert, amely lehetővé teszi a kapcsolódó szövegfájlok közötti gyors ugrást egyszerű `[[wiki]]` hivatkozások segítségével. Ezt a rendszert zökkenőmentes navigációra tervezték, és akkor működik a legjobban, ha úgy van beállítva, hogy az aktuális ablakban nyissa meg a hivatkozásokat.

## Optimális beállítások [optimal-settings]

A wikihivatkozás használatához engedélyezze a **Convert `[[wiki links]]`** lehetőséget a {% prefspane Preview %}-ban, és állítsa be az alapértelmezett kiterjesztést, amelyet a Marked használni fog a megfelelő fájlok keresésekor.

A legjobb élmény érdekében állítsa a **"A szövegfájlokra mutató hivatkozásoknak meg kell nyílniuk:"** beállítást *"az aktuális ablakban"* az {% prefspane Apps %}-ben. Ez biztosítja, hogy a navigáció természetesnek tűnik, és a történelem megmarad.

Ha a **A szintaktikai hibák kiemelése** engedélyezve van a {% prefspane Proofing %} alatt, akkor az aktuális könyvtárban lévő fájlnévvel nem egyező `[[wiki link]]` szintaxis piros színnel lesz kiemelve, jelezve, hogy a hivatkozott fájl nem létezik. Ezek a kiemelések a fájlok hozzáadásával frissülnek, de csak az aktuális fájl mentése vagy újratöltése után. Ha rákattint egy kiemelt hiányzó fájlhivatkozásra, a rendszer felajánlja egy új fájl létrehozását, szükség esetén hozzáfűzve az alapértelmezett kiterjesztést. Az új üres fájl megnyílik a Megjelölt mappában, és ha az Új dokumentumok szerkesztése engedélyezve van, a szerkesztő megnyílik az új fájllal.

## Hogyan működnek a Wiki hivatkozások [how-wiki-links-work]

- A **Wiki hivatkozások** a következő formátumot használják: `[[wiki link]]`.
- Ha rákattint egy wiki hivatkozásra, a Marked megkeresi a megfelelő fájlt **ugyanabban a könyvtárban**, mint az aktuális dokumentum.
- A fájlnak a Marked beállításaiban megadott kiterjesztéssel kell rendelkeznie (pl. `.md`), hacsak nem ad meg teljes fájlnevet kiterjesztéssel a linkben (pl. `[[notes.txt]]`).
- Ha a hivatkozáshoz a fájlnévtől eltérő szöveget szeretne használni, adja hozzá egy cső (`|`) után a hivatkozásban, pl. `[[wiki linking|A note about linking]]`, amely `[A note about linking](wiki-link.md)`-ként jelenik meg.
- Ha egy wikihivatkozás `#`-vel kezdődik, akkor az ugyanazon az oldalon horgonyhivatkozásként jelenik meg. A horgonynevek normalizálása kis- és nagybetűkkel, valamint az összes szóköz kötőjellel való helyettesítésével történik. Azoknál a processzoroknál, amelyek kötőjelek nélkül készítenek fejlécazonosítókat (például MultiMarkdown), pl. A `## wiki links` azonosítója `wikilinks`, ez a navigáció megszakadhat. Ilyen esetekben adja meg a megfelelő link azonosítót, szükség esetén csővel és címmel, pl. `[[#wikilinks|#wiki links]]`.

### Egyező fájlnevek [matching-file-names]

Ha olyan hivatkozást használ, mint a `[[wiki link]]`, a Marked a következő nevek bármelyikével fog keresni egy fájlt (feltételezve, hogy az alapértelmezett kiterjesztése `.md`):

- `wiki link.md`
- `WikiLink.md`
- `wiki-link.md`
- `Wiki-Link.md`
- `wiki_link.md`
- `Wiki_Link.md`
- `wikilink.md`
- `WikiLink.md`
- (és szóközök, kötőjelek, aláhúzásjelek és InterCaps egyéb kombinációi)

**A kis- és nagybetűk közötti egyeztetés nem tesz különbséget, és rugalmas elválasztókkal.**
Ha megad egy kiterjesztést a hivatkozásban (pl. `[[notes.txt]]`), a Marked pontosan azt a fájlt fogja keresni.

## Visszahivatkozások [backlinks]

Amikor egy szöveges fájlt megnyit, és a wiki navigációt engedélyezi, a könyvtár többi fájlját a rendszer a `[[links]]`-re keresi az aktuális fájlba. Ez a háttérben fog megtörténni, és a megnyitott dokumentum frissítésre kerül a visszamutató hivatkozások listájával, ha talál ilyet. A visszamutató hivatkozások megtekintéséhez a megjegyzések oldalsávjának nyitva kell lennie. Ha be van zárva, használja a Fogaskerék menüt (**Proofing->Megjegyzések megjelenítése**), vagy nyomja meg a {% kbd ^@c %} gombot a megnyitáshoz.


## Navigációs előzmények [navigation-history]

A Marked nyomon követi a navigációt a wikihivatkozásokon keresztül, lehetővé téve, hogy **hátra és előre** mozogjon a fájlelőzmények között – akárcsak egy webböngésző.

- **Vissza:** {% kbd @[ %}
- **Továbbá:** {% kbd @] %}

Az **Előzmények** menü segítségével bármelyik korábban meglátogatott fájlra ugorhat.