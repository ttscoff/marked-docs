# <%= @title %>

Marked kan PDF documenten (`.pdf`) rechtstreeks openen. Sleep een bestand naar Marked of gebruik {% appmenu File, Open... ({{cmd}}O) %}. Het document wordt geconverteerd naar Markdown voor voorbeeldweergave en export.

PDF import werkt het beste op **kleinere, op tekst gebaseerde PDFs** (dia's, artikelen, korte rapporten). Grote handleidingen, boeken en gescande documenten worden ondersteund, maar worden vaak langzaam of onvolmaakt geconverteerd – zie **Beperkingen** hieronder.

Marked is nog steeds een **preview**-tool: je bewerkt de PDF binnen Marked niet. Gebruik {% kbd cmd E %} om PDF te openen in **Preview** (of uw systeemstandaard), en Marked wordt vernieuwd wanneer het bestand op schijf verandert.

## Hoe conversie werkt [how-conversion-works]

PDF import gebruikt de [pdf22md](https://github.com/twardoch/pdf22md) bibliotheek (MIT-licentie; zie [pdf22md License](PDF22MD_License.html)). Marked voert de conversie uit op de achtergrond en toont een korte melding **Converteren**.

De converter:

- Extraheert **tekst** uit digitale PDFs met behulp van PDFKit
- Gebruikt **Vision OCR** op pagina's waar ingesloten tekst ontbreekt (gebruikelijk bij scans)
- Detecteert **koppen** van de lettergrootte indien mogelijk
- Bewaart **afbeeldingen** in een `assets` map naast de gegenereerde Markdown

Marked schakelt **niet** de optionele AI-opschoning van pdf22md in de app in. De conversiekwaliteit is afhankelijk van hoe de PDF is gemaakt.

## Cache en live preview [cache-and-live-preview]

Geconverteerde Markdown en afbeeldingen worden opgeslagen onder de Watchers-cache van Marked (`~/Library/Caches/Marked/Watchers/PDF/`). Het oorspronkelijke PDF pad blijft de documentbron voor het bekijken van bestanden.

Wanneer u de PDF in een andere toepassing opslaat of vervangt, detecteert Marked de wijziging en wordt deze automatisch opnieuw geconverteerd (hetzelfde samengevoegde herlaadgedrag als [RTF](RTF_Support.html) en [Scrivener](Scrivener_Support.html)).

## Exporteren en andere functies [export-and-other-features]

Na de conversie behandelt Marked het document als andere gecompileerde bronnen: export, statistieken en de meeste preview-functies worden uitgevoerd tegen de gegenereerde Markdown. Afbeeldingspaden in het voorbeeld wijzen op in de cache opgeslagen elementen totdat u exporteert.

## Beperkingen [limitations]

Stel uw verwachtingen dienovereenkomstig in: PDF-tot-Markdown is nuttig, niet perfect.

**Wat werkt goed**

- **Vector- en tekstgebaseerde PDFs** met echte ingesloten tekst (geëxporteerd uit Word, Pages, InDesign, enz.)
- **Gemiddelde lengte** — enkele tientallen pagina's worden doorgaans binnen een redelijke tijd omgezet met een goede structuur

**Wat is onbetrouwbaar**

- **OCR (gescand PDFs)** — Vision vult ontbrekende tekst in, maar de nauwkeurigheid is vaak slecht vergeleken met een speciale OCR-tool; verwacht typefouten, gebroken woorden en gemiste kolommen
- **Tabellen** — de lay-out wordt geraden op basis van tekstposities; samengevoegde cellen, geneste tabellen en complexe rasters overleven zelden als schone Markdown tabellen
- **Plaatsing van afbeeldingen** — figuren worden geëxtraheerd naar `assets/`, maar uitlijning, bijschriften en tekstomloop rond afbeeldingen worden niet betrouwbaar bewaard

**Grootte en prestaties**

- **Grote PDFs** (gebruikershandleidingen, schoolboeken, lange handleidingen) kunnen **erg lang** duren om te converteren, gebruiken aanzienlijk geheugen of leveren geen bruikbare Markdown op. Marked blijft responsief terwijl de conversie op de achtergrond wordt uitgevoerd, maar er is geen garantie dat een handleiding van 500 pagina's succesvol zal worden afgerond
- Als de conversie wordt voltooid met weinig of geen inhoud, geeft Marked een fout weer in plaats van een leeg voorbeeld achter te laten

**Andere limieten**

- **Wachtwoordbeveiligde PDFs** worden niet ondersteund in v1
- **Ingesloten PDF afbeeldingen in Markdown** (`![]()` verwijzend naar een `.pdf` bestand) hebben niets te maken met de PDF-import; ze openen alleen een `.pdf` omdat het hoofddocument de conversie activeert

Voor Word-documenten gebruikt u [Working with DOCX](Working_With_DOCX.html). Voor Rich Text gebruikt u [RTF and RTFD Support](RTF_Support.html).

## Gerelateerde onderwerpen [related-topics]

- [Opening Files](Opening_Files.html) — slepen en neerzetten, Recent openen, klembord
- [Exporting](Exporting.html) — sla HTML, PDF, DOCX en Markdown op uit het voorbeeld
- [pdf22md License](PDF22MD_License.html) — MIT-licentietekst van derden