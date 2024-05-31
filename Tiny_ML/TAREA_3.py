#Create a CNN to classify Cifar-10
#Learn about Cifar-10 here: https://www.cs.toronto.edu/~kriz/cifar.html

#In class you saw how to build a Convolutional Neural Network that classified Fashion MNIST. 
#Take what you learned to build a CNN that recognizes the 10 classes of CIFAR. It will be a similar network, 
#but there are some key differences you'll need to take into account.

#First, while MNIST were 28x28 monochome images (1 color channel), CIFAR are 32x32 color images (3 color channels).

#Second, MNIST images are simple, containing just the object, centered in the image, with no background. 
#CIFAR ones can have the object with a background -- for example airplanes might have a cloudy sky behind them! 
#As such you should expect your accuracy to be a bit lower.

#We start by setting up the problem for you.


#cifar me da imagenes de 32x32 a color
#tiene 5 carpetas de entrenamiento y una de test, cada una con 10.000 imagenes

import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0

#We then definte some of the model for you but leave most of it for you to fill in!

#A hint: your model may want to learn some high level features and then classify them.

FIRST_LAYER = tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(32, 32, 3))#YOUR CODE HERE#

#ojo es conv2d(32) y no 64. Porque?
HIDDEN_LAYER_TYPE_1 = tf.keras.layers.MaxPooling2D(2, 2)#YOUR CODE HERE#
HIDDEN_LAYER_TYPE_2 = tf.keras.layers.Conv2D(64, (3,3), activation='relu')#YOUR CODE HERE#
HIDDEN_LAYER_TYPE_3 = tf.keras.layers.MaxPooling2D(2,2)#YOUR CODE HERE#
HIDDEN_LAYER_TYPE_4 = tf.keras.layers.Conv2D(64, (3,3), activation='relu')#YOUR CODE HERE#
HIDDEN_LAYER_TYPE_5 = tf.keras.layers.Dense(64, activation='relu')#YOUR CODE HERE#

#aqui es dense de 64 y no 20, porque?
LAST_LAYER = tf.keras.layers.Dense(10)#YOUR CODE HERE#

#porque no lleva el soft max?

model = models.Sequential([
       FIRST_LAYER,
       HIDDEN_LAYER_TYPE_1,
       HIDDEN_LAYER_TYPE_2,
       HIDDEN_LAYER_TYPE_3,
       HIDDEN_LAYER_TYPE_4,
       layers.Flatten(),
       HIDDEN_LAYER_TYPE_5,
       LAST_LAYER,
])

#You then need to define loss function. And you can then train your model. Once training is done you'll see a plot of training 
#and validation accuracy. You'll know you have a reasonable model with a reasonable loss funciton if your final training accuracy ends up in the 70s (or possibly higher).

#A hint: your model may want to learn different categories.

LOSS = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)#YOUR CODE HERE#
#porque no puede ser: 'sparse_categorical_crossentropy'??
NUM_EPOCHS = 20 #You can change this value if you like to experiment with it to get better accuracy

# Compile the model
model.compile(optimizer='sgd',
              loss=LOSS,
              metrics=['accuracy'])

# Fit the model
history = model.fit(train_images, train_labels, epochs=NUM_EPOCHS, 
                    validation_data=(test_images, test_labels))

# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.xlim([0,NUM_EPOCHS])
plt.ylim([0.4,1.0])
plt.show()

#Finally, pick a better optimizer. And re-train your model. You'll know you have a reasonable model with a reasonable 
#loss funciton and optimizer if your final training accuracy ends up in the 80s (or possibly higher).

#A hint: your model may want to learn adaptively.
