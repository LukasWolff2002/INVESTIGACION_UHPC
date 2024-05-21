# First import the functions we will need
import sys

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

#Utilizando tensor flow
#Como definir un modelo de la forma mas simple posible:

model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])

#Sequential define que es una red secuencial => La clasica que se ve siempre
#Como solo se tiene una entrada, solo se utiliza 1 layer
#Se utiliza .Dense para especificar que es una conexion densa
#units dice cuantas neuronas se van a utilizar
#donde el input shape es 1 de la forma mas simple posible
#de esta forma tenemos algo asi:

# x ----> [neurona] ----> y

model.compile(optimizer='sgd', loss='mean_squared_error')

#se compila el modelo optimizando e indicando el tipo de error que se utilizara
#'sgd' Stocastic Gradient Descent => Tipo de aproximacion a solucion

#ahora especifico x e y

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype = float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype = float)

#para utilizar tensor flow, los arreglos deben ser array y no listas

#para que el modelo busque la relacion se hace el fiting;

model.fit(xs,ys,epochs = 500)

#500 significa que se hacen 500 iteraciones para llegar al minimo error posible
#finalmente se puede predecir que pasara con un valor utilizando el modelo obtenido

print(model.predict(np.array([10.0], dtype = float)))

#La ecuacion es 2x-1, ahora bien


#apuntes

# Output = (Weight * Input) + Bias
#So, for learning the linear relationship between our Xs and Ys, this maps perfectly, 
#where we want the weight to be learned as ‘2’, and the bias as ‘-1’. In the code you saw this happening.

#When multiple neurons work together in layers, the learned weights and biases across these layers can then have 
#the effect of letting the neural network learn more complex patterns. You’ll learn more about how this works later in the course.

#In your first Neural Network you saw neurons that were densely connected to each other, so you saw the Dense layer type. 
#As well as neurons like this, there are also additional layer types in TensorFlow that you’ll encounter. Here’s just a few of them:

#Convolutional layers contain filters that can be used to transform data. The values of these filters will be learned in the same way 
#as the parameters in the Dense neuron you saw here. Thus, a network containing them can learn how to transform data effectively. 
#This is especially useful in Computer Vision, which you’ll see later in this course. We’ll even use these convolutional layers that are 
#typically used for vision models to do speech detection! Are you wondering how or why? Stay tuned!

#Recurrent layers learn about the relationships between pieces of data in a sequence. There are many types of recurrent layer,
#with a popular one called LSTM (Long, Short Term Memory), being particularly effective. Recurrent layers are useful for predicting 
#sequence data (like the weather), or understanding text.