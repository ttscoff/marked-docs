<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A [MarsEdit][me] a bejegyzéseket az adatbázisában tárolja, nem laza fájlként a lemezen. A Marked ezért egy dedikált előnézeti munkafolyamatot használ, amely a futó MarsEdit alkalmazással kommunikál.

## MarsEdit előnézeti ablak [marsedit-preview-window]

Válassza a {% appmenu File, New, MarsEdit Preview %} lehetőséget. A Marked megkéri az AppleScriptet, hogy olvassa el a **elülső bejegyzést a MarsEditben** (a Red Sweater közvetlen, Mac App Store, Setapp és MarsEdit 4/5 csomagazonosítóit felismeri). Munka közben tartsa a MarsEdit futásban nyitott dokumentummal.

- **Kézi frissítés:** mentse a Marked előnézetéből, ha frissítést szeretne kényszeríteni.
- **Automatikus frissítések:** lehetővé teszi a megtekintést, így minden MarsEdit automatikus mentése a Megjelölve frissül.

Ha nincs elérhető bejegyzés, a Marked egy rövid hibát jelenít meg az előnézetben az elavult szöveg helyett.

### Kibővített bejegyzések [extended-posts]

A MarsEdit **extended** mezőjének tartalma a Marked előnézetében és forrásában WordPress-stílusú `<!--more-->` elválasztóval van elválasztva, így az oldalszámozás-orientált webhelyek (WordPress, Jekyll stb.) továbbra is látják a törést. A megjegyzés máshol ártalmatlan.

### Címkék és kategóriák a metaadatokban [tags-and-categories-in-metadata]

A MarsEdit címkéi és kategóriái a MultiMarkdown metaadatblokknak vannak kitéve. A MultiMarkdown processzorral ({% prefspane Processor %}) például hivatkozhat rájuk:

    Címkézve: [%tags]
    Közzétéve: [%categories]

[me]: https://www.red-sweater.com/marsedit/