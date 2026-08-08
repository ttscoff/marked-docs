# <%= @title %>

Marked permettra de définir certains attributs d'un document au format de métadonnées MultiMarkdown (détaillé ci-dessous). Vous pouvez les utiliser pour définir des caractéristiques et des styles qui affectent uniquement ce document sans modifier les paramètres par défaut.

La plupart des en-têtes MultiMarkdown sont ignorés par l'aperçu, mais les éléments suivants sont autorisés et affectent le rendu. Vous pouvez inclure d'autres métadonnées à restituer dans la sortie finale, Marked ignorera simplement les clés non répertoriées ci-dessous. Si vous enregistrez au format HTML et n'incluez *pas* de modèle, Marked affichera toutes les clés de métadonnées comme prévu.

## Format des métadonnées [metadata-format]

Les métadonnées sont saisies en haut du fichier Markdown ou immédiatement après tout en-tête YAML. Ils se composent d'une clé, suivie de deux points, d'espaces ou de tabulations facultatifs et de la valeur :

	Exemple de métadonnées : exemple de clé

Plusieurs entrées de métadonnées doivent figurer sur leurs propres lignes, mais sans aucun saut de ligne entre elles. La dernière entrée de métadonnées doit être suivie d'une ligne vide avant le début du texte du document.

	Premièrement : ceci est la première entrée de métadonnées
	Deuxièmement : c'est la deuxième entrée
	Troisième : la dernière entrée de métadonnées

	# Le début du texte du document

## Clés de métadonnées de Marked [marked-metadata-keys]

### Masquage des métadonnées pour les autres processeurs [hidingmeta]

**Remarque :** Si vous utilisez un processeur personnalisé ou publiez votre Markdown directement sur une source qui ne traite pas ces métadonnées, vous pouvez toujours l'utiliser en ajoutant des marqueurs de commentaires HTML avant et après les métadonnées. Contrairement à MultiMarkdown et à d'autres processeurs, Marked localisera ces balises n'importe où dans le document et les traitera/supprimera de la sortie. Ainsi, les éléments suivants dans l'en-tête fourniront les résultats souhaités dans Marked, mais n'apparaîtront pas ailleurs :

	<!--
	Marked Style: mon style personnalisé
	Custom Processor: true
	-->

*Assurez-vous simplement que la clé de métadonnées commence au début de la ligne, sans espaces ni tabulations, et ne mettez rien d'autre sur la ligne après la valeur.*

### Styles par document [per-document-styles]

La touche « `Marked Style:` » définira un style d'aperçu pour le document. La valeur peut être le nom d'un style par défaut ou un nom ou un chemin pour n'importe quel [Style personnalisé](Custom_Styles.html) que vous avez défini dans les paramètres. Si cette clé est trouvée et correspond à un style connu par Marked, ce style sera utilisé pour l'aperçu à chaque chargement du document le contenant.

**Exemple**

	Marked Style: Citoyen honnête

### Langue des citations [quotes-language]

Par défaut, Marked utilise des guillemets de style anglais. Vous pouvez modifier cela document par document avec la touche « `Quotes Language:` ». Les langues disponibles sont :

* dutch
* english
* french
* german
* guillemets
* swedish

**Exemple**

	Quotes Language: french

	Crée des «guillemets» en français.

### Niveau d'en-tête de base [base-header-level]

Vous pouvez définir le niveau d'en-tête à partir duquel Marked commence à compter avec la touche « `Base Header Level:` ». Cela devrait être un numéro de 1 à 6 et modifiera la façon dont les en-têtes "#" sont rendus. Si vous définissez le niveau d'en-tête sur 3, alors ce qui serait normalement un en-tête de premier niveau (h1) est rendu comme un en-tête de troisième niveau (h3) et les en-têtes suivants dans la hiérarchie sont décalés de 2 vers le haut.

**Exemple**

	Base Header Level: 3

	# Ce titre s'affichera sous la forme d'un h3

	## Ce titre sera un h4

	Rendu comme :

	<h3>Ce titre s'affichera au format h3</h3>

	<h4>Ce titre sera un h4</h4>

### Processeurs personnalisés [custom-processors]

Comme détaillé dans [Processeur personnalisé](Custom_Processor.html#preprocessor), vous pouvez activer ou désactiver un processeur personnalisé et un préprocesseur personnalisé à l'aide de métadonnées :

    Custom Processor: true
    Custom Preprocessor: false

"true" ou "false" active et désactive le pré/processeur.

La valeur « `Processor:` » peut être réglée sur « multimarkdown » ou « discount » pour forcer l'utilisation de l'un ou l'autre des processeurs internes. Ce paramètre par document ne modifiera pas le paramètre par défaut dans {% prefspane Processor %}.

### Imprimer les en-têtes/pieds de page [print-headersfooters]

Vous pouvez remplacer les paramètres de {% prefspane Export %} pour les en-têtes et pieds de page d'impression à l'aide des touches suivantes :

	print header left:
	print header center:
	print header right:
	print footer left:
	print footer center:
	print footer right:

Celles-ci peuvent inclure des [variables d'impression](Exporting.html#headers-and-footers) comme `%title`, `%page`, `%total`, etc., ainsi que des références à d'autres métadonnées utilisant `%md_[key without spaces]`.

### Marges d'impression [print-margins]

Définissez les marges de page pour l'impression et la sortie PDF paginé avec la touche `Margins:`. Les valeurs sont en points ; les suffixes comme `px`, `pt` et `em` sont ignorés. Fournissez deux chiffres pour les marges verticales et horizontales, ou quatre chiffres pour le haut, la droite, le bas et la gauche :

	Margins: 10 20
	Margins: 10, 20, 10, 20

Les marges des métadonnées remplacent les paramètres {% prefspane Export %} et les champs de marge dans le panneau d'exportation PDF.

### Insertion de JavaScript [inserting-javascript]

Cette méthode spécifie les données incluses dans la balise `<head>` du document. Marked ignore la plupart des valeurs de cette clé, sauf dans la sortie du document complet, mais respectera les scripts inclus de cette manière. Les balises de script définies ici ne figureront pas dans l'en-tête, cependant, elles seront ajoutées avant la balise de fermeture `</body>`. jQuery est déjà chargé et vous pouvez en profiter dans tous les scripts que vous injectez.

**Exemple**

	XHTML Header: <script>(function($){$('#wrapper').fadeOut();})(jQuery);</script>

		-ou-

	XHTML Header: <script src="myfancyscript.js"></script>
