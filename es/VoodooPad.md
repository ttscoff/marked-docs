<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[VoodooPad][vp] agrupa cada página en un único archivo de base de datos. Arrastre el `.vpdoc` a Marcado para obtener una vista previa de la página que se encuentra actualmente en primer plano en VoodooPad; use {% kbd cmd S %} en VoodooPad siempre que necesite Marked para recargar desde el disco.

Marked observa el documento en el disco e intercambia la vista previa cuando cambias de página dentro de VoodooPad.

## Imágenes incrustadas [embedded-images]

Cuando haces referencia a imágenes con Markdown o HTML y el binario se encuentra **dentro** de la base de datos de VoodooPad, Marked puede extraerlo para la vista previa. Las imágenes que son solo **alias** (archivos arrastrados por referencia) no se almacenan en el paquete; señale aquellas con rutas absolutas o rutas relativas al `.vpdoc` en el disco para que Marked pueda resolverlas.

[vp]: https://www.voodoopad.com/