import sys

import numpy as np
import tensorflow as tf
from tensorflow import keras

data = tf.keras.datasets.mnist
(training_images,trainning_labels),(val_images,val_labels)=data.load_data()
#se descarga la data desde tensor flow


#cada pixel va desde 0 a 255, por lo que buscamos normalizarlo, entonces buscamos valores entre 0 y 1
training_images = training_images/255.0
val_images = val_images/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),tf.keras.layers.Dense(20, activation=tf.nn.relu),tf.keras.layers.Dense(10,activation=tf.nn.softmax)])
#como las imagenes son de 28,28 se hace un input de 28,28 para que puedan entrar en la red neuronal
#por lo tanto se aplica el flaten layer, para estirar la imagen
#es decir, se entregan una lista de 784x1

#despues se define una capa de 20 neuronas
#activation=tf.nn.relu lo cual cambia cualquier output que sea menor a 0 a un valor igual a 0
#de esta forma nos aseguramos que el menor valor que de una neurona sea 0

#finalmente se hace una layer de 10 neuronas porque buscamos digitos entre 0 y 9, osea, una neurona por digito
#la funcion softmax ayuda a identificar la neurona con el mayor valor

#por lo tanto tenemos lo siguiente:

#input ----> [20 neuronas] ----> [10 neuronas] ----> output
#donde todas las neuronas estan entrelazadas entre si

#para compilar y entrenar el modelo es bastante similar

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics = ['accuracy'])

#adam hace todo lo del gradiente y error, solo que puede variar el tamaño del gradiente
#tambien hay muchas funciones loss
#en este caso como no es un solo valor, sino una categorizacion, se usa sparse

model.fit(training_images,trainning_labels,epochs=20)

#despues podemos testear el modelo
model.evaluate(val_images, val_labels)

classifications = model.predict(val_images)

print(classifications[0])
print(val_labels[0])

#podemos ver el peso en las distintas neuronas

#link a colab:
#https://colab.research.google.com/github/tinyMLx/colabs/blob/master/2-2-7-ExploringCategorical.ipynb#scrollTo=lqpHrDyp5acs

#se puede ver que le primera layer tiene un peso de 15680 = 28*28*20

#es decir, cada pixel tiene un peso en cada neurona

#luego el segundo layer tiene un peso de 200, ya que son 10 neuronas por 20 datos que provienen uno desde cada neurona anterior