# <%= @title %>

Marked exporte le HTML à partir de votre **aperçu en direct**, le même résultat rendu que vous voyez à l'écran. Utilisez l'exportation HTML lorsque vous avez besoin d'un extrait de code à coller dans un blog ou un CMS, ou d'un fichier `.html` autonome avec des styles et des images intégrés que vous pouvez ouvrir dans n'importe quel navigateur ou héberger n'importe où.

Le flux de travail typique est **prévisualiser d'abord, exporter ensuite le HTML** : ouvrez ou compilez votre document dans Marked, choisissez un thème, relisez-le dans l'aperçu en direct, puis exportez-le lorsque le balisage semble correct.

## Deux façons d'obtenir du HTML [two-ways-to-get-html]

### Copier le HTML (extrait) [copy-html-snippet]

**Copier HTML** place la source HTML de l'aperçu dans le presse-papiers, prête à être collée dans WordPress, Ghost, Squarespace, un forum, un modèle de courrier électronique ou toute application acceptant des fragments HTML.

* Menu Action → **Copier HTML**, ou {% kbd shift cmd C %} avec l'aperçu ciblé
* Copie le **corps HTML rendu** (pas un document complet avec le wrapper `<html>`)
* Facultatif : activez **Intégrer les images lors de la copie de HTML** dans {% prefspane Export %} pour encoder en Base64 les images locales sous forme d'URL `data:` dans la source collée.

Copier du HTML est idéal lorsque votre destination possède déjà sa propre feuille de style et que vous n'avez besoin que du balisage du contenu.

### Enregistrer le HTML (fichier) [save-html-file]

**Enregistrer HTML** écrit un fichier `.html` complet sur le disque.

* Exporter → **Enregistrer le HTML**, {% kbd cmd S %} ou **HTML** à partir du [Panneau d'exportation](Exporting.html#drawer) ({% kbd shift cmd e %})
* Choisissez le nom du fichier et l'emplacement dans la boîte de dialogue d'enregistrement
* Configurer les options d'exportation dans l'accessoire de dialogue (voir ci-dessous)

**Enregistrer HTML** est idéal pour archiver, partager un fichier autonome ou ouvrir le résultat directement dans un navigateur.

## Enregistrer les options HTML [save-html-options]

La boîte de dialogue Enregistrer HTML comprend un sélecteur de profil d'exportation et ces options :

![Enregistrer les options HTML][savehtml]

**Inclure le style dans la sortie**

Lorsque cette case est cochée, Marked intègre le CSS du thème d'aperçu sélectionné dans un bloc `<style>` à l'intérieur du fichier exporté. Choisissez n'importe quel thème intégré ou [Style personnalisé](Custom_Styles.html) dans le menu de style à côté de la case à cocher. Le résultat est un document HTML complet avec `<!DOCTYPE html>`, `<head>` et un div `#wrapper` autour de votre contenu, correspondant à ce que vous avez prévisualisé.

Lorsque cette case n'est pas cochée, Marked enregistre un document HTML minimal avec votre contenu rendu uniquement (pas de CSS de thème Marked). Utilisez-le lorsque vous souhaitez que du HTML brut soit collé ou importé dans un autre système fournissant son propre style.

**Intégrer des images locales pour du HTML autonome**

Lorsque **Inclure le style dans la sortie** est activé, vous pouvez également intégrer des images locales sous forme d'URL Base64 `data:` dans le fichier HTML. Le résultat est un fichier unique que vous pouvez envoyer par courrier électronique, télécharger ou héberger sans dossier `images/` séparé.

* Fonctionne avec des images référencées par des **chemins relatifs ou absolus** sur votre disque local
* Évitez les URL `file:///` : elles ne peuvent pas être intégrées de manière fiable
* Les images distantes (http/https) restent sous forme d'URL externes, sauf si vous les téléchargez au préalable.
* L'intégration Base64 peut produire des fichiers volumineux ; utilisez-la lorsque la portabilité compte plus que la taille du fichier

**Inclure JavaScript de mise en évidence de la syntaxe**

Lorsque la coloration syntaxique est activée dans {% prefspane Preview %}, cette option ajoute highlight.js CSS et JavaScript à partir d'un CDN afin que les blocs de code conservent leurs couleurs dans le fichier exporté. Le HTML exporté nécessite une connexion Internet pour que les ressources CDN se chargent.

**Inclure le lien MathJax ou KaTeX CDN**

Lorsque [MathJax](MathJax.html) ou KaTeX est activé pour l'aperçu, vous pouvez inclure les scripts CDN correspondants dans le HTML enregistré afin que les équations s'affichent dans un navigateur. Comme la coloration syntaxique, cela nécessite un accès au réseau lors de la visualisation du fichier, sauf si vous hébergez vous-même les scripts.

**Type d'exportation CriticMarkup**

Les documents avec [CriticMarkup](CriticMarkup.html) peuvent choisir si l'exportation affiche le texte modifié, le texte original ou le balisage complet.

**Exporter le profil**

Sélectionnez un [Profil d'exportation](Exporting.html#export-profiles) enregistré pour restaurer vos paramètres d'exportation HTML préférés (styles intégrés, images, coloration syntaxique, mathématiques) en une seule étape.

## Style avec des thèmes intégrés et personnalisés [styling-with-built-in-and-custom-themes]

Le **style d'aperçu** détermine l'apparence HTML lorsque **Inclure le style dans la sortie** est coché :

1. Choisissez un style dans le menu de style de la fenêtre d'aperçu (ou définissez un style par défaut dans {% prefspane Style %}).
2. Vérifiez la typographie, les titres, les blocs de code et les images dans l'aperçu en direct.
3. Enregistrez le HTML avec le même style sélectionné dans la boîte de dialogue d'exportation.

Chaque thème Marked intégré (Swiss, GitHub, Manuscript et le reste) peut être intégré. Les [Styles personnalisés](Custom_Styles.html) et les styles du [Gestionnaire de styles](Custom_Styles.html) fonctionnent de la même manière.

I> Certains CSS en aperçu uniquement (positionnement fixe, astuces de fenêtre d'affichage, inversion du mode sombre `@media screen`) peuvent ne pas se traduire un à un en dehors de Marked. Ouvrez le fichier enregistré dans un navigateur pour vérifier avant de le publier.

Pour obtenir des conseils sur la création, voir [Écrire du CSS personnalisé](Writing_Custom_CSS.html).

## En-têtes de métadonnées et MultiMarkdown [metadata-and-multimarkdown-headers]

Les métadonnées MultiMarkdown en haut de votre fichier source peuvent affecter l'exportation HTML :

* **`Title:`** : utilisé pour l'élément `<title>` lors de l'enregistrement d'un document HTML complet
* **`XHTML Header:`** / **`HTML Header:`** : injecte des balises supplémentaires dans le `<head>` exporté (scripts, balises de lien, balises méta)
* Les autres clés de métadonnées sont traitées en fonction de votre [processeur Markdown](Choosing_a_Processor.html)

Si vous utilisez des métadonnées pour les paramètres d'exportation mais que vous ne souhaitez pas que les clés soient visibles dans d'autres sorties, enveloppez-les dans des commentaires HTML : Marked recherche et traite les métadonnées commentées n'importe où dans le document. Voir [Paramètres par document](Per-Document_Settings.html).

## Documents multi-fichiers [multi-file-documents]

Pour les compilations de livres et de chapitres, utilisez [Documents multi-fichiers](Multi-File_Documents.html). Marked prévisualise le document fusionné et exporte un fichier HTML à partir du résultat compilé. Les fichiers inclus sont marqués de commentaires HTML indiquant leurs chemins d'accès source, utiles pour vérifier quel chapitre a contribué à quelle section.

## Coller dans d'autres applications [pasting-into-other-applications]

| Destination | Approche suggérée |
| :-- | :-- |
| Blog / CMS avec son propre thème | **Copier HTML** (extrait, pas de CSS Marked intégré) |
| Site ou archive statique | **Enregistrez le HTML** avec **Inclure le style dans la sortie** |
| Partage d'e-mails ou de fichiers (une pièce jointe) | **Enregistrez le HTML** avec **Intégrer des images locales** |
| WordPress, Ghost, Notion, etc. | **Copier le HTML** ; activez **Intégrer les images lors de la copie HTML** si l'éditeur ne résout pas les chemins locaux |
| Modification ultérieure dans un éditeur de code | **Enregistrez le HTML** sans style intégré, ou copiez l'extrait et enveloppez-le manuellement |

[Copier le texte enrichi](Exporting.html#rtfexportoptions) (menu Action) est une alternative lorsque l'application cible accepte le texte formaté plutôt que la source HTML.

## Sujets connexes [related-topics]

* [Exportation](Exporting.html) : panneau d'exportation, profils et autres formats
* [Exportation EPUB](EPUB_Export.html) : sortie ebook avec CSS intégré
* [Aperçu Live Markdown sur Mac](Live_Markdown_Preview_on_Mac.html) : aperçu du flux de travail avant l'exportation
* [Styles personnalisés](Custom_Styles.html) et [Paramètres : Exporter](Settings_Export.html)
* [Paramètres spécifiques HTML](HTML_Specific_Settings.html) : options du processeur pour la sortie HTML
* [Exportation AppleScript](AppleScript_Support.html) : automatiser la copie et l'enregistrement HTML

[savehtml]: images/SaveHTML.png @2x width=740px height=229px
