<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Ces options se trouvent dans la feuille **Configurer Apex**. Ouvrez-la depuis {% prefspane Processor %} lorsque le processeur par défaut est **Apex (bêta)**. Chaque option ne s'applique qu'à Apex. Les maths, Critic Markup, les hashtags, les inclusions de fichiers et les identifiants de titres restent dans les autres réglages de Marked.

Voir [Apex (bêta)](Apex.html) pour ce qu'est Apex et la syntaxe qu'il couvre.

Les cases de la feuille l'emportent sur les mêmes réglages d'un fichier de métadonnées Apex. Les chemins de fichiers sont facultatifs. Un chemin que Marked ne peut pas lire est ignoré, et l'aperçu continue.

## Fichiers [files]

CSL
: Un fichier Citation Style Language (`.csl`) utilisé quand Apex met en forme une bibliographie. Laissez vide pour utiliser le style nommé dans le document ou dans le fichier de métadonnées.

Bibliographie
: Un ou plusieurs fichiers de bibliographie. Types acceptés : BibTeX (`.bib`), CSL JSON (`.json`) et CSL YAML (`.yml`, `.yaml`). Cliquez sur **Ajouter** pour un autre fichier. Apex les consulte pour résoudre les citations.

Concordance
: Un ou plusieurs fichiers de concordance (`.tsv`, `.txt` ou `.csv`) utilisés pour construire un index. Cliquez sur **Ajouter** pour un autre fichier.

Fichier de métadonnées
: Un fichier de métadonnées externe (`.yml`, `.yaml`, `.txt` ou `.md`) fusionné avant l'exécution d'Apex. Si le document et le fichier définissent la même clé, les métadonnées du document l'emportent. Les cases de cette feuille l'emportent sur les valeurs du fichier de métadonnées.

## Syntaxe [syntax]

Activées par défaut, sauf indication contraire.

Tableaux
: Tableaux à barres verticales, avec une ligne d'en-tête et une ligne de séparation.

Notes de bas de page
: Notes de référence (`[^id]`) et notes en ligne.

Listes de définitions
: Listes terme et définition (`: définition`).

Exposant / indice
: `^super^` et `~sub~`. Désactivez cette option si un seul tilde ne doit pas signifier un indice. Le réglage Marked **Rendre ~texte~ comme du texte souligné** est distinct et entre en conflit avec l'indice.

Barré
: `~~supprimé~~`.

Liens automatiques URL et e-mails
: Les URL `https://` et les adresses e-mail nues deviennent des liens.

Divs délimités
: Blocs `::: nom` qui entourent une section d'un `<div>`.

Spans entre crochets
: Spans d'attributs en ligne, comme `[texte]{.class}`.

Listes alphabétiques
: Listes qui commencent par `a.` ou `A.`, en plus des nombres.

Marqueurs de liste mixtes
: Une liste peut mélanger `*`, `+` et `-` et rester une seule liste.

Markdown dans le HTML
: Le Markdown à l'intérieur des balises de bloc HTML est traité. Certaines balises peuvent encore casser.

Transformations de métadonnées
: Les marqueurs `[%key]` sont remplacés à partir des métadonnées du document.

## Tableaux et images [tables-and-images]

Tableaux en grille
: Tableaux dessinés avec `+` et `|`. Désactivés par défaut.

Tableaux souples
: Les tableaux à barres peuvent omettre les barres de début et de fin. Activés par défaut.

Alignement par cellule
: Les marqueurs d'alignement d'une cellule remplacent l'alignement de la colonne. Activé par défaut.

Légendes d'image
: Le titre de l'image, ou le texte de remplacement s'il n'y a pas de titre, devient une légende visible. Activé par défaut.

Légendes de titre seulement
: Seul le titre de l'image sert de légende. Le texte de remplacement est ignoré. Désactivé par défaut. Sans effet si **Légendes d'image** est désactivé.

## Liens et index [links-and-indexes]

Liens wiki
: Apex convertit `[[liens wiki]]`. Désactivé par défaut. Lorsqu'il est activé, Marked saute sa propre passe d'aperçu « Convertir les liens wiki » pour ce document, et Apex peut résoudre le fichier cible autrement que Marked. L'extension par défaut vient des réglages de liens wiki de Marked.

Assainir les URL de liens wiki
: Les URL générées sont mises en minuscules, les apostrophes sont retirées, et les autres caractères qui ne sont ni des lettres ni des chiffres sont remplacés. Désactivé par défaut. Disponible seulement si **Liens wiki** est activé.

Traitement de l'index
: Reconnaît les marqueurs d'index (styles MultiMarkdown, mmark, Leanpub et textindex). Activé par défaut.

Supprimer la sortie de l'index
: Lit toujours les marqueurs, mais n'imprime pas l'index généré. Désactivé par défaut.

## Encadrés (supplémentaires) [callouts-extra]

Les deux sont désactivés par défaut. Les encadrés Obsidian et Bear (`> [!NOTE]`) sont traités par Marked avant Apex et ne se règlent pas ici.

Encadrés Python-Markdown (!!!)
: Encadrés de style `!!! note`.

Encadrés Quarto
: Blocs Quarto `::: {.callout-note}`.

## Accessibilité [accessibility]

Les deux sont désactivés par défaut.

Libellés ARIA
: Ajoute des attributs ARIA qui décrivent la structure du HTML produit par Apex.

Ancres de titres
: Émet une ancre `<a>` sur chaque titre au lieu d'un simple `id` sur le titre.
