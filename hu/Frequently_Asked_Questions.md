<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %> [toc]

## A licenckódot már felhasználták [license_code_has_already_been_utilized]

Ha újonnan telepíti a Marked 2-t, és a „Licenckódot már felhasználtuk” hibaüzenet jelenik meg a licenc megadásakor, kérjük, <a href="mailto:me@brettterpstra.com">vegye fel velem a kapcsolatot</a>, és kérjen új licencet. **Kérjük, adja meg az e-mail címét, amellyel regisztrált, és/vagy a jelenlegi licenckódját.**

A Marked számára generált korai licencek használati korláttal rendelkeztek a gépi korlát helyett, így 3 telepítés ---még ugyanazon a gépen is ---aktiválásokat használna. Ezeket a határértékeket az újabban generált licencekben kijavították. A Marked 2 licenc megvásárlása lehetővé teszi a Marked 2 telepítését bármely saját gépére, ezért ne habozzon cserét kérni, ha problémákba ütközik.

[Tartalomjegyzék](#toc)

## Webhelylicencek és oktatási kedvezmények [site_licenses_and_educational_discounts]

Kedvezményes webhely-/tömeges licencek állnak rendelkezésre a Marked 2 számára. Vásárlási link kéréséhez, kérjük, lépjen kapcsolatba <a href="mailto:me@brettterpstra.com">Bretttel</a>, és adja meg a megvásárolni kívánt licencek számát.

**Kedvezmények**

- 5-9: **10% kedvezmény**
- 10-19: **12% kedvezmény**
- 20-49: **15% kedvezmény**
- 50+: **20% kedvezmény**

Oktatási kedvezmény is elérhető mind a közvetlen, mind a Mac App Store verzióhoz. A Mac App Store esetében a szabványos Apple oktatási kedvezmények engedélyezettek. Ha oktatási kedvezménnyel szeretne közvetlen verziót vásárolni, <a href="mailto:me@brettterpstra.com">vegye fel velem a kapcsolatot</a>, és kérjen kupont.

[Tartalomjegyzék](#toc)

## Az URL nem érvényesül, vagy „ismeretlen” értéket ad vissza [a_url_wont_validate_or_returns_unknown]

A Marked [link validation] (http://marked2app.com/help/Link_Validation.html) egy alapvető HEAD kérést használ annak meghatározására, hogy egy hivatkozás érvényes-e. A 200-as (sikeres) eredménytől eltérő minden vagy ismeretlent, vagy hibát ad, ha ez egy gyakori hibakód, például 404 (nem található) vagy 500 (szerverhiba). A hitelesítés mögött meghúzódó URL-ek (például Apple Developer URL-ek vagy bármi, amihez bejelentkezés szükséges) az „ismeretlen” értéket adják vissza, csakúgy, mint bizonyos webhelyek, például az Amazon.com, ahol a szerver bizarr válaszkódokat ad vissza. Marked nem sokat tehet ez ellen.

[Tartalomjegyzék](#toc)

## Egyéni processzorengedélyek a MAS-verzióban [custom_processor_permissions_in_mas_version]

A sandbox korlátozások miatt a Marked 2 Mac App Store verziója nem tud bizonyos típusú bináris eszközöket egyéni processzorként végrehajtani. Ha ebbe a korlátozásba ütközik, néhány lépést kipróbálhat.

1. Győződjön meg arról, hogy a **Speciális** panelen belépett a **Megjelölt 2** Beállításokba (⌘,), és rákattintott az "Engedélyek frissítése" lehetőségre. Ez megpróbálja a Megjelölt hozzáférést biztosítani a teljes alapértelmezett meghajtóhoz, kiküszöbölve a szkriptekkel és segédprogramokkal kapcsolatos problémákat, amelyeknek hozzá kell férniük az ideiglenes mappákhoz és a nem alapértelmezett helyekhez.
2. Próbáljon meg egy szkriptet. Hivatkozzon a futtatni kívánt segédprogramra (multimarkdown, kramdown stb.) egy shell szkriptben. Lehet bash, Ruby, Perl vagy Python szkript. Ezután a Speciális beállításokban állítsa be a processzort a kapcsolódó héjra vagy végrehajtható fájlra, a paramétereket pedig a szkript helyére. Például létrehozhatok egy bash szkriptet a ~/scripts/mmd_wrapper.sh címre mentve:
    
        #!/bin/bash
        macska | /usr/local/bin/multimarkdown
    
    Ezután tegye végrehajthatóvá (`chmod a+x ~/scripts/mmd_wrapper.sh`), és állítsa be az egyéni processzor beállításaimat:

        Processzor: /bin/bash
        Érvek: /Users/me/scripts/mmd_wrapper.sh
3. Egyes végrehajtható fájlok (különösen a Pandoc) egyszerűen nem működnek a sandboxon belül. Ebben az esetben vegye fel velem a kapcsolatot a végrehajtáskor megjelenő hibaablakon keresztül, hogy megkapja a crossgrade licencet a közvetlen verzióra.

[Tartalomjegyzék](#toc)

## Dokumentumon belüli hivatkozások az exportált PDF-ekben [intra-document_links_in_exported_pdfs]

A Marked PDF-exportálása jelenleg a WebKit nyomtatási funkcióit használja. Ennek egyik következménye, hogy a dokumentumon belüli (belső) hivatkozások, beleértve a tartalomjegyzékben lévőket is, nem ugranak a dokumentum más pontjaira. Úgy tűnik, ezt nem az Apple-nek szándékában áll kijavítani a WebKit Marked 2 által használt verziójában.

Egyes esetekben jó eredményeket érhet el, ha HTML-t exportál a beágyazott stílussal, majd a webböngészővel nyomtat PDF-be. Nem fogja megkapni a Marked összes exportálási funkcióját, de általában kap egy PDF-t működő belső hivatkozásokkal. Ez egyelőre kompromisszum.

[Tartalomjegyzék](#toc)

## Relatív elérési utak a mellékelt fájlokban [relative_paths_in_included_files]

A Marked [include syntax][include], valamint a [Scrivener files][scriv] használatával bevitt fájlok relatív elérési utakat használhatnak más fájlok hivatkozására. (_**Megjegyzés:** ez nem vonatkozik az IA Writer `/file` szintaxisát vagy CSV-fájlokat használó fájlokra_). A legújabb verzióktól (2.5.10+) ezek az elérési utak _a mellékelt fájlhoz_ vonatkoznak, nem az alapfájlhoz.

Adott egy ilyen fájl/mappa szerkezet:

    - base_file.md
    - almappa
        - include_file.md
    - képek
        - kép1.jpg

Ha az `included_file.md` egy relatív elérési úton hivatkozik az image1.jpg-re, akkor a következőképpen kell írni: `../images/image1.jpg`, _not_ `images/image1.jpg`. (`..` a szülőkönyvtárat jelöli) .

[include]: http://marked2app.com/help/Multi-File_Documents.html
[scriv]: http://marked2app.com/help/Scrivener_Support.html

[Tartalomjegyzék](#toc)

## Hogyan szerezhetem vissza az elveszett licencet (közvetlen verzió) [how_do_i_retrieve_a_lost_license_direct_version]

Ha elvesztette a Marked 2-höz a Paddle-n keresztül vásárolt licencét, a [my.paddle.com] oldalon (https://my.paddle.com/) visszakeresheti. Ha problémái vannak a bejelentkezéssel, privát kéréssel kérhet keresést a [támogatási oldalon](http://support.markedapp.com).

[Tartalomjegyzék](#toc)

## Alkalmazáson belüli vásárlási problémák (Error Domain=Paddle Code=0 "(null)") [in-app_purchase_issues_error_domainpaddle_code0_null]

A Paddle nemrég arról tájékoztatott, hogy az IAP-k meghibásodtak, és nem tervezik a javítást, mert nem elég fejlesztő implementálta őket. (Ami éppolyan frusztráló számomra, mint neked.) Az igazán frusztráló az, hogy nem hagyták abba a fizetést, ezért manuálisan vissza kell térítenem a vásárlásokat, amíg nem tesznek valamit az engedélyek kezelésével kapcsolatban. Egy új rendszer állítólag a következő hetekben fog megjelenni, így ha hajlandó várni, mindent megteszek annak érdekében, hogy a helyesírási/nyelvtani IAP összes jelenlegi vásárlása megfeleljen a következő rendszernek.

Ha inkább a visszatérítést részesíti előnyben, egyszerűen <a href="mailto:me@brettterpstra.com">küldjön nekem e-mailt közvetlenül</a> a licenchez használt e-mail fiókkal vagy a nyugtán szereplő tranzakcióazonosítóval.

**Frissítés:** A Paddle hivatalosan is bejelentette az új IAP-megoldást, és amint nyilvánosan elérhető lesz, bevezetésre kerül. A jelenlegi alkalmazáson belüli vásárlási licencek (Helyesírás/Nyelvtan) automatikusan áttelepítésre kerülnek, és új kuponkódot kapnak. Ennek hamarosan meg kell történnie.

[Tartalomjegyzék](#toc)

## Bekerített kódblokkok a behúzott kódblokkok belsejében [fenced_code_blocks_inside_indented_code_blocks]

Meglehetősen ritka esetekben érdemes bemutatni egy bekerített kódblokk kerítését. Általában ezt a Markdown-ban úgy lehet elérni, hogy behúzza a bekerített kódot, és egy behúzott "szó szerinti" blokkot kényszerít, amely tartalmazza a bekerített kódblokkot, amely ezután feldolgozás nélkül marad. A Marked eltérően kezeli a bekerített kódot (a több szintaxisopcióval való együttműködés részeként), ezért ennek eléréséhez dupla kerítést kell használni. Mivel tetszőleges számú backtick-et vagy hullámvonalat használhat egy kódblokk elkerítéséhez (amíg a nyitás és a záró számlálás megegyezik, csak két különböző hosszúságú kerítést használhat. Például

    ````".
    ```
    Valóságos elkerített kód
    ```
    `````

[Tartalomjegyzék](#toc)