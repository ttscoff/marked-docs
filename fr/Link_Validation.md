# <%= @title %>

La validation du lien envoie une requête ping à la destination d'une URL et teste les erreurs. Cela permet d'éviter les liens brisés et invalides dans votre document publié et est particulièrement utile pour les blogueurs.

## Validation des liens uniques [validating-single-links]

![][1]

[1]: images/validate_single.png @2x width=832px height=267px class=center

Cliquez et maintenez sur un lien dans l'aperçu jusqu'à ce qu'il clignote, puis relâchez pour ouvrir le menu d'action du lien. Choisissez "Valider le lien" pour lancer le test. Les résultats sont affichés dans la fenêtre contextuelle.

## Validation de tous les liens [validating-all-links]

![][2]

[2]: images/screenshots/mainwindow-feature-urlvalidate-crop.jpg @2x width=1089px height=300px class=center

Choisissez « Valider tous les liens » (raccourci {% kbd ctrl cmd L %}) dans le menu Action ou dans le menu contextuel. Tous les liens distants dans le document seront vérifiés et les résultats seront affichés dans une fenêtre contextuelle. En cliquant sur un lien dans la fenêtre contextuelle, vous faites défiler et mettez en surbrillance son lien respectif dans le document.

Les URL valides peuvent être masquées dans la fenêtre contextuelle grâce au bouton « Masquer les URL valides » en haut de celle-ci. Cela affichera uniquement les URL qui ont renvoyé un statut d'erreur.

Appuyer sur Échap masquera les résultats de la validation. Ils peuvent être à nouveau révélés en utilisant {% kbd ctrl cmd L %} ou le menu Action.

## Validation automatique [validating-automatically]

Activez « Valider automatiquement les URL lors de la mise à jour » dans les paramètres d'aperçu (ou en bas de la fenêtre contextuelle de validation du lien). Lors du chargement du document, les liens contenus seront testés en arrière-plan. Une boîte de dialogue s'affichera uniquement s'il y a des erreurs.

Pour désactiver la fenêtre contextuelle, désactivez-la dans les paramètres ou décochez la case en bas de la fenêtre contextuelle.
