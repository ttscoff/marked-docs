# <%= @title %>

Extrayez et dérobez les styles de n'importe quel site web.

## Qu'est-ce que le Voleur de styles ? [what-is-the-style-stealer]

Le Voleur de styles est un outil qui permet d'extraire les styles CSS de n'importe quel site web et de les appliquer à vos documents Markdown en tant que [styles personnalisés](Custom_Styles.html). Il est parfait pour :

- Les **blogueurs** qui souhaitent retrouver le style de leurs sites préférés
- Les **rédacteurs** qui doivent créer des documents correspondant à une marque ou une publication précise
- Les **développeurs** qui veulent prototyper rapidement avec des systèmes de design existants
- **Toute personne** souhaitant capturer l'apparence et l'ambiance d'un site web au design soigné

> Le Voleur de styles fonctionne mieux avec un site relativement bien structuré, avec des divisions de balisage claires. Il ne fonctionnera pas sur tous les sites, mais devrait donner de bons résultats sur la plupart d'entre eux.

> Pour de meilleurs résultats, ouvrez une page contenant le plus de contenu textuel possible. Par exemple, pour extraire les styles d'un blog, ouvrez directement un article, et non la page d'index principale.

## Comment utiliser le Voleur de styles [how-to-use-the-style-stealer]

### Étape 1 : Ouvrir le Voleur de styles [step-1-open-the-style-stealer]

Accédez au Voleur de styles via **Aide** → **Voleur de styles**.

### Étape 2 : Saisir une URL [step-2-enter-a-url]

Dans le champ URL, saisissez l'adresse du site web dont vous souhaitez extraire les styles. Le Voleur de styles fonctionne avec n'importe quel site accessible publiquement. Si le site est protégé par un paywall, vous devrez peut-être vous connecter pour pouvoir en extraire le contenu.

![Aperçu du Voleur de styles][preview]

  [preview]: images/style-stealer-preview.jpg @2x width=800

### Étape 3 : Charger et naviguer [step-3-load-and-navigate]

Cliquez sur **Extraire** ou appuyez sur {% kbd return  %} pour charger le site web. Une fois le site chargé, vous pouvez :

- **Naviguer** sur le site avec Commande+Clic sur les liens
- **Survoler** les zones de contenu pour les voir mises en évidence
- **Cliquer** sur la zone de contenu principale dont vous souhaitez extraire les styles

La zone de contenu principale que vous sélectionnez ne doit contenir que des titres, paragraphes, listes, etc. Ne sélectionnez pas une zone de contenu qui inclut des menus, des barres latérales ou tout autre contenu superflu. Il arrive souvent qu'un titre se trouve dans un conteneur distinct du contenu des paragraphes. Dans ce cas, essayez d'abord de sélectionner le plus petit conteneur qui englobe les deux. Si le résultat est décevant, cliquez à nouveau sur **Extraire** et sélectionnez uniquement le conteneur qui contient les paragraphes.

### Étape 4 : Extraire les styles [step-4-extract-styles]

Lorsque vous cliquez sur la zone de contenu, les styles qui s'appliquent à cette zone sont extraits. L'aperçu se recharge avec une page générique présentant tous les éléments HTML courants et la façon dont les styles extraits s'y appliquent.

Vous pouvez ensuite enregistrer ce style personnalisé dans votre dossier CSS personnalisé, pour l'utiliser dans n'importe quel document. Cliquez sur le bouton **Enregistrer** ou appuyez sur {% kbd cmd S %} pour l'enregistrer. Le style sera nommé d'après le domaine de l'URL que vous avez saisie.

![][img3]

  [img3]: images/style-stealer-stolen-800.jpg @2x width=800px height=637px class=center

## Ce qui est extrait [what-gets-extracted]

Le Voleur de styles capture un ensemble complet de styles, notamment :

### Typographie [typography]

- Les **familles de polices** et tailles pour tous les niveaux de titre (H1 à H6)
- Le style des **paragraphes**, y compris l'interligne et les espacements
- Les **couleurs de texte** et couleurs d'arrière-plan
- Les **graisses** et styles de police (gras, italique, etc.)

### Mise en page et espacement [layout-and-spacing]

- Les **marges et le remplissage** de tous les éléments
- Les styles et couleurs de **bordure**
- Les **couleurs d'arrière-plan**, y compris l'arrière-plan du corps pour les thèmes sombres

### Éléments interactifs [interactive-elements]

- Le style des **liens**, y compris les états survol et visité
- Le style des **boutons** et des éléments de formulaire
- Le style des **listes** (puces, numéros, retrait)

### Fonctionnalités spéciales [special-features]

- Le style du **premier paragraphe**
- La mise en forme des **citations en bloc**
- Le style du **code** et du texte préformaté
- Le style des **tableaux**
- Les **polices personnalisées** et les polices web

## Fonctionnalités avancées [advanced-features]

### Blocage des médias [media-blocking]

Le Voleur de styles bloque automatiquement le contenu multimédia (vidéos, images, audio) pour éviter les plantages et se concentrer sur le style du texte. Cela garantit un processus d'extraction fluide, même sur des sites très riches en médias.

### Prise en charge des pseudo-sélecteurs [pseudo-selector-support]

L'outil capture les pseudo-sélecteurs CSS tels que :

- Les états `:hover` pour les liens et boutons
- Les états de lien `:visited`
- Le style de paragraphe `:first-child`
- `::first-letter` pour les lettrines

### Filtrage intelligent [smart-filtering]

Le Voleur de styles filtre intelligemment :

- Les styles par défaut du navigateur
- Les préfixes vendeurs inutiles
- Les règles contradictoires ou redondantes
- Les styles qui rendraient le texte illisible

### Mode débogage [debug-mode]

Activez le mode débogage dans le Voleur de styles pour voir un journal détaillé du processus d'extraction. Cela est utile pour le dépannage ou pour comprendre quels styles sont capturés.

## Astuces pour de meilleurs résultats [tips-for-best-results]

### Choisir la bonne zone de contenu [choose-the-right-content-area]

- Cliquez sur la **zone de contenu principale** de la page, pas sur les en-têtes, barres latérales ou pieds de page
- Recherchez la zone contenant le texte de l'article, du billet de blog, ou le contenu principal
- Évitez les zones comportant beaucoup de JavaScript ou de contenu dynamique

### Gérer les thèmes sombres [handle-dark-themes]

Le Voleur de styles capture automatiquement les couleurs d'arrière-plan du corps, ce qui le rend parfait pour extraire les styles de thèmes sombres. L'aperçu montrera l'apparence de votre contenu avec le style sombre extrait.

### Considérations sur les polices [font-considerations]

- Les **polices web** sont capturées et incluses dans les styles extraits
  - Les polices chargées depuis une URL distante (par exemple Google Fonts) conserveront cette URL. Les polices chargées depuis des URL de données seront dupliquées dans la feuille de style générée.
- Les **polices système** se replieront avec élégance selon les systèmes
- Le **chargement des polices** peut prendre un instant dans l'aperçu

### Tester vos styles [testing-your-styles]

Après avoir enregistré des styles extraits :

1. Appliquez-les à un document de test
2. Vérifiez leur rendu avec votre contenu réel
3. Effectuez des ajustements en procédant ainsi :
   1. Ouvrez {% prefspane Style %}
   2. Sélectionnez le nouveau style dans le tableau des styles personnalisés
   3. Cliquez sur Afficher pour montrer le fichier dans le Finder
   4. Ouvrez le fichier dans n'importe quel éditeur de texte brut (TextEdit fonctionnera en mode texte brut) et effectuez les ajustements nécessaires

## Dépannage [troubleshooting]

### Le site web ne se charge pas [website-wont-load]

- Vérifiez que l'URL est correcte et accessible publiquement
- Certains sites peuvent bloquer les accès automatisés
- Essayez une autre page du même site

### Les styles semblent différents [styles-look-different]

- Les styles extraits sont basés sur le contenu spécifique que vous avez sélectionné
- Certains sites utilisent du CSS complexe qui ne se traduit pas toujours parfaitement
- Utilisez le CSS supplémentaire ou modifiez la feuille de style pour effectuer des ajustements précis

### Styles manquants [missing-styles]

- Assurez-vous d'avoir sélectionné la zone de contenu principale, et non une barre latérale ou un en-tête
- Certains styles peuvent être appliqués via JavaScript et ne seront pas capturés
- Consultez la console de débogage pour des informations détaillées sur l'extraction

## Raccourcis clavier [keyboard-shortcuts]

- {% kbd return  %} - Charger l'URL pour l'extraction
- {% kbd cmd S %} - Enregistrer le style extrait dans un fichier CSS de style personnalisé
- {% kbd cmd  %}-Clic - Naviguer sur les liens pendant l'aperçu

## Intégration avec les styles personnalisés [integration-with-custom-styles]

Les styles extraits sont enregistrés dans votre dossier CSS personnalisé et peuvent être :

- **Appliqués** à n'importe quel document via le menu Style
- **Modifiés** avec n'importe quel éditeur de texte
- **Partagés** avec d'autres personnes en copiant le fichier CSS
- **Combinés** avec d'autres styles personnalisés

Le Voleur de styles facilite la constitution d'une bibliothèque de beaux styles inspirés des sites web les mieux conçus d'Internet.
