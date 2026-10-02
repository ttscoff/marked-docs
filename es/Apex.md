# <%= @title %>

W> **El soporte de Apex en Marked está en fase beta.** El comportamiento puede cambiar a medida que la integración madure. Informa de problemas, renderizado inesperado o sintaxis faltante en [support.markedapp.com](https://support.markedapp.com).

Apex es un **procesador de Markdown unificado**: un único motor que pretende cubrir las funciones por las que la gente suele elegir CommonMark, GitHub Flavored Markdown (GFM), MultiMarkdown o Kramdown, sin renunciar a la sintaxis de los demás.

En Marked, **Apex (beta)** siempre se ejecuta en el modo **unificado** de Apex (todas esas familias de funciones activadas a la vez). Por ahora no puedes elegir un «modo CommonMark» o un «modo Kramdown» independiente de Apex dentro de Marked; eso podría llegar más adelante.

Consulta el [Markdown Dingus](x-marked-3://dingus?processor=apex) para experimentar con Apex, o abre {% appmenu Help, Markdown Reference %} y elige la pestaña **Apex** para ver una referencia rápida compacta.

---

## Por qué existe Apex [why-apex-exists]

Los «sabores» de Markdown surgieron por buenas razones --- GitHub necesitaba listas de tareas y tablas, MultiMarkdown necesitaba notas al pie y metadatos, Kramdown necesitaba listas de atributos --- pero elegir un procesador suele significar renunciar a la sintaxis de otro.

El objetivo de Apex es **consolidar** esas extensiones para que un mismo documento pueda usar:

- Los hábitos cotidianos de CommonMark / GFM (código en bloques delimitados, listas de tareas, tachado, tablas GFM)
- Notas al pie, abreviaturas y hábitos de metadatos al estilo MultiMarkdown
- Listas de definiciones, matemáticas y (para uso avanzado) listas de atributos al estilo Kramdown
- Comodidades orientadas a Marked, como llamadas de atención (callouts), Critic Markup y marcadores de TOC

La documentación completa original está en la [wiki de Apex](https://github.com/ApexMarkdown/apex/wiki). Esta página cubre lo que necesitas en el día a día dentro de la vista previa de Marked.

---

## Activar Apex en Marked [enabling-apex-in-marked]

1. Abre {% prefspane Processor %}.
2. Ajusta **Procesador de Markdown predeterminado** a **Apex (beta)**.
3. O bien anúlalo por documento con metadatos como `Processor: apex` (alias: `apex-beta`, `unified`).

Los alias también funcionan desde AppleScript, las acciones «Run Processor» de Conductor, la salida estándar de procesadores personalizados (`APEX`) y las URL de ajustes predeterminados de `x-marked://`.

T> En esta beta, Marked sigue expandiendo sus propias inclusiones de archivos (`<<[file]` y rutas de inclusión de Marked relacionadas) antes de que se ejecute Apex. El motor de inclusión nativo de Apex está desactivado en Marked por motivos de sandboxing. Usa las funciones de inclusión de Marked como ya lo haces.

---

## Sintaxis básica que Apex añade o unifica [basic-syntax]

El Markdown estándar (encabezados, énfasis, enlaces, imágenes, listas, citas, código) funciona como cabría esperar. Lo que sigue son los extras que más se necesitan al cambiar a Apex.

### Listas de tareas [task-lists]

```markdown
- [ ] Todo
- [x] Done
```

### Tachado [strikethrough]

```markdown
~~removed text~~
```

### Tablas [tables]

Tablas de barras verticales GFM con separadores de encabezado y alineación de columnas:

```markdown
| Left | Center | Right |
| :--- | :----: | ----: |
| a    | b      | c     |
```

Las funciones avanzadas de tablas (expansión de filas `^^`, expansión de columnas, títulos, tablas de cuadrícula, CSV) están documentadas en la wiki: [Tablas](https://github.com/ApexMarkdown/apex/wiki/Tables).

### Notas al pie [footnotes]

Estilo de referencia:

```markdown
See the note[^1].

[^1]: Footnote text.
```

También se admiten los estilos en línea habituales en MultiMarkdown / Kramdown. Más información: [Sintaxis](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Listas de definiciones [definition-lists]

```markdown
Apple
: A fruit.
: A computer company.
```

### Superíndice y subíndice [superscript-and-subscript]

```markdown
Text^super^ and H~2~O
```

### Matemáticas [math]

En línea `$x^2$` y en bloque `$$...$$` (los ajustes de MathJax / KaTeX de Marked siguen controlando la apariencia en la vista previa).

### Llamadas de atención [callouts]

Al estilo Obsidian / Bear:

```markdown
> [!NOTE]
> Something worth highlighting.
```

Consulta también la [sintaxis especial](Special_Syntax.html) de Marked y la página de la wiki de Apex sobre [Callouts](https://github.com/ApexMarkdown/apex/wiki/Callouts).

### Critic Markup [critic-markup]

```markdown
{++insertion++}
{--deletion--}
{==highlight==}
{>>comment<<}
```

Activa Critic Markup en Marked como siempre; Apex puede renderizar la sintaxis critic dentro del flujo del procesador. Consulta [CriticMarkup](CriticMarkup.html).

### Abreviaturas [abbreviations]

```markdown
*[HTML]: HyperText Markup Language

The HTML spec is long.
```

### Códigos de emoji [emoji-shortcodes]

```markdown
Ship it :rocket:
```

### Metadatos [metadata]

Se reconocen los metadatos iniciales YAML, los encabezados al estilo MultiMarkdown `Key: Value` y los bloques de título de Pandoc. Inserta valores con `[%key]` donde esté disponible.

Detalles de configuración: [Configuración](https://github.com/ApexMarkdown/apex/wiki/Configuration) y [Transformaciones de metadatos](https://github.com/ApexMarkdown/apex/wiki/Metadata-Transforms) en la wiki.

### Marcadores de tabla de contenidos [table-of-contents-markers]

Apex entiende los marcadores de TOC habituales, incluidos:

- `<!--TOC-->`
- `{{TOC}}` o `{{TOC:2-4}}`
- Al estilo Kramdown `{:toc}`

Excluye un encabezado con `{:.no_toc}` donde esté disponible IAL. Más información: [Sintaxis](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Marcadores especiales [special-markers]

Los comentarios HTML orientados a Marked, como `<!--BREAK-->` (salto de página) y `<!--PAUSE:N-->` (autodesplazamiento), siguen funcionando en las vistas previas con Apex.

---

## Temas avanzados (wiki) [advanced-topics-wiki]

Consulta la [wiki de Apex](https://github.com/ApexMarkdown/apex/wiki) para funciones potentes pero menos habituales en la vista previa del día a día:

| Topic | Wiki |
|------|------|
| Generación de índices | [Índices](https://github.com/ApexMarkdown/apex/wiki/Indices) |
| Citas / bibliografía | [Citas](https://github.com/ApexMarkdown/apex/wiki/Citations) |
| Listas de atributos en línea, spans, divisiones delimitadas | [Listas de atributos en línea](https://github.com/ApexMarkdown/apex/wiki/Inline-Attribute-Lists) |
| Documentos multiarchivo e inclusiones | [Documentos multiarchivo](https://github.com/ApexMarkdown/apex/wiki/Multi-File-Documents) |
| Formatos de ID de encabezado | [ID de encabezado](https://github.com/ApexMarkdown/apex/wiki/Header-IDs) |
| Imágenes multiformato | [Imágenes multiformato](https://github.com/ApexMarkdown/apex/wiki/Multi-Format-Images) |
| Modos de compatibilidad (CLI) | [Modos](https://github.com/ApexMarkdown/apex/wiki/Modes) |
| Plugins y filtros | [Plugins](https://github.com/ApexMarkdown/apex/wiki/Plugins), [Filtros](https://github.com/ApexMarkdown/apex/wiki/Filters) |
| Quarto / Pandoc / Jekyll | [Modo Quarto](https://github.com/ApexMarkdown/apex/wiki/Quarto-Mode), [Integración con Pandoc](https://github.com/ApexMarkdown/apex/wiki/Pandoc-Integration), [Jekyll](https://github.com/ApexMarkdown/apex/wiki/Using-Apex-with-Jekyll) |

---

## Véase también [see-also]

- [Elegir un procesador](Choosing_a_Processor.html) --- cuándo elegir MultiMarkdown, CommonMark, Kramdown, Discount o Apex
- [Ajustes: Procesador](Settings_Processor.html)
- [Markdown Dingus](Markdown_Dingus.html)
- [Página principal de la wiki de Apex](https://github.com/ApexMarkdown/apex/wiki)
- Informar de problemas: [support.markedapp.com](https://support.markedapp.com)
