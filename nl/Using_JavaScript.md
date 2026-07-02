# <%= @title %>

Marked gebruikt veel JavaScript om de functies te bieden die het in de preview biedt. Om deze reden kunnen er nogal wat complicaties optreden wanneer scripts in de hoofdtekst van het document worden opgenomen.

## Externe scripts

U kunt enkele externe scripts opnemen met behulp van een metadataregel 'CSS Header:' bovenaan uw document. Deze scripts worden echter niet in de koptekst ingevoegd, maar in de voettekst nadat de scripts van jQuery en Marked al zijn geladen. Dit is in de meeste gevallen ideaal. Het is mogelijk dat u nog steeds onverwacht gedrag ervaart, omdat Marked niet elk mogelijk scriptconflict kan compenseren. DOM-wijzigingen kunnen bijzonder problematisch zijn.

CSS-header: <script src="file.js"></script>

## Inline omvat

Er zijn veel toepassingen om JavaScript in de hoofdtekst van een document te laten verschijnen, zoals grafiekgeneratoren of andere Canvas-tools. Afhankelijk van de configuratie-instellingen en de processor die u gebruikt, worden deze vaak verminkt. De oplossing is om uw script en extra DOM-elementen in een extern bestand te plaatsen en de syntaxis van Marked te gebruiken voor ["raw" include files][syntax]. Deze bestanden worden op geen enkele manier verwerkt; hun inhoud wordt aan het bestand toegevoegd nadat de rest van de verwerking is voltooid.

Markdown tekst.

<<{bestand.html}

Meer Markdown tekst...

Om te experimenteren met en fouten op te sporen in het JavaScript dat in de preview van Marked wordt uitgevoerd, kunt u Safari's Web Inspector aan het voorbeeldvenster toevoegen met behulp van de stappen in [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector).

[syntax]: Special_Syntax.html#includingunprocessedtextorhtml
