<!-- MT draft for fr — Marked Share publish help. Review before publishing. -->
# <%= @title %>

**Marked Share** est le service de publication en ligne de Marked à l'adresse [share.markedapp.com](https://share.markedapp.com). Connectez votre Mac une fois, puis publiez le document de couverture sous la forme **TextPack** avec des images et des surlignages facultatifs du mode de lecture. Toute personne disposant du lien peut consulter le document sur le Web.

Cette fonctionnalité est distincte de l'**extension Partager** de macOS (menu Partager du système). Voir [Using the Share Extension](Share_Extension.html) pour envoyer des fichiers ou des sélections vers Marked à partir d'autres applications.

## Connectez votre compte [connect-your-account]

Avant votre première publication, connectez Marked à votre compte Share :

1. Choisissez {% appmenu Fichier, Publier, Connecter le compte… %}.
2. Marked ouvre votre navigateur par défaut pour vous connecter à share.markedapp.com.
3. Après avoir approuvé la connexion, le navigateur revient à Marked avec un lien de connexion sécurisé. Confirmez le libellé du compte affiché dans la boîte de dialogue.

Marked stocke le jeton API et la clé de périphérique dans le trousseau macOS sur ce Mac. Les informations d'identification ne sont pas écrites dans les journaux ou les rapports d'erreur.

Pour vous déconnecter, choisissez {% appmenu Fichier, Publier, Déconnecter le compte… %}. Les documents publiés restent en ligne ; révoquer l'accès à tout moment sur share.markedapp.com si nécessaire.

## Publier un document [publish-a-document]

Avec un document ouvert dans l'aperçu, choisissez {% appmenu Fichier, Publier, Publier… %}.

La première fois que vous publiez un document, Marked affiche une petite feuille d'options :

- **Titre** — affiché sur le partage (par défaut, le nom du document sans son extension).
- **Visibilité** — Privé, non répertorié ou public. Les nouvelles publications sont par défaut **Non répertoriées** (accessibles par lien, non répertoriées publiquement).
- **Style de lecture** — Éditorial, Manuscrit, Suisse, Contraste, Machine à écrire ou **Aucun**. Par défaut, le style d'aperçu du document est utilisé lorsque cela est possible. Share l'utilise comme suggestion ; les lecteurs peuvent l’ignorer. Choisissez **Aucun** pour publier sans style suggéré.
- **Inclure les surlignages et les commentaires** — intègre les surlignages du mode lecture dans le TextPack. La valeur par défaut est activée lorsque le document comporte des surlignages.
- **Autoriser les autres à remixer** : lorsque cette option est activée, les spectateurs peuvent partager le document sur Partager.

Marked crée un TextPack en arrière-plan (Markdown, actifs et `highlights.json` facultatif), le télécharge et enregistre l'URL de partage sur ce Mac.

### Mettre à jour une publication existante [update-an-existing-publish]

Une fois qu'un document est lié à Partager, l'élément de menu indique **Mettre à jour le document publié** au lieu de **Publier…**. Choisissez-le pour télécharger une nouvelle version TextPack. Marked envoie le hachage du contenu du serveur afin que les modifications simultanées provenant d'un autre Mac ou du Web soient détectées.

Si quelqu'un d'autre a d'abord mis à jour le document sur Partager, Marked demande s'il faut **Ecraser** avec la version de ce Mac, **Ouvrir sur le Web** ou **Annuler**.

## Après la publication [after-publishing]

Lorsqu'une publication est terminée, Marked confirme le succès et propose :

- **Copier le lien de partage** — {% appmenu Fichier, Publier, Copier le lien Share %}
- **Ouvert sur le Web** — {% appmenu Fichier, Publier, Ouvrir sur le web %}

Ces commandes s'appliquent au document de couverture lorsqu'il possède un enregistrement de publication lié.

## Fenêtre Documents publiés [published-documents-window]

Choisissez {% appmenu Fichier, Publier, Documents publiés… %} pour ouvrir une liste de documents publiés depuis ce Mac et synchronisés depuis votre compte Share.

Pour chaque entrée, vous pouvez :

- **Ouvrez** le fichier local lorsque Marked a encore un lien vers celui-ci sur le disque.
- **Importez** un TextPack lorsqu'il n'y a pas de fichier local (enregistrez-le n'importe où et ouvrez-le dans Marked).
- **Ouvrir sur le Web** ou **Copier le lien** pour l'URL de partage.
- **Révéler dans le Finder** lorsqu'un chemin local est connu.
- **Forget** supprime l'enregistrement de ce Mac sans supprimer le document en ligne.

La liste est actualisée à partir de Partager lorsque vous êtes connecté. Si vous êtes hors ligne ou déconnecté, Marked affiche les enregistrements mis en cache et peut vous inviter à vous reconnecter.

## Ce que vous pouvez publier [what-you-can-publish]

Vous pouvez publier n'importe quel document que Marked peut restituer, notamment :

- Enregistré Markdown et fichiers texte
- Aperçus transitoires (presse-papiers, streaming ou documents non enregistrés)
- TextBundles et autres formats pris en charge

Une seule opération de publication s'exécute à la fois par fenêtre de document ; l'élément de menu est désactivé pendant qu'un téléchargement est en cours.

## Conseils [tips]

- La publication inclut les images référencées par l'aperçu. Les lots très volumineux peuvent être rejetés avant le téléchargement ; réduisez les actifs intégrés si vous atteignez une limite de taille.
- Les faits saillants exportés dans TextPack utilisent le format JSON de surbrillance de Marked. Voir [Reading Mode](Reading_Mode.html) pour créer et exporter des faits saillants.
- Marked Share est disponible dans les versions Direct, Mac App Store, Setapp et Marked Pro. Aucun abonnement séparé n'est requis pour la publication.
