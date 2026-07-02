<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Los números importan tanto como las palabras.

## Vista previa de fórmulas con MathJax

![][1]

   [1]: imágenes/mathjax.jpg @2x ancho=713px alto=512px clase=centro

Al activar MathJax en {% prefspane Style %}, los scripts y CSS necesarios se incluirán en la vista previa. Luego, se puede utilizar la sintaxis matemática de MultiMarkdown en su documento de Markdown y se mostrarán los resultados.

Ejemplo de sintaxis de MMD MathJax:

    \\\\[ {e}^{i\pi } 1=0 \\\\]

Si elige incluir MathJax en un archivo HTML exportado, se utilizará un enlace CDN en lugar del código MathJax incrustado. Esto requiere una conexión a Internet para ver el MathML renderizado.

## Fuente de MathJax: local frente a CDN

Cuando MathJax está habilitado, Marked puede cargarlo desde:

- **Local**: una copia de MathJax v3 incluida dentro de la aplicación (se carga más rápido, funciona sin conexión).
- **CDN**: el CDN oficial de MathJax v3 (siempre actualizado, sin impacto en el paquete de aplicaciones).

La ventana emergente **MathJax Source** en {% prefspane Style %} te permite elegir:

- **Local**: utiliza el componente ES5 `tex-chtml.js` del paquete de aplicaciones.
- **CDN** – carga el mismo componente desde la CDN. Esto requiere una conexión a Internet.

Los archivos HTML exportados siempre hacen referencia a MathJax desde una CDN, independientemente de la fuente de la vista previa, por lo que siguen siendo pequeños y autónomos.

## Numeración de ecuaciones

Puede habilitar la numeración de ecuaciones en {% prefspane Style %}. Esto funciona tanto con MathJax como con KaTeX, pero se implementa de manera diferente internamente. Para MathJax v3, Marked asigna su configuración a la configuración adecuada de MathJax para que:

- Las "ecuaciones numéricas" controlan si se muestran números.
- La opción "lateral" controla si los números aparecen a la izquierda o a la derecha.
- La opción “Solo AMS” restringe la numeración a ecuaciones estilo AMS.

Estas opciones corresponden a las configuraciones `tex.tags` y `tex.tagSide` de MathJax bajo el capó.

## Paquetes adicionales

MathJax v3 es modular. Marked siempre habilita los paquetes principales de TeX/AMS y, opcionalmente, puedes activar paquetes adicionales en {% prefspane Style %}:

- **Física** (`physics`): notación física y comodidades.
- **Química** (`mhchem`) – ecuaciones químicas.
- **Bra–ket** (`braket`) – Notación bra–ket de Dirac.
- **Símbolos en negrita** (`boldsymbol`): símbolos matemáticos en negrita.

Haga clic en **Paquetes adicionales...** para abrir una pequeña lista de verificación donde puede activar o desactivar estos paquetes. Los cambios entrarán en vigor la próxima vez que Marked muestre matemáticas en la vista previa.

## Configuración avanzada de MathJax

Puede aplicar configuraciones personalizadas adicionales además de los valores predeterminados de Marked agregando un objeto JSON válido en el campo **Configuración avanzada**. Este campo se fusiona con el objeto de configuración de MathJax v3 (`window.MathJax`) antes de que se cargue MathJax. Puede contener [cualquier opción admitida por MathJax v3](https://docs.mathjax.org/en/latest/options/), por ejemplo:

    {
        "tex": {
            "inlineMath": [["$","$"],["\\\\(","\\\\)"]],
            "displayMath": [["$$","$$"],["\\\\[","\\\\]"]],
            "macros": {
                "tr": "{\\\\scriptscriptstyle\\\\mathrm{T}}"
            },
            "paquetes": { "[+]": ["física"] }
        }
    }

Este ejemplo ajusta los delimitadores TeX, agrega una macro `\tr` y habilita el paquete `physics` además del conjunto predeterminado. Con esta configuración, todo lo siguiente se representa correctamente:

    Fórmula en línea que usa paréntesis, \\\\({x}^{2} {y}^{2}=1\\\\), o con signos de dólar, ${x}^{2} {y}^{2}=1$.

    Mostrar con corchetes escapados:

    \\\\[ {e}^{i\pi } 333=0 \label{testme} \\\\]

    O con doble signo de dólar:

    $${x}_{1,2}=\\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a}$$

![][2]

   [2]: imágenes/mathjax2.jpg @2x ancho=837px alto=260px clase=centro

La configuración adicional amplía el objeto existente, por lo que solo se anularán las propiedades especificadas. Las opciones no especificadas permanecerán como predeterminadas para el ajuste preestablecido actual.

Tenga en cuenta que al utilizar el procesador MultiMarkdown con delimitadores no estándar, los caracteres dentro de la expresión se analizan, por lo que símbolos como `*` y `^` provocarán cambios tipográficos que dañarán el procesador MathJax. La mejor solución en estos casos es utilizar el procesador de descuentos en [Configuración del procesador](x-marked-3://pref/processor).

Marked realiza un poco de magia cuando MathJax o KaTeX están habilitados, convirtiendo la sintaxis matemática para garantizar que sea lo más compatible posible con el procesador actual (MultiMarkdown o Discount). Esto debería ser excelente en todas las circunstancias, pero si encuentra que causa problemas, [comuníquese con el soporte técnico](https://support.markedapp.com/questions/add).


## KaTeX

[katex]: https://katex.org/

[KaTeX][] está disponible como alternativa a MathJax. Es más liviano y, por lo tanto, más rápido de cargar, lo que puede resultar excelente en documentos con una gran cantidad de fórmulas. Sin embargo, no tiene tantas funciones y es posible que algunas ecuaciones que funcionan con MathJax (o LaTeX) no sean compatibles.

## Numeración automática de ecuaciones [numeración]

Puede habilitar la numeración de ecuaciones en {% prefspane Style %}. Esto funciona tanto con MathJax como con KaTeX. Puede seleccionar si los números aparecen en el lado izquierdo o derecho de la ecuación.

### En MatemáticasJax

En MathJax, esto usa la configuración:

    {
      TeX: { números de ecuación: { número automático: "todos" } }
    }

Si solo desea numerar ecuaciones AMS, seleccione "Solo AMS" a la derecha del menú desplegable "lateral".

### En KaTeX

KaTeX no ofrece numeración de ecuaciones. Para simular esto en Marked, se utiliza CSS y todas las ecuaciones de visualización están numeradas.

## Problemas de exportación

Los formatos de texto enriquecido no manejarán ecuaciones (ya sea de MathJax o KaTeX). Estarán ocultos en el documento de salida, ya que intentar incluir fuentes especiales resulta en un desastre mayor de lo que imaginas... Esto es algo que espero solucionar en algún momento, pero es una deficiencia por ahora.