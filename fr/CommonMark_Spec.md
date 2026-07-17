# <%= @title %>

Consultez le [Markdown Dingus](x-marked-3://dingus?processor=commonmark) pour expérimenter le processeur CommonMark (GFM).


## Qu'est-ce que CommonMark ? [what-is-commonmark]

CommonMark est une implémentation de Markdown fortement spécifiée et hautement compatible. Il a été créé pour résoudre les ambiguïtés et les incohérences de la spécification Markdown originale de John Gruber, qui ont conduit à des implémentations divergentes sur différentes plates-formes et outils.

## Pourquoi CommonMark existe [why-commonmark-exists]

La spécification Markdown originale de John Gruber était intentionnellement ambiguë dans de nombreux domaines, conduisant à des interprétations différentes selon diverses implémentations. Cela a créé des problèmes : le même document Markdown pouvait s'afficher différemment selon les plateformes (GitHub, StackOverflow, Reddit, etc.).

CommonMark fournit :

- **Spécifications non ambiguës** pour toute la syntaxe Markdown
- **Suite de tests complète** pour garantir un comportement cohérent
- **Règles de priorité claires** en cas de syntaxe conflictuelle
- **Algorithme d'analyse détaillé** qui peut être implémenté de manière cohérente

## Différences clés par rapport au Markdown standard [key-differences-from-standard-markdown]

### 1. **Règles d'analyse plus strictes** [1-stricter-parsing-rules]

CommonMark applique un comportement d'analyse plus cohérent :

**Lignes vides avant les éléments de bloc**

- CommonMark exige des lignes vides avant les titres, citations et listes
- Standard Markdown les autorise souvent sans lignes vides

```markdown
Text
# Heading
```

*CommonMark : nécessite une ligne vide avant le titre*

*Standard Markdown : l'autorise souvent sans ligne vide*

### 2. **Analyse des éléments de liste** [2-list-item-parsing]

**Exigences d'indentation**

- CommonMark a des règles précises pour l'indentation des éléments de liste
- Les sous-listes doivent être indentées de manière cohérente (généralement 4 espaces)
- Les implémentations Markdown standard varient sur ce point

```markdown
1. First item
   - Sublist item (4 spaces required in CommonMark)
2. Second item
```

**Continuation de liste**

- CommonMark a des règles claires pour savoir quand les éléments de la liste sont « lâches » ou « serrés ».
- Les listes « lâches » enveloppent les éléments dans des balises `<p>`, les listes « serrées » non

### 3. **Gestion des blocs de code** [3-code-block-handling]

**Blocs de code clôturés**

- CommonMark standardise la syntaxe des blocs de code clôturés avec des backticks ou des tildes
- Nécessite une indentation cohérente et des marqueurs de fermeture cohérents


    ```language
    code here
    ```


**Blocs de code indentés**

- CommonMark exige des lignes vides avant les blocs de code indentés
- Standard Markdown les autorise souvent sans lignes vides

### 4. **Traitement des liens et des images** [4-link-and-image-processing]

**Priorité des liens de référence**

- CommonMark a des règles claires pour lesquelles la définition de référence est prioritaire
- Plusieurs définitions pour la même référence sont traitées de manière cohérente

```markdown
[link1]: /url1
[link1]: /url2
[link1]  <!-- Uses /url2 in CommonMark -->
```

**Ordre d'analyse des liens**

- CommonMark traite les liens avant l'emphase
- Cela affecte la façon dont la syntaxe imbriquée est interprétée

### 5. **Emphase et forte emphase** [5-emphasis-and-strong-emphasis]

**Règles d'accentuation imbriquées**

- CommonMark dispose d'algorithmes spécifiques pour gérer les marqueurs imbriqués `*` et `_`
- Empêche une analyse ambiguë des motifs d'emphase complexes

```markdown
*foo *bar* baz*  <!-- Clear precedence rules in CommonMark -->
```

**Traitement des délimiteurs**

- CommonMark utilise un algorithme de « pile de délimiteurs » pour une analyse cohérente de l'emphase
- Les implémentations standard de Markdown varient dans leur approche

### 6. **Traitement des blocs HTML** [6-html-block-processing]

**Détection des blocs HTML**

- CommonMark dispose de 7 types différents de blocs HTML avec des règles spécifiques
- Chaque type a des exigences différentes pour les conditions de début/fin

```html
<div>
This is an HTML block in CommonMark
</div>
```

### 7. **Gestion des sauts de ligne** [7-line-break-handling]

**Sauts de ligne forcés**

- CommonMark nécessite deux espaces en fin de ligne pour les sauts de ligne forcés
- Un simple retour à la ligne devient un saut doux (ignoré en HTML)

```markdown
Line one
Line two  <!-- Two spaces before line break -->
```

### 8. **Références d'entités et de caractères** [8-entity-and-character-references]

**Références de caractères numériques**

- CommonMark prend en charge les références numériques décimales et hexadécimales
- Le support varie selon les implémentations Markdown standard

```html
&#8212;  <!-- Decimal -->
&#x2014; <!-- Hexadecimal -->
```

## Algorithme d'analyse CommonMark [commonmark-parsing-algorithm]

CommonMark utilise une approche d'analyse en deux phases :

### Phase 1 : structure de bloc [phase-1-block-structure]

1. **Traitement des lignes** : chaque ligne est analysée pour les marqueurs au niveau du bloc
2. **Blocs de conteneurs** : les blockquotes, les listes et autres conteneurs sont identifiés
3. **Blocs feuilles** : les titres, blocs de code et paragraphes sont traités
4. **Liens de référence** : les définitions de liens sont collectées pour un usage ultérieur

### Phase 2 : Structure en ligne [phase-2-inline-structure]

1. **Traitement en ligne** : le texte dans les blocs est analysé pour les éléments en ligne
2. **Analyse de l'emphase** : utilise l'algorithme de pile de délimiteurs pour une emphase cohérente
3. **Résolution des liens** : les liens de référence sont résolus à partir des définitions collectées
4. **Traitement d'entité** : les références de caractères sont converties en caractères réels

## Avantages de CommonMark [benefits-of-commonmark]

1. **Comportement prévisible** : la même entrée produit toujours la même sortie
2. **Compatibilité multiplateforme** : fonctionne de manière cohérente sur différents outils
3. **Tests complets** : une suite de tests complète garantit la fiabilité
4. **Documentation claire** : les spécifications détaillées éliminent les conjectures
5. **À l'épreuve du temps** : points d'extension bien définis pour les nouvelles fonctionnalités

## Notes d'implémentation [implementation-notes]

CommonMark est conçu pour être :

- **Conforme aux spécifications** : suit exactement la spécification CommonMark officielle
- **Test-driven** : réussit la suite de tests officielle CommonMark
- **Extensible** : peut être étendu avec des fonctionnalités supplémentaires tout en conservant la compatibilité
- **Rapide** : algorithmes d'analyse optimisés pour les performances

## Ressources [resources]

- [Spécification CommonMark](https://spec.commonmark.org/0.31.2/)
- [Suite de tests CommonMark](https://github.com/commonmark/commonmark-spec)
- [CommonMark Dingus](https://spec.commonmark.org/dingus/) - Outil de test en ligne
- [Forum de discussion CommonMark](https://talk.commonmark.org/)

---

*Cette documentation couvre CommonMark 0.31.2 (2024-01-28). Pour les informations les plus récentes, reportez-vous toujours à la spécification officielle.*
