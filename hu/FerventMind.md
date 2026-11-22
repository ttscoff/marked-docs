# <%= @title %>

A FerventMind-térképek (`.fvmd`) megnyílnak a Markedben. A Marked kicsomagolja a csomagot, és a FerventMind által mentett `text.md` fájlt mutatja.

## Markdown a térképben [markdown-in-the-map]

A Markdown megírását a FerventMindben, a **Settings > Files And Export** alatt, a **Markdown** csoportban lehet beállítani. A Marked a fájlt úgy jeleníti meg, ahogy el lett mentve.

![FerventMind Files And Export][fm-export]

A **Headings** határozza meg, hány szint marad címsor. A **Visible topics only** kihagyja az összehajtott ágban lévő témákat. A **Notes** és a **Task checkboxes** dönti el, hogy a jegyzetek és a feladatok bekerülnek-e a Markdownba. Ezek a beállítások a Markdown-exportálásra, a Copy As műveletre és a minden térképben elmentett Markdown-másolatra vonatkoznak, olyan alkalmazásokhoz, mint a Marked. Egy térkép felülírhatja őket a **Definitions • MAP** alatt.

Ha egy régebbi térképben nincs `text.md`, a Marked a `map.xml` alapján készít vázlatot: a cím az 1. címsor, a következő szint a 2. címsor, a mélyebb témák pedig beágyazott felsorolások. A jegyzetek a szakasz törzsévé válnak. A kész feladat bejelölt négyzet, a részleges feladat pedig a százalékát mutatja. A képek az `assets/` alatti fájlok, fájlnévből álló képaláírás nélkül.

## Térkép beillesztése [including-a-map]

Egy `.fvmd` beillesztése a **FerventMind files** jelölőnégyzetet használja az **Embed as Mermaid mind maps:** csoportban, a {% prefspane Apps %} lapon. Bekapcsolva a térképből Mermaid-diagram készül. Kikapcsolva a térkép `preview.png` képe ágyazódik be. Lásd: [Mindtérképek és körvonalak beágyazása](Embedding_Mind_Maps_and_Outlines.html).

## Megnyitás a szerkesztőben [open-in-editor]

Az **Open in Editor** ({% kbd cmd E %}) elindítja a FerventMindet.

[fm-export]: images/screenshots/ferventmind-files-and-export.jpg @2x width=808px height=640px
