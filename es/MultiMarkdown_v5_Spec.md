<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Consulte [Markdown Dingus](x-marked-3://dingus?processor=multimarkdown) para experimentar con el procesador MultiMarkdown.

## ¿Qué es MultiMarkdown?

MultiMarkdown es un procesador Markdown extendido diseñado para trabajar con documentos completos en lugar de solo fragmentos de páginas web. Amplía la sintaxis original de Markdown con funciones que permiten la conversión a múltiples formatos de salida, incluidos documentos HTML, LaTeX, PDF, ODF y Microsoft Word.

## Características clave

- **Centrado en documentos**: Diseñado para documentos completos, no solo fragmentos web
- **Salida multiformato**: Convierte a HTML, LaTeX, PDF, ODF, RTF y Word
- **Contenido sobre presentación**: se centra en la estructura y el significado del documento.
- **Multiplataforma**: funciona en cualquier sistema operativo con cualquier editor de texto
- **Extensible**: conjunto completo de funciones para requisitos de documentos complejos
- **Versión 5**: reescritura completa con rendimiento y confiabilidad mejorados

## Filosofía y objetivos de diseño

MultiMarkdown sigue el principio de que **el contenido es más importante que la presentación**. La atención se centra en representar el significado de los documentos (esto es una lista, esto es una tabla, etc.) en lugar de dictar fuentes, colores o estilos.

El objetivo es ser utilizable para el 80% de los documentos que escribe el 80% de las personas, lo que lo hace adecuado para novelas, tesis, documentación técnica y la mayoría del resto del contenido escrito.

## Funciones y extensiones principales

### 1. **Soporte de metadatos**

- Metadatos del documento en la parte superior de los archivos.
- Título, autor, fecha y variables personalizadas.
- Inclusión automática en encabezados de salida.

```markdown
title: My Document
author: John Doe
date: 2024-01-15
custom: value

<!-- A blank line ends the metadata -->
Content
---

# Document Content
```

**Variables de metadatos**

- Utilice valores de metadatos en todo el documento.
- Sintaxis: `[%variable_name]`
- Sustitución automática durante el procesamiento.

```markdown
Title: [%title]
Author: [%author]
Date: [%date]
```

### 2. **Tablas avanzadas**

**Soporte completo de mesa**

- Encabezados, alineación y estructuras de tablas complejas.
- Soporte para títulos y etiquetas de tablas.
- Referencias cruzadas a tablas.

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |

Table: Sample Table with Alignment
```

**Características de la mesa**

- Alineación de columnas usando dos puntos
- Títulos y etiquetas de tablas.
- Referencias cruzadas con `[Table 1]`
- Soporte para estructuras de tablas complejas.

### 3. **Notas a pie de página y citas**

**Notas a pie de página**

- Notas al pie de estilo de referencia con sintaxis `[^1]`
- Numeración y vinculación automática.
- Soporte para notas a pie de página en línea

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Soporte de citas**

- Formato de citas académicas.
- Generación de bibliografía.
- Soporte para varios estilos de citas.

```
This is a statement that should be attributed to
its source[p. 23][#Doe:2006].
```

Y a continuación se muestra la descripción de la referencia a ser.
utilizado en la bibliografía.

```
[#Doe:2006]: John Doe. *Some Big Fancy Book*.  Vanity Press, 2006.
```

En la salida HTML, las citas no se pueden distinguir de las notas a pie de página.

No es necesario que utilice un localizador (p. ej., página 23) y no existen reglas especiales sobre lo que se puede utilizar como localizador si decide utilizar uno. Si prefiere omitir el localizador, simplemente use un conjunto vacío de corchetes antes de la cita:

```
This is a statement that should be attributed to its
source[][#Doe:2006].
```

No existen reglas sobre el formato de clave de cita que utiliza (por ejemplo, Doe:2006), pero debe ir precedido de un `#`, al igual que las notas a pie de página usan `^`.

### 4. **Referencias cruzadas**

**Referencias cruzadas automáticas**

- Enlace a títulos, tablas, figuras y ecuaciones.
- Generación automática de etiquetas.
- Soporte para etiquetas personalizadas

```markdown
See [Table 1] for details.
Refer to [Section 2.1] for more information.

## Section 2.1 [section-2-1]
```

**Tipos de referencia**

- Títulos: `[Section 1]`, `[Heading Title]`
- Tablas: `[Table 1]`, `[Table: Caption]`
- Cifras: `[Figure 1]`, `[Figure: Caption]`
- Ecuaciones: `[Equation 1]`

### 5. **Listas de definiciones**

**Pares de término-definición**

- Soporte para listas de definiciones.
- Múltiples definiciones por término
- Salida HTML `<dl>` adecuada

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

### 6. **Bloques de código cercados**

**Bloques de códigos específicos del idioma**

- Triples backticks con especificación de idioma.
- Soporte de resaltado de sintaxis
- Detección automática de idioma

```markdown
```python
def hello():
    print("Hello, World!")
```
```

**Code Block Features**

- Language specification for syntax highlighting
- Support for many programming languages
- Proper HTML ⟦14⟧ output

### 7. **Math Support**

**Mathematical Expressions**

- LaTeX-compatible math syntax
- Both inline and block math support
- Integration with LaTeX output

```markdown
Inline math: $E = mc^2$

Block math:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 8. **Atributos de imagen y enlace**

**Enlaces e imágenes mejorados**

- Soporte para atributos HTML
- Ancho, alto, texto alternativo y más
- Mejor integración con formatos de salida.

```markdown
[Link text]: url.html title="Link title" class="external"
```

### 9. **Transclusión**

**Inclusión de archivos**

- Incluir otros archivos dentro de los documentos.
- Soporte para inclusiones anidadas
- Resolución automática de ruta

```markdown
{{chapter1.md}}
{{../shared/intro.md}}
```

**Características de transclusión**

- Inclusión de archivos con `{{filename}}`
- Soporte para rutas relativas y absolutas.
- Soporte de transclusión anidada
- Generación de manifiestos para archivos incluidos.

### 10. **Integración de CriticalMarkup**

**Seguimiento de cambios**

- Soporte para la sintaxis CriticMarkup
- Seguimiento de adiciones, eliminaciones y comentarios.
- Funciones de edición colaborativa

```markdown
This is {>>deleted text<<} and this is {++added text++}.

This is a {~~deletion~>replacement~~}.
```

### 11. **Tabla de contenido**

**Generación automática de TOC**

- `{{TOC}}` marcador de posición para la tabla de contenidos
- Estructura jerárquica basada en encabezados.
- Generación de TOC personalizable

```markdown
# Document Title

{{TOC}}

## Section 1
Content here...

## Section 2
More content...
```

### 12. **Abreviaturas**

**Abreviaturas de estilo HTML**

- Definir abreviaturas para la expansión automática.
- Soporte para información sobre herramientas y explicaciones.
- Salida HTML `<abbr>` adecuada

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

## MultiMarkdown v5 frente a otros tipos de Markdown

| Característica | MultiMarkdown v5 | Marca común (GFM) | Descuento | Kramdown | Estándar |
| ---------------- | ---------------- | ---------- | ------------ | -------- | -------- |
| Mesas | Sí | No | Sí | Sí | No |
| Tachado | Sí | No | Sí | No | No |
| Listas de tareas | Sí | No | Sí | No | No |
| Código vallado | Sí | Sí | Sí | Sí | No |
| Matemáticas | Sí | No | No | Sí | No |
| Notas a pie de página | Sí | No | Sí | Sí | No |
| Listas de definiciones | Sí | No | No | Sí | No |
| Abreviaturas | Sí | No | No | Sí | No |
| Listas de atributos | Sí | No | No | Sí | No |
| Extensiones | Sí | No | Limitado | Sí | No |
| Tipografía | Sí | No | Básico | Sí | No |
| Enlaces automáticos | Sí | No | Sí | No | No |
| Referencias cruzadas | Sí | No | No | No | No |
| Citas | Sí | No | No | No | No |
| Transclusión | Sí | No | No | No | No |
| Metadatos | Sí | No | No | No | No |

## Ventajas clave de MultiMarkdown v5

1. **Centrado en documentos**: Diseñado para documentos completos, no solo fragmentos web
2. **Salida multiformato**: Convierta a HTML, LaTeX, PDF, ODF, RTF y Word
3. **Apoyo académico**: citas, notas a pie de página y referencias cruzadas
4. **Funciones profesionales**: metadatos, transclusión y formato avanzado
5. **Multiplataforma**: funciona en cualquier sistema operativo
6. **Preparado para el futuro**: el formato de texto sin formato garantiza compatibilidad a largo plazo
7. **Extensible**: conjunto completo de funciones para requisitos de documentos complejos

## Casos de uso comunes

**Escritura Académica**

- Tesis, disertaciones y trabajos de investigación.
- Gestión de citas y generación de bibliografía.
- Referencias cruzadas y notas a pie de página.

**Documentación técnica**

- Documentación API y guías de usuario.
- Especificaciones técnicas y manuales.
- Documentación de código con resaltado de sintaxis.

**Publicación**

- Libros, artículos e informes.
- Salida multiformato para diferentes plataformas.
- Formato de documentos profesional.

**Gestión de contenidos**

- Sitios web de documentación.
- Bases de conocimiento y wikis.
- Proyectos de escritura colaborativa.

## Mejores prácticas

1. **Usar metadatos**: aprovechar la portada de YAML para obtener información del documento
2. **Estructura con encabezados**: use la jerarquía de encabezados adecuada para la generación de TOC
3. **Aproveche las referencias cruzadas**: utilice enlaces automáticos para una mejor navegación
4. **Organizar con Transclusión**: divida documentos grandes en archivos manejables
5. **Probar salida**: verificar el formato en diferentes formatos de salida
6. **Utilice citas**: implemente prácticas adecuadas de citación académica

## Migración desde otros tipos de Markdown

La mayoría de Markdown estándar funciona con MultiMarkdown sin cambios. Para aprovechar las funciones de MMD:

1. **Agregar metadatos**: incluya el texto frontal de YAML para obtener información del documento
2. **Utilice referencias cruzadas**: reemplace los enlaces manuales con referencias automáticas
3. **Implementar citas**: agregue el formato de cita académica adecuado
4. **Estructura con transclusión**: divida documentos grandes en archivos más pequeños
5. **Tablas de apalancamiento**: use funciones de tabla avanzadas para la presentación de datos

## Recursos

- [Guía del usuario de MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html)
- [Guía de sintaxis de MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html#syntax)
- [Repositorio GitHub MultiMarkdown](https://github.com/fletcher/MultiMarkdown-5)
- [Documentación de MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/)

---

*Esta documentación cubre MultiMarkdown v5.1.0. Para obtener la información más actualizada, consulte siempre la documentación oficial de MultiMarkdown en [fletcher.github.io/MultiMarkdown-5](https://fletcher.github.io/MultiMarkdown-5/).*