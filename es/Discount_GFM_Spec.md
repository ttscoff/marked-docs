<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Consulte [Markdown Dingus](x-marked-3://dingus?processor=discount) para experimentar con el procesador de descuentos.

## ¿Qué es el descuento GFM? [what-is-discount-gfm]

Discount GFM (GitHub Flavored Markdown) es un procesador Markdown basado en C que implementa la sintaxis extendida de Markdown de GitHub. Se basa en la biblioteca Discount original, pero se ha mejorado con funciones específicas de GitHub, como tablas, listas de tareas, texto tachado y enlaces URL automáticos.

## Características clave [key-characteristics]

- **Rendimiento basado en C**: implementación rápida y nativa de C para un rendimiento óptimo
- **Compatibilidad de GitHub**: implementa las extensiones Markdown de GitHub para una máxima compatibilidad
- **Ligero**: dependencias mínimas y espacio reducido
- **Extensible**: admite varias extensiones de Markdown y opciones personalizadas
- **Soporte HTML5**: genera resultados HTML5 modernos con marcado semántico adecuado

## Principales diferencias con el descuento estándar [major-differences-from-standard-markdown]

### 1. **Extensiones de Markdown con sabor a GitHub** [1-github-flavored-markdown-extensions]

**Tablas**

- Soporte completo para tablas estilo GitHub con opciones de alineación
- Encabezados, separadores y filas de datos con estructura de tabla HTML adecuada
- Alineación de columnas usando dos puntos (`:`) en filas separadoras

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Listas de tareas**

- Soporte para casillas de verificación estilo GitHub en listas
- Casillas de verificación interactivas (representadas como elementos de entrada HTML)
- Se admiten estados marcados y no marcados

```markdown
- [x] Completed task
- [ ] Pending task
- [x] Another completed task
```

**Texto tachado**

- El texto encerrado entre tildes dobles (`~~`) se tacha
- Utiliza etiquetas HTML `<del>` para marcado semántico
- Admite múltiples tildes para enfatizar

```markdown
~~This text is crossed out~~
~~Mistaken text that should be removed~~
```

### 2. **Compatibilidad mejorada con bloques de código** [2-enhanced-code-block-support]

**Bloques de código cercados**

- Comillas triples (```` ``` ````) para bloques de código
- Especificación de idioma para resaltado de sintaxis.
- No se requiere sangría (a diferencia del Markdown estándar)

```markdown
```javascript
function hello() {
  console.log("Hello, World!");
}
```
```

**Automatic Language Detection**

- Support for many programming languages
- Proper syntax highlighting when supported
- Fallback to plain text for unsupported languages

### 3. **Automatic URL Linking** [3-automatic-url-linking]

**URL Autolinking**

- Automatic conversion of URLs to clickable links
- Support for http, https, and ftp protocols
- Email addresses automatically converted to mailto links

```markdown
Visit http://example.com for more information.
Contact us at user@example.com
```

**Detección de enlace inteligente**

- Reconoce URL sin marcado explícito
- Maneja varios formatos y protocolos de URL
- Opciones de seguridad de enlace configurables

### 4. **Funciones de lista avanzadas** [4-advanced-list-features]

**Listas alfabéticas**

- Listas ordenadas con marcadores alfabéticos (a, b, c, etc.)
- Progresión automática a través del alfabeto.
- Salida HTML `<ol type="a">` adecuada

```markdown
a. First item
b. Second item
c. Third item
```

**Procesamiento de listas mejorado**

- Mejor manejo de listas anidadas
- Espaciado y sangría mejorados.
- Soporte para tipos de listas mixtas

### 5. **Soporte de notas al pie** [5-footnotes-support]

**Notas al pie de estilo de referencia**

- Numeración automática de notas a pie de página
- Enlaces de referencia con sintaxis `[^1]`
- Definiciones de notas al pie al final del documento.

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Procesamiento automático de notas al pie**

- Genera una estructura de notas al pie HTML adecuada
- Vínculos entre referencias y definiciones.
- Numeración secuencial en todo el documento.

### 6. **Integración HTML** [6-html-integration]

**Soporte HTML5**

- Reconocimiento completo de etiquetas HTML5
- Generación de marcado semántico adecuado
- Estructura y atributos HTML modernos.

**Bloques HTML sin formato**

- Soporte para HTML dentro de Markdown
- Escape y desinfección adecuados.
- Integración con la sintaxis de Markdown.

### 7. **Reglas de énfasis mejoradas** [7-enhanced-emphasis-rules]

**Énfasis relajado**

- Los guiones bajos simples (`_`) no crean énfasis en medio de las palabras.
- Mejor para documentar código y contenido técnico.
- Evita el énfasis no deseado en los identificadores.

```markdown
This is a variable_name that won't be emphasized.
This is _emphasized text_ that will be styled.
```

**Múltiples niveles de énfasis**

- Soporte para negrita, cursiva y énfasis combinado
- Consistente con las reglas estándar de énfasis de Markdown
- Salida HTML adecuada con etiquetas `<strong>` y `<em>`

### 8. **Generación de tabla de contenidos** [8-table-of-contents-generation]

**TOC automático**

- Genera tabla de contenidos a partir de títulos.
- Estructura jerárquica basada en niveles de encabezado.
- Opciones de generación de TOC configurables

**Generación de ID de encabezado**

- Generación automática de ID para encabezados.
- Enlaces de anclaje para una fácil navegación
- Formato de identificación consistente

## Descuento GFM frente a otros tipos de rebajas [discount-gfm-vs-other-markdown-flavors]

| Característica | Descuento | Marca común (GFM) | Kramdown | Rebajas múltiples | Estándar |
| ---------------- | ------------ | ---------- | -------- | ------------- | -------- |
| Mesas | Sí | No | Sí | Sí | No |
| Tachado | Sí | No | No | Sí | No |
| Listas de tareas | Sí | No | No | Sí | No |
| Código vallado | Sí | Sí | Sí | Sí | No |
| Matemáticas | No | No | Sí | Sí | No |
| Notas a pie de página | Sí | No | Sí | Sí | No |
| Listas de definiciones | No | No | Sí | Sí | No |
| Abreviaturas | No | No | Sí | No | No |
| Listas de atributos | No | No | Sí | No | No |
| Extensiones | Limitado | No | Sí | Sí | No |
| Tipografía | Básico | No | Sí | No | No |
| Enlaces automáticos | Sí | No | No | No | No |
| Listas alfabéticas | Sí | No | No | No | No |

## Ventajas clave del descuento GFM [key-advantages-of-discount-gfm]

1. **Compatibilidad con GitHub**: perfecto para contenido que necesita funcionar en GitHub
2. **Rendimiento**: implementación rápida basada en C
3. **Simplicidad**: Centrado en las funciones principales de GitHub sin complejidad
4. **Confiabilidad**: implementación estable y bien probada
5. **Cumplimiento de estándares**: sigue la especificación Markdown de GitHub
6. **Ligero**: uso mínimo de recursos y dependencias

## Casos de uso comunes [common-use-cases]

**Documentación de GitHub**

- Archivos README y documentación del proyecto.
- Páginas y wikis de GitHub
- Descripciones de problemas y solicitudes de extracción.

**Redacción técnica**

- Documentación de código y tutoriales.
- Documentación API
- Especificaciones técnicas

**Gestión de contenidos**

- Publicaciones y artículos de blog.
- Sitios web de documentación.
- Bases de conocimiento

**Edición colaborativa**

- Documentación del equipo
- Documentos de planificación del proyecto.
- Notas y actas de reuniones.

## Opciones de configuración [configuration-options]

Discount GFM admite varias opciones de configuración:

- **Enlace automático**: activar/desactivar la detección automática de URL
- **Notas al pie**: Controlar el procesamiento de notas al pie
- **Tabla de contenido**: configuración de generación de TOC
- **Seguridad HTML**: validación y desinfección de enlaces
- **Modo estricto**: reglas de análisis mejoradas
- **Cotizaciones inteligentes**: conversión automática de cotizaciones

## Detalles de implementación [implementation-details]

**Opciones del analizador**

- `kGHMarkdownAutoLink`: Habilitar enlace URL automático
- `kGHMarkdownFootnotes`: Habilitar procesamiento de notas al pie
- `kGHMarkdownTOC`: Habilitar generación de tabla de contenidos
- `kGHMarkdownSafeLinks`: Restringir enlaces a protocolos seguros
- `kGHMarkdownNoHTMLTags`: Deshabilitar el procesamiento de etiquetas HTML

**Características de salida**

- Marcado semántico HTML5
- Jerarquía de títulos adecuada
- Estructuras de mesa accesibles.
- Salida HTML limpia y válida

## Mejores prácticas [best-practices]

1. **Utilice tablas con moderación**: las tablas son poderosas pero pueden ser complejas de mantener.
2. **Aprovechar las listas de tareas**: excelente para la gestión y documentación de proyectos
3. **Utilizar enlaces automáticos**: permita que el procesador maneje la conversión de URL automáticamente
4. **Estructura con encabezados**: use la jerarquía de encabezados adecuada para una mejor generación de TOC
5. **Prueba en GitHub**: Verifique la compatibilidad con el renderizado de GitHub

## Migración desde Standard Markdown [migration-from-standard-markdown]

La mayoría de Markdown estándar funciona con Discount GFM sin cambios. Para aprovechar las funciones de GFM:

1. **Agregar tablas**: convertir datos al formato de tabla estilo GitHub
2. **Utilice listas de tareas**: reemplace las viñetas con casillas de verificación cuando corresponda
3. **Habilitar tachado**: use `~~text~~` para contenido tachado
4. **Aproveche los enlaces automáticos**: elimine el marcado manual de enlaces para URL simples
5. **Encabezados de estructura**: garantice una jerarquía de encabezados adecuada para la generación de TOC

## Recursos [resources]

- [Especificación de rebajas con sabor a GitHub](https://github.github.com/gfm/)
- [Documentación de la biblioteca de descuentos](https://www.pell.portland.or.us/~orc/Code/discount/)
- [Guía de rebajas de GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Hoja de referencia de rebajas](https://www.markdownguide.org/cheat-sheet/)

---

*Esta documentación cubre el descuento GFM implementado en Marked. Para obtener la información más actualizada, consulte siempre la especificación oficial de GitHub Flavored Markdown.*