import os
import requests
import zipfile
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow_datasets as tfds



# Directorios de entrenamiento y validación
train_duck_dir = 'PROYECTO/FOTOS/TRAIN/DUCK'
train_mug_dir = 'PROYECTO/FOTOS/TRAIN/MUG_RESHAPE'
validation_duck_dir = 'PROYECTO/FOTOS/VALIDATION/DUCK'
validation_mug_dir = 'PROYECTO/FOTOS/VALIDATION/MUG_RESHAPE'

# Listar y mostrar los nombres de los archivos en cada directorio
def list_files(directory):
    try:
        file_names = os.listdir(directory)
        print(file_names[:10])
    except FileNotFoundError:
        print(f"Directory not found: {directory}")

#list_files(train_duck_dir)
#list_files(train_mug_dir)
#list_files(validation_duck_dir)
#list_files(validation_mug_dir)

model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image with 3 bytes color
    # This is the first convolution
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(224, 224, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    # The second convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The third convolution
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fourth convolution
    tf.keras.layers.Conv2D(256, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    # Only 1 output neuron. It will contain a value from 0-1 where 0 for 1 class 
    # ('horses') and 1 for the other ('humans')
    tf.keras.layers.Dense(1, activation='sigmoid')
])

print(model.summary())



# Corrected optimizer initialization
optimizer = RMSprop(learning_rate=0.0001)
model.compile(loss='binary_crossentropy',
              optimizer=optimizer,
              metrics=['acc'])

#Organize your data into Generators

# All images will be augmented according to whichever lines are uncommented 
# below. We can first try without any of the augmentation beyond the rescaling
train_datagen = ImageDataGenerator(
      rescale=1./255,
      #rotation_range=40,
      #width_shift_range=0.2,
      #height_shift_range=0.2,
      #shear_range=0.2,
      #zoom_range=0.2,
      #horizontal_flip=True,
      #fill_mode='nearest'
      )

# Flow training images in batches of 128 using train_datagen generator
train_generator = train_datagen.flow_from_directory(
        'PROYECTO/FOTOS/TRAIN',  # This is the source directory for training images
        target_size=(224, 224),  # All images will be resized to 100x100
        batch_size=32,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

validation_datagen = ImageDataGenerator(rescale=1./255)

validation_generator = validation_datagen.flow_from_directory(
        'PROYECTO/FOTOS/VALIDATION',
        target_size=(224, 224),
        class_mode='binary')

history = model.fit(
      train_generator,
      epochs=100,
      verbose=1,
      validation_data=validation_generator)


#hacer un programa de labeling


