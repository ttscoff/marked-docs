<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## ¿Qué es el descuento?

Markdown es un lenguaje de marcado liviano que le permite escribir utilizando un formato de texto plano fácil de leer y escribir y luego convertirlo a HTML estructuralmente válido. El objetivo primordial del diseño de la sintaxis de formato de Markdown es hacerla lo más legible posible.

## Sintaxis básica

### Encabezados

Cree encabezados usando símbolos hash (`#`). El número de hashes determina el nivel del encabezado:

```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

### Énfasis

**Texto en negrita** con asteriscos dobles o guiones bajos dobles:

```markdown
**Bold text**
__Bold text__
```

*Texto en cursiva* usando asteriscos simples o guiones bajos simples:

```markdown
*Italic text*
_Italic text_
```

### Listas

**Listas desordenadas** que utilizan asteriscos, signos más o guiones:

```markdown
* Item 1
* Item 2
* Item 3

+ Item 1
+ Item 2
+ Item 3

- Item 1
- Item 2
- Item 3
```

**Listas ordenadas** usando números seguidos de puntos:

```markdown
1. First item
2. Second item
3. Third item
```

### Enlaces

**Enlaces en línea** con el texto entre corchetes y la URL entre paréntesis:

```markdown
[Link text](http://example.com)
```

**Enlaces de referencia** con el texto entre corchetes y una referencia entre corchetes:

```markdown
[Link text][reference]

[reference]: http://example.com "Optional title"
```

**Enlaces automáticos** colocando las URL entre corchetes angulares:

```markdown
<http://example.com>
<user@example.com>
```

### Imágenes

Las imágenes utilizan una sintaxis similar a la de los enlaces pero con un signo de exclamación al principio:

```markdown
![Alt text](http://example.com/image.jpg)
![Alt text][image-reference]

[image-reference]: http://example.com/image.jpg "Optional title"
```

### Citas en bloque

Cree citas en bloque usando el símbolo mayor que (`>`) al comienzo de cada línea:

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> You can have multiple paragraphs in a blockquote.
```

### Código

**Código en línea** usando comillas invertidas:

```markdown
Use ⟦4⟧ in your text.
```

**Bloques de código** sangrando con cuatro espacios o una tabulación:

```markdown
    This is a code block.
    It preserves formatting and spacing.
    Multiple lines are supported.
```

### Reglas horizontales

Cree reglas horizontales utilizando tres o más guiones, asteriscos o guiones bajos:

```markdown
---

***

___
```

### Saltos de línea

**Saltos de línea estrictos** al terminar una línea con dos o más espacios:

```markdown
This line ends with two spaces.
This creates a hard line break.
```

**Saltos de línea suaves** simplemente presionando Enter (crea un espacio en HTML):

```markdown
This line
continues on the next line with a space.
```

### Personajes que escapan

Escapar de caracteres especiales usando barras invertidas:

```markdown
\*This text is not italic\*
\[This is not a link\]
```

Personajes comunes de los que se puede escapar:
- `\` barra invertida
- `` ` `` acento grave
- `*` asterisco
- `_` guión bajo
- `{}` llaves
- `[]` corchetes
- `()` paréntesis
- `#` picadillo
- `+` más
- `-` menos
- `.` punto
- `!` signo de exclamación

## Mejores prácticas

1. **Utilice líneas en blanco** para separar diferentes elementos y mejorar la legibilidad.
2. **Sea coherente** con sus opciones de formato (por ejemplo, utilice `*` o `_` para enfatizar)
3. **Manténgalo simple**: Markdown está diseñado para ser legible como texto sin formato
4. **Pruebe su resultado** para asegurarse de que se muestre como se esperaba
5. **Utilice texto de enlace significativo** en lugar de frases genéricas como "haga clic aquí"

## Patrones comunes

### Listas anidadas

```markdown
1. First item
   - Nested item
   - Another nested item
2. Second item
   - More nested content
```

### Listas con párrafos

```markdown
1. First item

   This is a paragraph under the first item.

2. Second item

   This is a paragraph under the second item.
```

### Citas en bloque con otros elementos

```markdown
> This is a blockquote with **bold text** and *italic text*.
>
> - It can contain lists
> - And other Markdown elements
>
> > Nested blockquotes are also possible.
```

## Resumen

Markdown proporciona una forma sencilla y legible de formatear texto que se puede convertir fácilmente a HTML. La clave es mantenerlo simple y legible mientras se utilizan los elementos básicos de sintaxis de manera consistente. Con la práctica, descubrirá que Markdown se convierte en algo natural y facilita mucho la redacción de contenido estructurado.

---

*Este tutorial cubre la sintaxis principal de Markdown tal como se define en la especificación original. Para funciones más avanzadas, consulte la documentación de procesadores Markdown específicos como CommonMark (GFM), MultiMarkdown o GitHub Flavored Markdown.*