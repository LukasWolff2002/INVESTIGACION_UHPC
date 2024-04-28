![INFOMRE](INFORME/INFORME.pdf)

# Ideas

Este documento proporciona una guía detallada sobre cómo configurar y gestionar los buffers para la captura de imágenes con cámaras Basler utilizando la biblioteca Pylon en Python.

## Buffer

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

## Crear una lista con tamaño predefinido

Calcular el número aproximado de enteros que puedes almacenar en 1 MB:Si cada entero usa aproximadamente 28 bytes, y la lista vacía usa 64 bytes:

```python
bytes_per_int = 28
base_list_size = 64
target_memory_use = 1048576  # 1 MB en bytes

# Calcular cuántos enteros podrías almacenar
num_ints = (target_memory_use - base_list_size) // bytes_per_int

lista = [0] * num_ints
```

## Listas vinculadas

cceso a elementos: El acceso a un elemento en listas vinculadas es generalmente más lento. Las listas de Python permiten el acceso directo a cualquier índice en tiempo constante 𝑂(1), mientras que las listas vinculadas requieren un recorrido secuencial desde el inicio (o el final, en el caso de listas doblemente vinculadas) hasta el nodo deseado, lo que resulta en un tiempo O(n) en el peor caso.

Inserción y eliminación de elementos: Aquí es donde las listas vinculadas pueden superar a las listas de Python, especialmente si estás insertando o eliminando elementos cerca del inicio de la lista o en posiciones que ya conoces (sin necesidad de buscar). Las listas vinculadas pueden realizar estas operaciones en O(1) si tienes una referencia directa al nodo de interés, mientras que las listas de Python requieren O(n) debido a la necesidad de desplazar elementos para mantener el orden.










