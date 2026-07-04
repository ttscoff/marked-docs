<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

{% apponly div %}
*A dokumentáció legfrissebb verziójához keresse fel az [online verzió][súgót].*
{% endapponly %}

**Mindenképpen nézze meg a [Megjelölt oktatóvideók] (https://www.youtube.com/playlist?list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ) növekvő gyűjteményét.**

## Mi az a Markdown?

[daringfireball]: http://daringfireball.net/projects/markdown/basics
[mmd5]: https://fletcher.github.io/MultiMarkdown-5/
[mdguide]: https://www.markdownguide.org/
[help]: http://markedapp.com/help/

A Markdown egy egyszerű szimbólumokat használó alapvető jelölőnyelv, amely lehetővé teszi HTML írását (és más formátumokba exportálását) egyszerű szintaxissal, például `*italics*` és `**bold**`. A Markdownt John Gruber hozta létre, és gyorsan a webes publikálás, a jegyzetelés, sőt a könyvkiadás defacto szabványává válik. Lehetővé teszi, hogy egy csomó eszköztár és formázási hegedülés nélkül írjon, csak szavakat jelenít meg az oldalon, és hagyja, hogy a processzorok (például a Marked) kezeljék a stílust és a formázást.

A Marked együttműködik a GitHub Flavored Markdown, CommonMark (GFM), Kramdown és MultiMarkdown szoftverekkel, és több változat szintaxisát is konvertálhatja előnézethez (kibővíthető úgy, hogy szinte bármilyen processzorral működjön, amire szüksége van, beleértve a Textile-t, a reStructuredText-et, a Wikitextet és egyebeket). Feltételezem, hogy --- mivel Ön itt van --- tudja, mi az a jelölőnyelvek közül legalább egy. Ha nem, kezdje el John Gruber [Markdown Basics][daringfireball] oldalán, nézze meg a [MarkdownGuide.org][mdguide] oldalt. A Marked teljes Markdown szintaktikai útmutatót tartalmaz a súgó menüben.

A [Markdown Dingus](x-marked-3://dingus) segítségével kísérletezhet a Markdown által támogatott különböző ízekkel.

## Mi van megjelölve?

A Marked egy élő Markdown előnézeti alkalmazás macOS-hez --- egy szerkesztő-agnosztikus (Multi)Markdown Preview alkalmazás, amely figyeli a fájl módosításait, és minden mentéskor frissíti az előnézetet. A formázás részleteinek szétválasztása és automatizálása lehetővé teszi, hogy többet összpontosítson az írásra és kevésbé a prezentációra, miközben továbbra is figyelemmel kíséri a végterméket.

A beállítási munkafolyamatokról és a szerkesztő-specifikus gyorsindításokról lásd: [Élő Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html). A termék rövidebb áttekintéséért látogasson el a [markedapp.com/markdown-preview] oldalra (https://markedapp.com/markdown-preview/).

A Megjelölt bármely helyileg elérhető fájllal működik, beleértve az iCloud dokumentumokat is. Csak húzzon egy szöveges dokumentumot bármelyik szerkesztő eszköztáráról a Megjelölt elemre, és az HTML-előnézetként jeleníti meg, és elkezdi követni a változásokat, és írás közben frissíti az előnézetet. Még [többfájlos dokumentumokat](Multi-File_Documents.html) is le tud fordítani egy alapvető „include” szintaxis használatával, vagy Scrivener, Leanpub és mmd_merge indexformátumokból.

A Marked további funkciókkal rendelkezik, beleértve a szószámot és más dokumentumstatisztikát, képes más alkalmazások felett lebegni, vagy elhalványulni a háttérben, és számos jól kidolgozott stílusban megjelenítheti a munkáit. Nyomtatható vagy PDF, Word dokumentumok, teljes HTML-dokumentumok (stílusok és képek) formájában, vagy HTML-forrás- vagy RTF-adatokat másolhat a vágólapra egy billentyűleütéssel. A Marked rendelkezik egy alapvető AppleScript szótárral és egy [URL-kezelővel](URL_Handler.html) is, amelyek megkönnyítik a munkafolyamatba való integrálását.

Igen, és működik egy csomó kedvenc alkalmazásoddal: szövegszerkesztőkkel a Vimtől és az Emacs-től a Sublime Text és TextMate-ig, Markdown szerkesztők, mint a MultiMarkdown Composer, Byword és iA Writer, még olyan alkalmazások is, amelyekre talán nem is számítasz, mint például az Ulysses, a Scrivener, a VoodooPad, a MarsEdit és még sok más.

## Felhasználási példa

A Marked bármely szövegszerkesztőt Markdown-kompatibilis szerkesztővé változtat. Az előnézet mindig elérhető, és munka közben frissül.

* Ha kedvenc szerkesztője nem kínál élő Markdown előnézetet, nyissa meg a dokumentumot, amelyen dolgozik, a Marked alkalmazásban, és úsztassa le az ablakot oldalra a teljes értékű Markdown írási élmény érdekében.
* Szeret írni vagy blogolni MacVim vagy más terminál alapú szerkesztőben? Most már van egy szinkronizált Markdown előnézete munka közben.
* A Marked a meglévő Markdown előnézeten felül és azon túlmenően is kínál megjelenítési lehetőségeket, és ehelyett használható teljes szószám és dokumentumstatisztika, írási javaslatok biztosítására, és még a Markdown formázási hibáinak kiemelésére is.
* A Marked szerkesztő nélkül is használható. Csak húzza a Markdown fájlokat az ikonra az előnézetük megtekintéséhez, kinyomtatásához és PDF, DOC, RTF vagy HTML forráskódba exportáláshoz. A megjelölt **megnyithat `.rtf` és `.rtfd` fájlokat** is forrásdokumentumként ([RTF és RTFD támogatás](RTF_Support.html)).
* Az automatikus mentést végző alkalmazásokban az előnézet minden segítség nélkül lépést tart az írással. Használja bármelyik szerkesztővel... vagy az összes* szerkesztővel.
* Könyvet írni? A Marked több fájlt is összeállíthat a munkája teljes előnézetéhez, és még a mellékelt fájlok változásait is meg tudja nézni, és minden mentéskor frissíti a fő dokumentumot. Akár egy egész mappát is meg tud nézni a változások miatt, és automatikusan átváltja az előnézetet az éppen frissített fájlra. Ha készen áll, közzéteheti EPUB, DOCX vagy TextBundle formátumban.
* AI kódoló platformmal dolgozik? Nyisson meg egy tervet vagy dokumentációs mappát a Marked alkalmazásban, és amikor a mappában lévő Markdown fájl megváltozik, a Marked megjeleníti azt, és automatikusan a legutóbbi szerkesztés pontjáig görget. A Marked Sellő diagramokat jelenít meg, és mindenféle kiterjesztett szintaxist képes kezelni. Kövesse nyomon a terveket és a dokumentációt munka közben, anélkül, hogy váltana a fájlok között.