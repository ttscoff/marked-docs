# Markdownifier

Le Markdownifier est un outil qui extrait automatiquement le contenu des pages Web et le convertit au format Markdown propre. Il traite intelligemment le contenu Web pour vous fournir uniquement le texte et la structure significatifs, en filtrant les publicités, les éléments de navigation et tout autre encombrement.

![URL Markdownify][importurl]

[importurl]: import-url@2x.jpg width=800 class=center

## Comment ça marche

Le Markdownifier utilise des algorithmes avancés d'extraction de contenu pour :

1. **Récupérer et analyser** le contenu d'une page Web
2. **Identifier le texte et la structure de l'article principal**
3. **Nettoyer et formater** le contenu dans le Markdown approprié
4. **Filtrer** les publicités, la navigation et autres éléments hors contenu
5. **Conserver** le formatage important comme les en-têtes, les listes et les liens

## Ouverture du Markdownifier

Pour accéder au Markdownifier, ouvrez {% appmenu File, New, Markdownify URL (@~k) %}. Entrez l'URL que vous souhaitez Markdownify et appuyez sur Retour ({% kbd return %}).

## Utilisation du Markdownifier

### Utilisation de base

1. **Ouvrez Markdownifier** en utilisant l'une des méthodes ci-dessus
2. **Entrez une URL** dans le champ de texte
3. **Cliquez sur "Automatique"** ou appuyez sur `Retour` pour extraire le contenu
4. Le contenu extrait s'ouvrira **automatiquement** dans un nouveau document Marked

### Sélection manuelle du contenu

Si l'extraction automatique ne capture pas le contenu souhaité :

1. Cliquez sur le bouton **"Manuel"** pour charger la page dans une vue Web.
2. **Naviguez et faites défiler** pour trouver le contenu souhaité
3. **Cliquez sur le bouton « Extraire le contenu »** qui apparaît sur la page Web.
4. Le contenu sélectionné sera converti en Markdown et ouvert dans Marked

### Intégration du presse-papiers

Le Markdownifier détecte automatiquement les URL dans votre presse-papiers lorsqu'elles sont ouvertes :

- Si une URL est trouvée, elle sera **pré-remplie** dans le champ URL
- Vous devez toujours cliquer sur **"Automatique"** ou appuyer sur `Retour` pour le traiter
- Cela empêche le traitement accidentel des URL du presse-papiers

## Traitement du contenu

### Validation automatique du contenu

Le Markdownifier valide intelligemment le contenu extrait pour garantir qu'il contient un texte significatif :

- **Supprime les métadonnées** (frontmatter YAML, en-têtes MultiMarkdown)
- **Supprime les définitions de liens** et les liens de style référence
- **Filtre** les URL autonomes et les éléments de navigation
- **Compresse les espaces** pour une évaluation précise de la longueur
- **Nécessite un minimum de 200 caractères** de contenu réel

Si le contenu extrait est trop court ou semble être principalement constitué de navigation/annonces, le Markdownifier reviendra automatiquement en mode de sélection manuelle.

### Formatage du contenu

Le contenu extrait est formaté en Markdown propre avec :

- **Lien source** en haut : `[source](original-url)`
- **Insertion du titre H1** si nécessaire
- **Listes conservées** (ordonnées et non ordonnées)
- **Liens maintenus** et mise en forme de l'accentuation
- **Paragraphes propres** avec un espacement approprié

## Fonctionnalités de sécurité

### Prévention des accidents

Le Markdownifier comprend plusieurs mesures de sécurité pour éviter les crashs :

- **Bloque les URL problématiques** (réseaux publicitaires, services de suivi, contenu lié à la cryptographie)
- **Filtre les images corrompues** pouvant entraîner des problèmes de rendu
- **Désactive les fonctionnalités Web avancées** qui pourraient provoquer une instabilité
- **Récupération automatique en cas de crash** avec repli en mode sans échec

### Protection de la vie privée

- **Le mode de navigation privée** empêche le suivi et les cookies
- **Aucun plugin ni exécution Java** pour des raisons de sécurité
- **JavaScript limité** avec blocage de l'API crypto
- **Le filtrage des ressources** bloque le suivi et le contenu publicitaire

## Dépannage

### Contenu non extrait

Si l'extraction automatique échoue :

1. **Essayez la sélection manuelle** à l'aide du bouton "Manuel"
2. **Vérifiez si le site nécessite JavaScript** - certains sites nécessitent un chargement manuel
3. **Vérifiez que l'URL** est accessible et contient le contenu de l'article
4. **Recherchez les paywalls ou les exigences de connexion** qui pourraient bloquer l'accès

### Problèmes de WebView

Si la vue Web devient instable :

1. Le Markdownifier **entrera automatiquement en mode sans échec**
2. **JavaScript sera désactivé** pour éviter les plantages
3. **Utilisez le bouton "Convertir"** au lieu de la sélection manuelle
4. **Fermez et rouvrez** le Markdownifier pour réinitialiser

### Contenu manquant

Si un contenu important manque dans l'extraction :

1. L'**algorithme automatique** l'a peut-être filtré
2. **Utilisez la sélection manuelle** pour choisir le contenu spécifique que vous souhaitez
3. **Vérifiez le HTML source** pour voir si le contenu est chargé dynamiquement
4. **Essayez une URL différente** si le site a une structure complexe

## Conseils pour de meilleurs résultats

### Sélection d'URL

- **Utilisez les URL des articles** plutôt que la page d'accueil ou les pages de catégorie
- **Évitez les URL avec des paramètres de suivi** lorsque cela est possible

### Qualité du contenu

- **Les articles plus longs** extraient généralement mieux que les articles courts
- **Un contenu bien structuré** avec des titres appropriés fonctionne mieux
- **Évitez les sites avec du JavaScript lourd** pour une extraction automatique

### Sélection manuelle

- **Attendez que la page soit complètement chargée** avant de l'extraire
- **Faites défiler le contenu** pour vous assurer que tout est chargé
- **Survolez les zones** pour sélectionner la plus petite boîte bleue contenant tout le contenu que vous souhaitez extraire
- **Cliquez** lorsque vous avez trouvé le contenu souhaité

## Fonctionnalités avancées

### Traitement par lots

Pendant que Markdownifier traite une URL à la fois, vous pouvez :

- **Mettez plusieurs URL en file d'attente** en ouvrant le Markdownifier plusieurs fois
- **Utiliser l'intégration des services** pour traiter les URL d'autres applications
- **Copiez le contenu extrait** et collez-le dans les documents Marked existants

### Intégration avec Marked

Le contenu extrait s'ouvre dans Marked avec :

- **Nom automatique des fichiers** basé sur le titre de l'article
- **Préservation de l'URL source** dans les métadonnées du document
- **Capacités complètes de Marked** pour la lecture et l'exportation

## Détails techniques

### Types de contenu pris en charge

- **Articles HTML** avec balisage standard
- **Articles de blog** et articles d'actualité
- **Documentation** et pages d'aide
- **Messages du forum** et contenu des discussions

### Limites

- Les **sites payants** peuvent nécessiter une connexion et une extraction manuelle.
- Les **sites utilisant beaucoup de JavaScript** peuvent nécessiter une sélection manuelle.
- Le **contenu dynamique** chargé après le chargement de la page peut être manqué, mais l'extraction manuelle peut le capturer
- **Les mises en page complexes** peuvent inclure des éléments de navigation indésirables

Le Markdownifier est conçu pour rendre l'extraction de contenu Web aussi simple et fiable que possible, tout en offrant des options de secours pour les sites Web complexes ou problématiques.
