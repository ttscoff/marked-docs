<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Az Ask About Document az **Apple Intelligence** és a macOS legújabb verzióiba beépített, eszközön található nyelvi modellt használja, hogy összefoglalja a Markdown előnézetét, és megválaszolja a tartalmával kapcsolatos kérdéseket. Minden feldolgozás a Mac számítógépen történik; A dokumentum szövegét nem küldi el a Marked szerverei vagy harmadik féltől származó mesterséges intelligenciaszolgáltatások ehhez a funkcióhoz.

## Amit az Apple Intelligence nyújt [what-apple-intelligence-provides]

Az Apple Intelligence az Apple rendszere az eszközön található generatív funkciókhoz. A Marked az Apple **Foundation Models** keretrendszerét használja, hogy hozzáférjen ugyanahhoz az eszközön lévő modellhez, amely a rendszeríró eszközöket működteti, és közvetlenül a Markedben található a dokumentumközpontú feladatokhoz.

A Megjelölve elküldi a dokumentum egyszerű szövegét (a jelölés szintaxisát az egyértelműség kedvéért törölve) ennek a helyi modellnek. A modell összefoglalókat, körvonalakat és válaszokat generál az előnézeti ablak melletti lebegő panelen. Mivel a modell helyben fut, offline módban működik, miután az Apple Intelligence be van állítva, és a rendszermodell letöltése befejeződött.

Az Apple Intelligence az olyan nyelvi feladatokban a legjobb, mint az összegzés, a felvázolás, a kulcsfontosságú pontok kiemelése és a megadott szöveggel kapcsolatos kérdések megválaszolása. Ez nem egy általános kódolási segéd vagy számológép, és a nagyon hosszú dokumentumokat szakaszokban kezelik, így az eredmények a modell környezeti korlátain belül maradnak.

## Rendszerkompatibilitás [system-compatibility]

Az Ask About Document csak akkor jelenik meg, ha a Mac képes futtatni a funkciót.

**Kötelező:**

- **macOS 26 (Tahoe)** vagy újabb
- Egy **Mac Apple Intelligence támogatással** (az Apple eszközkövetelményeinek megfelelő Apple szilícium Mac-ek)
- **Az Apple Intelligence bekapcsolva** a Rendszerbeállításokban

**Nem támogatott:**

- Az Apple Intelligence programra alkalmatlanként megjelölt Intel Mac és más Mac számítógépek
- a Tahoe 26-nál korábbi macOS verziók
- Nyers **HTML-előnézetek** (a funkció Markdown és szöveges dokumentum-munkafolyamatokhoz való)

Ha a Mac megfelel a feltételeknek, de a menüelem hiányzik, győződjön meg arról, hogy az Apple Intelligence engedélyezve van, és hogy a Marked jelenlegi verzióját futtatja, amely tartalmazza ezt a funkciót. A menü a nem támogatott rendszereken teljesen el van rejtve, nem pedig letiltott állapotban.

## Az Apple Intelligence engedélyezése [enabling-apple-intelligence]

1. Nyissa meg a **Rendszerbeállítások** lehetőséget.
2. Nyissa meg az **Apple Intelligence & Siri** (vagy az **Apple Intelligence**, a macOS verziótól függően).
3. Kapcsolja be az **Apple Intelligence** szolgáltatást, és hajtsa végre az Apple által kért beállítási lépéseket.
4. Várja meg, amíg az eszközön lévő modell befejezi a letöltést, ha a rendszer kéri. Amíg a modell készen nem áll, a Marked megjelenítheti a menüelemet, de megjelenítheti azt az üzenetet, hogy az Apple Intelligence még készül.

A Megjelölt nem tartalmaz külön beállítást ehhez a funkcióhoz. Az elérhetőség a macOS által jelentett rendszermodell-állapotot követi.

## Nyitó Kérdezzen a dokumentumról [opening-ask-about-document]

Nyissa meg a panelt az alábbi módszerek bármelyikével:

- **Előnézet > Kérdezzen a dokumentumról…**
- {% kbd shift ctrl cmd I %} billentyűparancs (miközben a Markdown előnézeti dokumentum az aktív ablak)

A panel a dokumentumablak bal oldalához csatlakozik. Nyitott dokumentumra van szüksége olvasható szöveggel; üres dokumentum vagy csak HTML-előnézet nem kínálja fel a parancsot.

## A Kérdezzen a dokumentumról panel [the-ask-about-document-panel]

A panel egyszerű csevegési nézet szerint van felszerelve:

- **Előre beállított műveletek** felül a gyakori feladatokhoz
- Egy **választerület** a közepén, ahol az összefoglalók és a válaszok jelennek meg (streaming, ahogy generálják őket)
- Egy **kérdésmező** az alján, ahol egyéni kérdéseket írhat be a **Kérdezzen** és **Mégse** gombokkal

A válasz befejezése után a fókusz visszatér a kérdésmezőre, így kattintás nélkül kérhet nyomon követést.

### Előre beállított műveletek [preset-actions]

| Akció | Mit csinál |
| :-- | :-- |
| **Dokumentum összefoglalása** | A teljes dokumentum rövid összefoglalóját készíti. A hosszú dokumentumokat szakaszokba foglalják és kombinálják. |
| **A kiválasztás összefoglalása** | Csak az előnézetben kiválasztott szöveget foglalja össze. Először válassza ki a szöveget; Ellenkező esetben a Megjelölt felkéri, hogy válasszon vagy használja a Dokumentum összegzése funkciót. |
| **Vázlat** | Hierarchikus vázlatot készít a dokumentum szerkezetéről címsorok és felsoroláspontok segítségével. |
| **Kulcspontok** | Felsorolásos listaként felsorolja a dokumentum legfontosabb pontjait. |

Az előre beállított műveletekhez nincs szükség szövegre a kérdésmezőben. Kattintson egy gombra, és várja meg a választ a fenti panelen.

### Saját kérdések feltevése [asking-your-own-questions]

1. Írjon be egy kérdést a panel alján lévő mezőbe, például "Milyen problémát old meg ez a dokumentum?" vagy "Ki a célközönség?"
2. Nyomja meg a **Return** vagy kattintson a **Kérdés** gombra.
3. Olvassa el a választ, ahogy az a választerületre áramlik.

Ha kérdése van egy adott részlettel kapcsolatban, **jelölje ki azt a szöveget az előnézetben**, mielőtt feltenné. A Megjelölve a kijelölést kontextusként küldi el a teljes dokumentum helyett, amikor egy kijelölés aktív.

A folyamatban lévő kérés leállításához kattintson a **Mégse** gombra.

## Példák [examples]

### Egy hosszú cikk gyors áttekintése [quick-overview-of-a-long-article]

Nyisson meg egy hosszú blogbejegyzést vagy jelentést a Marked alkalmazásban, válassza az **Előnézet > Kérdezzen a dokumentumról…** lehetőséget, majd kattintson a **Dokumentum összegzése** lehetőségre. Használja az összefoglalót annak eldöntésére, hogy elolvassa-e a teljes darabot, vagy frissítse az emlékezetét a piszkozattól távol.

### Megjegyzések a kiválasztott bekezdéshez [notes-on-a-selected-paragraph]

Jelöljön ki egy sűrű bekezdést az előnézetben, nyissa meg a Kérdezze meg a dokumentumot, majd kattintson a **Kijelölés összegzése** lehetőségre. Hasznos, ha csak egy szakasz rövidebb változatára van szüksége.

### Szerkezeti felülvizsgálat [structural-review]

Kattintson a **Vázlat** elemre egy sok címsorral rendelkező piszkozaton, hogy megtudja, az argumentum logikusan halad-e, vagy használja a **Kulcspontok** lehetőséget, mielőtt elküldene egy dokumentumot valakinek, hogy ellenőrizze, a fő gondolatok világosak-e.

### Célzott kérdések [targeted-questions]

Ha nincs aktív kijelölés, írja be a következő kérdéseket:

- "Mi a három fő ajánlás?"
- "Ez a dokumentum említést tesz az engedélyezésről?"
- "Sorozza fel az említett dátumokat vagy határidőket."

Ha a kijelölés aktív, tegyél fel szűkebb kérdéseket, például "Mit feltételez ez a bekezdés az olvasóról?" vagy "Írja át ezt az ötletet egy mondatban" (a modell válaszol a kijelölésre; nem szerkeszti a forrásfájlt).

## Tippek és korlátozások [tips-and-limitations]

- **Adatvédelem:** A feldolgozás az Apple eszközön található modelljét használja. A Megjelölt továbbra is helyben olvassa be a dokumentum szövegét, hogy tartalmat biztosítson a modellnek; megfelelően kezelje az érzékeny anyagokat.
- **Pontosság:** Ellenőrizd a fontos tényeket a forrásoddal. A mesterséges intelligencia összefoglalói kihagyhatnak részleteket, vagy félreértelmezhetik a kétértelmű részeket.
- **Hossz:** A rendkívül hosszú dokumentumok feldolgozása darabokban történik. Az összefoglalók és válaszok közvetetten tükrözik a teljes szöveget; az egyik szakasz pontossága érdekében először válassza ki azt a szakaszt.
- **Nyelv:** Az eredmények követik az Apple Intelligence rendszermodell nyelvi lehetőségeit a Mac számítógépen.
- **Elutasítások:** A rendszer elutasíthat egyes kéréseket az Apple biztonsági irányelvei alapján.

Ha az Ask About Document nem érhető el, ellenőrizze az Apple Intelligence állapotának Rendszerbeállításait, és győződjön meg arról, hogy egy Markdown dokumentum előnézetét tekinti meg egy támogatott Macen, amelyen macOS 26 vagy újabb rendszer fut.