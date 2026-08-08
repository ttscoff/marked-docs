<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

La versión Mac App Store (MAS) de Marked se ejecuta en un entorno aislado que restringe ciertas operaciones por razones de seguridad. Esto puede afectar algunas características, particularmente cuando se utilizan procesadores personalizados con scripts o archivos binarios externos.

## Restricciones comunes de la zona de pruebas [common-sandbox-restrictions]

### Ejecutar binarios de comando [run-command-binaries]

El problema más común que encuentran los usuarios es que los binarios externos no se pueden ejecutar directamente en la versión MAS. Esto afecta:

- **Procesadores externos** como Pandoc, Kramdown u otras herramientas de línea de comandos
- **Scripts personalizados** que dependen de archivos binarios externos
- **Utilidades del sistema** a las que no se puede acceder desde el entorno sandbox

### Soluciones alternativas [workarounds]

#### Copiar archivos binarios al paquete de aplicaciones [copying-binaries-to-the-app-bundle]

Si necesita utilizar procesadores externos como Pandoc en la versión MAS, puede copiar el binario en el paquete de la aplicación:

1. Haga clic derecho en Marked.app → **Mostrar contenido del paquete**
2. Vaya a **Contenido/Recursos/**
3. Cree una carpeta `bin` si no existe
4. Copie su binario (por ejemplo, `pandoc`) en esta carpeta `bin`
5. Hazlo ejecutable: `chmod +x` el binario
6. En la acción Ejecutar comando, haga referencia a él como:
   - `YOUR_BINARY_NAME [arguments]`
   - O utilice la ruta completa: `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`

**Nota**: Los scripts con shebangs externos (como los scripts de Python que apuntan a `/opt/homebrew/bin/python`) se ejecutarán automáticamente a través de intérpretes del sistema cuando se copien en el paquete. Es posible que la versión MAS aún tenga problemas para ejecutar archivos binarios que en realidad son scripts de Python o Ruby en lugar de archivos binarios.

**Importante**: Deberá volver a copiar los archivos binarios después de cada actualización de la aplicación, ya que las actualizaciones reemplazan el paquete completo.

#### Uso de scripts integrados [using-embedded-scripts]

En lugar de ejecutar comandos externos, puede utilizar la acción **Ejecutar script integrado** en Reglas personalizadas. Esto le permite escribir scripts directamente en el editor de código de Marked, que puede acceder a los intérpretes del sistema que están disponibles dentro del sandbox.

## Cambiar a la versión sin espacio aislado [crossgrade]

Si necesita usar archivos binarios externos con frecuencia o encuentra otras limitaciones de espacio aislado, es posible que desee cambiar a la versión sin espacio aislado de Marked. La versión sin espacio aislado no tiene tales restricciones y puede ejecutar cualquier herramienta de línea de comandos o script que haya instalado.

### Para usuarios de suscripción [for-subscription-users]

Si tienes una suscripción activa a Mac App Store:

1. **Cancela tu suscripción a MAS** en Configuración del sistema → ID de Apple → Medios y compras → Suscripciones
2. **Descargue la prueba gratuita** desde [https://markedapp.com](https://markedapp.com)
3. **Inicia una suscripción a Paddle** directamente a través de la aplicación o sitio web

La versión Paddle ofrece las mismas funciones sin restricciones de sandboxing.

### Para titulares de desbloqueo permanente [for-permanent-unlock-holders]

Si compró un desbloqueo permanente o una licencia de por vida a través de Mac App Store, [envíe un correo electrónico al desarrollador](mailto:marked@brettterpstra.com?subject=Marked%20License%20Crossgrade&body=Why%20include%20your%20UUID%20%28Help-%3ECopy%20UUID%20in%20Marked%29%20in%20this%20email%20for%20receipt%20verification.) para solicitar una verificación gratuita de por vida. Licencia de pádel.

**Importante**: Para verificar su compra, incluya uno de los siguientes en su correo electrónico:

- Su **identificador de usuario** (UUID): use **Ayuda->Copiar UUID** para copiarlo en su portapapeles y luego péguelo en su correo electrónico.
- Su **ID de transacción** del recibo de la App Store (puede encontrarlo en su historial de compras en la aplicación App Store)

Mac App Store no proporciona su dirección de correo electrónico a los desarrolladores, por lo que verificamos las compras utilizando ID de transacción o identificadores de usuario almacenados en nuestro servidor. Incluir esta información nos ayudará a verificar rápidamente tu compra y generar tu licencia de Paddle gratuita.

### Versión de configuración [setapp-version]

Alternativamente, si tiene una suscripción a Setapp, puede usar la versión Setapp de Marked, que tampoco está protegida y tiene acceso completo a los recursos del sistema.

## Recursos adicionales [additional-resources]

Para obtener más información sobre los procesadores personalizados y sus capacidades, consulte [Procesador personalizado](Custom_Processor.html).