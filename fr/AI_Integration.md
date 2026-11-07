<!-- MT-DRAFT: machine translation; human review required -->
# <%= @title %>

Donnez à un agent LLM un fichier skill pour qu'il puisse ouvrir des fichiers et des dossiers dans Marked, afficher une section des Réglages et modifier des préférences. L'agent utilise le [gestionnaire d'URL](URL_Handler.html) de Marked. Aucun module ni serveur supplémentaire n'est nécessaire.

## Télécharger le skill [download-the-skill]

{% download "SKILL.md" "Skill d'agent pour ouvrir des fichiers dans Marked et modifier des préférences. Enregistrez-le sous le nom SKILL.md." %}

Le fichier est du Markdown simple, avec un court en-tête que l'agent lit avant d'agir. Vous pouvez remettre le même fichier à tout agent qui accepte un skill ou une instruction permanente.

## L'installer [install-it]

Placez le fichier dans un dossier portant le nom du skill, et conservez le nom `SKILL.md`.

Avec Cursor, ces deux emplacements conviennent :

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

Le premier est disponible dans chaque projet. Le second ne s'applique qu'à ce projet. Les autres agents peuvent utiliser le même texte comme instruction de projet s'ils n'ont pas de dossier de skills.

Une fois le skill installé, demandez à l'agent d'ouvrir un fichier ou un dossier dans Marked. Il doit lancer une commande de ce genre :

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

Un dossier utilise la même commande. Le chemin doit exister, et les espaces comme les autres caractères réservés doivent être encodés en pourcent. Voir le [gestionnaire d'URL](URL_Handler.html) pour le schéma complet, y compris refresh, Streaming Preview et les rappels.

## Préférences [preferences]

Le skill couvre aussi deux commandes de préférences :

`pref`
: Ouvre les Réglages sur une section nommée. Le nom dans l'URL reste en anglais, par exemple `Preview` ou `Style`. La commande ne modifie aucune valeur.

`defaults`
: Définit une préférence que Marked a déjà enregistrée, puis recharge les aperçus ouverts. Passez `refresh=0` pour laisser les aperçus tels quels. L'agent doit lire les préférences actuelles avant d'en écrire une, car une clé inconnue est ignorée.

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## Voir aussi [related]

[Utilisation de Marked with Agentic Coding](Using_Marked_with_Agentic_Coding.html) explique comment surveiller un dossier de plans et de notes pendant qu'un agent les rédige. L'[utilitaire de ligne de commande](Command_Line_Utility.html) offre le même type d'accès depuis le shell, sans agent.
