<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

La herramienta de línea de comandos `mk` brinda fácil acceso a las funciones de Marked desde la terminal, lo que permite la automatización del flujo de trabajo y la integración con scripts de shell y otras herramientas de línea de comandos.

## Instalación

La forma recomendada de instalar `mk` es con Homebrew:

```bash
brew tap ttscoff/thelab
brew install ttscoff/thelab/mk
```

Si no utiliza Homebrew, descargue e instale el paquete firmado:

{% download "https://github.com/ttscoff/mk/releases/latest/download/mk.pkg" "Signed PKG installer for mk. Double-click to launch Installer and follow the prompts." %}

Después de descargar `mk.pkg`, haz doble clic en él y sigue las instrucciones del instalador.

## Uso básico

### Abrir archivos

Abra un archivo de rebajas en Marked desde la línea de comando:

```bash
mk file.md
mk ~/Documents/notes.md
mk --raise document.md  # Open and raise window above all others
```

### Transmisión de contenido desde STDIN

Transmita contenido directamente a la vista previa de transmisión de Marked:

```bash
echo "# Hello World" | mk
cat notes.md | mk
mk -  # Explicitly use STDIN
```

La ventana Vista previa de transmisión se abrirá y mostrará el contenido en tiempo real a medida que se transmite desde otros comandos.

## Referencia de comando

### Operaciones de archivos

**`mk [file]`** — Abrir un archivo de rebajas en Marcado

**`mk [file] --raise`** — Abra el archivo y levante la ventana por encima de todas las demás

### STDIN y transmisión

**`mk`** o **`mk -`**: leer desde STDIN y abrir Vista previa de transmisión

**`mk --stream`** — Abrir la ventana Vista previa de transmisión sin leer STDIN

### Gestión de vista previa

**`mk --refresh`** — Actualiza la ventana de vista previa frontal

**`mk --refresh all`** — Actualiza todas las ventanas de vista previa abiertas

**`mk --refresh file.md`** — Actualiza la vista previa de un archivo específico (si está abierto)

### Preferencias

**`mk --pref`** — Abrir preferencias marcadas (página General)

**`mk --pref Advanced`** — Abrir preferencias en una página específica

**`mk --defaults KEY=VALUE [KEY=VALUE...]`** — Establecer preferencias de usuario (se permiten varios pares)

```bash
mk --defaults syntaxHighlight=1 includeMathJax=0 processor=multimarkdown
```

### Gestión de estilo

**`mk --style NAME`** — Establecer estilo de vista previa para ventanas abiertas

**`mk --add-style FILE`** — Agrega un archivo CSS como estilo personalizado a Marcado

```bash
mk --add-style ~/Styles/custom.css
```

### Ejecución de JavaScript

**`mk --dojs "JAVASCRIPT_COMMAND"`** — Ejecute JavaScript en la ventana del frente

**`mk --dojs "SCRIPT" all`** — Ejecute JavaScript en todas las ventanas

**`mk --dojs "SCRIPT" file.md`** — Ejecute JavaScript en archivos específicos

```bash
mk --dojs "window.scrollTo(0,0)"
mk --dojs "alert('Hello')" all
```

### Extracción e importación de contenido

**`mk --extract URL`** — Extrae contenido de la URL y ábrelo en Marcado

```bash
mk --extract https://example.com/article
```

**`mk --importurl [URL]`** — Abrir la ventana Importar URL (opcionalmente con URL)

**`mk --stylestealer [URL]`** — HUD Open Style Stealer (opcionalmente con URL)

### Comandos de utilidad

**`mk --paste`** — Crear nuevo documento desde el portapapeles

**`mk --preview TEXT`** — Vista previa del texto directamente en un documento nuevo

**`mk --dingus`** — Abra Markdown Dingus para probar procesadores

**`mk --help`** o **`mk -h`** — Mostrar información de uso

**`mk --version`** o **`mk -v`** — Mostrar información de la versión

## Ejemplos

```bash
# Open a file
mk document.md

# Stream markdown from a file
cat notes.md | mk

# Process and preview
grep -i "important" notes.md | mk

# Refresh all previews
mk --refresh all

# Add a custom style
mk --add-style ~/Documents/MyTheme.css

# Set preferences
mk --defaults syntaxHighlight=1 processor=multimarkdown

# Run JavaScript in all windows
mk --dojs "window.scrollTo(0,0)" all

# Extract content from a webpage
mk --extract https://blog.example.com/article

# Preview text directly
mk --preview "## Hello\n\nThis is **markdown** text!"
```

## Integración

### Alias de shell

Agregue a su `~/.zshrc` o `~/.bash_profile`:

```bash
alias mko='mk --raise'      # Open with raise
alias mkr='mk --refresh all' # Refresh all
```

### Guiones

Utilice `mk` en scripts de shell para automatización:

```bash
#!/bin/bash
# Watch a file and stream changes to Marked
fswatch -o document.md | while read; do
  cat document.md | mk
done
```

### Flujos de trabajo

Combinar con otras herramientas:

```bash
# Convert clipboard to markdown and preview
pbpaste | markdown | mk

# Search and preview
grep -r "TODO" . | head -20 | mk
```

## Código abierto

La herramienta de línea de comandos `mk` es de código abierto y está disponible en GitHub:

**https://github.com/ttscoff/mk**

Puedes:
- Ver el código fuente
- Aportar mejoras
- Informar problemas
- Construir desde la fuente si es necesario

La herramienta está escrita en Swift y se puede compilar usando Xcode. Consulte el [README](https://github.com/ttscoff/mk) para obtener instrucciones de compilación.

## Versión

Verifique su versión `mk` instalada con:

```bash
mk --version
```

## Funciones relacionadas

- Consulte [Controlador de URL](URL_Handler) para obtener más información sobre el esquema de URL de Marked.
- Consulte [Vista previa de transmisión](Streaming_Preview) para obtener detalles sobre la función de vista previa de transmisión
- Consulte [Integración de flujo de trabajo](Workflow_Integration) para ver ejemplos de automatización.