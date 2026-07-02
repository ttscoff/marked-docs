<!-- MT-DRAFT: machine translation; human review required -->

# Permisos de procesador personalizados en la versión MAS

Debido a restricciones de espacio aislado, la versión de Marked para Mac App Store no puede ejecutar ciertos tipos de herramientas binarias como procesadores personalizados. Si se encuentra con esta limitación, hay algunos pasos que puede probar.

1. Asegúrese de haber ingresado a **Configuración marcada** ({% kbd cmd , %}), en el panel **Avanzado** y haber hecho clic en "Actualizar permisos". Esto intentará otorgar acceso a Marked a toda su unidad predeterminada, solucionando problemas con scripts y utilidades que necesitan acceder a carpetas temporales y ubicaciones no predeterminadas.
2. Intente utilizar un script. Haga referencia a la utilidad que desea ejecutar (multimarkdown, kramdown, etc.) en un script de shell. Puede ser un script bash, Ruby, Perl o Python. Luego configure el procesador en Configuración avanzada en el shell o ejecutable relacionado, y los parámetros en la ubicación del script. Por ejemplo, puedo crear un script bash guardado en ~/scripts/mmd_wrapper.sh:

        #!/bin/bash
        gato | /usr/local/bin/multimarkdown

    Luego, hazlo ejecutable (`chmod a+x ~/scripts/mmd_wrapper.sh`) y configura mis ajustes de Procesador personalizado:

        Procesador: /bin/bash
        Argumentos: /Users/me/scripts/mmd_wrapper.sh
3. Algunos ejecutables (especialmente Pandoc) simplemente no funcionan en el sandboxing. En este caso, comuníquese conmigo a través de la ventana de error que aparece durante la ejecución para recibir una licencia cruzada para la versión directa.