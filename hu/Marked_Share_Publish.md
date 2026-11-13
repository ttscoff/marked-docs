<!-- MT draft for hu — Marked Share publish help. Review before publishing. -->
# <%= @title %>

**Marked Share** a Marked online közzétételi szolgáltatása a [share.markedapp.com](https://share.markedapp.com) címen. Csatlakoztassa egyszer a Mac-et, majd tegye közzé az elülső dokumentumot **TextPack**-ként képekkel és opcionális olvasási mód kiemelésekkel. A link birtokában bárki megtekintheti a dokumentumot az interneten.

Ez a funkció elkülönül a macOS **Megosztás bővítményétől** (a rendszer Megosztás menüje). Lásd [Using the Share Extension](Share_Extension.html), ha más alkalmazásokból fájlokat vagy kijelöléseket küldhet a Marked kifejezésbe.

## Csatlakoztassa fiókját [connect-your-account]

Az első közzététel előtt csatlakoztassa a Marked megosztási fiókjához:

1. Válassza a {% appmenu Fájl, Közzététel, Fiók csatlakoztatása… %} lehetőséget.
2. A Marked megnyitja az alapértelmezett böngészőt, és bejelentkezik a share.markedapp.com címen.
3. Miután jóváhagyta a csatlakozást, a böngésző visszatér a Marked kifejezéshez egy biztonságos bejelentkezési hivatkozással. Erősítse meg a párbeszédpanelen megjelenő fiókcímkét.

A Marked az API-tokkent és az eszközkulcsot a macOS-kulcstartóban tárolja ezen a Mac-en. A hitelesítő adatok nem íródnak naplókba vagy hibajelentésekbe.

A kapcsolat bontásához válassza a {% appmenu Fájl, Közzététel, Fiók leválasztása… %} lehetőséget. A közzétett dokumentumok online maradnak; szükség esetén bármikor visszavonhatja a hozzáférést a share.markedapp.com oldalon.

## Dokumentum közzététele [publish-a-document]

Amikor egy dokumentum meg van nyitva az előnézetben, válassza a {% appmenu Fájl, Közzététel, Közzététel… %} lehetőséget.

Amikor először tesz közzé egy dokumentumot, a Marked egy kis beállítási lapot jelenít meg:

- **Cím** – a Megosztásban látható (alapértelmezésben a dokumentum neve, kiterjesztése nélkül).
- **Láthatóság** – Privát, Nem listázott vagy Nyilvános. Az új közzétételek alapértelmezett értéke **Nem listázott** (linken keresztül elérhető, nyilvánosan nem szerepel).
- **Olvasási stílus** – Szerkesztői, Kéziratos, Svájci, Kontraszt, Írógép vagy **Nincs**. Alapértelmezés szerint a dokumentum előnézeti stílusa, amikor lehetséges. A Share ezt javaslatként használja; az olvasók felülbírálhatják. A javasolt stílus nélküli közzétételhez válassza a **Nincs** lehetőséget.
- **Kiemelések és megjegyzések szerepeltetése** – Az olvasási mód kiemelései beágyazása a TextPack kifejezésbe. Alapértelmezés szerint be van kapcsolva, ha a dokumentumban vannak kiemelések.
- **Engedélyezze másoknak az újrakeverést** – ha engedélyezve van, a megtekintők a Megosztás funkcióval bővíthetik a dokumentumot.

A Marked létrehoz egy TextPack-t a háttérben (Markdown, eszközök és opcionális `highlights.json`), feltölti, és rögzíti a megosztási URL-t ezen a Mac-en.

### Meglévő közzététel frissítése [update-an-existing-publish]

Miután egy dokumentumot összekapcsolt a Megosztással, a menüben a **Közzététel…** helyett a **Közzététel…** felirat olvasható. Válassza ki a TextPack új verziójának feltöltéséhez. A Marked elküldi a szerver tartalomkivonatát, így a rendszer észleli a másik Macről vagy az internetről végzett egyidejű szerkesztéseket.

Ha valaki más frissítette először a dokumentumot a Share funkcióval, a Marked megkérdezi, hogy **Felülírja** ezen Mac verzióval, **Megnyitás a weben** vagy **Mégse**.

## A [after-publishing] közzététele után

Amikor a közzététel befejeződik, a Marked megerősíti a sikerességet, és felajánlja:

- **Megosztási hivatkozás másolása** - {% appmenu Fájl, Közzététel, Share-link másolása %}
- **Megnyitás a weben** - {% appmenu Fájl, Közzététel, Megnyitás a weben %}

Ezek a parancsok az elülső dokumentumra vonatkoznak, ha van csatolt közzétételi rekordja.

## Közzétett dokumentumok ablak [published-documents-window]

Válassza a {% appmenu Fájl, Közzététel, Közzétett dokumentumok… %} lehetőséget a Macről közzétett és Share-fiókjával szinkronizált dokumentumok listájának megnyitásához.

Minden bejegyzésnél a következőket teheti:

- **Nyissa meg** a helyi fájlt, amikor a Marked még mindig tartalmaz hivatkozást a lemezen.
- **Importáljon** egy TextPack kifejezést, ha nincs helyi fájl (mentse bárhová, és nyissa meg a következővel: Marked).
- **Megnyitás a weben** vagy **Link másolása** a megosztási URL-hez.
- **Megjelenítés a Finderben**, ha ismert a helyi elérési út.
- A **Forget** eltávolítja a rekordot erről a Macről anélkül, hogy törölné az online dokumentumot.

Amikor csatlakozik, a lista frissül a Megosztástól. Ha offline állapotban van, vagy nincs kapcsolat, a Marked megjeleníti a gyorsítótárazott rekordokat, és felkérheti az újbóli csatlakozásra.

## Mit tehet közzé [what-you-can-publish]

A Marked által megjeleníthető bármely dokumentumot közzéteheti, beleértve a következőket:

- Mentett Markdown és szöveges fájlok
- Átmeneti előnézetek (vágólap, adatfolyam vagy nem mentett dokumentumok)
- TextBundles és egyéb támogatott formátumok

Egyszerre csak egy közzétételi művelet fut le dokumentumablakonként; feltöltés közben a menüpont le van tiltva.

## Tippek [tips]

- A közzététel tartalmazza az előnézet által hivatkozott képeket. A nagyon nagy kötegeket feltöltés előtt visszautasíthatjuk; csökkentse a beágyazott eszközök számát, ha eléri a méretkorlátot.
- A TextPack formátumban exportált kiemelések a Marked kiemelt JSON formátumát használják. A kiemelések létrehozásához és exportálásához lásd a [Reading Mode](Reading_Mode.html) részt.
- A Marked Megosztás elérhető a Direct, a Mac App Store, a Setapp és a Marked Pro verziókban. A közzétételhez külön előfizetés nem szükséges.
