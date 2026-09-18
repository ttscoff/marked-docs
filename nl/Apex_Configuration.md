<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Deze opties staan in het blad **Configure Apex**. Open het vanuit {% prefspane Processor %} wanneer de standaardprocessor **Apex (bèta)** is. Elke optie geldt alleen voor Apex. Wiskunde, Critic Markup, hashtags, bestandsincludes en kop-ID's blijven in de andere instellingen van Marked.

Zie [Apex (bèta)](Apex.html) voor wat Apex is en welke syntaxis het dekt.

Selectievakjes in het blad winnen van dezelfde instellingen in een Apex-metadatabestand. Bestandspaden zijn optioneel. Een pad dat Marked niet kan lezen, wordt overgeslagen en het voorbeeld loopt toch.

## Bestanden [files]

CSL
: Een Citation Style Language-bestand (`.csl`) dat Apex gebruikt bij het opmaken van een bibliografie. Laat dit leeg om de stijl uit het document of het metadatabestand te gebruiken.

Bibliografie
: Een of meer bibliografiebestanden. Toegestane typen zijn BibTeX (`.bib`), CSL JSON (`.json`) en CSL YAML (`.yml`, `.yaml`). Klik op **Add** voor nog een bestand. Apex zoekt hierin bij het oplossen van citaties.

Concordantie
: Een of meer concordantiebestanden (`.tsv`, `.txt` of `.csv`) voor het maken van een index. Klik op **Add** voor nog een bestand.

Metadatabestand
: Een extern metadatabestand (`.yml`, `.yaml`, `.txt` of `.md`) dat wordt samengevoegd voordat Apex draait. Als het document en het bestand dezelfde sleutel zetten, winnen de metadata van het document. Selectievakjes in dit blad winnen van waarden in het metadatabestand.

## Syntaxis [syntax]

Standaard aan, tenzij anders vermeld.

Tabellen
: Pijptabellen, inclusief een koprij en een scheidingsrij.

Voetnoten
: Verwijzende voetnoten (`[^id]`) en inline voetnoten.

Definitielijsten
: Term-en-definitielijsten (`: definitie`).

Superscript / subscript
: `^super^` en `~sub~`. Zet dit uit als een enkele tilde geen subscript mag betekenen. De Marked-instelling **~text~ als onderstreping weergeven** staat los en botst met subscript.

Doorhalen
: `~~verwijderd~~`.

URL's en e-mail automatisch linken
: Kale `https://`-URL's en e-mailadressen worden links.

Omheinde divs
: `::: naam`-blokken die een sectie in een `<div>` wikkelen.

Spans tussen haakjes
: Inline attribuutspans, zoals `[tekst]{.class}`.

Alfabetische lijsten
: Lijsten die met `a.` of `A.` beginnen, naast getallen.

Gemengde lijstmarkeringen
: Een lijst mag `*`, `+` en `-` mengen en toch één lijst blijven.

Markdown in HTML
: Markdown binnen HTML-bloktags wordt verwerkt. Sommige markup kan nog steeds stukgaan.

Metadatatransformaties
: `[%key]`-plaatshouders worden vervangen vanuit documentmetadata.

## Tabellen en afbeeldingen [tables-and-images]

Rastertabellen
: Tabellen getekend met `+` en `|`. Standaard uit.

Soepelere tabellen
: Pijptabellen mogen de begin- en eindpijpen weglaten. Standaard aan.

Uitlijning per cel
: Uitlijningsmarkeringen in een cel overschrijven de kolomuitlijning. Standaard aan.

Afbeeldingsbijschriften
: De titel van de afbeelding, of de alt-tekst als er geen titel is, wordt een zichtbaar bijschrift. Standaard aan.

Alleen titelbijschriften
: Alleen de afbeeldingstitel wordt het bijschrift. Alt-tekst wordt genegeerd. Standaard uit. Heeft geen effect tenzij **Afbeeldingsbijschriften** aan staat.

## Koppelingen en indexen [links-and-indexes]

Wikikoppelingen
: Apex zet `[[wikikoppelingen]]` om. Standaard uit. Staat dit aan, dan slaat Marked de eigen voorvertoningsstap "Wikikoppelingen omzetten" voor dat document over, en Apex kan het doelbestand anders oplossen dan Marked. De standaardextensie komt uit de wikikoppelingsinstellingen van Marked.

Wikikoppeling-URL's opschonen
: Gegenereerde URL's worden kleine letters, apostroffen verdwijnen, en andere tekens die geen letter of cijfer zijn worden vervangen. Standaard uit. Alleen beschikbaar als **Wikikoppelingen** aan staat.

Indexverwerking
: Herkent indexmarkeringen (MultiMarkdown-, mmark-, Leanpub- en textindex-stijl). Standaard aan.

Indexuitvoer onderdrukken
: Leest de markeringen nog wel, maar drukt de gegenereerde index niet af. Standaard uit.

## Callouts (extra) [callouts-extra]

Beide staan standaard uit. Obsidian- en Bear-callouts (`> [!NOTE]`) worden door Marked vóór Apex afgehandeld en worden hier niet ingesteld.

Python-Markdown-callouts (!!!)
: Callouts in de stijl `!!! note`.

Quarto-callouts
: Quarto-blokken `::: {.callout-note}`.

## Toegankelijkheid [accessibility]

Beide staan standaard uit.

ARIA-labels
: Voegt ARIA-attributen toe die de structuur van de HTML van Apex beschrijven.

Kopankers
: Zet een `<a>`-anker op elke kop in plaats van alleen een `id` op de kop.
