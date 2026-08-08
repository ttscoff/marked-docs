# <%= @title %>

Consultez le [Markdown Dingus](x-marked-3://dingus?processor=kramdown) pour expérimenter le processeur Kramdown.

## Qu'est-ce que Kramdown ? [what-is-kramdown]

Kramdown est un convertisseur rapide et pur Ruby Markdown-superset qui étend la syntaxe Markdown d'origine avec des fonctionnalités trouvées dans d'autres implémentations telles que Maruku, PHP Markdown Extra et Pandoc. Il fournit une syntaxe stricte avec des règles définies tout en conservant la compatibilité avec la plupart des documents Markdown.

## Caractéristiques clés [key-characteristics]

- **Rapide et pur Ruby** : entièrement écrit en Ruby pour plus de performances et de portabilité
- **Syntaxe stricte** : fournit des règles définies et des spécifications claires
- **Fonctionnalités améliorées** : inclut de nombreuses extensions introuvables dans Markdown standard
- **Intégration Jekyll** : processeur Markdown par défaut pour le générateur de site statique Jekyll
- **Complet** : prend en charge les éléments au niveau du bloc et au niveau du span avec une personnalisation étendue

## Différences majeures par rapport au Markdown standard [major-differences-from-standard-markdown]

### 1. **Éléments améliorés au niveau des blocs** [1-enhanced-block-level-elements]

**Listes de définitions**

- Kramdown prend en charge les listes de définitions (pas dans le Markdown standard)
- Utilise `:` pour séparer les termes des définitions

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

**Tableaux**

- Prise en charge complète des tableaux avec en-têtes, alignement et formatage
- Plus complet que la syntaxe de base du tableau Markdown

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Blocs mathématiques**

- Prise en charge des expressions mathématiques utilisant la syntaxe LaTeX
- Prise en charge des mathématiques en ligne et en bloc

```markdown
Inline math: $E = mc^2$

Block math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 2. **Marquage de texte avancé** [2-advanced-text-markup]

**Notes de bas de page**

- Prise en charge complète des notes de bas de page avec numérotation automatique
- Notes de bas de page de style référence avec la syntaxe `[^1]`

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Abréviations**

- Prise en charge des abréviations de style HTML
- Expansion automatique des abréviations définies

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

**Symboles typographiques**

- Conversion automatique des caractères typographiques courants
- Citations intelligentes, tirets cadratins, ellipses, etc.

```markdown
"Smart quotes" and -- em dashes -- and ... ellipses
Even << guillemets >>
```

### 3. **Listes d'attributs et extensions** [3-attribute-lists-and-extensions]

**Définitions de liste d'attributs (ALD)**

- Définir des ensembles d'attributs réutilisables
- Prise en charge des identifiants, des classes et des attributs personnalisés

```markdown
{:ref-name: #myid .my-class title="My Title"}

A paragraph with attributes.
{: #para-one .highlight}
```

**Listes d'attributs en ligne (IAL)**

- Attacher des attributs à des éléments spécifiques
- Prise en charge au niveau du bloc et au niveau de l'étendue

```markdown
This *is*{:.underline} some `code`{:#id}{:.class}.
A [link](test.html){:rel='something'} and some **tools**{:.tools}.
```

**Extensions**

- Système d'extension personnalisé pour des fonctionnalités supplémentaires
- Extensions intégrées pour les commentaires et les options

```markdown
{::comment}
This text is completely ignored by kramdown.
{:/comment}

{::options key="val" /}
```

### 4. **Prise en charge améliorée des blocs de code** [4-enhanced-code-block-support]

**Spécification de la langue**

- Mise en évidence automatique de la syntaxe pour les blocs de code clôturés
- Prise en charge de nombreux langages de programmation

    ```ruby
    def hello
      puts "Hello, World!"
    end
    ```

**Blocs de code standard**

- Gestion améliorée des blocs de code indentés
- Meilleure intégration avec d'autres éléments de bloc

### 5. **Règles d'analyse plus strictes** [5-stricter-parsing-rules]

**Retour à la ligne**

- Prise en charge du contenu emballé (syntaxe paresseuse)
- Des règles claires pour savoir quand le retour à la ligne est autorisé
- Non recommandé pour la lisibilité mais pris en charge pour la compatibilité

**Gestion des onglets**

- Suppose que les tabulations sont des multiples de quatre
- Tabulations autorisées uniquement au début des lignes pour l'indentation
- Ne doit pas être précédé d'espaces

**Limites des blocs**

- Des règles claires indiquant quand les éléments doivent commencer/se terminer sur les limites des blocs
- Comportement cohérent sur différents types d'éléments

### 6. **Prise en charge avancée des liens et des images** [6-advanced-link-and-image-support]

**Liens automatiques**

- Détection automatique améliorée des liens
- Meilleure gestion des URL et des adresses email

**Liens de référence**

- Traitement amélioré des liens de référence
- Meilleure résolution des conflits pour plusieurs définitions

**Attributs de l'image**

- Prise en charge des attributs d'image via les IAL
- Largeur, hauteur, texte alternatif et autres attributs HTML

```markdown
![Alt text](image.jpg){:width="300" height="200" class="responsive"}
```

### 7. **Intégration HTML** [7-html-integration]

**Blocs HTML**

- Meilleure gestion du HTML dans Markdown
- Prise en charge des attributs et du traitement HTML
- Plus flexible que la gestion HTML Markdown standard

**Étendues HTML**

- HTML en ligne avec prise en charge des attributs
- Meilleure intégration avec la syntaxe Markdown

### 8. **Expressions mathématiques** [8-mathematical-expressions]

**Mathématiques en ligne**

- `$...$` syntaxe pour les expressions mathématiques en ligne
- Syntaxe compatible LaTeX

**Bloquer les mathématiques**

- `$$...$$` syntaxe pour les expressions mathématiques en bloc
- Prise en charge des équations et formules complexes

## Kramdown vs autres saveurs Markdown [kramdown-vs-other-markdown-flavors]

| Fonctionnalité | Kramdown | CommonMark (GFM) | Format GitHub | MultiMarkdown | Standard |
| ---------------- | -------- | ---------- | --------------- | ------------- | -------- |
| Barré | Non | Oui | Non | Non | Non |
| Listes de tâches | Non | Non | Oui | Oui | Non |
| Code clôturé | Oui | Oui | Oui | Oui | Non |
| Mathématiques | Oui | Non | Oui | Oui | Non |
| Notes de bas de page | Oui | Oui | Oui | Oui | Non |
| Listes de définitions | Oui | Non | Non | Oui | Non |
| Abréviations | Oui | Non | Non | Non | Non |
| Listes d'attributs | Oui | Non | Non | Non | Non |
| Typographie | Oui | Non | Non | Oui | Non |

## Avantages clés de Kramdown [key-advantages-of-kramdown]

1. **Ensemble complet de fonctionnalités** : comprend de nombreuses extensions introuvables dans d'autres implémentations
2. **Intégration Jekyll** : intégration transparente avec le générateur de site statique Jekyll
3. **Écosystème Ruby** : implémentation de Pure Ruby avec une bonne prise en charge des outils Ruby
4. **Extensibilité** : système d'extension personnalisé pour des fonctionnalités supplémentaires
5. **Prise en charge des attributs** : système d'attributs riche pour la personnalisation de la sortie HTML
6. **Support mathématique** : prise en charge intégrée des expressions mathématiques LaTeX
7. **Analyse stricte** : règles d'analyse claires et sans ambiguïté

## Cas d'utilisation courants [common-use-cases]

**Sites Jekyll**

- Processeur par défaut pour la génération de sites statiques Jekyll
- Excellent pour les sites de documentation et de blogs

**Documentation technique**

- Support mathématique à la rédaction scientifique et technique
- Listes d'attributs pour une personnalisation HTML avancée

**Rédaction académique**

- Prise en charge des notes de bas de page pour les citations et les références
- Expressions mathématiques pour formules et équations

**Gestion de contenu**

- Extensions pour des fonctionnalités personnalisées
- Listes d'attributs pour les métadonnées et le style

## Ressources [resources]

- [Documentation sur la syntaxe Kramdown](https://kramdown.gettalong.org/syntax.html)
- [Documentation du convertisseur Kramdown](https://kramdown.gettalong.org/converter.html)
- [Guide d'intégration de Jekyll](https://jekyllrb.com/docs/configuration/markdown/)
- [Dépôt Kramdown GitHub](https://github.com/gettalong/kramdown)

## Migration depuis le Markdown standard [migration-from-standard-markdown]

La plupart des documents Markdown standard fonctionnent avec Kramdown sans modification. Pour profiter des fonctionnalités de Kramdown :

1. **Ajouter des listes de définitions** : convertissez les glossaires et les listes de termes
2. **Utiliser les listes d'attributs** : ajoutez des identifiants, des classes et des attributs personnalisés
3. **Implémenter les notes de bas de page** : convertir les références entre parenthèses

## Meilleures pratiques [best-practices]

1. **Évitez la syntaxe paresseuse** : ne comptez pas sur le packaging dur pour la lisibilité
2. **Utiliser les listes d'attributs** : exploitez les IAL pour le style et les métadonnées
3. **Indentation cohérente** : utilisez des espaces au lieu de tabulations lorsque cela est possible

---

*Cette documentation couvre Kramdown 2.5.1. Pour les informations les plus récentes, reportez-vous toujours à la documentation officielle sur [kramdown.gettalong.org](https://kramdown.gettalong.org/).*
