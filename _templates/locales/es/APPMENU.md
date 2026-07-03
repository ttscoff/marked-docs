# appmenu reference — Spanish (es)

Ready-made Spanish menu paths for the `{% appmenu … %}` tags. Translate only the **menu text**; leave shortcut tokens (`{{cmd}}O`, `(~@$m)`, `(@~k)` …) exactly as they are. Paths should match the localized app (`es.lproj`).

Verify each path in the running Spanish Marked app before publishing.

## File → Archivo

| English | Spanish |
|---|---|
| `File, Open... ({{cmd}}O)` | `Archivo, Abrir… ({{cmd}}O)` |
| `File, Open...` | `Archivo, Abrir…` |
| `File, Open Recent` | `Archivo, Abrir recientes` |
| `File, Quick Open` | `Archivo, Abrir rápido` |
| `File, Quick Actions…` | `Archivo, Acciones rápidas…` |
| `File, New ({{cmd}}N)` | `Archivo, Nuevo ({{cmd}}N)` |
| `File, Export` | `Archivo, Exportar…` |

## Preview → Vista previa

| English | Spanish |
|---|---|
| `Preview, Dark Mode ({{opt}}{{cmd}}I)` | `Vista previa, Modo oscuro ({{opt}}{{cmd}}I)` |
| `Preview, Dark Mode` | `Vista previa, Modo oscuro` |
| `Preview, Refresh` | `Vista previa, Actualizar` |
| `Preview, Show Status Bar ({{ctrl}}/)` | `Vista previa, Mostrar barra de estado ({{ctrl}}/)` |

## Style → Estilo

| English | Spanish |
|---|---|
| `Style, Manage Styles (~@$m)` | `Estilo, Administrar estilos (~@$m)` |
| `Style, Generate a Custom Style` | `Estilo, Generar un estilo personalizado` |

## Help → Ayuda

| English | Spanish |
|---|---|
| `Help` | `Ayuda` |
| `Help, Markdown Reference` | `Ayuda, Referencia de Markdown` |
| `Help, Report an Issue` | `Ayuda, Informar de un problema` |
| `Help, Markdown Dingus` | `Ayuda, Dingus de Markdown` |

## Settings

- `{% prefspane General %}` and similar keep the **English pane ID** — never translate those.
- In prose, use **Ajustes** (matches `Ajustes…` in the Spanish app menu).
