# <%= @title %>

Il existe plusieurs façons d'intégrer des JavaScript supplémentaires dans Marked.

## Inclure du JavaScript par document [including-javascript-per-document]

Vous pouvez inclure des scripts dans un seul document en utilisant les balises `<script>` dans le contenu lui-même. Cela peut être utile pour les bibliothèques comme [D3](https://d3js.org/) pour les visualisations de données dont vous n'avez besoin que dans des documents spécifiques :

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

Si vous utilisez MultiMarkdown comme processeur, vous pouvez inclure des scripts dans les métadonnées et ils seront insérés dans le document. Étant donné que Marked produit uniquement un « extrait », la clé `XHTML Header` n'est pas idéale. Utilisez plutôt `CSS Header` et les scripts seront insérés au bas du document.

	CSS Header: <script src="file.js"></script>

Pour actualiser les scripts inclus lorsque le contenu change, voir [Hooks](#hooks).

## Inclure du JavaScript [including-javascript]

Vous pouvez inclure votre propre JavaScript à partir de fichiers locaux, de CDN ou en collant du code brut. Pour y accéder, ouvrez {% prefspane Style %} et cliquez sur le bouton *Règles personnalisées*.

Configurez une nouvelle règle personnalisée ou ajoutez des scripts à une règle existante. Pour ajouter des scripts à chaque fichier, définissez le prédicat sur « le nom du fichier contient * ».

L'éditeur d'actions pour une règle personnalisée propose trois options pour inclure des scripts :

Insérer un fichier JavaScript
: Permet de sélectionner un fichier local à insérer à la fin du document

Insérer du JavaScript à partir de l'URL
: Vous permet d'inclure un CDN ou une autre URL distante, ce qui créera une balise `<script>` à la fin du document avec l'URL liée

Insérer du JavaScript
: Ouvre un éditeur de code dans lequel vous pouvez écrire/coller votre propre code JavaScript

Ces scripts seront insérés à la fin de l'aperçu, avant la balise du document. Si vous devez appeler une fonction init ou mettre à jour à chaque fois que l'aperçu est mis à jour, consultez [Inclure le JavaScript brut](Embedding_Scripts.html#hooks) et familiarisez-vous avec les [hooks](#hooks) de Marked.

## Mermaid et autres scripts [mermaid]

jQuery est inclus par défaut et vous pouvez l'utiliser dans tous les scripts que vous ajoutez à Marked en utilisant l'une des méthodes ci-dessous.

[Mermaid](https://mermaid.js.org/intro/) pour les diagrammes de type Markdown est désormais inclus par défaut dans chaque document. Tout bloc de code clôturé avec le langage `mermaid` sera automatiquement rendu sous forme de diagramme.

Au bas du {% prefspane Style %}, une case à cocher pour « Diagrammes de panoramique et de zoom » est disponible lorsque le contenu Mermaid est présent. Cocher cette case entraînera le zoom des diagrammes avec un défilement {% kbd cmd %} et un panoramique en cliquant et en faisant glisser. Le script de cette fonctionnalité est inclus à partir d'un CDN et nécessite une connexion Internet.

S'il y a une bibliothèque particulière que vous souhaiteriez voir incluse par défaut, veuillez me le faire savoir sur le [forum BrettTerpstra.com](https://forum.brettterpstra.com/) ou via [le site d'assistance](https://support.markedapp.com/questions/add).

## Hooks [hooks]

Depuis les versions récentes, Marked n'effectue plus une actualisation complète de la page lors de la mise à jour du contenu, mais injecte plutôt le nouveau contenu dans le DOM sans nécessiter de chargement de page. Cela signifie que les scripts inclus qui se déclenchent lors du chargement de la page ne seront pas redéclenchés lorsque le contenu est mis à jour. Marked fournit une fonctionnalité de hooks pour s'adapter à cela. Pour enregistrer un hook, vous devez inclure un deuxième bloc de script appelant la [fonction `Marked.hooks.register()`](https://markedapp.com/jsapi/Marked.hooks.html#.register__anchor), qui accepte un déclencheur, dans ce cas 'update', et une fonction à exécuter.

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script>
	Marked.hooks.register('update', function() {
		// Re-run your D3 visualization when content updates
		d3.selectAll('.chart').each(function() {
			// your D3 render logic here
		});
	});
</script>
```

Toutes les [fonctionnalités API](https://markedapp.com/jsapi/) de Marked peuvent être utilisées dans ce champ. (Vous pouvez également utiliser l'API dans n'importe quel script chargé.) Pour un débogage interactif et une expérimentation avec l'API dans un aperçu en direct, consultez la section [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) pour plus de détails sur l'utilisation du menu Développement de Safari avec Marked.

Désormais, chaque fois qu'une mise à jour est effectuée (chaque fois que le fichier source surveillé est enregistré), la fonction transmise sera exécutée. Tant que le script que vous exécutez a une fonction d'initialisation ou de rendu, vous pouvez l'appeler avec un hook et le rendre à chaque fois que votre document est enregistré et qu'une mise à jour est déclenchée.



*[CDN]: réseau de distribution de contenu
