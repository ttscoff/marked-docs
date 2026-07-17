# <%= @title %>

## Qu'est-ce que Markdown ? [what-is-markdown]

Markdown est un langage de balisage léger qui vous permet d'écrire dans un format texte brut facile à lire et à écrire, puis de le convertir en HTML structurellement valide. L'objectif de conception primordial de la syntaxe de formatage de Markdown est de la rendre aussi lisible que possible.

## Syntaxe de base [basic-syntax]

### Titres [headers]

Créez des titres en utilisant des symboles dièse (`#`). Le nombre de dièses détermine le niveau de titre :

```markdown
# Titre 1
## Titre 2
### Titre 3
#### Titre 4
##### Titre 5
###### Titre 6
```

### Emphase [emphasis]

**Texte en gras** en utilisant des doubles astérisques ou doubles traits de soulignement :

```markdown
**Texte en gras**
__Texte en gras__
```

*Texte en italique* en utilisant des astérisques simples ou des traits de soulignement simples :

```markdown
*Texte en italique*
_Texte en italique_
```

### Listes [lists]

**Listes non ordonnées** utilisant des astérisques, des signes plus ou des tirets :

```markdown
* Élément 1
* Élément 2
* Élément 3

+ Élément 1
+ Élément 2
+ Élément 3

- Élément 1
- Élément 2
- Élément 3
```

**Listes ordonnées** utilisant des nombres suivis de points :

```markdown
1. Premier élément
2. Deuxième élément
3. Troisième élément
```

### Liens [links]

**Liens en ligne** avec le texte entre crochets et l'URL entre parenthèses :

```markdown
[Texte du lien](http://example.com)
```

**Liens de référence** avec le texte entre crochets et une référence entre crochets :

```markdown
[Texte du lien][reference]

[reference]: http://example.com "Titre facultatif"
```

**Liens automatiques** en entourant les URL de chevrons :

```markdown
<http://example.com>
<user@example.com>
```

### Images [images]

Les images utilisent une syntaxe similaire aux liens, mais avec un point d'exclamation au début :

```markdown
![Texte alternatif](http://example.com/image.jpg)
![Texte alternatif][image-reference]

[image-reference]: http://example.com/image.jpg "Titre facultatif"
```

### Citations [blockquotes]

Créez des citations en utilisant le symbole supérieur à (`>`) au début de chaque ligne :

```markdown
> Ceci est une citation.
> Elle peut s'étendre sur plusieurs lignes.
>
> Vous pouvez avoir plusieurs paragraphes dans une citation.
```

### Code [code]

**Code en ligne** en utilisant des backticks :

```markdown
Utilisez `code` dans votre texte.
```

**Blocs de code** en indentant avec quatre espaces ou une tabulation :

```markdown
    Ceci est un bloc de code.
    Il préserve la mise en forme et l'espacement.
    Plusieurs lignes sont prises en charge.
```

### Règles horizontales [horizontal-rules]

Créez des règles horizontales en utilisant trois tirets, astérisques ou traits de soulignement ou plus :

```markdown
---

***

___
```

### Sauts de ligne [line-breaks]

**Sauts de ligne forcés** en terminant une ligne par deux espaces ou plus :

```markdown
Cette ligne se termine par deux espaces.
Cela crée un saut de ligne forcé.
```

**Sauts de ligne doux** en appuyant simplement sur Entrée (crée un espace en HTML) :

```markdown
Cette ligne
se poursuit sur la ligne suivante avec un espace.
```

### Échappement de caractères [escaping-characters]

Échappez les caractères spéciaux en utilisant des barres obliques inverses :

```markdown
\*Ce texte n'est pas en italique\*
\[Ceci n'est pas un lien\]
```

Caractères courants pouvant être échappés :
- `\` barre oblique inverse
- `` ` `` accent grave
- `*` astérisque
- `_` trait de soulignement
- `{}` accolades
- `[]` crochets
- `()` parenthèses
- `#` dièse
- `+` plus
- `-` moins
- `.` point
- `!` point d'exclamation

## Bonnes pratiques [best-practices]

1. **Utilisez des lignes vides** pour séparer les différents éléments et améliorer la lisibilité
2. **Soyez cohérent** dans vos choix de formatage (par exemple, utilisez soit `*` soit `_` pour l'emphase)
3. **Restez simple** : Markdown est conçu pour être lisible en texte brut
4. **Testez votre résultat** pour vous assurer qu'il s'affiche comme prévu
5. **Utilisez un texte de lien significatif** plutôt que des phrases génériques comme « cliquez ici »

## Modèles courants [common-patterns]

### Listes imbriquées [nested-lists]

```markdown
1. Premier élément
   - Élément imbriqué
   - Un autre élément imbriqué
2. Deuxième élément
   - Plus de contenu imbriqué
```

### Listes avec paragraphes [lists-with-paragraphs]

```markdown
1. Premier élément

   Voici un paragraphe sous le premier élément.

2. Deuxième élément

   Voici un paragraphe sous le deuxième élément.
```

### Citations avec d'autres éléments [blockquotes-with-other-elements]

```markdown
> Ceci est une citation avec du **texte en gras** et du *texte en italique*.
>
> - Elle peut contenir des listes
> - Et d'autres éléments Markdown
>
> > Les citations imbriquées sont également possibles.
```

## Résumé [summary]

Markdown offre une façon simple et lisible de formater du texte qui peut être facilement converti en HTML. La clé est de rester simple et lisible tout en utilisant les éléments de syntaxe de base de manière cohérente. Avec de la pratique, vous constaterez que Markdown devient une seconde nature et facilite grandement la rédaction de contenu structuré.

---

*Ce tutoriel couvre la syntaxe Markdown de base telle que définie dans la spécification originale. Pour des fonctionnalités plus avancées, consultez la documentation des processeurs Markdown spécifiques comme CommonMark (GFM), MultiMarkdown ou GitHub Flavored Markdown.*
