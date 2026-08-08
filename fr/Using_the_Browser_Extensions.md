# <%= @title %>

Marked inclut des extensions de navigateur qui vous permettent d'envoyer directement des URL de page ou du contenu sélectionné vers Marked 3.

## Installation [install]

Téléchargez et installez depuis [https://markedapp.com/extensions](https://markedapp.com/extensions) :

- Firefox / Zen
- Chrome / Brave / Edge
- Safari (intégrée)

## Fonctionnement de l'extension [how-the-extension-works]

Lorsque vous cliquez sur un bouton de l'extension, celui-ci ouvre une URL personnalisée traitée par Marked 3 via le schéma `x-marked-3://markdownify`.

### `Markdownifier l'URL` [markdownify-url]

Dans le popup de l'extension, cliquez sur **`Markdownifier l'URL`** pour envoyer l'URL de la page actuelle à Marked.

### `Markdownifier la sélection` [markdownify-selection]

Dans le popup de l'extension, cliquez sur **`Markdownifier la sélection`** lorsque vous avez une sélection sur la page.

Marked reçoit le HTML de la sélection actuelle et le convertit en Markdown.

### Select Section (mode de sélection par bloc) [select-section-block-selection-mode]

![][1]

[1]: images/marked-3-chrome-1.jpg width=1280px height=800px class=center

Cliquez sur **Select Section** pour entrer en « mode de sélection de section » :

- Survolez la page pour mettre en évidence les éléments de bloc que vous pouvez sélectionner.
- Cliquez sur un bloc pour l'envoyer immédiatement à Marked (envoi simple).
- Cmd-cliquez sur des blocs pour en sélectionner plusieurs (Cmd-cliquez à nouveau pour retirer un bloc).
- Appuyez sur Retour pour envoyer les blocs actuellement sélectionnés.
- Appuyez sur Échap pour annuler le mode de sélection de section.

Pendant la sélection, le popup propose également des contrôles de zoom pour vous aider à cliquer sur des sections petites ou denses :

![][2]

[2]: images/marked-3-chrome-2.jpg width=1280px height=800px class=center

- `-` fait un zoom arrière
- **Fit Height** fait un zoom pour que la page s'ajuste à la hauteur de la fenêtre
- `+` fait un zoom avant
