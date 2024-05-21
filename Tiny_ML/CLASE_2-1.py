#para entender porque model(10) no da exactamente 19, podemos emular la neurona

# First import the functions we will need
import sys

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

class Model(object):
    def __init__(self):
        self.w = tf.Variable(10.0)
        self.b = tf.Variable(10.0)

    def __call__(self,x):
        return (self.w*x + self.b)
    
def loss(predicted_y,target_y):
    return tf.reduce_mean(tf.square(predicted_y-target_y))

def train(model,xs,ys,learning_rate):
    with tf.GradientTape() as t:
        current_loss = loss(model(xs),ys) #comparamos los resultados del modelo con los reales

    dw,db = t.gradient(current_loss,[model.w,model.b]) #podemos obtener los gradientes, reasignando dw y db
    model.w.assign_sub(learning_rate*dw)
    model.b.assign_sub(learning_rate*db)
    
    return current_loss
    
model = Model()
xs = [-1, 0, 1, 2, 3, 4]
ys = [-3, -1, 1, 3, 5, 7]
    
print(model(xs))

#donde el resultado es:
#[ 0. 10. 20. 30. 40. 50.]
#por lo cual estamos muy lejos de la realidad

#entonces hay que repetir el proceso
#podemos medir la precision con una funcion loss

#ahora, tambien podemos hacer una funcion de entrenamiento
model = Model()
list_w, list_b = [], []
epochs = range(50)
losses = []
for epoch in epochs:
    list_w.append(model.w.numpy())
    list_b.append(model.b.numpy())
    current_loss = train(model,xs,ys,learning_rate=0.1)
    losses.append(current_loss)
    print('Epoch %2d: w=%1.2f b=%1.2f, loss=%2.5f' %
        (epoch, list_w[-1], list_b[-1], current_loss))
    
    # Plot the w-values and b-values for each training Epoch against the true values
TRUE_w = 2.0
TRUE_b = -1.0
plt.plot(epochs, list_w, 'r', epochs, list_b, 'b')
plt.plot([TRUE_w] * len(epochs), 'r--', [TRUE_b] * len(epochs), 'b--')
plt.legend(['w', 'b', 'True w', 'True b'])
plt.show()

print(model.predict([10.0]))