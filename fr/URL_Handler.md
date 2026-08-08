# <%= @title %>

Le gestionnaire d'URL de Marked offre des possibilités supplémentaires de script et d'automatisation de flux de travail. Vous pouvez par exemple inclure une URL dans les notes d'une autre application, qui ouvrira un fichier dans Marked lorsqu'on cliquera dessus. Plusieurs actions sont possibles, comme indiqué ci-dessous.

## Le schéma d'URL [the-url-scheme]

Le schéma d'URL de Marked est `x-marked`, appelé avec des options telles que `x-marked://open?file=/Users/username/Desktop/report.md`.

Vous pouvez cibler spécifiquement Marked 3 en utilisant `x-marked-3` au lieu de `x-marked`. Les méthodes et paramètres sont exactement les mêmes qu'avec `x-marked`, mais seul Marked 3 répondra à `x-marked-3`.

## Appel depuis la ligne de commande ou un script [calling-from-the-command-linescripts]

Il est possible d'appeler le gestionnaire d'URL depuis la ligne de commande ou un script à l'aide de la [commande `open`](http://brettterpstra.com/2014/08/06/shell-tricks-the-os-x-open-command/) de macOS :

	open 'x-marked://open?file=filename.md'
	open 'x-marked://refresh?file=filename.md'

### Appel en arrière-plan [calling-in-the-background]

Vous pouvez appeler la commande `open` avec l'indicateur `-g` pour exécuter le résultat en arrière-plan sans changer le focus. Pour exécuter la commande en arrière-plan et faire remonter la fenêtre au premier plan sans lui donner le focus :

	open -g 'x-marked://open?file=filename.md&raise=true'

## Paramètres facultatifs [optional-parameters]

### x-success [x-success]

N'importe quelle commande peut inclure un paramètre de requête **x-success**. Définissez-le avec une URL à appeler après l'exécution de la commande. Par exemple : `x-marked://open/?file=filename.md&x-success=ithoughts:`. Vous pouvez également fournir un identifiant de bundle (comme `com.googlecode.iterm`) pour ouvrir une application qui ne dispose pas de schéma d'URL propre.

### raise [raise]

Un paramètre **raise** peut être transmis à toute commande acceptant un paramètre `file`, ou affectant toutes les fenêtres. Une fois l'action exécutée, la ou les fenêtres concernées remonteront au-dessus de toutes les autres fenêtres (toutes applications confondues) avant de revenir ou d'exécuter un rappel.

	"x-marked://refresh?file=filename.md&raise=true"

### speedread [speedread]

Un paramètre **speedread** peut être transmis aux commandes du gestionnaire d'URL qui ouvrent un document d'aperçu (`open`, `paste`, `preview` et `stream`). Définissez `speedread=1` pour démarrer automatiquement Lecture rapide dès que l'aperçu ciblé est prêt.

Exemples :

	x-marked://open?file=/Users/username/Desktop/report.md&speedread=1

	x-marked://preview?text=Some%20text&speedread=1

	x-marked://paste?speedread=1

# Commandes disponibles [available-commands]

Les commandes suivantes sont disponibles pour le gestionnaire d'URL `x-marked`.

## addstyle [addstyle]

Ajoute un nouveau style personnalisé à Marked.

##### Paramètres : [parameters]

**css** : texte CSS encodé en URL à écrire dans un style personnalisé. Requis, sauf si un paramètre **file** est fourni.

**file** : chemin complet (POSIX) vers un fichier CSS à ajouter à Marked. Requis, sauf si un paramètre **css** est fourni.

**name** : le nom du style à générer.

Avec le paramètre **css**, ce nom sera utilisé à la fois comme nom de fichier lors de l'écriture sur le disque (avec l'ajout de « .css ») et comme nom d'élément de menu. Il est requis pour le paramètre **css**, et facultatif pour **file** (le nom de fichier sera utilisé si le paramètre name est vide).

	x-marked://addstyle?name=My+new+style&css=...

	x-marked://addstyle?file=/Users/myuser/Custom+Styles/Unicorn.css

Si vous incluez un nom avec le paramètre file, l'élément de menu prendra ce nom plutôt que le nom du fichier. Si vous réutilisez le même nom avec un chemin différent, l'élément de menu sera mis à jour avec le nouveau chemin, plutôt que d'ajouter un second élément portant le même nom.

## defaults [defaults]

Définit les Paramètres utilisateur. Accepte une liste de clés et de valeurs sous forme de paramètres de requête. Seules les clés existantes seront définies. Si la modification de préférence nécessite une actualisation, toutes les fenêtres seront actualisées automatiquement, sauf si `refresh=0` est transmis.

Utilisez 1 pour vrai et 0 pour faux sur les valeurs booléennes.

##### Paramètres : [parameters-2]

**refresh** _(facultatif)_ : si défini sur 0, l'actualisation automatique des fenêtres d'aperçu ouvertes est désactivée

* Par défaut : 1 (vrai)

##### Exemple : [example]

	x-marked://defaults?syntaxHighlight=1&includeMathJax=0

La méthode `defaults` est principalement conçue pour permettre au développeur d'ajouter des liens vers des fonctionnalités ésotériques qui pourraient ne pas être autrement accessibles dans les Paramètres. Il existe toutefois certaines options standards que vous pourriez vouloir activer/désactiver lors de l'automatisation. Voici quelques Paramètres courants que vous pourriez vouloir contrôler pendant l'automatisation :

syntaxHighlight
: active ou désactive la coloration syntaxique

includeMathJax
: active ou désactive la gestion interne de MathJax

processor
: définissez sur `multimarkdown` ou `mmd` pour passer au processeur MultiMarkdown, ou sur `discount` ou `gfm` pour utiliser le processeur Discount

h1IsPageBreak, h2IsPageBreak, breakBeforeFootnotes
: sauts de page automatiques à l'export avant les titres de niveau 1 et 2, et avant les notes de bas de page.


## dingus [dingus]

Ouvre le Markdown Dingus pour tester différents processeurs Markdown.

	x-marked://dingus

##### Paramètres : [parameters-3]

**processor** (facultatif) : indique quel processeur sélectionner par défaut. Valeurs valides :

- `multimarkdown` - processeur MultiMarkdown
- `commonmark` - processeur CommonMark (GFM)
- `discount` ou `discount (gfm)` - processeur Discount
- `kramdown` - processeur Kramdown

Exemples :

- `x-marked://dingus?processor=kramdown` - ouvre avec Kramdown sélectionné
- `x-marked://dingus?processor=commonmark` - ouvre avec CommonMark (GFM) sélectionné

*Remarque :* Ceci ouvre la fenêtre Markdown Dingus, qui permet de tester et comparer différents processeurs Markdown (MultiMarkdown, CommonMark (GFM), Discount et Kramdown) côte à côte. Idéal pour expérimenter avec la syntaxe Markdown et comprendre les différences entre processeurs.

## stylestealer / steal [stylestealer-steal]

Ouvre la fenêtre HUD du Voleur de styles. Utile lorsque vous souhaitez capturer le CSS d'une page en ligne ou lancer une session d'extraction manuelle de contenu sans passer par l'interface.

	Synonymes : x-marked://stylestealer … , x-marked://steal …

##### Paramètres : [parameters-4]

**url** _(facultatif)_ : une URL à préremplir dans la fenêtre du Voleur de styles. Si omis, le HUD s'ouvre vide.

Exemples :

- `x-marked://stylestealer?url=https%3A%2F%2Fmarkedapp.com`
- `x-marked://steal/https:%2F%2Fexample.com`

## importurl / markdownify [importurl-markdownify]

Ouvre la fenêtre « Importer une URL » (Extracteur de contenu) afin de lancer manuellement le pipeline du Markdownifier. Cette commande n'effectue **pas** l'extraction automatiquement : celle-ci est gérée par la commande `extract` ci-dessous.

	Synonymes : x-marked://importurl … , x-marked://markdownify …

##### Paramètres : [parameters-5]

**url** _(facultatif)_ : préremplit le champ Importer une URL. Si omis, la fenêtre s'ouvre avec un champ vide, en attente d'un lien à coller.
**html** _(facultatif, markdownify uniquement)_ : lorsqu'il est fourni sur `x-marked://markdownify`, ce paramètre doit être du HTML brut encodé en URL. Marked convertira le HTML en Markdown selon les mêmes règles que l'aperçu du presse-papiers, et l'ouvrira dans un document temporaire, comme si vous aviez collé ce HTML dans une fenêtre d'aperçu du presse-papiers.

Exemples :

- `x-marked://importurl?url=https%3A%2F%2Fexample.com%2Farticle`
- `x-marked://markdownify/https:%2F%2Fnews.ycombinator.com`

## do [do]

Exécute une commande JavaScript dans une fenêtre de document. L'ensemble de l'API JavaScript de Marked est [documentée ici](https://markedapp.com/help/jsapi/).

##### Paramètres : [parameters-6]

**js** _(requis)_ : chaîne de requête contenant une commande JavaScript

* Accepte des paramètres de chemin faisant référence à des noms de fichiers, ou « all »
* Des chemins séparés par / permettent de rechercher plusieurs fichiers
* Les noms de fichiers partiels seront complétés avec la meilleure correspondance

		x-marked://do/filename1/filename2?js=...
		x-marked://do/all?js=...

**file** : paramètre de requête contenant des chemins/noms de fichiers séparés par des virgules

	x-marked://do?file=filename1,filename2&js=...

S'appliquera à la fenêtre au premier plan si aucun nom de fichier n'est fourni (ou si « all » n'est pas transmis)

## help [help]

Ouvre le système d'aide interne de Marked, en spécifiant éventuellement un sujet. Ceci est principalement destiné à un usage interne, mais reste accessible par URL. L'URL d'une section donnée peut être copiée en faisant un clic droit sur l'icône de signet à droite d'un titre, puis en sélectionnant __Copier le lien__. L'aide intégrée et la recherche de **Marked 3** utilisent le schéma `x-marked-3` pour ces liens, afin que macOS les ouvre dans Marked 3 lorsque Marked 2 est également installé ; les exemples ci-dessous utilisent cette forme.

##### dingus [dingus-2]

Ouvre le Markdown Dingus pour tester différents processeurs Markdown.

	x-marked://dingus

##### Paramètres : [parameters-7]

**processor** (facultatif) : indique quel processeur sélectionner par défaut. Valeurs valides :

- `multimarkdown` - processeur MultiMarkdown
- `commonmark` - processeur CommonMark (GFM)
- `discount` ou `discount (gfm)` - processeur Discount
- `kramdown` - processeur Kramdown

Exemples :

- `x-marked://dingus?processor=kramdown` - ouvre avec Kramdown sélectionné
- `x-marked://dingus?processor=commonmark` - ouvre avec CommonMark (GFM) sélectionné

*Remarque :* Ceci ouvre la fenêtre Markdown Dingus, qui permet de tester et comparer différents processeurs Markdown (MultiMarkdown, CommonMark (GFM), Discount et Kramdown) côte à côte. Idéal pour expérimenter avec la syntaxe Markdown et comprendre les différences entre processeurs.

##### Paramètres :

**page** _(facultatif)_ : le titre exact d'une page existante, avec une ancre facultative

	x-marked-3://help?page=Document_Statistics

Les espaces sont remplacés par des underscores, selon la convention de nommage des fichiers d'aide de Marked. Des deux-points (:) peuvent être utilisés à la place d'un dièse (#) pour spécifier une ancre.

La cible peut être spécifiée uniquement par le chemin (sans chaîne de requête) :

	x-marked-3://help/Keyword_Highlighting:editingkeywords


## extract [extract]

Extrait le contenu d'une URL web et l'ouvre comme nouveau document dans Marked.

	x-marked://extract?url=https://example.com

##### Paramètres : [parameters-8]

**url** _(requis)_ : l'URL web dont extraire le contenu. Doit commencer par `http://` ou `https://`

**window** _(facultatif)_ : nom de la fenêtre

**id** _(facultatif)_ : identifiant d'espace de noms

**base** _(facultatif)_ : URL de base pour les liens relatifs

**raise** _(facultatif)_ : définissez sur `true` pour faire remonter la fenêtre après ouverture

**manual** _(facultatif)_ : définissez sur `true` pour ouvrir la fenêtre d'extraction manuelle du Voleur de styles plutôt que d'effectuer une extraction automatique.

- Lorsque `manual=true`, Marked ouvre le Voleur de styles, préremplit le champ URL (si fourni), supprime toute boîte de dialogue d'ouverture automatique, et vous permet de sélectionner et d'extraire de manière interactive les styles/contenus avant d'enregistrer.
- Lorsqu'il est omis ou défini sur `false`, Marked exécute l'extracteur automatique (Markdownifier) et ouvre directement le résultat comme nouveau document temporaire.

##### Exemples : [examples]

	x-marked://extract?url=https://news.ycombinator.com

	x-marked://extract?url=https://github.com&window=GitHub&raise=true

	x-marked://extract?url=https://example.com/article&manual=true

	x-marked://extract?url=https://blog.example.com/post-title

*Remarque :* Cette commande utilise le service d'extraction de contenu de Marked pour récupérer des pages web, en extraire un contenu propre à l'aide de Readability, le convertir au format Markdown, et ouvrir le résultat dans un nouveau document temporaire. Le contenu extrait inclut des métadonnées (titre, URL source, date) et est formaté en Markdown propre. Idéal pour capturer et éditer rapidement du contenu web.

## open [open]

Ouvre le document spécifié dans Marked.

	x-marked://open?file=/Users/username/Desktop/report.md

##### Paramètres : [parameters-9]

**file** *(requis)* : le chemin POSIX complet du document à ouvrir, ou une liste de chemins séparés par des virgules

**speedread** *(facultatif)* : définissez sur `1` pour démarrer automatiquement Lecture rapide après l'ouverture.

`open` accepte également un chemin dont les composants seront combinés en une seule URL

	x-marked://open/~/nvALT2.2

Si le chemin de fichier fourni n'existe pas ou ne peut pas être ouvert, Marked passera tout de même au premier plan. L'exécution sans le paramètre *file*, ou avec une valeur vide, ouvrira simplement Marked.

Marked ouvrira également des fichiers si seul le chemin d'un fichier est appelé sur le gestionnaire d'URL, par exemple `x-marked:///Users/username/Desktop/report.md`.

## paste [paste]

Crée un nouveau document à partir du contenu actuel du presse-papiers.

	x-marked://paste

##### Paramètres : [parameters-10]

**speedread** *(facultatif)* : définissez sur `1` pour démarrer automatiquement Lecture rapide après l'ouverture de l'aperçu du presse-papiers.

*Remarque :* Ceci crée un document temporaire à l'aide de la commande « Aperçu du presse-papiers ». Tout texte présent dans votre presse-papiers est ajouté à un nouveau document vierge, qui est ensuite ouvert dans Marked. S'il est fermé sans être enregistré, il est perdu.

## preview [preview]

Prévisualise le texte spécifié dans un nouveau document.

	x-marked://preview?text=Some%20text%20to%20%2A%2Apreview%2A%2A%0A

##### Paramètres : [parameters-11]

**text** *(requis)* : le texte à insérer dans l'aperçu. Le texte encodé en pourcentage sera décodé avant l'affichage du document.

**speedread** *(facultatif)* : définissez sur `1` pour démarrer automatiquement Lecture rapide après l'ouverture du texte en aperçu.

## stream [stream]

Ouvre une fenêtre d'aperçu en continu depuis le presse-papiers.

	x-marked://stream

##### Paramètres : [parameters-12]

**speedread** *(facultatif)* : définissez sur `1` pour démarrer automatiquement Lecture rapide après l'ouverture de l'aperçu en continu.

*Remarque :* Ceci crée un document temporaire à l'aide de la commande « Aperçu du presse-papiers ». Le texte transmis est ajouté à un nouveau document vierge, qui est ensuite ouvert dans Marked. S'il est fermé sans être enregistré, il est perdu.

## refresh [refresh]

Actualise l'aperçu d'un document, ou de tous les aperçus ouverts.

##### Paramètres : [parameters-13]

**file** : paramètre de requête contenant des chemins/noms de fichiers séparés par des virgules (les fichiers doivent être actuellement ouverts dans Marked). Un appel sans paramètre `file`, ou avec `?file=all`, actualisera toutes les fenêtres ouvertes.

Le paramètre *file* peut être partiel : Marked actualisera toutes les fenêtres ouvertes présentant une correspondance partielle dans le *nom de fichier* (et non le chemin complet). Passer « all » actualisera toutes les fenêtres.

	x-marked://refresh

	x-marked://refresh?file=/Users/username/Desktop/report.md

	x-marked://refresh?file=report.md

Si appelé sans paramètre `file` mais avec des chemins de document spécifiés dans l'URL, les chemins séparés par / permettront de rechercher plusieurs fichiers, et les noms de fichiers partiels seront complétés avec la meilleure correspondance.

	x-marked://refresh/filename1/filename2

## style [style]

Définit le style d'aperçu (CSS) pour un ou plusieurs documents.

##### Paramètres : [parameters-14]

**css** _(requis)_ : chaîne de requête contenant le nom ou le chemin d'un style. Les styles doivent être présents dans le menu Style de Marked, en tant que style par défaut ou style personnalisé ajouté manuellement.

* Accepte des paramètres de chemin faisant référence à des noms de fichiers, ou « all »
* Des chemins séparés par / permettent de rechercher plusieurs fichiers
* Les noms de fichiers partiels seront complétés avec la meilleure correspondance

		x-marked://style/filename1/filename2?css=...
		x-marked://style/all?css=...

**file** : paramètre de requête contenant des chemins/noms de fichiers séparés par des virgules

	x-marked://style?file=filename1,filename2&css=...

Cette méthode s'appliquera à la fenêtre au premier plan si aucun nom de fichier n'est fourni (ou si « all » n'est pas transmis).

