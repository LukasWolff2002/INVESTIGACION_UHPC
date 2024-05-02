# Sincronizacion Camaras Basler

## Tarea 1

En primer lugar, se planteo el objetivo de sincronizar las camaras para poder hacer una grabacion tridimencional. De este modo, las camaras debian sacar
fotos al mismo instante, para lo cual se desarrollo un codigo python por medio de la libreria pypylon.

[CODIGO SINCRONIZACION CAMARAS](SINCRONIZACION_CAMARAS.py)

El proceso detallado se encuentra en el siguiente informe:

[INFORME SINCRONIZACION CAMARAS](INFORME_1/INFORME_1.pdf)

## Tarea 2

Posterior a sincronizar las camaras, se observo que el codigo permitia sacar como maximo 20 fotos. En base a lo anterior, se optimizo el codigo utilizando listas concatenadas y el buffer de cada camara.

[CODIGO MULTIPLES DISPAROS SINCRONIZADOS](MULTIPLES_DISPAROS_SINCRONIZADOS.py)

El proceso detallado se encuentra en el siguiente informe:

[INFORME MULTIPLES DISPAROS SINCRONIZADOS](INFORME_2/INFORME_2.pdf)

## Calibrar Camras

Para poder calibrar las camaras en terminos de posicion y enfoque se utiliza el siguiente codigo:

[CALIBRAR CAMARAS](CALIBRAR_CAMARAS.py)

#nota: aun no se termina de optimizar, ya que es un codigo reciclado, ademas, una opcion es implementarlo en el codigo final.

