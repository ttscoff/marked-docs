<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Használja együtt két kedvenc íróeszközét.

> A Marked továbbra is tudja olvasni a Scrivener 2.0 fájlokat, de a fejlesztés a Marked 2.5.11 utáni 3-as verzióra fog koncentrálni.

## A Scrivener 3.0 alapjai

Húzzon egy Scrivener projektet (.scriv) a Marked (Megjelölt) elemre, és a rendszer lefordítja és megtekinti az előnézetet. Ha azt a lehetőséget választja, hogy .scriv fájlokat nyissa meg a Scrivenerben (fent), a Marked a Scrivener programot is elindítja, amikor a fájlt a Marked mappába húzza.

Más dokumentumokhoz hasonlóan a Scrivener-fájlok módosításai mentéskor élőben frissülnek. Továbbá, ha egy Scrivener-dokumentum az előtérben van a Marked-ben, a {% kbd cmd E %} megnyitja azt a Scrivenerben.

## Iratgyűjtő dokumentumok szűrése

Amikor megnyit egy Scrivener-projektet a Marked alkalmazásban, az előnézeti tartalom csak a kiválasztott iratgyűjtő dokumentumokból épül fel. A `.scriv` fájlok szűrése mindig aktív; a szűrőpanel csak egy kényelmes módja annak, hogy kicserélje a mellékelt tartalmat.

Nyissa meg a panelt a **Proofing > Filter Scrivener Documents** ({% kbd opt-cmd-f %}) részben. A menüelemen egy pipa látható, miközben a panel látható. A panel bezárása nem kapcsolja ki a szűrést és nem állítja vissza a beállításokat.

A szűrőpanel felsorolja a projekt kötőanyag-szakaszait (Vázlat, Kutatás és egyéb legfelső szintű iratgyűjtők a Kuka kivételével). Alapértelmezés szerint minden szakasz össze van csukva. Bontsa ki a szakaszt a dokumentumainak és mappáinak vázlatos megjelenítéséhez:

- Jelölje be a **szöveges dokumentumok** bejelölését, vagy törölje a jelölést, ha bele szeretné venni az előnézetbe, vagy kizárhatja azt.
- Kattintson egy **mappa** sorra az összes leszármazottjának kijelöléséhez vagy kijelölésének megszüntetéséhez. A kötőjel a jelölőnégyzetben azt jelenti, hogy csak néhány leszármazott van kiválasztva.
- Azok a sorok, amelyeknél a **Include in Compile** ki van kapcsolva a Scrivenerben, szürkén jelennek meg, de továbbra is ellenőrizheti őket, hogy megtekinthesse őket a Megjelölt részben.
- A **Képek, PDF-ek és egyéb, nem szöveges** kötőelemek megjelennek a listában, de nem választhatók ki.
- A **Hiányzó RTF** fájlok továbbra is megjelennek; ha tartalmat ad hozzá a Scrivenerhez, miközben a Marked nyitva van, az előnézeti frissítés a mentéskor ugyanúgy történik, mint bármely más Scrivener-módosítás.

Használja a **Select All** és **Select All** a panel tetején a teljes projekthez. Minden szakaszfejléc csak az adott szakaszhoz rendelkezik **Mind** és **Nincs** gombokkal. **Az összes kijelölésének törlése** azt jelenti, hogy a rendszer nem ellenőrzi a dokumentumokat.

Ha nincs kiválasztva, az előnézetben egy rövid üzenet jelenik meg a szűrőpanel megnyitásához vezető hivatkozással (`x-marked://scrivenerfilter`). Használhatja ezt az URL-t szkriptekben vagy más alkalmazásokban, hogy megemelje az elülső Scrivener-dokumentum paneljét a Megjelölve.

A jelölőnégyzetek kiválasztását a rendszer Scrivener-projektenként menti (az `.scrivx` fájlban található projektazonosítóval), és visszaállítja, amikor legközelebb megnyitja a projektet a Marked alkalmazásban. A projekt első megnyitásakor a Marked csak azokat a **Piszkozat** iratgyűjtő dokumentumokat választja ki, amelyek **Include in Compile** jelzője Igen (vagy nincs beállítva, amit a Scrivener Igenként kezel). A kutatás és egyéb kötőanyagok ellenőrzés nélkül indulnak el; compile-excluded Piszkozatelemek bejelöletlenül indulnak, de továbbra is kiválaszthatók a listában.

A Scrivener 2 projektek csak a **Piszkozat** kötőanyagot jelenítik meg a szűrőpanelen. A Scrivener 3 projektek minden kötőanyagot tartalmaznak, kivéve a Kukat.

A szűrőpanel nyitva maradhat más eszközök mellett, mint például a **Szóismétlés megjelenítése**. A jelölőnégyzet módosítása rövid késleltetés után újrafordítja az előnézetet; ha egy nagy projekt még mindig fordítás alatt áll, a Marked megszakítja a folyamatban lévő importálást, és újrakezdi az új kijelöléssel.

## Markdown fejlécek a Scrivener címekből

A Marked hierarchikus Markdown fejléceket is létrehozhat Önnek a Scrivener fájl oldalai alapján. Ennek engedélyezéséhez jelölje be a fent látható lehetőséget.

## MultiMarkdown metaadatok

Ha a Vázlat mappában lévő első dokumentum neve „metaadat”, akkor a rendszer MultiMarkdown metaadatként kezeli az előnézeti dokumentum elején. Ehhez a szakaszhoz a „Markdown Headers from Scrivener Titles” (Feljebb leírt) beállítástól függetlenül nem lesz beszúrva fejléc ehhez a szakaszhoz, ami lehetővé teszi a MultiMarkdown processzor számára, hogy metaadatként olvassa be, és ennek megfelelően engedélyezze a cseréket és az exportálási lehetőségeket.

Ezt a fájlt YAML-formátumúvá teheti, ha processzora YAML-t kezel.

Ha nem használ `metadata` dokumentumot, a Marked a projekt fordítási beállításaiból (`Settings/compile.xml`) is előírhatja a MultiMarkdown metaadatokat, ugyanazokat a **Cím** és **Szerző** mezőket használva, amelyeket a Scrivener a MultiMarkdownba exportál. Ez alapértelmezés szerint engedélyezve van (`scrivenerCompileMetadata` beállítási billentyű). Az egyéni metaadatmezők csak akkor jelennek meg, ha a projekt **MMD Metaadat** fordítási beállításaiban jelennek meg, nem pedig dokumentumonkénti egyéni mezőkből.

## Linkek

Külső (HTTP) hivatkozásokhoz használhatja a Markdown szintaxist vagy a Scrivener hivatkozásformázását. A Marked a feldolgozás előtt konvertálja a Scrivener formátumot Markdown formátumba.

## Megjegyzések

A Marked képes feldolgozni a dokumentumon belül létrehozott megjegyzéseket és lábjegyzeteket.

## Táblázatok

A Marked képes átalakítani az alapvető Scrivener táblákat. Ha azonban táblázatot szeretne tartalmazni a kimenetben, a legjobb, ha [MultiMarkdown táblázatformátumban] (https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#tables) teszi ezt. (A [TableFlip](http://tableflipapp.com/) nevű alkalmazás egyszerű feladattá teheti ezek létrehozását.)

## További Scrivener funkciók

Az alapvető fordítási és előnézeti funkciókon kívül a Marked néhány Scrivener-specifikus konvenciót is támogat. Először is, a Scrivener-dokumentumban használhatja a "Formázás megőrzése" funkciót soron belül vagy egy önálló szövegblokkon, és az előnézetben kódblokkokká konvertálódik.

A Marked a Scrivener _inline_ lábjegyzeteit is olvassa. Ha lábjegyzetet ad meg egy bekezdésen belül vagy a végén, az az előnézetben MultiMarkdown lábjegyzetté alakul.

## Képek használata a Scrivener dokumentumban

A képek beágyazhatók a Scrivener dokumentumba, vagy a Markdown képszintaxissal hivatkozhatnak rájuk. A képcímke Markdown verziója `![alt text](path/to/image.ext "optional title/description")`. Referencia formátum is használható:

    ![alt szöveg][img1]

    [img1]: /path/to/image.ext "opcionális leírás"

A HTML-kimenet alapútvonala az Előnézetben a Scrivener dokumentumot tartalmazó mappára lesz beállítva. Így, ha a képeket ugyanabba a mappába helyezi, mint a munkadokumentumot, akkor azok közvetlenül elérhetők. Ha a Scrivener-dokumentum a `~/Desktop/TestDoc.scriv`-ben található, és a `~/Desktop/testimage.png`-ben van egy "testimage.png" nevű kép, akkor a következő módon adhatja hozzá a képet a dokumentumhoz:

    ![Tesztkép](testimage.png)

A dokumentum szülőmappáján alapuló relatív elérési utak működni fognak, az abszolút elérési utak pedig lehetővé teszik a képekhez való hozzáférést bárhol, de előfordulhat, hogy nem hordozhatóak a HTML-kimenethez.

## Biztonsági megjegyzés

Egy gyorsítótár-mappa jön létre a ~/Library/Application Support/Marked mappában, amikor megnyitja a .scriv fájlt a Marked alkalmazásban. Ez nem védett mappa, ezért ha az eredeti dokumentum titkosított lemezen van, vagy más módon védett, vegye figyelembe, hogy a tartalma titkosítatlan lesz a gyorsítótárban. A korlátozott védelem érdekében biztosíthatja, hogy ez a gyorsítótár ne jelenjen meg a Spotlightban, ha hozzáadja a ~/Library/Application Support/Marked elemet a Spotlight adatvédelmi beállításaihoz.

Lásd: [További alkalmazásintegrációk](Additional_Application_Support.html) a vágólap előnézetéhez, a wikihivatkozásokhoz, a szkriptekhez és az alkalmazásonkénti útmutatók teljes listájához.