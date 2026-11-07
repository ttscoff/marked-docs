<!-- MT-DRAFT: machine translation; human review required -->
# <%= @title %>

Entrega a un agente LLM un archivo de skill para que pueda abrir archivos y carpetas en Marked, ir a una sección de Ajustes y cambiar preferencias. El agente usa el [controlador de URL](URL_Handler.html) de Marked. No hace falta un plugin ni un servidor aparte.

## Descargar el skill [download-the-skill]

{% download "SKILL.md" "Skill de agente para abrir archivos en Marked y cambiar preferencias. Guárdalo como SKILL.md." %}

El archivo es Markdown sencillo, con un encabezado breve que el agente lee antes de actuar. Puedes entregar el mismo archivo a cualquier agente que acepte un skill o una instrucción fija.

## Instalarlo [install-it]

Coloca el archivo en una carpeta con el nombre del skill y conserva el nombre `SKILL.md`.

En Cursor valen estas dos rutas:

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

La primera está disponible en todos los proyectos. La segunda solo se aplica a ese proyecto. Otros agentes pueden usar el mismo texto como instrucción del proyecto si no tienen una carpeta de skills.

Cuando esté instalado, pide al agente que abra un archivo o una carpeta en Marked. Debería ejecutar un comando como este:

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

Una carpeta usa el mismo comando. La ruta tiene que existir, y los espacios y otros caracteres reservados deben ir codificados con porcentaje. Consulta el [controlador de URL](URL_Handler.html) para el esquema completo, incluidos refresh, Streaming Preview y las devoluciones de llamada.

## Preferencias [preferences]

El skill también cubre dos comandos de preferencias:

`pref`
: Abre Ajustes en una sección con nombre. El nombre en la URL se queda en inglés, por ejemplo `Preview` o `Style`. No cambia ningún valor.

`defaults`
: Define una preferencia que Marked ya tiene guardada y vuelve a cargar las vistas previas abiertas. Pasa `refresh=0` para dejar las vistas previas como están. El agente debe leer las preferencias actuales antes de escribir una, porque una clave desconocida se ignora.

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## Relacionado [related]

[Uso de marcado con codificación agente](Using_Marked_with_Agentic_Coding.html) explica cómo vigilar una carpeta de planes y notas mientras un agente las escribe. La [utilidad de línea de comando](Command_Line_Utility.html) ofrece el mismo tipo de acceso desde la shell, sin un agente.
