# <%= @title %>

A FerventMind-térképek (`.fvmd`) megnyílnak a Markedben. A Marked kicsomagolja a csomagot. Ha van benne `text.md`, az a fájl az előnézet. Ha nincs, a Marked a `map.xml` alapján vázlatot készít.

## Vázlat a térképből [outline-from-the-map]

A témák szövege címsor lesz a **Headings through level** beállítás szintjéig (alapértelmezés szerint 2). A mélyebb témák beágyazott felsorolások lesznek, így az ott lévő feladatok megtartják a lista jelölőnégyzetét. A jegyzetek a szakasz törzsévé válnak. A kész feladat bejelölt négyzet, a részleges feladat pedig a százalékát mutatja. A képek az `assets/` alatti fájlok, fájlnévből álló képaláírás nélkül.

## Csak a látható témák [display-only-visible-topics]

A **Display only visible topics** a {% prefspane Apps %} *FerventMind* csoportjában kihagyja az összehajtott ágban lévő témákat, amikor a Marked elkészíti a vázlatot. A térképben már mentett `text.md` fájlt nem módosítja.

## Térkép beillesztése [including-a-map]

Egy `.fvmd` beillesztése a **FerventMind files** jelölőnégyzetet használja az **Embed as Mermaid mind maps:** csoportban, a {% prefspane Apps %} lapon. Bekapcsolva a látható vagy a teljes fa Mermaid-diagramja készül, a fenti jelölőnégyzet szerint. Kikapcsolva a térkép `preview.png` képe ágyazódik be. Lásd: [Mindtérképek és körvonalak beágyazása](Embedding_Mind_Maps_and_Outlines.html).

## Megnyitás a szerkesztőben [open-in-editor]

Az **Open in Editor** ({% kbd cmd E %}) elindítja a FerventMindet.
