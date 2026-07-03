<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Borradores][borradores] en Mac puede reflejar el borrador activo en Marcado usando **Vista previa de transmisión marcada**, el mismo canal basado en el portapapeles descrito en [Vista previa de transmisión](Streaming_Preview.html). También puedes enviar el borrador actual una vez con una **acción** de la comunidad (no habrá actualizaciones en vivo hasta que lo ejecutes nuevamente).

## Vista previa de transmisión (Borradores para Mac)

1. En Marcado, elija {% appmenu File, New, Streaming Preview %} para que esté lista una ventana de vista previa de la transmisión.
2. En **Borradores para Mac**, abra **Configuración** y habilite **Habilitar compatibilidad con vista previa de transmisión de aplicaciones marcadas**.
3. Utilice **Abrir Marcado** si Borradores lo ofrece para presentar Marcado, luego edítelo en Borradores; la vista previa se actualiza a medida que cambia el borrador.

![][preferencias de borrador]

Cuando esta opción está activada, Drafts lleva Markdown a Marked a través de la integración de Marked expone para vistas previas de transmisión (en lugar de depender de ver un archivo en el disco).

### Obtener marcado

Si aparece **Obtener aplicación Marked** en la hoja de configuración de Borradores, úsela cuando Marked aún no esté instalado.

## Vista previa en acción marcada (actualización manual)

Instale la acción comunitaria [**Vista previa en Marcado**](https://actions.getdrafts.com/a/11f) desde el Directorio de Borradores. Envía el **borrador de texto actual** a Marcado usando una URL `x-marked://preview?text=…` (Borradores sustituye el contenido del borrador). **Los contenidos no se actualizan en vivo**: ejecuta la acción nuevamente cuando quieras que Marcado coincida con el borrador.

Este enfoque es útil para comprobaciones ocasionales, mientras que la **vista previa de transmisión** es adecuada para sesiones de escritura continua.

Drafts también se ejecuta en iPhone y iPad; La integración de vista previa de transmisión documentada aquí se aplica a **Borradores para Mac** con Marcado en la misma Mac.

[draftsprefs]: images/Drafts_streaming_preview_preference.png width=842px height=182px class=center

[drafts]: https://getdrafts.com/