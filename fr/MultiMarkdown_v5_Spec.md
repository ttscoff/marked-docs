# <%= @title %>

Consultez le [Markdown Dingus](x-marked-3://dingus?processor=multimarkdown) pour expérimenter le processeur MultiMarkdown.

## Qu'est-ce que MultiMarkdown ? [what-is-multimarkdown]

MultiMarkdown est un processeur Markdown étendu conçu pour fonctionner avec des documents complets plutôt qu'avec de simples fragments de pages Web. Il étend la syntaxe Markdown d'origine avec des fonctionnalités qui permettent la conversion vers plusieurs formats de sortie, notamment les documents HTML, LaTeX, PDF, ODF et Microsoft Word.

## Caractéristiques clés [key-characteristics]

- **Axé sur les documents** : conçu pour des documents complets, pas seulement des extraits Web
- **Sortie multiformat** : convertit en HTML, LaTeX, PDF, ODF, RTF et Word
- **Contenu sur présentation** : se concentre sur la structure et la signification du document
- **Cross-Platform** : fonctionne sur n'importe quel système d'exploitation avec n'importe quel éditeur de texte
- **Extensible** : ensemble de fonctionnalités riches pour les exigences de documents complexes
- **Version 5** : réécriture complète avec des performances et une fiabilité améliorées

## Objectifs de philosophie et de conception [philosophy-and-design-goals]

MultiMarkdown suit le principe selon lequel **le contenu est plus important que la présentation**. L'accent est mis sur la représentation de la signification des documents (il s'agit d'une liste, d'un tableau, etc.) plutôt que sur la dictée des polices, des couleurs ou du style.

L'objectif est d'être utilisable pour 80 % des documents rédigés par 80 % des personnes, ce qui le rend adapté aux romans, aux thèses, à la documentation technique et à la plupart des autres contenus écrits.

## Principales fonctionnalités et extensions [major-features-and-extensions]

### 1. **Prise en charge des métadonnées** [1-metadata-support]

- Documenter les métadonnées en haut des fichiers
- Titre, auteur, date et variables personnalisées
- Inclusion automatique dans les en-têtes de sortie

```markdown
title: Mon document
author: John Doe
date: 2024-01-15
custom: valeur

<!-- Une ligne vide termine les métadonnées -->
Contenu
---

# Contenu du document
```

**Variables de métadonnées**

- Utiliser les valeurs de métadonnées dans tout le document
- Syntaxe : `[%variable_name]`
- Substitution automatique pendant le traitement

```markdown
Titre : [%title]
Auteur : [%author]
Date : [%date]
```

### 2. **Tableaux avancés** [2-advanced-tables]

**Prise en charge complète des tables**

- En-têtes, alignement et structures de tableaux complexes
- Prise en charge des légendes et des étiquettes des tableaux
- Renvois aux tableaux

```markdown
| En-tête 1 | En-tête 2 | En-tête 3 |
| :------- | :------: | -------: |
| Gauche   |  Centre  |   Droite |
| Aligné   |  Aligné  |   Aligné |

Table: Exemple de tableau avec alignement
```

**Caractéristiques du tableau**

- Alignement des colonnes à l'aide de deux-points
- Légendes et étiquettes des tableaux
- Renvois croisés avec `[Table 1]`
- Prise en charge des structures de tables complexes

### 3. **Notes de bas de page et citations** [3-footnotes-and-citations]

**Notes de bas de page**

- Notes de bas de page de style référence avec la syntaxe `[^1]`
- Numérotation et liaison automatiques
- Prise en charge des notes de bas de page en ligne

```markdown
Ceci est une phrase avec une note de bas de page[^1].

[^1]: Ceci est le contenu de la note de bas de page.
```

**Aide aux citations**

- Formatage des citations académiques
- Génération de bibliographie
- Prise en charge de différents styles de citation

```
Ceci est une déclaration qui doit être attribuée à
sa source[p. 23][#Doe:2006].
```

Et voici la description de la référence à être
utilisé dans la bibliographie.

```
[#Doe:2006]: John Doe. *Un livre extraordinaire quelconque*.  Vanity Press, 2006.
```

Dans la sortie HTML, les citations ne peuvent pas être distinguées des notes de bas de page.

Vous n'êtes pas obligé d'utiliser un localisateur (par exemple p. 23), et il n'y a pas de règles spéciales sur ce qui peut être utilisé comme localisateur si vous choisissez d'en utiliser un. Si vous préférez omettre le localisateur, utilisez simplement un jeu de crochets vide avant la citation :

```
Ceci est une déclaration qui doit être attribuée à sa
source[][#Doe:2006].
```

Il n'y a pas de règles sur le format de clé de citation que vous utilisez (par exemple Doe:2006), mais il doit être précédé d'un `#`, tout comme les notes de bas de page utilisent `^`.

### 4. **Références croisées** [4-cross-references]

**Références croisées automatiques**

- Lien vers les titres, tableaux, figures et équations
- Génération automatique d'étiquettes
- Prise en charge des étiquettes personnalisées

```markdown
Voir [Table 1] pour plus de détails.
Consultez [Section 2.1] pour plus d'informations.

## Section 2.1
```

**Types de référence**

- Rubriques : `[Section 1]`, `[Heading Title]`
- Tableaux : `[Table 1]`, `[Table: Caption]`
- Chiffres : `[Figure 1]`, `[Figure: Caption]`
- Équations : `[Equation 1]`

### 5. **Listes de définitions** [5-definition-lists]

**Paires terme-définition**

- Prise en charge des listes de définitions
- Plusieurs définitions par terme
- Sortie HTML `<dl>` appropriée

```markdown
Terme 1
: Définition 1

Terme 2
: Définition 2a
: Définition 2b
```

### 6. **Blocs de code clôturés** [6-fenced-code-blocks]

**Blocs de code spécifiques à la langue**

- Triple backticks avec spécification de langue
- Prise en charge de la coloration syntaxique
- Détection automatique de la langue

```markdown
```python
def hello():
    print("Hello, World!")
```
```

**Fonctionnalités des blocs de code**

- Spécification du langage pour la coloration syntaxique
- Prise en charge de nombreux langages de programmation
- Sortie HTML `<code>` appropriée

### 7. **Prise en charge des mathématiques** [7-math-support]

**Expressions mathématiques**

- Syntaxe mathématique compatible LaTeX
- Prise en charge des mathématiques en ligne et en bloc
- Intégration avec la sortie LaTeX

```markdown
Mathématiques en ligne : $E = mc^2$

Mathématiques en bloc :

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 8. **Attributs d'image et de lien** [8-image-and-link-attributes]

**Liens et images améliorés**

- Prise en charge des attributs HTML
- Largeur, hauteur, texte alternatif, etc.
- Meilleure intégration avec les formats de sortie

```markdown
[Texte du lien]: url.html title="Titre du lien" class="external"
```

### 9. **Transclusion** [9-transclusion]

**Inclusion de fichier**

- Inclure d'autres fichiers dans les documents
- Prise en charge des inclusions imbriquées
- Résolution automatique du chemin

```markdown
{{chapter1.md}}
{{../shared/intro.md}}
```

**Fonctionnalités de transclusion**

- Inclusion de fichier avec `{{filename}}`
- Prise en charge des chemins relatifs et absolus
- Prise en charge de la transclusion imbriquée
- Génération de manifeste pour les fichiers inclus

### 10. **Intégration CriticMarkup** [10-criticmarkup-integration]

**Suivi des modifications**

- Prise en charge de la syntaxe CriticMarkup
- Suivre les ajouts, les suppressions et les commentaires
- Fonctionnalités d'édition collaborative

```markdown
Ceci est {>>texte supprimé<<} et ceci est {++texte ajouté++}.

Ceci est une {~~suppression~>remplacement~~}.
```

### 11. **Table des matières** [11-table-of-contents]

**Génération automatique de la table des matières**

- `{{TOC}}` espace réservé pour la table des matières
- Structure hiérarchique basée sur les rubriques
- Génération de table des matières personnalisable

```markdown
# Titre du document

{{TOC}}

## Section 1
Contenu ici...

## Section 2
Plus de contenu...
```

### 12. **Abréviations** [12-abbreviations]

**Abréviations de style HTML**

- Définir des abréviations pour l'expansion automatique
- Prise en charge des info-bulles et des explications
- Sortie HTML `<abbr>` appropriée

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

Ceci utilise HTML et CSS.
```

## MultiMarkdown v5 vs autres saveurs Markdown [multimarkdown-v5-vs-other-markdown-flavors]

| Fonctionnalité | MultiMarkdown v5 | CommonMark (GFM) | Discount | Kramdown | Standard |
| ---------------- | ---------------- | ---------- | ------------ | -------- | -------- |
| Tableaux | Oui | Non | Oui | Oui | Non |
| Barré | Oui | Non | Oui | Non | Non |
| Listes de tâches | Oui | Non | Oui | Non | Non |
| Code clôturé | Oui | Oui | Oui | Oui | Non |
| Mathématiques | Oui | Non | Non | Oui | Non |
| Notes de bas de page | Oui | Non | Oui | Oui | Non |
| Listes de définitions | Oui | Non | Non | Oui | Non |
| Abréviations | Oui | Non | Non | Oui | Non |
| Listes d'attributs | Oui | Non | Non | Oui | Non |
| Rallonges | Oui | Non | Limité | Oui | Non |
| Typographie | Oui | Non | De base | Oui | Non |
| Liens automatiques | Oui | Non | Oui | Non | Non |
| Références croisées | Oui | Non | Non | Non | Non |
| Citations | Oui | Non | Non | Non | Non |
| Transclusion | Oui | Non | Non | Non | Non |
| Métadonnées | Oui | Non | Non | Non | Non |

## Avantages clés de MultiMarkdown v5 [key-advantages-of-multimarkdown-v5]

1. **Axé sur les documents** : conçu pour des documents complets, pas seulement des extraits Web
2. **Sortie multiformat** : conversion en HTML, LaTeX, PDF, ODF, RTF et Word
3. **Soutien académique** : citations, notes de bas de page et références croisées
4. **Fonctionnalités professionnelles** : métadonnées, transclusion et formatage avancé
5. **Multiplateforme** : fonctionne sur n'importe quel système d'exploitation
6. **À l'épreuve du temps** : le format de texte brut garantit une compatibilité à long terme
7. **Extensible** : ensemble de fonctionnalités riches pour les exigences de documents complexes

## Cas d'utilisation courants [common-use-cases]

**Rédaction académique**

- Thèses, mémoires et documents de recherche
- Gestion des citations et génération de bibliographie
- Renvois croisés et notes de bas de page

**Documentation technique**

- Documentation API et guides utilisateurs
- Spécifications techniques et manuels
- Documentation du code avec coloration syntaxique

**Publication**

- Livres, articles et rapports
- Sortie multiformat pour différentes plateformes
- Mise en forme professionnelle des documents

**Gestion de contenu**

- Sites de documentation
- Bases de connaissances et wikis
- Projets d'écriture collaborative

## Meilleures pratiques [best-practices]

1. **Utiliser les métadonnées** : exploitez le contenu YAML pour les informations sur les documents
2. **Structure avec en-têtes** : utilisez la hiérarchie de titres appropriée pour la génération de la table des matières
3. **Tirez parti des références croisées** : utilisez les liens automatiques pour une meilleure navigation
4. **Organisez avec Transclusion** : divisez les documents volumineux en fichiers gérables
5. **Test de sortie** : vérifiez le formatage dans différents formats de sortie
6. **Utiliser les citations** : mettre en œuvre des pratiques de citation académique appropriées

## Migration à partir d'autres versions de Markdown [migration-from-other-markdown-flavors]

La plupart des Markdown standard fonctionnent avec MultiMarkdown sans modifications. Pour profiter des fonctionnalités MMD :

1. **Ajouter des métadonnées** : inclure les éléments préliminaires YAML pour les informations sur le document
2. **Utilisez des références croisées** : remplacez les liens manuels par des références automatiques
3. **Mettre en œuvre les citations** : ajouter un formatage approprié des citations académiques
4. **Structure avec transclusion** : divisez les documents volumineux en fichiers plus petits
5. **Tirer parti des tableaux** : utilisez les fonctionnalités avancées des tableaux pour la présentation des données

## Ressources [resources]

- [Guide de l'utilisateur MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html)
- [Guide de syntaxe MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html#syntax)
- [Dépôt GitHub MultiMarkdown](https://github.com/fletcher/MultiMarkdown-5)
- [Documentation MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/)

---

*Cette documentation couvre MultiMarkdown v5.1.0. Pour les informations les plus récentes, reportez-vous toujours à la documentation officielle de MultiMarkdown sur [fletcher.github.io/MultiMarkdown-5](https://fletcher.github.io/MultiMarkdown-5/).*
