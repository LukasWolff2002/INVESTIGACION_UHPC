import sys

import numpy as np
import tensorflow as tf
from tensorflow import keras

# This script requires TensorFlow 2 and Python 3.
if tf.__version__.split('.')[0] != '2':
    raise Exception((f"The script is developed and tested for tensorflow 2. "
                     f"Current version: {tf.__version__}"))

if sys.version_info.major < 3:
    raise Exception((f"The script is developed and tested for Python 3. "
                     f"Current version: {sys.version_info.major}"))

#First lets re-train our original single layer network and see what the prediction is for X = 10.0 and what the learned weights are.

my_layer = keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([my_layer])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

#model.fit(xs, ys, epochs=500)
print('PRIMER MODELO LISTO')

#print(model.predict(np.array([10.0],dtype = float)))


#print('my layer', my_layer.get_weights())

#my layer [array([[1.9966538]], dtype=float32), array([-0.98962575], dtype=float32)]

print(' ')
#Next lets train a 2-layer network and see what its prediction and weights are.

my_layer_1 = keras.layers.Dense(units=2, input_shape=[1])
#ahora hay 2 neuronas, donde solo hay una de input
my_layer_2 = keras.layers.Dense(units=1)
model = tf.keras.Sequential([my_layer_1, my_layer_2])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)
print('SEGUNDO MODELO LISTO')

print(model.predict(np.array([10.0],dtype = float)))

#[[18.999996]]
#lo cual se acerca mas a la solucion real


print('my layer 1',my_layer_1.get_weights())
print('my layer 2',my_layer_2.get_weights())

#my layer 1 [array([[1.141897  , 0.32763204]], dtype=float32), array([-0.4088987 , -0.16436072], dtype=float32)]
#my layer 2 [array([[1.5629493],[0.6570553]], dtype=float32), array([-0.2529167], dtype=float32)]

#Finally we can manually compute the output for our 2-layer network to better understand how it works.

value_to_predict = 10.0

layer1_w1 = (my_layer_1.get_weights()[0][0][0])
layer1_w2 = (my_layer_1.get_weights()[0][0][1])
layer1_b1 = (my_layer_1.get_weights()[1][0])
layer1_b2 = (my_layer_1.get_weights()[1][1])


layer2_w1 = (my_layer_2.get_weights()[0][0])
layer2_w2 = (my_layer_2.get_weights()[0][1])
layer2_b = (my_layer_2.get_weights()[1][0])

neuron1_output = (layer1_w1 * value_to_predict) + layer1_b1
neuron2_output = (layer1_w2 * value_to_predict) + layer1_b2

neuron3_output = (layer2_w1 * neuron1_output) + (layer2_w2 * neuron2_output) + layer2_b

print(neuron3_output)

#en este caso tenemos

# input ----> [neurona]
#                       ----> [neurona]----->output
# input ----> [neurona]   

#por ejemplo para hacer clasificacion de imagenes, queremos una neurona output para cada tipo de clasificacion    
#por lo tanto se enciende la con mayor probabilidad

#ejemplo
#gato [0,1]
#perro [1,0]  