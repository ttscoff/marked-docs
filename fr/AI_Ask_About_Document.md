# <%= @title %>

**Poser des questions sur le document** utilise Apple Intelligence et le modèle linguistique intégré aux versions récentes de macOS pour résumer votre aperçu Markdown et répondre aux questions sur son contenu. Tout le traitement s'effectue sur votre Mac ; le texte du document n'est pas envoyé aux serveurs de Marked ou aux services d'IA tiers pour cette fonctionnalité.

## Ce que fournit Apple Intelligence [what-apple-intelligence-provides]

Apple Intelligence est le système d'Apple pour les fonctionnalités génératives sur l'appareil. Marked utilise le framework **Foundation Models** d'Apple pour accéder au même modèle sur l'appareil qui alimente les outils d'écriture système, exposé directement dans Marked pour les tâches axées sur les documents.

Marked envoie le texte brut de votre document (la syntaxe Markdown est retirée pour plus de clarté) à ce modèle local. Le modèle génère des résumés, des plans et des réponses dans un panneau flottant à côté de votre fenêtre d'aperçu. Étant donné que le modèle s'exécute localement, il fonctionne hors ligne une fois qu'Apple Intelligence est configuré et que le téléchargement du modèle système est terminé.

Apple Intelligence excelle dans les tâches langagières telles que le résumé, la création de plans, l'extraction des points clés et la réponse à des questions sur un texte donné. Ce n'est pas un assistant de codage généraliste ni une calculatrice, et les documents très longs sont traités par sections afin que les résultats restent dans les limites de contexte du modèle.

## Compatibilité système [system-compatibility]

Poser des questions sur le document apparaît uniquement lorsque votre Mac peut exécuter la fonctionnalité.

**Requis :**

- **macOS 26 (Tahoe)** ou version ultérieure
- Un **Mac avec prise en charge Apple Intelligence** (Mac Apple Silicon répondant aux exigences des appareils Apple)
- **Apple Intelligence activée** dans les paramètres système

**Non pris en charge :**

- Les Mac Intel et les autres Mac marqués comme non éligibles à Apple Intelligence
- Les versions de macOS antérieures à Tahoe 26
- Les aperçus **HTML** bruts (la fonctionnalité s'adresse aux flux de travail Markdown et texte)

Si votre Mac est éligible mais que l'élément de menu est absent, vérifiez qu'Apple Intelligence est activée et que vous utilisez une version récente de Marked qui inclut cette fonctionnalité. Le menu est entièrement masqué sur les systèmes non pris en charge plutôt qu'affiché dans un état désactivé.

## Activer Apple Intelligence [enabling-apple-intelligence]

1. Ouvrez **Réglages Système**.
2. Accédez à **Apple Intelligence & Siri** (ou **Apple Intelligence**, selon votre version de macOS).
3. Activez **Apple Intelligence** et effectuez toutes les étapes de configuration demandées par Apple.
4. Attendez que le modèle sur l'appareil termine le téléchargement si vous y êtes invité. Jusqu'à ce que le modèle soit prêt, Marked peut afficher l'élément de menu mais indiquer qu'Apple Intelligence est toujours en train de se préparer.

Marked n'inclut pas de préférence distincte pour cette fonctionnalité. La disponibilité suit l'état du modèle système signalé par macOS.

## Ouvrir le panneau Poser des questions sur le document [opening-ask-about-document]

Ouvrez le panneau à l'aide de l'une de ces méthodes :

- **Aperçu > Poser des questions sur le document…**
- Raccourci clavier {% kbd shift ctrl cmd I %} (tandis qu'un document d'aperçu Markdown est la fenêtre active)

Le panneau s'ancre sur le côté gauche de la fenêtre du document. Vous avez besoin d'un document ouvert avec du texte lisible ; un document vide ou un aperçu HTML uniquement ne proposera pas la commande.

## Le panneau Poser des questions sur le document [the-ask-about-document-panel]

Le panneau est organisé comme une simple vue de discussion :

- **Actions prédéfinies** en haut pour les tâches courantes
- Une **zone de réponse** au milieu où apparaissent les résumés et les réponses (en streaming au fur et à mesure de leur génération)
- Un **champ de question** en bas où vous saisissez des questions personnalisées, avec les boutons **Demander** et **Annuler**.

Une fois la réponse terminée, le focus revient au champ de question afin que vous puissiez poser une question de suivi sans avoir à cliquer.

### Actions prédéfinies [preset-actions]

| Action | Ce qu'elle fait |
| :-- | :-- |
| **Résumer le document** | Produit un bref résumé cohérent du document complet. Les documents longs sont résumés par sections, puis combinés. |
| **Résumer la sélection** | Résume uniquement le texte actuellement sélectionné dans l'aperçu. Sélectionnez d'abord du texte ; sinon, Marked vous invite à faire une sélection ou à utiliser Résumer le document. |
| **Plan** | Construit un plan hiérarchique de la structure du document à partir des titres et des puces. |
| **Points clés** | Répertorie les points les plus importants du document sous forme de liste à puces. |

Les actions prédéfinies ne nécessitent pas de texte dans le champ de question. Cliquez sur un bouton et attendez la réponse dans le panneau ci-dessus.

### Poser vos propres questions [asking-your-own-questions]

1. Tapez une question dans le champ situé en bas du panneau, par exemple « Quel problème ce document résout-il ? » ou « Quel est le public visé ? »
2. Appuyez sur **Retour** ou cliquez sur **Demander**.
3. Lisez la réponse au fur et à mesure qu'elle s'affiche dans la zone de réponse.

Pour des questions sur un passage spécifique, **sélectionnez ce texte dans l'aperçu** avant de poser la question. Marked envoie la sélection comme contexte au lieu du document entier lorsqu'une sélection est active.

Cliquez sur **Annuler** pour arrêter une demande en cours.

## Exemples [examples]

### Aperçu rapide d'un long article [quick-overview-of-a-long-article]

Ouvrez un long article de blog ou un rapport dans Marked, choisissez **Aperçu > Poser des questions sur le document…**, puis cliquez sur **Résumer le document**. Utilisez le résumé pour décider si vous devez lire l'article en entier ou simplement vous rafraîchir la mémoire après une pause dans la rédaction.

### Notes sur un paragraphe sélectionné [notes-on-a-selected-paragraph]

Sélectionnez un paragraphe dense dans l'aperçu, ouvrez Poser des questions sur le document, puis cliquez sur **Résumer la sélection**. Utile lorsque vous avez seulement besoin d'une version plus courte d'une section.

### Revue structurelle [structural-review]

Cliquez sur **Plan** sur un brouillon comportant de nombreux titres pour voir si l'argumentation suit une logique cohérente, ou utilisez **Points clés** avant d'envoyer un document à quelqu'un d'autre pour vérifier que les idées principales sont claires.

### Questions ciblées [targeted-questions]

Sans sélection active, tapez des questions telles que :

- « Quelles sont les trois principales recommandations ? »
- « Ce document mentionne-t-il des questions de licence ? »
- « Liste toutes les dates ou échéances mentionnées. »

Avec une sélection active, posez des questions plus précises comme « Que ce paragraphe suppose-t-il sur le lecteur ? » ou « Reformule cette idée en une phrase » (le modèle répond à propos de la sélection ; il ne modifie pas votre fichier source).

## Conseils et limites [tips-and-limitations]

- **Confidentialité :** le traitement utilise le modèle sur l'appareil d'Apple. Marked lit quand même le texte de votre document localement pour le fournir à ce modèle ; traitez les contenus sensibles en conséquence.
- **Précision :** vérifiez les faits importants par rapport à votre source. Les résumés générés par IA peuvent omettre des détails ou mal interpréter des passages ambigus.
- **Longueur :** les documents extrêmement longs sont traités par blocs. Les résumés et réponses reflètent indirectement le texte complet ; pour plus de précision sur une section, sélectionnez-la d'abord.
- **Langue :** les résultats suivent les capacités linguistiques du modèle Apple Intelligence installé sur votre Mac.
- **Refus :** le système peut refuser certaines demandes en fonction des politiques de sécurité d'Apple.

Si Poser des questions sur le document n'est pas disponible, vérifiez l'état de Réglages Système pour Apple Intelligence et assurez-vous de prévisualiser un document Markdown sur un Mac pris en charge exécutant macOS 26 ou version ultérieure.
