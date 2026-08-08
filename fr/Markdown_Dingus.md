# <%= @title %>

Le Markdown Dingus est un outil de test spécialisé qui vous aide à comprendre comment les différents processeurs Markdown gèrent votre contenu. Il fournit une interface à trois volets où vous pouvez modifier le Markdown, afficher la source HTML générée et voir l'aperçu rendu simultanément.

Le Dingus partage une certaine maniabilité de bas niveau avec celui de l'aperçu de Marked, comme un traitement spécial des blocs de code clôturés. Il n'exécute __pas__ les [Règles personnalisées](Custom_Processor.html) (Conductor). Il utilise la plupart des paramètres par défaut, ignorant les paramètres comme « nouvelles lignes GitHub » et « cases à cocher GitHub », donc le résultat peut différer de ce que vous voyez dans un aperçu Markdown normal.

## Les règles personnalisées ne s'appliquent pas [custom-rules-do-not-apply]

Le Dingus est un __bac à sable de processeur__ : votre Markdown va directement au processeur intégré que vous choisissez (MultiMarkdown, CommonMark (GFM), Discount ou Kramdown). Les [Règles personnalisées](Custom_Processor.html) ne s'y exécutent jamais : pas d'actions de prétraitement, de règles de recherche/remplacement, commandes shell, insertion de texte/fichier ou d'autres étapes de Conductor.

Dans un aperçu normal, les règles personnalisées peuvent modifier le Markdown avant le rendu, définir les styles, injecter du CSS ou du JavaScript, et plus encore. Rien de tout cela ne se produit lorsque vous modifiez dans le Dingus. Modifier les règles personnalisées pendant que le Dingus est ouvert ne met pas à jour son aperçu.

Le Dingus __peut__ utiliser les mêmes [styles CSS d'aperçu](Custom_Styles.html) que la fenêtre principale (via le menu de style dans le volet de sortie). Ce n'est qu'une apparence ; ce n'est pas la même chose que d'exécuter des règles personnalisées.

__Ouvrir dans Dingus__ à partir d'un aperçu charge le tampon Markdown actuel du document. Si des règles personnalisées avaient déjà été exécutées lorsque ce fichier a été ouvert dans Marked, vous pouvez voir leurs effets dans le texte (par exemple, du texte inséré par une règle), mais le Dingus ne réappliquera pas les règles au fur et à mesure que vous tapez. Pour tester des règles personnalisées, utilisez un aperçu Marked standard, ou enregistrez depuis le Dingus et ouvrez le fichier avec __Open in Marked__.

## Qu'est-ce qu'un « Dingus » ? [what-is-a-dingus]

Un « dingus » est un terme emprunté au développement web qui fait référence à un simple outil de test ou à un environnement sandbox. Le Markdown Dingus vous permet d'expérimenter la syntaxe Markdown et de voir immédiatement comment les différents processeurs l'interprètent.

## Accéder au Dingus [accessing-the-dingus]

Le Markdown Dingus est accessible depuis [{% appmenu Help, Open Markdown Dingus %}][2]. C'est particulièrement utile lorsque vous êtes :

* En train d'apprendre une nouvelle syntaxe Markdown
* En train de dépanner des problèmes de rendu
* En train de choisir entre différents processeurs
* En train de rédiger une documentation qui doit fonctionner sur plusieurs systèmes

## Disposition à trois volets [three-pane-layout]

![][1]

La fenêtre Dingus est divisée en trois volets synchronisés :

### 1. Entrée Markdown (volet de gauche) [1-markdown-input-left-pane]

* __Coloration syntaxique__ : votre Markdown est mis en évidence avec des couleurs pour rendre la structure claire
* __Édition en direct__ : saisissez et voyez les modifications reflétées instantanément dans les autres volets
* __Grande police__ : police Menlo 21 pt pour une édition confortable

__Options déroulantes__ (en haut à droite du volet de gauche) : le menu **Options** vous permet de basculer :

* __Afficher les numéros de ligne__ : Affiche une gouttière à gauche avec un numéro de ligne par paragraphe (les lignes retournées comptent pour une ligne).
* __Afficher les invisibles__ : affiche les espaces sous forme de points médians (·), les tabulations sous forme d'une flèche vers la droite (→) et les nouvelles lignes comme symbole de retour chariot (↵) en gris clair pour que vous puissiez repérer les espaces blancs parasites.
* __Mettre en évidence les gremlins__ : met un fond rouge clair sur les caractères non-ASCII (par exemple, guillemets bouclés, emoji) et un fond rouge sombre sur les caractères invisibles problématiques (par exemple, espaces de largeur nulle). Les caractères de tabulation et de nouvelle ligne normaux ne sont pas mis en évidence.

Vos choix sont enregistrés et restaurés lors de votre prochaine ouverture du Dingus.

__Barre de recherche__ : appuyez sur **⌘F** pour afficher la barre de recherche sous l'étiquette « Entrée Markdown ». Vous pouvez rechercher et remplacer dans l'éditeur, utiliser **⌘G** pour Rechercher suivant et **⇧⌘G** pour Rechercher précédent, et remplacer une ou toutes les correspondances. Appuyez sur la touche de fermeture ou **⌘F** à nouveau pour masquer la barre de recherche.

### 2. Source HTML (volet du milieu) [2-html-source-middle-pane]

* __HTML généré__ : voyez exactement quel HTML le processeur sélectionné crée
* __Syntaxe mise en évidence__ : le HTML est codé par couleur pour faciliter la lecture

### 3. Aperçu rendu (volet droit) [3-rendered-preview-right-pane]

* __Aperçu en direct__ : découvrez à quoi ressemblera votre Markdown une fois rendu
* __Prise en charge des emoji__ : les emojis de style GitHub comme `:zzz:` sont convertis en images
* __Défilement automatique__ : défile automatiquement pour afficher votre position d'édition actuelle

## Édition dans le Dingus [editing-in-the-dingus]

Le volet de saisie Markdown comprend des fonctionnalités d'édition intelligentes pour rendre l'écriture de Markdown plus rapide et plus naturelle.

### Nouvelle ligne intelligente (touche Retour) [smart-newline-return-key]

Un appui sur Retour s'adapte à la ligne actuelle :

* __Listes__ : Sur une ligne de liste (`-`, `*`, `+` ou `1.`), insère un nouvel élément de liste avec le marqueur correct. Les listes numérotées continuent avec le numéro suivant.
* __Citations__ : Sur une ligne commençant par `>`, insère une nouvelle ligne de citation de bloc.
* __Clôtures de code__ : sur une ligne avec trois backticks ou plus (par exemple ` ``` `), insère une ligne vide entre les clôtures d'ouverture et de fermeture.
* __Autres lignes__ : insère une nouvelle ligne normale.

### Appariement des caractères [character-pairing]

Lorsque vous tapez un caractère d'ouverture, l'éditeur insère le caractère de fermeture et place le curseur entre eux. Paires prises en charge : `"` `'` `(` `[` `` ` `` `<`.

* __Avec sélection__ : Encapsule le texte sélectionné dans la paire.
* __Sans sélection__ : Insère la paire avec le curseur entre eux.
* __Remplacement__ : Si le caractère suivant est déjà le délimiteur de fermeture, le taper à nouveau déplace le curseur au-delà au lieu d'insérer un double.
- __Espace dans une paire vide__ : Si le curseur se trouve entre une paire vide (par exemple `(|)`), taper un espace remplace le caractère de fermeture par un espace.

### Touches de raccourci [shortcut-keys]

| Raccourci | Actions |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⌘F** | Afficher ou masquer la barre de recherche dans le volet de saisie Markdown |
| **⌘G** | Rechercher suivant (lorsque la barre de recherche est visible) |
| **⇧⌘G** | Rechercher précédent (lorsque la barre de recherche est visible) |
| **⌘B** | Gras : enveloppez la sélection dans `**` ou insérez `**\|**` avec le curseur entre |
| **⌘I** | Italique : enveloppez la sélection dans `_` ou insérez `_\|_` avec le curseur entre |
| **⇧⌘L** | Marqueur de liste de cycles (non ordonné ↔ ordonné) |
| **Onglet** | Mettre en retrait une ligne ou un élément de liste |
| **Maj+Tab** | Ligne ou élément de liste sortant |
| **⌃⌘→** | Indenter une ligne ou un élément de liste (identique à Tab) |
| **⌃⌘←** | Ligne ou élément de liste retiré (identique à Shift+Tab) |
| **⌃⌘↑** | Déplacer le paragraphe vers le haut (couper le paragraphe, y compris la nouvelle ligne, coller une ligne vers le haut) |
| **⌃⌘↓** | Déplacer le paragraphe vers le bas (couper le paragraphe, y compris la nouvelle ligne, coller une ligne vers le bas) |
| **⌘K** | Insérez ou enveloppez un lien Markdown : enveloppez la sélection comme `[text]()` et placez le curseur dans l'URL, ou insérez `[]()` avec le curseur entre les crochets lorsqu'il n'y a pas de sélection |
| **⌘U** | Basculer le volet de sortie (Source/Aperçu) |
| **⌥⌘↑** | Développer la sélection : mot → délimiteurs internes/externes → phrase → paragraphe → bloc contigu (tel qu'un tableau ou un bloc de code) → liste/citation de bloc/bloc de code → document |
| **⌥⌘↓** | Contracte la sélection en redescendant à travers les mêmes niveaux jusqu'à la position d'origine du curseur |

Tab/Shift+Tab (et ⌃⌘←/⌃⌘→) respectent la structure de la liste et des citations : ils indentent/désindentent les éléments de liste et ajoutent ou suppriment `>` des lignes de citation de bloc. Déplacer le paragraphe vers le haut/bas sélectionne le paragraphe entier sous le curseur (y compris sa nouvelle ligne finale), le coupe et le colle au-dessus ou en dessous du paragraphe adjacent afin que les paragraphes ne fusionnent pas.

### Coller une URL intelligente [magic-links-and-footnotes-f6-f7]

Lorsque vous collez et que le presse-papier contient une URL du format `protocol://...` sans espaces :

* __Avec une sélection__ : la sélection se transforme en lien Markdown : `[selected text](url)`.
* __Sans sélection__ : l'URL est insérée sous forme d'auto-lien : `<url>`.

Cela facilite la transformation des URL copiées en liens sans saisie manuelle.

### Sélection intelligente (⌥⌘↑ / ⌥⌘↓) [smart-url-paste]

L'éditeur Dingus prend en charge __l'expansion de la sélection sémantique__ :

* __⌥⌘↑__ commence au curseur et élargit la sélection à travers :
	- le mot actuel
	- le contenu délimité intérieur et extérieur (guillemets, parenthèses, crochets et blocs de code clôturés)
	- la phrase actuelle
	- le paragraphe actuel
	- le bloc de lignes contigu et non vide (par exemple, un tableau entier ou un bloc de code multiligne sans lignes vides)
	- l'élément de liste englobant, la citation de bloc ou le bloc de code
	- l'intégralité du document
* __⌥⌘↓__ redescend à travers les mêmes niveaux jusqu'à ce qu'il revienne à la position initiale du curseur.

Chaque pression se déplace toujours vers une sélection strictement plus grande ou plus petite, de sorte que vous n'obtiendrez jamais d'appuis sur des touches « sans effet » pendant que vous êtes en expansion ou en contraction.

## Utiliser le Dingus comme éditeur [using-the-dingus-as-an-editor]

Le Dingus n'est pas destiné à remplacer un éditeur de texte complet, mais il peut être très pratique pour des modifications rapides avec un __aperçu en direct__, surtout lorsque vous voulez voir exactement comment les changements seront rendus. Tout le comportement d'édition de texte décrit dans [Édition dans le Dingus][3] s'applique ici.

### Ouvrir un fichier/créer un nouveau fichier [opening-a-filecreating-a-new-file]

* __Créer un nouveau fichier dans le Dingus__
	- Choisissez __{% appmenu File, New, New Markdown File %}__ (⌘N).
	- Lorsque vous y êtes invité, choisissez __Dingus__ pour démarrer un nouveau document Dingus non enregistré.
	- Les nouveaux documents Dingus s'ouvrent avec un exemple de contenu sélectionné ; commencez simplement à taper pour le remplacer.
* __Ouvrir un fichier existant dans le Dingus__
	- Utilisez __{% appmenu File, Open in Dingus... %}__ (⌥⌘O), ou, avec la fenêtre Dingus active, cliquez sur __Open…__ dans la barre d'état. La commande ouvre la fenêtre Dingus si besoin, puis affiche le panneau Ouvrir.
	- Choisissez n'importe quel fichier texte brut/Markdown pris en charge ; son contenu remplacera le tampon Dingus actuel.
* __Ouvrez un document d'aperçu Marked dans le Dingus__
	- Depuis une fenêtre d'aperçu normale, utilisez __{% appmenu Preview, Open in Dingus %}__ (⌥⌘E).
	- Le Markdown du document actuel est chargé dans le Dingus pour que vous puissiez expérimenter sans toucher au fichier original jusqu'à ce que vous choisissiez de sauvegarder. Les règles personnalisées ne sont pas appliquées dans le Dingus ; voir [Les règles personnalisées ne s'appliquent pas](#custom-rules-do-not-apply).

### Enregistrer un fichier [saving-a-file]

* __Enregistrer les modifications dans le fichier actuel__
	- Dans la fenêtre Dingus, cliquez sur __Save__ dans la barre d'état, ou utilisez __{% appmenu File, Save Dingus %}__ (⌘S).
	- Si le document Dingus n'a pas encore été enregistré, vous serez invité à indiquer un emplacement et un nom de fichier ; après ça, ⌘S met à jour le même fichier.
* __Enregistrer sous / dupliquer dans un nouveau fichier__
	- Utilisez __{% appmenu File, Save Dingus As... %}__ (⌥⌘S).
	- Cela ouvre toujours une boîte de dialogue __Enregistrer sous__ et écrit le contenu actuel du Dingus dans un nouveau fichier sans écraser l'original.

### Aperçu dans Marked [previewing-in-marked]

* __Ouvrez le document Dingus en tant qu'aperçu Marked complet__
	- Cliquez sur __Ouvrir dans Marked__ dans la barre d'état de Dingus, ou utilisez __{% appmenu File, Open Dingus in Marked %}__ (⌘P).
	- Si le document Dingus n'est pas enregistré ou comporte des modifications non enregistrées, vous serez d'abord invité à enregistrer ; puis Marked ouvre un aperçu standard pour ce fichier.

En utilisant ces commandes, vous pouvez traiter le Dingus comme un éditeur léger pour des solutions rapides et des expériences, puis passer à un aperçu Marked complet ou à votre éditeur habituel lorsque vous êtes prêt pour une édition plus approfondie.

## Sélection du processeur [processor-selection]

Utilisez le menu déroulant en haut pour basculer entre les différents processeurs Markdown :

* __MultiMarkdown__ : processeur complet avec tables, notes de bas de page et support mathématique
* __CommonMark (GFM)__ : processeur standard et rapide suivant la spécification CommonMark
* __Discount__ : GitHub Flavored Markdown avec listes de tâches et tableaux
* __Kramdown__ : processeur avancé avec fonctionnalités supplémentaires comme les IAL et la typographie

## Pourquoi utiliser le Dingus ? [why-use-the-dingus]

### Comprendre les différences entre les processeurs [understanding-processor-differences]

Différents processeurs Markdown gèrent la syntaxe différemment. Le Dingus vous aide à :

* __Comparer les résultats__ : découvrez exactement le rendu de chaque processeur pour le même Markdown
* __Déboguer les problèmes__ : identifiez pourquoi certaines syntaxes ne fonctionnent pas comme prévu
* __Apprendre la syntaxe__ : comprendre les différences subtiles entre les implémentations de processeur

### Tester avant d'écrire [testing-before-writing]

Avant de vous engager dans un style Markdown particulier dans votre document :

* __Valider la syntaxe__ : assurez-vous que votre Markdown sera rendu correctement
* __Choisissez les processeurs__ : décidez quel processeur fonctionne le mieux pour votre contenu
* __Expérimentez en toute sécurité__ : essayez une nouvelle syntaxe sans affecter vos documents réels

## Cas d'utilisation courants [common-use-cases]

### Différences de syntaxe des tableaux [table-syntax-differences]

Certains processeurs gèrent la syntaxe des tableaux différemment. Le Dingus vous permet de voir quel processeur prend le mieux en charge vos besoins de formatage de tableau.

### Prise en charge des notes de bas de page [footnote-support]

Tous les processeurs ne prennent pas en charge les notes de bas de page. Utilisez le Dingus pour vérifier que la syntaxe des notes de bas de page fonctionne avec le processeur que vous avez choisi.

### Mathématiques et caractères spéciaux [math-and-special-characters]

Testez comment différents processeurs gèrent les expressions mathématiques et les caractères typographiques spéciaux.

## Conseils pour une utilisation efficace [tips-for-effective-use]

1. __Commencer simplement__ : commencez par le Markdown de base et ajoutez progressivement de la complexité
2. __Tester les cas limites__ : essayez des combinaisons de syntaxe inhabituelles pour comprendre les limites du processeur
3. __Comparez côte à côte__ : basculez entre les processeurs pour voir clairement les différences
4. __Utiliser du contenu réel__ : copiez le contenu réel de vos documents pour tester des scénarios du monde réel

Le Dingus est un outil puissant pour tous ceux qui souhaitent comprendre les nuances des différentes implémentations de Markdown et s'assurer que leur contenu s'affiche correctement sur diverses plates-formes et processeurs.

[1]: images/dingus-interface-800.jpg @2x width=800px height=573px class=center
[2]: x-marked-3://dingus
[3]: #editing-in-the-dingus
