![INFOMRE](INFORME/INFORME.pdf)

# Manejo de Buffers con Cámaras Basler y Pylon en Python

Este documento proporciona una guía detallada sobre cómo configurar y gestionar los buffers para la captura de imágenes con cámaras Basler utilizando la biblioteca Pylon en Python.

## Configuración del Buffer

El manejo adecuado del buffer es crucial para asegurar una captura de imágenes eficiente y continua, especialmente en aplicaciones de alta velocidad.

### Buffer basico

Para evitar la pérdida de imágenes y manejar la captura rápida, puedes incrementar el número de buffers que la cámara utiliza:

```python
camera.MaxNumBuffer = 50
```

Es importante gestionar los buffers de manera eficiente durante la captura de imágenes para evitar el llenado excesivo y garantizar un procesamiento fluido:

```python
while camera.IsGrabbing():
    result = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
    if result.GrabSucceeded():
        # Procesamiento de la imagen capturada
        image = result.Array
        # Aquí se podría realizar alguna operación con la imagen
    result.Release()
```

Liberar cada buffer con result.Release() después de su uso es esencial para mantener la disponibilidad de buffers para nuevas imágenes.

### Si quiero almacenar X imagenes en el buffer
```python
camera.MaxNumBuffer = 10  # Permite almacenar hasta 10 imágenes en el buffer.

camera.OutputQueueSize = 10  # Configura el tamaño de la cola de salida para almacenar hasta 10 imágenes.
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

# Asegúrate de que la cámara esté configurada para grabar
camera.StartGrabbingMax(100)  # Asume que quieres capturar un máximo de 100 imágenes en total.

while camera.IsGrabbing():
    result = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
    
    if result.GrabSucceeded():
        # Procesa la imagen aquí
        image = result.Array
        print("Imagen procesada")

    # Libera el buffer después de procesar cada conjunto de X imágenes
    if result.BlockID % 10 == 0:  # Asume que X es 10
        result.Release()

# Detener la captura después de completar el bucle
camera.StopGrabbing()
```
Monitorización del buffer: Implementa alguna forma de monitorización para asegurarte de que los buffers no se llenen completamente sin ser procesados, lo cual podría causar la pérdida de imágenes nuevas.







