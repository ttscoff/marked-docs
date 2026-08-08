# <%= @title %>

Marked kan automatisch responsieve `<picture>` elementen bouwen voor lokale afbeeldingen wanneer begeleidende bestanden in de **donkere modus** en **Retina** naast de afbeelding staan ​​waarnaar u verwijst. Dit gebruikt dezelfde naamgevingsconventies als de DocC-documentatiecatalogi van Apple, maar werkt voor **elk Markdown of HTML document** met normale afbeeldingspaden die een bestandsextensie bevatten.

Zie ook [DocC Support](DocC_Support.html) voor catalogusreferenties zonder uitbreidingen in `.docc` bundels.

## Afbeeldingsvarianten inschakelen [enabling-image-variants]

Schakel in {% prefspane Apps %} **Donkere en @2x afbeeldingsvarianten oplossen** in (standaard ingeschakeld) onder DocC-instellingen.

Deze voorkeur staat los van **Resolve DocC-afbeeldingsreferenties**, die alleen van toepassing is binnen `.docc` catalogi. Afhankelijk van uw project kunt u één, beide of geen van beide gebruiken.

## Naamgevingsconventie [naming-convention]

Plaats variantbestanden in **dezelfde map** als de primaire afbeelding. Marked zoekt naar vier combinaties op basis van de basisnaam:

| Rol | Voorbeeld bestandsnaam |
|------|-----------------|
| Licht (1x) | `icon.png` |
| Donker (1x) | `icon~dark.png` |
| Licht (2x) | `icon@2x.png` |
| Donker (2x) | `icon~dark@2x.png` |

De volgorde van de achtervoegsels is flexibel — `icon@2x~dark.png` en `icon~dark@2x.png` worden op dezelfde manier behandeld.

Ondersteunde extensies: `png`, `jpg`, `jpeg`, `gif`, `svg`, `webp` en `pdf`.

## Wat wordt herschreven [what-gets-rewritten]

Marked scant uw document **vóór** de definitieve voorbeeldweergave:

- **Markdown:** `![Alt text](images/icon.png)`
- **HTML:** `<img src="images/icon.png" alt="Alt text">`

Als er minstens **twee** overeenkomende variantbestanden op schijf staan, wordt de referentie vervangen door een `<picture>` blok. Eén extra bestand is voldoende; je hebt niet alle vier de varianten nodig.

Voorbeelduitvoer wanneer lichte, donkere en @2x-bestanden aanwezig zijn:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/icon~dark.png 1x, images/icon~dark@2x.png 2x">
  <source srcset="images/icon.png 1x, images/icon@2x.png 2x">
  <img src="images/icon.png" alt="Alt text">
</picture>
```

Het voorbeeld (en de HTML-export) volgt vervolgens het systeemuiterlijk van de gebruiker voor donkere varianten en de pixeldichtheid van het apparaat voor @2x assets.

## Wat wordt overgeslagen [what-is-skipped]

Marked herschrijft **niet**:

- Externe URL's (`http://`, `https://`, `data:`)
- Referenties die al naar een `~dark` bestand verwijzen
- `<img>` tags die al in een bestaand `<picture>` element zitten
- Extensieloze namen zoals `![Diagram](diagram)` — gebruik [DocC Support](DocC_Support.html) voor verwijzingen in catalogusstijl

## Live preview en bekijken van bestanden [live-preview-and-file-watching]

Wanneer varianten worden gedetecteerd, voegt Marked **elk bestaand variantbestand** toe aan de controlelijst naast het hoofddocument. Het opslaan van `icon~dark.png` in een externe editor activeert hetzelfde herladen van livebeelden als het bewerken van `icon.png`.

## Tips [tips]

- Verwijs indien mogelijk naar de **light 1x**-afbeelding in uw bron (`icon.png`, niet `icon~dark.png`). Marked ontdekt broers en zussen van dat pad.
- Als u alleen `@2x` items heeft, neem dan ten minste één andere variant op (meestal `~dark`), anders laat Marked de referentie ongewijzigd.
- Variantresolutie gebruikt paden **ten opzichte van het document** (of de map van het opgenomen bestand voor geneste include's), dezelfde basispadregels als [Multi-file Documents](Multi-File_Documents.html).

## Gerelateerde onderwerpen [related-topics]

- [DocC Support](DocC_Support.html) — extensieloze afbeeldingsnamen in `.docc` catalogi
- [Settings: Apps](Settings_Apps.html) — voorkeur schakelt tussen DocC en afbeeldingsvarianten
- [Previewing](Previewing.html) — live preview en bestandsupdates