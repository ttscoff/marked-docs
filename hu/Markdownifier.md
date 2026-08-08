<!-- MT-DRAFT: machine translation; human review required -->

# Markdownifier [markdownifier]

A Markdownifier egy olyan eszköz, amely automatikusan kivonja a tartalmat a weboldalakról, és tiszta Markdown formátumba konvertálja. Intelligensen dolgozza fel a webes tartalmat, hogy csak az értelmes szöveget és szerkezetet adja meg, kiszűrve a hirdetéseket, a navigációs elemeket és az egyéb zűrzavarokat.

![Markdownify URL][importurl]

  [importurl]: import-url@2x.jpg width=800 class=center

## Hogyan működik [how-it-works]

A Markdownifier fejlett tartalomkivonási algoritmusokat használ a következőkre:

1. **Nézze le és elemezze** a weboldal tartalmát
2. **Azonosítsa a fő cikk** szövegét és szerkezetét
3. **Tisztítsa meg és formázza** a tartalmat a megfelelő Markdown-ba
4. **Szűrje ki** a hirdetéseket, a navigációt és az egyéb nem tartalmi elemeket
5. **Őrizze meg** a fontos formázásokat, például fejléceket, listákat és hivatkozásokat

## A Markdownifier megnyitása [opening-the-markdownifier]

A Markdownifier eléréséhez nyissa meg a {% appmenu File, New, Markdownify URL (@~k) %} lehetőséget. Írja be a jelölni kívánt URL-t, és nyomja meg a Return ({% kbd return %}) billentyűt.

## A Markdownifier használata [using-the-markdownifier]

### Alapvető használat [basic-usage]

1. **Nyissa meg a Markdownifiert** a fenti módszerek bármelyikével
2. **Írjon be egy URL-t** a szövegmezőbe
3. **Kattintson az „Automatikus”** lehetőségre, vagy nyomja meg a `Return` gombot a tartalom kibontásához
4. A kivont tartalom **automatikusan megnyílik** egy új megjelölt dokumentumban

### Manuális tartalomválasztás [manual-content-selection]

Ha az automatikus kibontás nem rögzíti a kívánt tartalmat:

1. Kattintson a **"Kézi"** gombra az oldal webes nézetben való betöltéséhez
2. **Navigációval és görgetéssel** keresse meg a kívánt tartalmat
3. **Kattintson a weboldal felett megjelenő "Tartalom kibontása"** gombra
4. A kiválasztott tartalom Markdown-ba lesz konvertálva, és megnyílik a Marked-ben

### Vágólap integráció [clipboard-integration]

A Markdownifier megnyitásakor automatikusan észleli a vágólapon lévő URL-eket:

- Ha talál egy URL-t, az **előre kitöltve** lesz az URL mezőben
- Továbbra is rá kell kattintania az **„Automatikus”** lehetőségre, vagy meg kell nyomnia a `Return` gombot a feldolgozáshoz
- Ez megakadályozza a vágólap URL-címeinek véletlen feldolgozását

## Tartalomfeldolgozás [content-processing]

### Automatikus tartalomellenőrzés [automatic-content-validation]

A Markdownifier intelligensen ellenőrzi a kivont tartalmat, hogy biztosítsa az értelmes szöveget:

- **Strips metaadatok** (YAML frontmatter, MultiMarkdown fejlécek)
- **Eltávolítja a hivatkozásdefiníciókat** és a hivatkozási stílusú hivatkozásokat
- **Kiszűri** az önálló URL-eket és a navigációs elemeket
- **Tömöríti a szóközt** a pontos hosszbecslés érdekében
- **Minimum 200 karaktert igényel** a tényleges tartalom

Ha a kinyert tartalom túl rövid, vagy túlnyomórészt navigációnak/hirdetésnek tűnik, a Markdownifier automatikusan visszaáll kézi kiválasztási módba.

### Tartalom formázása [content-formatting]

A kivont tartalom tiszta Markdown formázása a következőkkel:

- **Forrás link** felül: `[source](original-url)`
- **H1 cím beszúrása** szükség esetén
- **Megőrzött listák** (rendezett és rendezetlen)
- **Fenntartott hivatkozások** és hangsúlyos formázás
- **Tiszta bekezdések** megfelelő térközökkel

## Biztonsági funkciók [safety-features]

### Balesetmegelőzés [crash-prevention]

A Markdownifier számos biztonsági intézkedést tartalmaz az összeomlások megelőzésére:

- **Letiltja a problémás URL-eket** (hirdetési hálózatok, nyomkövetési szolgáltatások, titkosítással kapcsolatos tartalom)
- **Szűri a sérült képeket**, amelyek renderelési problémákat okozhatnak
- **Letiltja a fejlett internetes funkciókat**, amelyek instabilitást okozhatnak
- **Automatikus összeomlás-helyreállítás** csökkentett módú tartalékkal

### Adatvédelem [privacy-protection]

- A **Privát böngészési mód** megakadályozza a követést és a cookie-kat
- **Nincs plugin vagy Java** végrehajtás a biztonság érdekében
- **Korlátozott JavaScript** kriptográfiai API-blokkolással
- **Az erőforrás-szűrés** blokkolja a nyomon követést és a hirdetéstartalmat

## Hibaelhárítás [troubleshooting]

### A tartalom nincs kivonva [content-not-extracted]

Ha az automatikus kivonás sikertelen:

1. **Próbálja ki a kézi kiválasztást** a "Kézi" gomb segítségével
2. **Ellenőrizze, hogy a webhely megköveteli-e a JavaScript használatát** – egyes webhelyeket manuálisan kell betölteni
3. **Ellenőrizze, hogy az URL** elérhető-e, és cikktartalmat tartalmaz-e
4. **Keresse meg azokat a fizetőfalakat vagy bejelentkezési követelményeket**, amelyek blokkolhatják a hozzáférést

### WebView-problémák [webview-issues]

Ha a webes nézet instabillá válik:

1. A Markdownifier **automatikusan csökkentett módba lép**
2. **A JavaScript le lesz tiltva** az összeomlások megelőzése érdekében
3. **Használja a "Konvertálás" gombot** a kézi kiválasztás helyett
4. **Zárja be, majd nyissa meg újra** a Markdownifier-t a visszaállításhoz

### Hiányzó tartalom [missing-content]

Ha fontos tartalom hiányzik a kivonatból:

1. Lehet, hogy az **automatikus algoritmus** szűrte ki
2. **Használja a kézi kiválasztást** a kívánt tartalom kiválasztásához
3. **Ellenőrizze a forrás HTML-kódot**, hogy megtudja, a tartalom dinamikusan betöltődik-e
4. **Próbáljon másik URL-t**, ha a webhely összetett szerkezetű

## Tippek a legjobb eredményekhez [tips-for-best-results]

### URL kiválasztása [url-selection]

- **Használjon cikk URL-t** a kezdőlap vagy a kategóriaoldalak helyett
- **Ha lehetséges, kerülje a nyomkövetési paraméterekkel** rendelkező URL-eket

### Tartalomminőség [content-quality]

- A **hosszabb cikkek** általában jobbak, mint a rövid bejegyzések
- A **Jól felépített tartalom** megfelelő címsorokkal működik a legjobban
- **Kerülje el az erős JavaScriptet** tartalmazó webhelyeket az automatikus kinyeréshez

### Kézi kiválasztás [manual-selection]

- **Várja meg, amíg az oldal teljesen betöltődik**, mielőtt kicsomagolja
- **Görgesse végig a tartalmat**, hogy megbizonyosodjon arról, hogy minden betöltődik
- **Vigye az egérmutatót a területek fölé** a legkisebb kék mező kiválasztásához, amely tartalmazza az összes kivonatolni kívánt tartalmat
- **Kattintson**, ha megtalálta a kívánt tartalmat

## Speciális funkciók [advanced-features]

### Kötegelt feldolgozás [batch-processing]

Amíg a Markdownifier egyszerre egy URL-t dolgoz fel, Ön a következőket teheti:

- **Várjon sorba több URL-t** a Markdownifier többszöri megnyitásával
- **Használja a Szolgáltatások integrációját** más alkalmazásokból származó URL-ek feldolgozásához
- **Másolja ki a kivont tartalmat** és illessze be a meglévő megjelölt dokumentumokba

### Integráció Markeddel [integration-with-marked]

A kivonatolt tartalom megnyílik a következővel jelölve:

- **Automatikus fájlelnevezés** a cikk címe alapján
- **Forrás URL megőrzése** a dokumentum metaadataiban
- **Teljes megjelölt képességek** az olvasáshoz és az exportáláshoz)

## Műszaki adatok [technical-details]

### Támogatott tartalomtípusok [supported-content-types]

- **HTML-cikkek** szabványos jelöléssel
- **Blogbejegyzések** és hírcikkek
- **Dokumentáció** és súgóoldalak
- **Fórumbejegyzések** és vitatartalom

### Korlátozások [limitations]

- A **fizetős oldalak** bejelentkezést és manuális kibontást igényelhetnek
- **A JavaScriptet erősen használó webhelyek** manuális kiválasztást igényelhetnek
- Az oldalbetöltés után betöltött **dinamikus tartalom** előfordulhat, hogy kimarad, de a kézi kibontással rögzíthető
- **Az összetett elrendezések** nem kívánt navigációs elemeket tartalmazhatnak

A Markdownifier célja a webtartalom kinyerése a lehető legegyszerűbb és legmegbízhatóbb legyen, miközben tartalék lehetőségeket biztosít az összetett vagy problémás webhelyek számára.