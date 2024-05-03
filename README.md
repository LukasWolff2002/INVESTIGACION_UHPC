# Sincronización Cámaras Basler

## Tarea 1

En primer lugar, se planteó el objetivo de sincronizar las cámaras para poder hacer una grabación tridimensional. De este modo, las cámaras debían sacar
fotos al mismo instante, para lo cual se desarrolló un código Python por medio de la librería Pypylon.

[CODIGO SINCRONIZACION CAMARAS](SINCRONIZACION_CAMARAS.py)

El proceso detallado se encuentra en el siguiente informe:

[INFORME SINCRONIZACION CAMARAS](INFORME_1/INFORME_1.pdf)

## Tarea 2

Posterior a sincronizar las cámaras, se observó que el código permitía sacar como máximo 20 fotos. En base a lo anterior, se optimizó el código utilizando listas concatenadas y el buffer de cada cámara.

[CODIGO MULTIPLES DISPAROS SINCRONIZADOS](MULTIPLES_DISPAROS_SINCRONIZADOS.py)

El proceso detallado se encuentra en el siguiente informe:

[INFORME MULTIPLES DISPAROS SINCRONIZADOS](INFORME_2/INFORME_2.pdf)

## Calibrar Cámaras

Para poder calibrar las cámaras en términos de posición y enfoque se utiliza el siguiente código:

[CALIBRAR CAMARAS](CALIBRAR_CAMARAS.py)

# Nota: Aún no se termina de optimizar, ya que es un código reciclado, además, una opción es implementarlo en el código final.


