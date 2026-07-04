<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A [Curio][curio] egy vizuális ötletbörze és jegyzetelő alkalmazás, amely a szerkesztett elemet streamelheti a Marked **streaming előnézet** csatornájára.

## Stream Kijelölve megjelölve

1. A Megjelölt területen válassza a {% appmenu File, New, Streaming Preview %} lehetőséget, hogy készen álljon a streaming előnézeti ablaka.
2. A Curio programban kapcsolja be a **Nézet → Megjelölt adatfolyam** lehetőséget.

Ha duplán kattint egy ábra, jegyzet, lista vagy más elem szerkesztéséhez a Curio alkalmazásban, a jelölés a streaming előnézetéhez folyik, és írás közben frissül.

A megjelölt frissítések szinte valós időben, ugyanazt a `mkStreamingPreview` vágólapra vonatkozó szerződést követve, mint más integrált alkalmazásoknál – lásd a [Technikai részletek](Streaming_Preview.html#developers) részt a [Streaming előnézet](Streaming_Preview.html) alatt.

Ha az előnézetek frissítése leáll, győződjön meg arról, hogy a streamelés előnézeti ablaka meg van nyitva a Megjelölt menüben, és egyszer a Curio alkalmazásban kapcsolja a **Kijelölt adatfolyam megjelöltre** lehetőséget.

[curio]: https://www.zengobi.com/products/curio/