# <%= @title %>

Er zijn verschillende manieren om extra JavaScripts in Marked in te sluiten.

## Inclusief JavaScript per document [including-javascript-per-document]

U kunt scripts in één document opnemen met `<script>` tags in de inhoud zelf. Dit kan handig zijn voor bibliotheken zoals [D3](https://d3js.org/) voor datavisualisaties die je alleen in specifieke documenten nodig hebt:

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

Als u MultiMarkdown als uw verwerker gebruikt, kunt u scripts in de metagegevens opnemen en deze in het document invoegen. Omdat Marked alleen "snippet" uitvoert, is de sleutel `XHTML Header` niet ideaal. Gebruik in plaats daarvan `CSS Header` en de scripts worden onderaan het document ingevoegd.

CSS-header: <script src="file.js"></script>

Om opgenomen scripts te laten vernieuwen wanneer de inhoud verandert, zie [Hooks](#hooks).

## Inclusief JavaScript [including-javascript]

U kunt uw eigen JavaScript toevoegen vanuit lokale bestanden, CDN's of door onbewerkte code te plakken. Om hier toegang toe te krijgen, opent u {% prefspane Style %} en klikt u op de knop *Custom Regels*.

Stel een nieuwe Custom regel in of voeg scripts toe aan een bestaande regel. Om scripts aan elk bestand toe te voegen, stelt u het predikaat in op "bestandsnaam bevat *".

De Acties-editor voor een Custom Regel heeft drie opties voor het opnemen van scripts:

JavaScript-bestand invoegen
: Hiermee kunt u een lokaal bestand selecteren dat u aan het einde van het document wilt invoegen

JavaScript invoegen vanaf URL
: Hiermee kunt u een CDN of een andere externe URL opnemen, waardoor een `<script>` tag aan het einde van het document wordt gemaakt waaraan de URL is gekoppeld

JavaScript invoegen
: Opent een code-editor waarin u uw eigen JavaScript-code kunt schrijven/plakken

Deze scripts worden aan het einde van het voorbeeld ingevoegd, vóór de documenttag. Als u elke keer dat de preview wordt bijgewerkt een init-functie moet aanroepen of moet bijwerken, raadpleeg dan [Including Raw JavaScript](Embedding_Scripts.html#hooks) en maak uzelf vertrouwd met de [hooks](#hooks) van Marked.

## Zeemeermin en andere scripts [mermaid]

jQuery is standaard inbegrepen en u kunt het gebruiken in alle scripts die u aan Marked toevoegt met behulp van een van de onderstaande methoden.

[Mermaid](https://mermaid.js.org/intro/) voor Markdown-achtige diagrammen is nu standaard in elk document opgenomen. Elk afgeschermd codeblok met de taal `mermaid` wordt automatisch als diagram weergegeven.

Onderaan de {% prefspane Style %} is een selectievakje voor "Pan- en zoomdiagrammen" beschikbaar wanneer zeemeermininhoud aanwezig is. Als u dit vakje aanvinkt, zoomen de diagrammen in met {% kbd cmd %}-scroll, en pannen ze door te klikken en te slepen. Het script voor deze functie is afkomstig van een CDN en vereist een internetverbinding.

Als u een bepaalde bibliotheek standaard wilt zien, laat het me dan weten via [BrettTerpstra.com forum](https://forum.brettterpstra.com/) of via [the support site](https://support.markedapp.com/questions/add).

## Haken [hooks]

Vanaf recente versies voert Marked niet langer een volledige paginavernieuwing uit bij het bijwerken van inhoud, maar injecteert de nieuwe inhoud in de DOM zonder dat de pagina hoeft te worden geladen. Dit betekent dat opgenomen scripts die worden geactiveerd bij het laden van de pagina, niet opnieuw worden geactiveerd wanneer de inhoud wordt bijgewerkt. Marked biedt hiervoor een "hooks"-functie. Om een ​​hook te registreren, moet je een tweede scriptblok toevoegen dat de [<!--MKPH0--> function](https://markedapp.com/jsapi/Marked.hooks.html#.register__anchor) aanroept, dat een trigger accepteert, in dit geval 'update', en een functie die moet worden uitgevoerd.

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script>
	Marked.hooks.register('update', function() {
		// Re-run your D3 visualization when content updates
		d3.selectAll('.chart').each(function() {
			// your D3 render logic here
		});
	});
</script>
```

Alle [API functionality](https://markedapp.com/jsapi/) van Marked kunnen in dit veld worden gebruikt. (Je kunt de API ook in alle geladen scripts gebruiken.) Voor interactief debuggen en experimenteren met de API in een live preview, zie de [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) sectie voor details over het gebruik van Safari's Develop-menu met Marked.

Telkens wanneer er een update wordt uitgevoerd (wanneer het bewaakte bronbestand wordt opgeslagen), wordt de doorgegeven functie uitgevoerd. Zolang het script dat je gebruikt een of andere init- of renderfunctie heeft, kun je het met een hook aanroepen en het elke keer laten renderen als je document wordt opgeslagen en er een update wordt geactiveerd.



*[CDN]: Contentdistributienetwerk