import sys

import numpy as np
import tensorflow as tf
from tensorflow import keras

data = tf.keras.datasets.mnist
(training_images,trainning_labels),(test_images, test_labels)=data.load_data()

training_images = training_images/255.0
test_images = test_images/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),tf.keras.layers.Dense(20, activation=tf.nn.relu),tf.keras.layers.Dense(10,activation=tf.nn.softmax)])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics = ['accuracy'])

model.fit(training_images,trainning_labels,validation_data = (val_images,val_labels),epochs=20)

#Agrego validation data, para para tener mas data de como se ve ejerciendo el training

#puedo agregar una validacion de modelo

model.evaluate(test_images, test_labels)

#y finalmente testeo el modelo
#model.evaluate(val_images, val_labels, epochs = 20)

#classifications = model.predict(val_images)

#print(classifications[0])
#print(val_labels[0])
