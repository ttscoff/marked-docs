<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked incluye extensiones de navegador que le permiten enviar URL de páginas o contenido seleccionado directamente a Marked 3.

## Instalar [install]

Descargue e instale desde [https://markedapp.com/extensions](https://markedapp.com/extensions):

-Firefox/Zen
- Cromo / Valiente / Borde
- Safari (incluido)

## Cómo funciona la extensión [how-the-extension-works]

Cuando haces clic en un botón de extensión, se abre una URL personalizada manejada por Marked 3 usando el esquema `x-marked-3://markdownify`.

### `Markdownify URL` [markdownify-url]

En la ventana emergente de la extensión, haga clic en **`Markdownify URL`** para enviar la URL de la página actual a Marked.

### `Markdownify Selection` [markdownify-selection]

En la ventana emergente de extensión, haga clic en **`Markdownify Selection`** cuando tenga una selección en la página.

Marked recibe el HTML de la selección actual y lo convierte en Markdown.

### Seleccionar sección (modo de selección de bloque) [select-section-block-selection-mode]

![][1]

[1]: images/marked-3-chrome-1.jpg width=1280px height=800px class=center

Haga clic en **Seleccionar sección** para ingresar al “modo de selección de sección”:

- Pase el cursor sobre la página para resaltar los elementos del bloque que puede seleccionar.
- Haga clic en un bloque para enviarlo inmediatamente a Marcado (envío único).
- Cmd y haga clic en bloques para seleccionar varios bloques (Cmd y haga clic nuevamente para eliminar un bloque).
- Presione Retorno para enviar los bloques seleccionados actualmente.
- Presione Esc para cancelar el modo de selección de sección.

Mientras selecciona, la ventana emergente también proporciona controles de zoom para ayudarlo a hacer clic en secciones pequeñas o densas:

![][2]

[2]: images/marked-3-chrome-2.jpg width=1280px height=800px class=center

- `-` se aleja
- **Ajustar altura** hace zoom para que la página se ajuste a la altura de la ventana gráfica
- `+` hace zoom