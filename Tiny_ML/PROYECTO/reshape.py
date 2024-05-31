import os
import tensorflow as tf
from PIL import Image
import numpy as np

def load_and_reshape_image(image_path, new_shape):
    # Cargar imagen
    image = tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(image, channels=3)
    # Cambiar el tamaño de la imagen
    image = tf.image.resize(image, new_shape)
    # Normalizar la imagen si es necesario
    image = image / 255.0
    return image.numpy()

def save_image(image_array, output_path):
    # Convertir de un array de TensorFlow a una imagen PIL y guardarla
    image = Image.fromarray((image_array * 255).astype(np.uint8))
    image.save(output_path)

# Directorios
input_directory = 'PROYECTO/FOTOS/TRAIN/MUG'
output_directory = 'PROYECTO/FOTOS/TRAIN/MUG_RESHAPE'

# Asegúrate de que el directorio de salida existe
os.makedirs(output_directory, exist_ok=True)

# Nuevo tamaño deseado para las imágenes
new_shape = (224, 224)  # Ejemplo: 128x128 píxeles

# Procesar todas las imágenes en el directorio de entrada
for filename in os.listdir(input_directory):
    if filename.endswith('.jpg'):  # Asegúrate de ajustar esto según tus formatos de imagen
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)
        
        # Cargar, redimensionar y guardar la imagen
        reshaped_image = load_and_reshape_image(input_path, new_shape)
        save_image(reshaped_image, output_path)

print("Proceso completado. Las imágenes redimensionadas están en:", output_directory)
