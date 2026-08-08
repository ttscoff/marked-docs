<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A megjelölve közvetlenül megnyithatja a Rich Text formátumú (`.rtf`) és az RTFD (`.rtfd`) dokumentumokat. Húzzon egy fájlt a Megjelölt elemre, vagy használja a {% appmenu File, Open... ({{cmd}}O) %} gombot. A dokumentumot Markdown formátumba konvertálja az előnézet és az exportálás céljából.

Ez jól működik a **Pages**, **TextEdit**, **Word** és más RTF- vagy RTFD-mentő alkalmazások dokumentumaival. A Megjelölt továbbra is egy **előnézeti** eszköz: az eredeti alkalmazásban szerkesztheti, a Megjelölt frissítések pedig mentéskor.

## Hogyan működik az átalakítás [how-conversion-works]

A Marked az RTF-et HTML-vé konvertálja a rendszerszöveg-motor segítségével, majd Markdown-ba. Az átalakító:

- A **nagy bekezdésbetűméreteket** leképezi a címsorok szintjére (a dokumentum leggyakoribb törzsméretéhez viszonyítva)
- Ahol lehetséges, megőrzi a **félkövér**, *dőlt betűket* és a hivatkozásokat
- Kivonja a **képeket** az RTFD-csomagokból és a beágyazott mellékletekből
- **nem** kezeli az RTF fájlneveket képfeliratként (lásd a lenti képeket)

Ugyanezt a konverziós folyamatot használják a Scrivener RTF fordításához és az egyéb dokumentumokban található RTF-fájlokhoz.

## Élő előnézet [live-preview]

Amikor egy másik alkalmazásba menti az RTF- vagy RTFD-fájlt, a Marked észleli a változást, és automatikusan frissíti az előnézetet.

## Képek [images]

Az RTF nem határoz meg külön "felirat" mezőt a Cocoa által HTML-be exportált módon. Ami az elrendezésben feliratnak tűnik, az általában **normál szöveg** a következő bekezdésben, és a Megjelölve ezt törzsszövegként tartja meg.

A beágyazott képek és az RTFD-kötegekben lévő képek (például `pastedGraphic.png` az oldalak exportálásánál) az `~/Library/Caches/Marked/Watchers/` alatti gyorsítótár mappájába másolódnak. Az előnézeti kép elérési útja azokra a gyorsítótárazott fájlokra mutat, amíg nem exportálja.

A megjelölt **nem** használja a képfájl nevét alternatív szövegként vagy MultiMarkdown ábrafeliratként. A kép alatt nem szabad látnia a `pastedGraphic.png` jelet, hacsak nem írta be ezt a szöveget a dokumentumba.

## Exportálás és egyéb funkciók [export-and-other-features]

Az átalakítás után a Marked a dokumentumot más lefordított forrásokhoz hasonlóan kezeli (hasonlóan a [Scrivener](Scrivener_Support.html) és [DOCX](Working_With_DOCX.html)-hez): az exportálás, a statisztika és a legtöbb előnézeti funkció a Watchers gyorsítótárában tárolt generált Markdown-on fut.

## Korlátozások [limitations]

A konverzió minősége a forrásalkalmazástól függ. Általánosságban:

- A **címsorok** a betűméretből származnak, nem a Word/Pages vázlatstílusaiból
- **Bonyolult elrendezés** (csak pozicionálásra használt többoszlopos táblázatok, szövegdobozok) előfordulhat, hogy nem felelnek meg tisztán a Markdown-nak
- Az **egyenletek** RTF-ben nem támogatottak az előnézetben (lásd a [MathJax](MathJax.html)-t a Markdown matematikához)
- A **örökölt `.doc`** (bináris szó) nem támogatott; először mentse el DOCX vagy RTF formátumban

A fájl mentése nélküli egyszeri beillesztéshez használja helyette a [Vágólap előnézete](Opening_Files.html#from-the-clipboard)-t.

## Kapcsolódó témák [related-topics]

- [PDF támogatás](PDF_Support.html) -- PDF dokumentumok megnyitása Markdown forrásként
- [DOCX használata](Working_With_DOCX.html) -- Word-dokumentumok változáskövetéssel és megjegyzésekkel
- [Fájlok megnyitása](Opening_Files.html) -- fogd és vidd, Nyissa meg a Legutóbbit, vágólap
- [Exportálás](Exporting.html) -- Rich Text másolása és RTFD mentése (exportálás), eltérve az RTF forrásfájlként való megnyitásától