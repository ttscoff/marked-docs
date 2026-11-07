<!-- MT-DRAFT: machine translation; human review required -->
# <%= @title %>

Adjon egy LLM-ügynöknek egy skillfájlt, hogy fájlokat és mappákat nyisson meg a Markedben, egy Beállítások-szakaszra ugorjon, és módosítsa a beállításokat. Az ügynök a Marked [URL-kezelőjét](URL_Handler.html) használja. Külön bővítmény vagy kiszolgáló nem kell.

## A skill letöltése [download-the-skill]

{% download "SKILL.md" "Ügynök-skill fájlok megnyitásához a Markedben és beállítások módosításához. Mentse SKILL.md néven." %}

A fájl egyszerű Markdown, rövid fejléccel, amelyet az ügynök a cselekvés előtt elolvas. Ugyanezt a fájlt bármelyik ügynöknek odaadhatja, amely skillt vagy állandó utasítást fogad.

## Telepítés [install-it]

Tegye a fájlt egy, a skillről elnevezett mappába, és hagyja meg a `SKILL.md` fájlnevet.

A Cursorban mindkét hely megfelelő:

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

Az első minden projektben elérhető. A második csak arra a projektre vonatkozik. Más ügynökök ugyanazt a szöveget projektutasításként használhatják, ha nincs skillmappájuk.

A telepítés után kérje meg az ügynököt, hogy nyisson meg egy fájlt vagy mappát a Markedben. Ehhez hasonló parancsot kell futtatnia:

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

Egy mappa ugyanazt a parancsot használja. Az útvonalnak léteznie kell, a szóközöket és a többi foglalt karaktert pedig százalékosan kódolni kell. A teljes sémát, a refresh parancsot, a Streaming Previewt és a visszahívásokat is, az [URL-kezelő](URL_Handler.html) írja le.

## Beállítások [preferences]

A skill két beállítási parancsot is leír:

`pref`
: Megnyitja a Beállításokat egy megnevezett szakasznál. Az URL-ben a név angol marad, például `Preview` vagy `Style`. Nem módosít értéket.

`defaults`
: Olyan beállítást ír, amelyet a Marked már tárol, majd újratölti a nyitott előnézeteket. A `refresh=0` változatlanul hagyja az előnézeteket. Az ügynöknek olvasnia kell a jelenlegi beállításokat, mielőtt ír egyet, mert az ismeretlen kulcsot a Marked figyelmen kívül hagyja.

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## Kapcsolódó [related]

Az [Ügynöki kódolással jelölt használata](Using_Marked_with_Agentic_Coding.html) azt írja le, hogyan figyelhet egy terveket és jegyzeteket tartalmazó mappát, miközben egy ügynök írja őket. A [Command Line Utility](Command_Line_Utility.html) ugyanilyen hozzáférést ad a parancssorból, ügynök nélkül.
