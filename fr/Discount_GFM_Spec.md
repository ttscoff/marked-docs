# <%= @title %>

Consultez le [Markdown Dingus](x-marked-3://dingus?processor=discount) pour expérimenter le processeur Discount.

## Qu'est-ce que Discount GFM ? [what-is-discount-gfm]

Discount GFM (GitHub Flavored Markdown) est un processeur Markdown basé sur C qui implémente la syntaxe Markdown étendue de GitHub. Il est basé sur la bibliothèque Discount d'origine mais amélioré avec des fonctionnalités spécifiques à GitHub telles que des tableaux, des listes de tâches, du texte barré et des liens URL automatiques.

## Caractéristiques clés [key-characteristics]

- **Performances basées sur C** : implémentation C rapide et native pour des performances optimales
- **Compatibilité GitHub** : implémente les extensions Markdown de GitHub pour une compatibilité maximale
- **Léger** : dépendances minimales et faible encombrement
- **Extensible** : prend en charge diverses extensions Markdown et options personnalisées
- **Prise en charge HTML5** : génère une sortie HTML5 moderne avec un balisage sémantique approprié

## Différences majeures par rapport au Markdown standard [major-differences-from-standard-markdown]

### 1. **Extensions Markdown façon GitHub** [1-github-flavored-markdown-extensions]

**Tableaux**

- Prise en charge complète des tables de style GitHub avec options d'alignement
- En-têtes, séparateurs et lignes de données avec une structure de tableau HTML appropriée
- Alignement des colonnes à l'aide de deux-points (`:`) dans les lignes de séparation

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Listes de tâches**

- Prise en charge des cases à cocher de style GitHub dans les listes
- Cases à cocher interactives (rendu sous forme d'éléments d'entrée HTML)
- Les états cochés et non cochés sont pris en charge

```markdown
- [x] Completed task
- [ ] Pending task
- [x] Another completed task
```

**Texte barré**

- Le texte entouré de doubles tildes (`~~`) devient barré
- Utilise les balises HTML `<del>` pour le balisage sémantique
- Prend en charge plusieurs tildes pour mettre l'accent

```markdown
~~This text is crossed out~~
~~Mistaken text that should be removed~~
```

### 2. **Prise en charge améliorée des blocs de code** [2-enhanced-code-block-support]

**Blocs de code clôturés**

- Triple backticks (```` ``` ````) pour les blocs de code
- Spécification du langage pour la coloration syntaxique
- Aucune indentation requise (contrairement au Markdown standard)

```markdown
```javascript
function hello() {
  console.log("Hello, World!");
}
```
```

**Détection automatique du langage**

- Prise en charge de nombreux langages de programmation
- Coloration syntaxique appropriée si prise en charge
- Repli sur texte brut pour les langages non pris en charge

### 3. **Liaison automatique des URL** [3-automatic-url-linking]

**Liens automatiques d'URL**

- Conversion automatique des URL en liens cliquables
- Prise en charge des protocoles http, https et ftp
- Les adresses e-mail sont automatiquement converties en liens mailto

```markdown
Visit http://example.com for more information.
Contact us at user@example.com
```

**Détection de lien intelligent**

- Reconnaît les URL sans balisage explicite
- Gère divers formats et protocoles d'URL
- Options de sécurité de liaison configurables

### 4. **Fonctionnalités avancées de la liste** [4-advanced-list-features]

**Listes alphabétiques**

- Listes ordonnées avec marqueurs alphabétiques (a, b, c, etc.)
- Progression automatique dans l'alphabet
- Sortie HTML `<ol type="a">` appropriée

```markdown
a. First item
b. Second item
c. Third item
```

**Traitement amélioré des listes**

- Meilleure gestion des listes imbriquées
- Espacement et indentation améliorés
- Prise en charge des types de listes mixtes

### 5. **Prise en charge des notes de bas de page** [5-footnotes-support]

**Notes de bas de page de style référence**

- Numérotation automatique des notes de bas de page
- Liens de référence avec la syntaxe `[^1]`
- Définitions des notes de bas de page à la fin du document

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Traitement automatique des notes de bas de page**

- Génère une structure de note de bas de page HTML appropriée
- Liens entre références et définitions
- Numérotation séquentielle dans tout le document

### 6. **Intégration HTML** [6-html-integration]

**Prise en charge HTML5**

- Reconnaissance complète des balises HTML5
- Génération de balisage sémantique appropriée
- Structure et attributs HTML modernes

**Blocs HTML bruts**

- Prise en charge du HTML dans Markdown
- Échappement et nettoyage appropriés
- Intégration avec la syntaxe Markdown

### 7. **Règles d'accentuation améliorées** [7-enhanced-emphasis-rules]

**Emphase détendue**

- Les traits de soulignement simples (`_`) ne créent pas d'emphase au milieu des mots
- Mieux pour documenter le code et le contenu technique
- Empêche l'accentuation indésirable dans les identifiants

```markdown
This is a variable_name that won't be emphasized.
This is _emphasized text_ that will be styled.
```

**Plusieurs niveaux d'accentuation**

- Prise en charge de l'accentuation gras, italique et combinée
- Conforme aux règles d'accentuation standard de Markdown
- Sortie HTML appropriée avec les balises `<strong>` et `<em>`

### 8. **Génération de la table des matières** [8-table-of-contents-generation]

**Table des matières automatique**

- Génère une table des matières à partir des titres
- Structure hiérarchique basée sur les niveaux de rubriques
- Options de génération de table des matières configurables

**Génération d'ID de titre**

- Génération automatique d'identifiants pour les rubriques
- Liens d'ancrage pour une navigation facile
- Formatage d'identification cohérent

## Discount GFM par rapport aux autres saveurs Markdown [discount-gfm-vs-other-markdown-flavors]

| Fonctionnalité | Discount | CommonMark (GFM) | Kramdown | MultiMarkdown | Standard |
| ---------------- | ------------ | ---------- | -------- | ------------- | -------- |
| Tableaux | Oui | Non | Oui | Oui | Non |
| Barré | Oui | Non | Non | Oui | Non |
| Listes de tâches | Oui | Non | Non | Oui | Non |
| Code clôturé | Oui | Oui | Oui | Oui | Non |
| Mathématiques | Non | Non | Oui | Oui | Non |
| Notes de bas de page | Oui | Non | Oui | Oui | Non |
| Listes de définitions | Non | Non | Oui | Oui | Non |
| Abréviations | Non | Non | Oui | Non | Non |
| Listes d'attributs | Non | Non | Oui | Non | Non |
| Rallonges | Limité | Non | Oui | Oui | Non |
| Typographie | De base | Non | Oui | Non | Non |
| Liens automatiques | Oui | Non | Non | Non | Non |
| Listes alphabétiques | Oui | Non | Non | Non | Non |

## Avantages clés de Discount GFM [key-advantages-of-discount-gfm]

1. **Compatibilité GitHub** : parfait pour le contenu qui doit fonctionner sur GitHub
2. **Performances** : implémentation rapide basée sur C
3. **Simplicité** : axé sur les fonctionnalités de base de GitHub sans complexité
4. **Fiabilité** : mise en œuvre stable et bien testée
5. **Conformité aux normes** : suit la spécification Markdown de GitHub
6. **Léger** : utilisation minimale des ressources et dépendances

## Cas d'utilisation courants [common-use-cases]

**Documentation GitHub**

- Fichiers README et documentation du projet
- Pages GitHub et wikis
- Descriptions des problèmes et des demandes d'extraction

**Rédaction technique**

- Documentation du code et tutoriels
- Documentation API
- Spécifications techniques

**Gestion de contenu**

- Articles et articles de blog
- Sites de documentation
- Bases de connaissances

**Édition collaborative**

- Documentation de l'équipe
- Documents de planification du projet
- Notes et procès-verbaux de réunion

## Options de configuration [configuration-options]

Discount GFM prend en charge diverses options de configuration :

- **Auto-linking** : activer/désactiver la détection automatique d'URL
- **Notes de bas de page** : Contrôler le traitement des notes de bas de page
- **Table des matières** : paramètres de génération de la table des matières
- **Sécurité HTML** : validation et nettoyage des liens
- **Mode strict** : règles d'analyse améliorées
- **Smart Quotes** : conversion automatique des guillemets droits en guillemets typographiques

## Détails de mise en œuvre [implementation-details]

**Options de l'analyseur**

- `kGHMarkdownAutoLink` : Activer la liaison automatique d'URL
- `kGHMarkdownFootnotes` : Activer le traitement des notes de bas de page
- `kGHMarkdownTOC` : Activer la génération de la table des matières
- `kGHMarkdownSafeLinks` : Restreindre les liens vers des protocoles sécurisés
- `kGHMarkdownNoHTMLTags` : Désactiver le traitement des balises HTML

**Fonctionnalités de sortie**

- Balisage sémantique HTML5
- Hiérarchie des titres appropriée
- Structures de tables accessibles
- Sortie HTML propre et valide

## Meilleures pratiques [best-practices]

1. **Utilisez les tables avec parcimonie** : les tables sont puissantes mais peuvent être complexes à gérer
2. **Tirer parti des listes de tâches** : idéal pour la gestion de projet et la documentation
3. **Utiliser les liens automatiques** : laissez le processeur gérer automatiquement la conversion d'URL
4. **Structure avec titres** : utilisez la hiérarchie de titres appropriée pour une meilleure génération de table des matières
5. **Test sur GitHub** : Vérifier la compatibilité avec le rendu de GitHub

## Migration depuis le Markdown standard [migration-from-standard-markdown]

La plupart des Markdown standard fonctionnent avec Discount GFM sans modifications. Pour profiter des fonctionnalités de GFM :

1. **Ajouter des tables** : convertissez les données au format de table de style GitHub
2. **Utilisez les listes de tâches** : remplacez les puces par des cases à cocher, le cas échéant
3. **Activer le barré** : utilisez `~~text~~` pour le contenu barré
4. **Tirer parti des liens automatiques** : supprimez le balisage manuel des liens pour les URL simples
5. **En-têtes de structure** : garantir une hiérarchie de titres appropriée pour la génération de la table des matières

## Ressources [resources]

- [Spécification GitHub Flavored Markdown](https://github.github.com/gfm/)
- [Documentation de la bibliothèque Discount](https://www.pell.portland.or.us/~orc/Code/discount/)
- [Guide Markdown de GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Aide-mémoire Markdown](https://www.markdownguide.org/cheat-sheet/)

---

*Cette documentation couvre Discount GFM tel qu'implémenté dans Marked. Pour obtenir les informations les plus récentes, reportez-vous toujours à la spécification officielle GitHub Flavored Markdown.*
