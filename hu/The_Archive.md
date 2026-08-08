<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Az [Archívum][archívum] a jegyzeteit fájlként tárolja a lemezen, és közvetlenül tükrözheti a szerkesztett jegyzeteket a Marked **streaming előnézet** csatornájában.

## Az adatfolyam előnézete megjelölve [stream-preview-to-marked]

1. A Megjelölt területen nyissa meg a {% appmenu File, New, Streaming Preview %} elemet (vagy használjon újra egy meglévő streaming előnézeti ablakot).
2. Váltson az Archívumra, és válassza a **Jegyzet → Megjelölt adatfolyam előnézete** lehetőséget, hogy az Archívum aktiválja a Megjelölt funkciót, és megkezdje a legelső jegyzetszöveg küldését.

Megjelölt frissítések gépelés közben az Archívumban, ugyanazt a `mkStreamingPreview` vágólapra vonatkozó szerződést követve, mint a többi integrált alkalmazások esetében – lásd a [Technikai részletek](Streaming_Preview.html#developers) részt a [Streaming előnézet](Streaming_Preview.html) alatt.

Ha az előnézetek elavultnak tűnnek, ellenőrizze, hogy a streamelési ablak továbbra is a legelső helyen van-e a Megjelölve, és kapcsolja be egyszer az Archiválás menüparancsot.

[archive]: https://www.zettelkasten.de/the-archive/