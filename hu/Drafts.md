<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A [Piszkozatok][piszkozatok] Mac rendszeren tükrözhetik az aktív piszkozatot a Marked-be a **Megjelölt streamelési előnézet** használatával – ez ugyanaz a vágólap-alapú csatorna, amelyet a [Streaming Preview](Streaming_Preview.html) részben leírtak. Az aktuális piszkozatot egyszer elküldheted egy közösségi **művelettel** (nincs élő frissítés, amíg újra nem futtatod).

## Streaming előnézet (piszkozatok Machez) [streaming-preview-drafts-for-mac]

1. A Megjelölt területen válassza a {% appmenu File, New, Streaming Preview %} lehetőséget, hogy készen álljon a streaming előnézeti ablaka.
2. A **Piszkozatok Machez** alkalmazásban nyissa meg a **Beállítások** lehetőséget, és engedélyezze a **Megjelölt alkalmazás-streamelési előnézet támogatásának engedélyezése** lehetőséget.
3. Használja a **Megjelölt megnyitása** lehetőséget, ha a Piszkozatok felkínálja a Marked előrehozását, majd szerkessze a Piszkozatokban; az előnézet frissül, ahogy a vázlat módosul.

![][draftsprefs]

Ha ez a lehetőség be van kapcsolva, a Piszkozatok a Markdown funkciót a Marked értékre tolja a Marked exponált integráción keresztül a streamelési előnézetekhez (ahelyett, hogy a lemezen lévő fájlt nézné meg).

### Legyen megjelölve [get-marked]

Ha a **Get Marked App** megjelenik a Piszkozatok beállítási lapján, akkor használja, ha a Marked még nincs telepítve.

## Előnézet a Megjelölt műveletben (kézi frissítés) [preview-in-marked-action-manual-refresh]

Telepítse a [**Preview in Marked**](https://actions.getdrafts.com/a/11f) közösségi műveletet a Piszkozatok könyvtárból. Az **aktuális piszkozatszöveget** elküldi a Marked-nek egy `x-marked://preview?text=…` URL használatával (a piszkozatok helyettesítik a piszkozat tartalmát). **A tartalom nem frissül élőben**: futtassa újra a műveletet, amikor azt szeretné, hogy a Megjelölt egyezzen a piszkozattal.

Ez a megközelítés alkalmankénti ellenőrzéseknél hasznos, míg a **streaming előnézet** megfelel a folyamatos írási munkameneteknek.

A Piszkozatok iPhone-on és iPaden is futnak; Az itt dokumentált streaming előnézeti integráció a **Piszkozatok Mac-hez** alkalmazásra vonatkozik, amelyen ugyanazon a Mac-en található Marked.

[draftsprefs]: images/Drafts_streaming_preview_preference.png width=842px height=182px class=center

[drafts]: https://getdrafts.com/