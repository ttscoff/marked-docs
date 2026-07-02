<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Curio][curio] es una aplicación visual de lluvia de ideas y toma de notas que puede transmitir el elemento que estás editando al canal **vista previa de transmisión** de Marked.

## Transmisión seleccionada para marcar

1. En Marcado, elija {% appmenu File, New, Streaming Preview %} para que esté lista una ventana de vista previa de la transmisión.
2. En Curio, active **Ver → Transmisión seleccionada para marcar**.

Cuando haces doble clic para editar una figura, nota, lista u otro elemento en Curio, su Markdown fluye a la vista previa de transmisión y se actualiza a medida que escribes.

Actualizaciones marcadas casi en tiempo real, siguiendo el mismo `mkStreamingPreview` contrato de portapapeles que otras aplicaciones integradas; consulte [Detalles técnicos](Streaming_Preview.html#developers) en [Vista previa de transmisión](Streaming_Preview.html).

Si las vistas previas dejan de actualizarse, confirme que haya una ventana de vista previa de transmisión abierta en Marcado y cambie **Transmisión seleccionada a Marcada** una vez en Curio.

[curio]: https://www.zengobi.com/products/curio/