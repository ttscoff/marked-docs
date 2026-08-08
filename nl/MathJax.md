# <%= @title %>

Cijfers zijn net zo belangrijk als woorden.

## Voorbeeldformules bekijken met MathJax [preview-formulas-with-mathjax]

![][1]

   [1]: images/mathjax.jpg @2x width=713px height=512px class=center

Door MathJax in de {% prefspane Style %} in te schakelen, worden de benodigde scripts en CSS in de preview opgenomen. Vervolgens kan de MultiMarkdown wiskundige syntaxis worden gebruikt in uw Markdown document en zullen de resultaten worden weergegeven.

Voorbeeld MMD MathJax syntaxis:

\\\\[ {e}^{i\pi } 1=0 \\\\]

Als u ervoor kiest om MathJax op te nemen in een geëxporteerd HTML bestand, wordt een CDN-link gebruikt in plaats van de ingesloten MathJax code. Hiervoor is een internetverbinding vereist om de weergegeven MathML te bekijken.

## MathJax bron: lokaal versus CDN [mathjax-source-local-vs-cdn]

Wanneer MathJax is ingeschakeld, kan Marked het laden vanuit:

- **Lokaal**: een kopie van MathJax v3 gebundeld in de app (sneller te laden, werkt offline).
- **CDN**: de officiële MathJax v3 CDN (altijd up-to-date, geen impact op de app-bundel).

In de pop-up **MathJax Bron** in {% prefspane Style %} kunt u kiezen:

- **Lokaal** – gebruikt de ES5 `tex-chtml.js` component uit de app-bundel.
- **CDN** – laadt hetzelfde onderdeel vanuit het CDN. Hiervoor is een internetverbinding vereist.

Geëxporteerde HTML bestanden verwijzen altijd naar MathJax vanuit een CDN, ongeacht de voorbeeldbron, zodat ze op zichzelf staand en klein blijven.

## Nummering van vergelijkingen [equation-numbering]

U kunt vergelijkingsnummering inschakelen in {% prefspane Style %}. Dit werkt met zowel MathJax als KaTeX, maar wordt intern anders geïmplementeerd. Voor MathJax v3 wijst Marked uw instellingen toe aan de juiste MathJax configuratie, zodat:

- "Getalvergelijkingen" bepaalt of er getallen worden weergegeven.
- De optie “zijkant” bepaalt of cijfers links of rechts verschijnen.
- De optie “Alleen AMS” beperkt de nummering tot vergelijkingen in AMS-stijl.

Deze opties komen overeen met de `tex.tags` en `tex.tagSide` instellingen van MathJax onder de motorkap.

## Extra pakketten [additional-packages]

MathJax v3 is modulair. Marked schakelt altijd de kern TeX/AMS-pakketten in, en je kunt optioneel extra pakketten inschakelen in {% prefspane Style %}:

- **Natuurkunde** (`physics`) – natuurkundige notatie en gemakken.
- **Chemie** (`mhchem`) – scheikundige vergelijkingen.
- **Bra–ket** (`braket`) – Dirac bra–ket-notatie.
- **Vetgedrukte symbolen** (`boldsymbol`) – vetgedrukte wiskundige symbolen.

Klik op **Extra pakketten...** om een ​​kleine checklist te openen waarin u deze pakketten kunt in- of uitschakelen. Wijzigingen worden van kracht de volgende keer dat Marked wiskunde in het voorbeeld weergeeft.

## MathJax geavanceerde configuratie [mathjax-advanced-configuration]

U kunt aanvullende aangepaste configuraties toepassen bovenop de standaardinstellingen van Marked door een geldig JSON-object toe te voegen in het veld **Geavanceerde configuratie**. Dit veld wordt samengevoegd met het configuratieobject MathJax v3 (`window.MathJax`) voordat MathJax wordt geladen. Het kan [any options supported by MathJax v3](https://docs.mathjax.org/en/latest/options/) bevatten, bijvoorbeeld:

{
        "tex": {
            "inlineMath": [["$","$"],["\\\\(","\\\\)"]],
            "displayMath": [["$$","$$"],["\\\\[","\\\\]"]],
            "macro's": {
                "tr": "{\\\\scriptscriptstyle\\\\mathrm{T}}"
            },
            "pakketten": { "[+]": ["natuurkunde"] }
        }
    }

In dit voorbeeld worden de TeX-scheidingstekens aangepast, wordt een macro `\tr` toegevoegd en wordt het pakket `physics` ingeschakeld naast de standaardset. Met deze instellingen worden al het volgende correct weergegeven:

Inline formule met haakjes, \\\\({x}^{2} {y}^{2}=1\\\\), of met dollartekens, ${x}^{2} {y}^{2}=1$.

Weergave met ontsnapte haakjes:

\\\\[ {e}^{i\pi } 333=0 \label{testme} \\\\]

Of met dubbele dollartekens:

$${x}_{1,2}=\\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a}$$

![][2]

   [2]: images/mathjax2.jpg @2x width=837px height=260px class=center

De aanvullende configuratie breidt het bestaande object uit, zodat alleen de opgegeven eigenschappen worden overschreven. Niet-gespecificeerde opties blijven de standaardinstelling voor de huidige voorinstelling.

Houd er rekening mee dat bij gebruik van de MultiMarkdown-processor met niet-standaard scheidingstekens de tekens in de expressie worden geparseerd, zodat symbolen als `*` en `^` typografische wijzigingen veroorzaken die de MathJax-processor kapot maken. De beste oplossing in deze gevallen is het gebruik van de Discount-processor in [Processor settings](x-marked-3://pref/processor).

Marked voert een beetje magie uit wanneer MathJax of KaTeX is ingeschakeld, waarbij de wiskundige syntaxis wordt geconverteerd om ervoor te zorgen dat deze zo compatibel mogelijk is met de huidige processor (MultiMarkdown of Discount). Dit zou onder alle omstandigheden goed moeten zijn, maar als je merkt dat het problemen veroorzaakt, [contact support](https://support.markedapp.com/questions/add)!


## KaTeX [katex]

[katex]: https://katex.org/

[KaTeX][] is beschikbaar als alternatief voor MathJax. Het is lichter van gewicht en daarom sneller te laden, wat geweldig kan zijn bij documenten met een groot aantal formules. Het heeft echter niet zoveel functies, en sommige vergelijkingen die werken met MathJax (of LaTeX) worden mogelijk niet ondersteund.

## Automatische vergelijkingsnummering [numbering]

U kunt vergelijkingsnummering inschakelen in {% prefspane Style %}. Dit werkt met zowel MathJax als KaTeX. U kunt selecteren of getallen aan de linker- of rechterkant van de vergelijking verschijnen.

### Over MathJax [in-mathjax]

In MathJax wordt hiervoor de instelling gebruikt:

{
      TeX: { vergelijkingsnummers: { autoNumber: "alles" } }
    }

Als u alleen AMS-vergelijkingen wilt nummeren, selecteert u 'Alleen AMS' rechts van het vervolgkeuzemenu 'Zijkant'.

### Over KaTeX [in-katex]

KaTeX biedt geen nummering van vergelijkingen. Om dit in Marked te simuleren, wordt CSS gebruikt en zijn alle weergavevergelijkingen genummerd.

## Exportproblemen [export-issues]

Rich Text-formaten kunnen geen vergelijkingen verwerken (noch met MathJax, noch met KaTeX). Ze zullen verborgen worden in het uitvoerdocument, omdat het opnemen van de speciale lettertypen resulteert in een grotere puinhoop dan je zou denken... Dit is iets dat ik op een gegeven moment hoop op te lossen, maar op dit moment een tekortkoming.

