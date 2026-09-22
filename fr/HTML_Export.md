Marked exporte le HTML à partir de votre **aperçu en direct** --- le même rendu que celui affiché à l'écran. Utilisez l'export HTML lorsque vous avez besoin d'un extrait à coller dans un blog ou un CMS, ou d'un fichier `.html` autonome avec styles et images intégrés, que vous pouvez ouvrir dans n'importe quel navigateur ou héberger n'importe où.

Le flux de travail habituel est le suivant : **aperçu d'abord, export HTML ensuite** : ouvrez ou compilez votre document dans Marked, choisissez un thème, relisez-le dans l'aperçu en direct, puis exportez une fois que le rendu vous convient.

## Deux façons d'obtenir du HTML [two-ways-to-get-html]

### Copier le HTML (extrait) [copy-html-snippet]

**Copier le HTML** place le code source HTML de l'aperçu dans le presse-papiers --- prêt à être collé dans WordPress, Ghost, Squarespace, un forum, un modèle d'e-mail, ou toute application acceptant des fragments HTML.

* Menu Action → **Copier le HTML**, ou {% kbd shift cmd C %} avec l'aperçu au premier plan
* Copie le **HTML du corps rendu** (pas un document complet avec l'enveloppe `<html>`)
* Optionnel : activez **Intégrer les images lors de la copie du HTML** dans {% prefspane Export %} pour encoder en Base64 les images locales sous forme d'URL `data:` dans le code source collé

Copier le HTML est idéal lorsque votre destination possède déjà sa propre feuille de style et que vous n'avez besoin que du balisage du contenu.

### Enregistrer le HTML (fichier) [save-html-file]

**Enregistrer le HTML** écrit un fichier `.html` complet sur le disque.

* Export → **Enregistrer le HTML**, {% kbd cmd S %}, ou **HTML** depuis le [panneau d'export](Exporting.html#drawer) ({% kbd shift cmd e %})
* Choisissez le nom de fichier et l'emplacement dans la boîte de dialogue d'enregistrement
* Configurez les options d'export dans l'accessoire de la boîte de dialogue (voir ci-dessous)

Enregistrer le HTML est idéal pour l'archivage, le partage d'un fichier autonome, ou l'ouverture directe du résultat dans un navigateur.

## Options d'enregistrement HTML [save-html-options]

La boîte de dialogue Enregistrer le HTML comprend un sélecteur de profil d'export et les options suivantes :

![Options d'enregistrement HTML][savehtml]

**Inclure le style dans le résultat**

Lorsque cette option est cochée, Marked intègre le CSS du thème d'aperçu sélectionné dans un bloc `<style>` à l'intérieur du fichier exporté. Choisissez n'importe quel thème intégré ou [style personnalisé](Custom_Styles.html) dans le menu de styles situé à côté de la case à cocher. Le résultat est un document HTML complet avec `<!DOCTYPE html>`, `<head>`, et une div `#wrapper` autour de votre contenu --- correspondant à ce que vous avez vu dans l'aperçu.

Lorsque cette option est décochée, Marked enregistre un document HTML minimal contenant uniquement votre contenu rendu (sans le CSS des thèmes de Marked). Utilisez cette option lorsque vous souhaitez du HTML brut à coller ou importer dans un autre système qui fournit son propre habillage.

**Intégrer les images locales pour un HTML autonome**

Lorsque **Inclure le style dans le résultat** est activé, vous pouvez également intégrer les images locales sous forme d'URL Base64 `data:` dans le fichier HTML. Le résultat est un fichier unique que vous pouvez envoyer par e-mail, mettre en ligne ou héberger sans dossier `images/` séparé.

* Fonctionne avec les images référencées par des **chemins relatifs ou absolus** sur votre disque local
* Évitez les URL `file:///` --- elles ne peuvent pas être intégrées de manière fiable
* Les images distantes (http/https) restent des URL externes, sauf si vous les téléchargez au préalable
* L'intégration en Base64 peut produire des fichiers volumineux ; utilisez-la lorsque la portabilité compte plus que la taille du fichier

**Inclure le JavaScript de coloration syntaxique**

Lorsque la coloration syntaxique est activée dans {% prefspane Preview %}, cette option ajoute le CSS et le JavaScript de highlight.js depuis un CDN afin que les blocs de code conservent leurs couleurs dans le fichier exporté. Le HTML exporté a alors besoin d'une connexion internet pour charger les ressources du CDN.

**Inclure le lien CDN MathJax ou KaTeX**

Lorsque [MathJax](MathJax.html) ou KaTeX est activé pour l'aperçu, vous pouvez inclure les scripts CDN correspondants dans le HTML enregistré afin que les équations s'affichent dans un navigateur. Comme pour la coloration syntaxique, cela nécessite un accès réseau lors de la consultation du fichier, sauf si vous hébergez vous-même les scripts.

**Type d'export CriticMarkup**

Les documents contenant du [CriticMarkup](CriticMarkup.html) peuvent choisir si l'export affiche le texte modifié, le texte original, ou le balisage complet.

**Profil d'export**

Sélectionnez un [profil d'export](Exporting.html#export-profiles) enregistré pour restaurer en une seule étape vos paramètres d'export HTML préférés (styles intégrés, images, coloration syntaxique, formules mathématiques).

## Habillage avec des thèmes intégrés et personnalisés [styling-with-built-in-and-custom-themes]

Le **style d'aperçu** détermine l'apparence du HTML lorsque **Inclure le style dans le résultat** est coché :

1. Choisissez un style dans le menu de styles de la fenêtre d'aperçu (ou définissez-en un par défaut dans {% prefspane Style %}).
2. Vérifiez la typographie, les titres, les blocs de code et les images dans l'aperçu en direct.
3. Enregistrez le HTML avec le même style sélectionné dans la boîte de dialogue d'export.

Tous les thèmes intégrés de Marked --- Swiss, GitHub, Manuscript, et les autres --- peuvent être intégrés. Les [styles personnalisés](Custom_Styles.html) et les styles du [Gestionnaire de styles](Custom_Styles.html) fonctionnent de la même façon.

Le **CSS additionnel** provenant de {% prefspane Style %} est inclus lors de l'export HTML lorsque les styles sont intégrés. Le `<body>` exporté reçoit la classe `mk-has-additional-css` afin que les sélecteurs CSS additionnels réécrits par Marked continuent de correspondre. Voir [Créer du CSS personnalisé](Writing_Custom_CSS.html#additional-css-settings).

I> Certains CSS propres à l'aperçu (positionnement fixe, astuces liées au viewport, inversion du mode sombre `@media screen`) peuvent ne pas se transposer à l'identique en dehors de Marked. Ouvrez le fichier enregistré dans un navigateur pour vérifier avant publication.

Pour des conseils de rédaction, consultez [Créer du CSS personnalisé](Writing_Custom_CSS.html).

## Métadonnées et en-têtes MultiMarkdown [metadata-and-multimarkdown-headers]

Les métadonnées MultiMarkdown en haut de votre fichier source peuvent affecter l'export HTML :

* **`Title:`** --- utilisé pour l'élément `<title>` lors de l'enregistrement d'un document HTML complet
* **`XHTML Header:`** / **`HTML Header:`** --- injecte des balises supplémentaires dans le `<head>` exporté (scripts, balises link, balises meta)
* Les autres clés de métadonnées sont traitées selon votre [processeur Markdown](Choosing_a_Processor.html)

Si vous utilisez des métadonnées pour des paramètres d'export mais ne souhaitez pas que les clés soient visibles dans d'autres résultats, encadrez-les de commentaires HTML --- Marked recherche et traite les métadonnées en commentaire n'importe où dans le document. Voir [Paramètres par document](Per-Document_Settings.html).

## Documents multi-fichiers [multi-file-documents]

Pour les livres et les compilations de chapitres, utilisez [Documents multi-fichiers](Multi-File_Documents.html). Marked prévisualise le document fusionné et exporte un seul fichier HTML à partir du résultat compilé. Les fichiers inclus sont signalés par des commentaires HTML indiquant leur chemin source --- utile pour vérifier quel chapitre a contribué à quelle section.

## Coller dans d'autres applications [pasting-into-other-applications]

| Destination | Approche suggérée |
| :-- | :-- |
| Blog / CMS avec son propre thème | **Copier le HTML** (extrait, sans CSS Marked intégré) |
| Site statique ou archive | **Enregistrer le HTML** avec **Inclure le style dans le résultat** |
| E-mail ou partage de fichier (une seule pièce jointe) | **Enregistrer le HTML** avec **Intégrer les images locales** |
| WordPress, Ghost, Notion, etc. | **Copier le HTML** ; activez **Intégrer les images lors de la copie du HTML** si l'éditeur ne résout pas les chemins locaux |
| Édition ultérieure dans un éditeur de code | **Enregistrer le HTML** sans style intégré, ou copier l'extrait et l'encadrer manuellement |

[Copier le texte enrichi](Exporting.html#rtfexportoptions) (menu Action) est une alternative lorsque l'application cible accepte du texte formaté plutôt que du code source HTML.

## Sujets connexes [related-topics]

* [Exporter](Exporting.html) --- panneau d'export, profils et autres formats
* [Export EPUB](EPUB_Export.html) --- sortie ebook avec CSS intégré
* [Aperçu Markdown en direct sur Mac](Live_Markdown_Preview_on_Mac.html) --- flux de travail d'aperçu avant l'export
* [Styles personnalisés](Custom_Styles.html) et [Paramètres : Export](Settings_Export.html)
* [Paramètres spécifiques au HTML](HTML_Specific_Settings.html) --- options du processeur pour la sortie HTML
* [Export AppleScript](AppleScript_Support.html) --- automatiser la copie et l'enregistrement HTML

[savehtml]: images/SaveHTML.png @2x width=740px height=229px
