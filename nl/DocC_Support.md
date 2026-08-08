# <%= @title %>

Marked begrijpt [Apple DocC](https://www.swift.org/documentation/docc/) documentatiecatalogi (`.docc` bundels). Wanneer u een voorbeeld van Markdown bekijkt dat zich in of naast een catalogus bevindt, kan Marked **extensieloze** afbeeldingsverwijzingen omzetten naar bestanden in de map `Resources` van de catalogus, inclusief varianten `~dark` en `@2x`.

Voor normale Markdown documenten die **paden met bestandsextensies** (`images/icon.png`) gebruiken, zie [Image Variants](Image_Variants.html). Die functie werkt overal; DocC-resolutie is catalogusspecifiek.

## DocC-resolutie inschakelen [enabling-docc-resolution]

Schakel in {% prefspane Apps %} **Resolve DocC image references** in (standaard ingeschakeld).

DocC-detectie wordt uitgevoerd wanneer Marked een `.docc` catalogusvoorouder van het geopende document vindt. Er is geen speciaal URL-schema of Xcode-integratie vereist; open de Markdown van de catalogus op dezelfde manier als elk ander bestand.

## Extensieloze referenties [extensionless-references]

Binnen een DocC-catalogus verwijzen auteurs doorgaans naar afbeeldingen **zonder** een pad of extensie:

```markdown
![Order flow](OrderStateTransitions)
```

Marked zet `OrderStateTransitions` om in `Resources/OrderStateTransitions.png` (of een ander ondersteund type) wanneer dat bestand in de catalogus bestaat.

Verwijzingen die al een pad en extensie bevatten — `images/chart.png` — worden in plaats daarvan overgelaten aan [Image Variants](Image_Variants.html) en worden niet herschreven door DocC-resolutie.

## Donkere modus en Retina-varianten [dark-mode-and-retina-variants]

DocC-catalogi verzenden vaak meerdere bestanden per afbeelding:

| Rol | Voorbeeld in `Resources/` |
|-----|-----------------------|
| Licht (1x) | `diagram.png` |
| Donker (1x) | `diagram~dark.png` |
| Licht (2x) | `diagram@2x.png` |
| Donker (2x) | `diagram~dark@2x.png` |

Als er meer dan één variant bestaat, zendt Marked dezelfde responsieve `<picture>` opmaak uit zoals beschreven in [Image Variants](Image_Variants.html). Een verwijzing naar één bestand leidt nog steeds tot een normaal pad `<img>` of `![](Resources/...)`.

## HTML en Markdown [html-and-markdown]

DocC-resolutie is van toepassing tijdens de include-pass van Marked:

- **Markdown bronnen** — `![alt](ImageName)` referenties
- **HTML bronnen** — `<img src="ImageName">` zonder extensie

Beide worden bijgewerkt voordat de preview wordt weergegeven.

## Bestanden bekijken [file-watching]

Opgeloste afbeeldingen in de map catalogus `Resources` worden toegevoegd aan de volglijst van Marked. Als u een variantbestand extern bewerkt, wordt het voorbeeld bijgewerkt zonder handmatig vernieuwen.

## Gerelateerde onderwerpen [related-topics]

- [Image Variants](Image_Variants.html) — `~dark` en `@2x` detectie voor op extensies gebaseerde paden in elk project
- [Xcode Playgrounds](Xcode_Playgrounds.html) — preview Snel speeltuincommentaar
- [Settings: Apps](Settings_Apps.html) — DocC- en afbeeldingsvariantvoorkeuren