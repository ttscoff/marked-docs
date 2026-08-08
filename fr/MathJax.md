# <%= @title %>

Les chiffres comptent autant que les mots.

## Prévisualiser les formules avec MathJax [preview-formulas-with-mathjax]

![][1]

[1]: images/mathjax.jpg @2x width=713px height=512px class=center

En activant MathJax dans le {% prefspane Style %}, les scripts et CSS nécessaires seront inclus dans l'aperçu. Ensuite, la syntaxe mathématique MultiMarkdown peut être utilisée dans votre document Markdown et les résultats seront affichés.

Exemple de syntaxe MMD MathJax :

    \\\\[ {e}^{i\pi } 1=0 \\\\]

Si vous choisissez d'inclure MathJax dans un fichier HTML exporté, un lien CDN sera utilisé à la place du code MathJax intégré. Cela nécessite une connexion Internet pour afficher le MathML rendu.

## Source MathJax : local ou CDN [mathjax-source-local-vs-cdn]

Lorsque MathJax est activé, Marked peut le charger depuis :

- **Local** : une copie de MathJax v3 fournie dans l'application (plus rapide à charger, fonctionne hors ligne).
- **CDN** : le CDN officiel MathJax v3 (toujours à jour, aucun impact sur l'app bundle).

La fenêtre contextuelle **MathJax Source** dans {% prefspane Style %} vous permet de choisir :

- **Local** – utilise le composant ES5 `tex-chtml.js` du bundle d'applications.
- **CDN** – charge le même composant à partir du CDN. Cela nécessite une connexion Internet.

Les fichiers HTML exportés font toujours référence à MathJax à partir d'un CDN, quelle que soit la source d'aperçu, ils restent donc autonomes et petits.

## Numérotation des équations [equation-numbering]

Vous pouvez activer la numérotation des équations dans {% prefspane Style %}. Cela fonctionne à la fois avec MathJax et KaTeX, mais est implémenté différemment en interne. Pour MathJax v3, Marked mappe vos paramètres à la configuration MathJax appropriée afin que :

- « Équations numériques » contrôle si des nombres sont affichés.
- L'option « côté » contrôle si les chiffres apparaissent à gauche ou à droite.
- L'option « AMS uniquement » restreint la numérotation aux équations de style AMS.

Ces options correspondent aux paramètres `tex.tags` et `tex.tagSide` de MathJax sous le capot.

## Forfaits supplémentaires [additional-packages]

MathJax v3 est modulaire. Marked active toujours les packages TeX/AMS de base, et vous pouvez éventuellement en activer des supplémentaires dans {% prefspane Style %} :

- **Physique** (`physics`) – notation physique et commodités.
- **Chimie** (`mhchem`) – équations de chimie.
- **Bra–ket** (`braket`) – Notation Dirac bra–ket.
- **Symboles gras** (`boldsymbol`) – symboles mathématiques en gras.

Cliquez sur **Packages supplémentaires…** pour ouvrir une petite liste de contrôle dans laquelle vous pouvez activer ou désactiver ces packages. Les modifications prendront effet la prochaine fois que Marked restituera les mathématiques dans l'aperçu.

## Configuration avancée de MathJax [mathjax-advanced-configuration]

Vous pouvez appliquer des configurations personnalisées supplémentaires en plus des valeurs par défaut de Marked en ajoutant un objet JSON valide dans le champ **Configuration avancée**. Ce champ est fusionné dans l'objet de configuration MathJax v3 (`window.MathJax`) avant le chargement de MathJax. Il peut contenir [toutes les options prises en charge par MathJax v3](https://docs.mathjax.org/en/latest/options/), par exemple :

    {
        "tex": {
            "inlineMath": [["$","$"],["\\\\(","\\\\)"]],
            "displayMath": [["$$","$$"],["\\\\[","\\\\]"]],
            "macros": {
                "tr": "{\\\\scriptscriptstyle\\\\mathrm{T}}"
            },
            "packages": { "[+]": ["physics"] }
        }
    }

Cet exemple ajuste les délimiteurs TeX, ajoute une macro `\tr` et active le package `physics` en plus de l'ensemble par défaut. Avec ces paramètres, tous les éléments suivants s'affichent correctement :

    Formule en ligne utilisant des parenthèses, \\\\({x}^{2} {y}^{2}=1\\\\), ou avec des signes dollar, ${x}^{2} {y}^{2}=1$.

    Affichage avec parenthèses échappées :

    \\\\[ {e}^{i\pi } 333=0 \label{testme} \\\\]

    Ou avec des signes double dollar :

    $${x}_{1,2}=\\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a}$$

![][2]

[2]: images/mathjax2.jpg @2x width=837px height=260px class=center

La configuration supplémentaire étend l'objet existant, de sorte que seules les propriétés spécifiées seront remplacées. Les options non spécifiées resteront par défaut pour le préréglage actuel.

Notez qu'en utilisant le processeur MultiMarkdown avec des délimiteurs non standard, les caractères à l'intérieur de l'expression sont analysés, donc des symboles comme `*` et `^` entraîneront des modifications typographiques qui briseront le processeur MathJax. La meilleure solution dans ces cas est d'utiliser le processeur Discount dans [Paramètres du processeur](x-marked-3://pref/processor).

Marked effectue un peu de magie lorsque MathJax ou KaTeX sont activés, convertissant la syntaxe mathématique pour garantir qu'elle est aussi compatible que possible avec le processeur actuel (MultiMarkdown ou Discount). Cela devrait être génial en toutes circonstances, mais si vous trouvez que cela pose des problèmes, [contactez le support](https://support.markedapp.com/questions/add) !


## KaTeX [katex]

[katex]: https://katex.org/

[KaTeX][] est disponible comme alternative à MathJax. Il est plus léger et donc plus rapide à charger, ce qui peut s'avérer très utile sur les documents contenant un grand nombre de formules. Cependant, il n'a pas autant de fonctionnalités et certaines équations fonctionnant avec MathJax (ou LaTeX) peuvent ne pas être prises en charge.

## Numérotation automatique des équations [numbering]

Vous pouvez activer la numérotation des équations dans {% prefspane Style %}. Cela fonctionne à la fois avec MathJax et KaTeX. Vous pouvez choisir si les nombres apparaissent sur le côté gauche ou droit de l'équation.

### Dans MathJax [in-mathjax]

Dans MathJax, cela utilise le paramètre :

    {
      TeX : {equationNumbers : { autoNumber : "all" } }
    }

Si vous souhaitez numéroter uniquement les équations AMS, sélectionnez « AMS uniquement » à droite du menu déroulant « côté ».

### Dans KaTeX [in-katex]

KaTeX ne propose pas de numérotation d'équations. Pour simuler cela dans Marked, CSS est utilisé et toutes les équations d'affichage sont numérotées.

## Problèmes d'exportation [export-issues]

Les formats Rich Text ne géreront pas les équations (que ce soit par MathJax ou KaTeX). Elles seront cachées dans le document de sortie, car essayer d'inclure les polices spéciales entraîne un désordre plus important que vous ne l'imaginez... C'est quelque chose que j'espère corriger à un moment donné, mais c'est une lacune pour le moment.
