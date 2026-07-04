<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A [VoodooPad][vp] minden oldalt egyetlen adatbázisfájlba köt. Húzza a `.vpdoc`-t a Megjelölt elemre, hogy megtekinthesse a VoodooPad aktuálisan legelső oldalát; használja a {% kbd cmd S %}-t a VoodooPadben, amikor meg kell jelölnie a lemezről való újratöltést.

A Marked figyeli a dokumentumot a lemezen, és felcseréli az előnézetet, amikor oldalt vált a VoodooPadben.

## Beágyazott képek

Ha a képekre Markdown vagy HTML használatával hivatkozik, és a bináris **belül** a VoodooPad adatbázisban él, a Marked ki tudja bontani az előnézethez. A csak **álnevek** (hivatkozással behúzott fájlok) nem tárolódnak a kötegben – mutasson azokra a képekre, amelyeknek abszolút elérési útja vagy a lemezen lévő `.vpdoc`-hoz viszonyított elérési útja van, hogy a Marked fel tudja oldani őket.

[vp]: https://www.voodoopad.com/