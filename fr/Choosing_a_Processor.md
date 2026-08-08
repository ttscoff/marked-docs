# <%= @title %>

Marked peut prévisualiser le même fichier avec plusieurs processeurs Markdown intégrés. Chacun fait des compromis différents entre le **flux de rédaction** (livres, blogs, README GitHub) et le **contrôle de la sortie** (ID, classes, métadonnées). Vous choisissez la valeur par défaut dans {% prefspane Processor %} ; vous pouvez également remplacer le processeur pour un document donné.

Cette page résume les différences entre les quatre principaux processeurs. Pour tous les détails de syntaxe, consultez les pages de référence sous **Aide → Référence Markdown** (par exemple [Spécification MultiMarkdown v5](MultiMarkdown_v5_Spec.html), [Spécification Kramdown](Kramdown_Spec.html), [Spécification CommonMark](CommonMark_Spec.html), [Spécification Discount GFM](Discount_GFM_Spec.html)).

---

## MultiMarkdown (v5) [multimarkdown-v5]

**Idéal pour :** la prose longue, la rédaction académique ou technique, et tout ce qui repose sur des **métadonnées**, des **citations** et des fonctionnalités **spécifiques à MultiMarkdown**.

Marked embarque **MultiMarkdown 5** (voir le [guide utilisateur MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/) pour la documentation d'origine).

### Avantages [strengths]

- **Documents narratifs ou riches en références :** notes de bas de page, bibliographie/citations et tableaux sont traités en priorité.
- **Métadonnées :** blocs de métadonnées MultiMarkdown standard (en-têtes `Key: Value`) plus **transclusion** et autres commodités MMD décrites dans le guide v5.
- **Substitution de métadonnées :** les clés des métadonnées peuvent être insérées dans le corps du texte via un remplacement de type `[%key]`, afin que les titres, noms d'auteur et valeurs similaires restent synchronisés avec l'en-tête.
- **Tableaux, images et références croisées :** conformes aux fonctionnalités documentées pour MultiMarkdown 5.

### ID et titres manuels [ids-and-manual-headings]

- Les ID de titre sont **normalisés** de façon à produire généralement des slugs **en minuscules et concaténés** (pas d'espaces, les mots sont accolés).
- Pour les **ID de titre manuels**, MultiMarkdown utilise la forme : `## Headline Text [my-id]` (l'identifiant entre crochets après le texte du titre).

### Quand choisir autre chose [when-to-pick-something-else]

Si vous avez besoin de listes de tâches **façon GitHub** et du comportement exact de l'analyseur actuel de GitHub, préférez **CommonMark (GFM)**. Si vous avez besoin de **classes/ID HTML précis** sur des éléments arbitraires, envisagez **Kramdown**.

---

## Kramdown [kramdown]

**Idéal pour :** documents pour lesquels vous souhaitez **un contrôle précis sur la sortie HTML** : **classes**, **ID** et attributs personnalisés, afin que votre CSS puisse cibler des blocs et des étendues spécifiques.

La [référence de syntaxe kramdown](https://kramdown.gettalong.org/syntax.html) fait autorité.

### Avantages [strengths-2]

- **Globalement compatible** avec les habitudes de style MultiMarkdown pour un usage Markdown courant, tout en ajoutant ses propres extensions.
- **Listes d'attributs en ligne et de bloc (IAL) :** associez `{: #id .class key="value"}` à des paragraphes, titres, blocs de code, liens, images, et plus encore : idéal pour les sites de type Jekyll et les feuilles de style personnalisées.
- **ID de titre :** kramdown normalise les ID de titre générés automatiquement en mots **en minuscules, séparés par des traits d'union** (par exemple `my-section-title`). Pour les **ID manuels**, utilisez la forme `{#id}` après le texte du titre, par exemple en Setext : `My Section {#my-section}` puis la ligne de soulignement, ou en ATX : `# My Section {#my-section}` (voir la section [headers](https://kramdown.gettalong.org/syntax.html#headers) de kramdown pour le placement exact et les règles IAL).
- **Listes de définitions, notes de bas de page, typographie intelligente, blocs mathématiques :** riche ensemble de fonctionnalités pour les pipelines de publication qui nécessitent plus qu'un simple Markdown.

### Quand choisir autre chose [when-to-pick-something-else-2]

Si vous dépendez de la substitution de métadonnées **propre à MultiMarkdown** (`[%key]`) ou de flux de citation spécifiques à MMD, **MultiMarkdown** conviendra probablement mieux. Pour les **README et docs de dépôt** qui doivent correspondre à GitHub en ligne, **CommonMark (GFM)** est généralement plus proche.

---

## CommonMark (GitHub Flavored Markdown / cmark-gfm) [commonmark-github-flavored-markdown-cmark-gfm]

**Idéal pour :** **fichiers README**, **descriptions de problèmes/PR** et **documentation de projet** qui doivent correspondre le plus étroitement possible au **comportement Markdown actuel de GitHub**.

Marked utilise un moteur orienté **GFM** (cmark-gfm). La spécification formelle est la [GitHub Flavored Markdown Spec](https://github.github.com/gfm/), construite sur [CommonMark](https://commonmark.org/).

### Avantages [strengths-3]

- **Correspondance la plus proche de GitHub :** les tableaux, les barrés, les éléments de la liste de tâches, les blocs de code clôturés avec des balises de langue et les liens automatiques se comportent comme le rendu GitHub moderne.
- **Analyse sans ambiguïté :** CommonMark définit précisément la préséance bloc/inline et les règles de liste : plus strict dans certains cas limites que le comportement Markdown.pl « classique », mais **plus prévisible** une fois les règles apprises.
- **Pratique pour le texte à retour à la ligne manuel :** les règles de paragraphe et de liste sont conçues pour bien se comporter avec une prose à retour à la ligne forcé (voir les sections de la spécification sur les continuations paresseuses et les listes).

### ID des titres [header-ids]

Les ancres de titre générées automatiquement sont généralement **en minuscules et séparées par des traits d'union**, conformément aux slugging courants de style GitHub.

### Quand choisir autre chose [when-to-pick-something-else-3]

GFM ne réplique pas les flux de travail **métadonnées MultiMarkdown**, **kramdown IAL** ou **MMD citation**. Pour les livres, thèses, ou les métadonnées importantes, utilisez **MultiMarkdown** ou **Kramdown** selon le cas.

---

## Discount [discount]

**Idéal pour :** un processeur **rapide basé sur C** qui suit le **Markdown classique** et un ensemble de fonctionnalités **plus anciennes à saveur GitHub**, utile lorsque vous souhaitez un comportement plus proche du **Markdown original** plus des tableaux, des notes de bas de page et des extensions associées sans le livre de règles complet de CommonMark.

Accueil du projet : [Discount](https://www.pell.portland.or.us/~orc/Code/discount/).

### Avantages [strengths-4]

- **Tableaux de style PHP Markdown Extra** et de nombreuses extensions (notes de bas de page, blocs de code délimités si activés, etc. ; voir la [spécification Discount GFM](Discount_GFM_Spec.html) de Marked pour savoir ce que Marked active).
- **Extras « GitHub » optionnels** dans la version amont de Discount (par exemple les listes à cases à cocher, lorsqu'elles sont compilées avec les bons indicateurs) ; Marked documente la combinaison qu'il embarque dans la page des spécifications Discount.
- **Typographie de style SmartyPants** et autres commodités décrites sur le site Discount (bien que tous les processeurs inclus offrent en fait des fonctionnalités de typographie).
- Philosophiquement proche du **Markdown de John Gruber**, avec des extensions pratiques en plus, plutôt que la suite de tests complète de CommonMark.

### Quand choisir autre chose [when-to-pick-something-else-4]

Pour une **parité parfaite au pixel près avec le github.com** d'aujourd'hui, préférez **CommonMark (GFM)**. Pour les **métadonnées et citations MultiMarkdown**, utilisez **MultiMarkdown**.

---

## Comparaison rapide [quick-comparison]

| Critère | MultiMarkdown | Kramdown | CommonMark (GFM) | Discount |
|--------|---------------|--------|-----------------------|--------------|
| **Usage principal** | Prose, articles, livres | HTML stylisé, sites de type Jekyll | README, docs façon GitHub | Markdown classique + extensions |
| **Citations / métadonnées MMD** | Fort | Via une syntaxe différente | Non | Non |
| **Style d'ID de titre manuel** | `## Title [id]` | `## Title {: #id }` (IAL) | Règles de slug spec/GitHub | Aucun |
| **ID de titre automatiques** | Minuscules concaténées | Minuscules séparées par des traits d'union | Minuscules séparées par des traits d'union | Minuscules séparées par des traits d'union |
| **Attributs supplémentaires (classes/identifiants)** | Mécanismes MMD limités | **IAL, très solides** | Limité | Limité |

---

## Voir aussi [see-also]

- [Paramètres : Processeur](Settings_Processor.html), processeur par défaut et options associées
- [Markdown Dingus](Markdown_Dingus.html), essayez les processeurs côte à côte dans Marked
- [Processeur personnalisé](Custom_Processor.html), branchez votre propre chaîne d'outils si nécessaire
