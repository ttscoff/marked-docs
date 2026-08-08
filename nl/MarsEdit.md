# <%= @title %>

[MarsEdit][me] slaat berichten op in de database, niet als losse bestanden op schijf. Marked gebruikt daarom een ​​speciale preview-workflow die communiceert met de actieve MarsEdit-applicatie.

## MarsEdit Preview-venster [marsedit-preview-window]

Kies {% appmenu File, New, MarsEdit Preview %}. Marked vraagt ​​AppleScript om de **voorpost in MarsEdit** te lezen (de bundel-ID's van Red Sweater voor direct, Mac App Store, Setapp en MarsEdit 4/5 worden herkend). Houd MarsEdit actief met een document open terwijl u werkt.

- **Handmatig vernieuwen:** sla op vanuit de preview van Marked als u een update wilt forceren.
- **Automatische updates:** schakel het kijken in, zodat elke automatische opslag van MarsEdit Marked wordt vernieuwd.

Als er geen bericht beschikbaar is, geeft Marked een korte fout weer in het voorbeeld in plaats van verouderde tekst.

### Uitgebreide berichten [extended-posts]

De inhoud in het **uitgebreide** veld van MarsEdit wordt in het voorbeeld en de broncode van Marked gescheiden met behulp van een `<!--more-->` scheidingslijn in WordPress-stijl, zodat op paginering gerichte sites (WordPress, Jekyll, enz.) nog steeds de scheiding zien. Elders is de opmerking onschadelijk.

### Tags en categorieën in metadata [tags-and-categories-in-metadata]

De tags en categorieën van MarsEdit worden blootgesteld aan het MultiMarkdown metadatablok. Met de MultiMarkdown processor ({% prefspane Processor %}) kunt u er als volgt naar verwijzen:

Getagd: [%tags]
    Geplaatst in: [%categorieën]

[me]: https://www.red-sweater.com/marsedit/
