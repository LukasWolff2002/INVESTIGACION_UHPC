#podemos pasar de algo asi:

#import tensorflow as tf
#mnist = tf.keras.datasets.fashion_mnist
#(training_images, training_labels), (val_images, val_labels) = mnist.load_data()
#training_images=training_images / 255.0
#val_images=val_images / 255.0
#model = tf.keras.models.Sequential([
#  tf.keras.layers.Flatten(),
#  tf.keras.layers.Dense(20, activation=tf.nn.relu),
#  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
#])
#model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#model.fit(training_images, training_labels, validation_data=(val_images, val_labels), epochs=20)

#a algo asi: import tensorflow as tf

#link a colab;
#https://colab.research.google.com/github/tinyMLx/colabs/blob/master/2-3-5-FashionMNISTConvolutions.ipynb#scrollTo=uRLfZ0jt-fQI

import tensorflow as tf
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (val_images, val_labels) = mnist.load_data()
training_images=training_images.reshape(60000, 28, 28, 1)
training_images=training_images / 255.0
val_images=val_images.reshape(10000, 28, 28, 1)
val_images=val_images/255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28, 28, 1)),
  #es importante esta linea de codigo, donde se especifican las dimenciones de la imagen. Como es blanco y negro solo tiene un canal y por eso el 1, de 
  #forma contraria, si es a color hay 3 canales, entonces seria un 3

  #ademas se especifica una convolucion 2D, es 2D porque tenemos ancho y alto
  #el numero 64 quiere decir que se aplican 64 filtros
  #3,3 indica el tamaño del filtro
  tf.keras.layers.MaxPooling2D(2, 2),
  #se aplica el pooling, donde usamos max ya que tomamos el valor mas alto. existe medio min etc
  #como es 2.2 se elige un pixel cada un arreglo de 2x2
  tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),
  tf.keras.layers.Flatten(),
  #se aplica el flaten
  tf.keras.layers.Dense(20, activation='relu'),
  #hay 20 neuronas intermedias al igual que antes
  tf.keras.layers.Dense(10, activation='softmax')
  #hay 10 neuronas de output como antes
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
model.fit(training_images, training_labels, validation_data=(val_images, val_labels), epochs=20)

#It's likely gone up to about 97% on the training data and 91% on the validation data.

#That's significant, and a step in the right direction!

#Try running it for more epochs -- say about 100, and explore the results! But while the results 
#might seem really good, the validation results may actually go down, due to something called 'overfitting' which will be discussed later.

#(In a nutshell, 'overfitting' occurs when the network learns the data from the training set really well, but it's too 
#specialised to only that data, and as a result is less effective at seeing other data. For example, if all your 
#life you only saw red shoes, then when you see a red shoe you would be very good at identifying it, but blue suade shoes might confuse you...
#and you know you should never mess with my blue suede shoes.)

#Then, look at the code again, and see, step by step how the Convolutions were built:

#Step 1 is to gather the data. You'll notice that there's a bit of a change here in that the training data needed to be reshaped. 
#That's because the first convolution expects a single tensor containing everything, so instead of 60,000 28x28x1 items in a list, 
#we have a single 4D list that is 60,000x28x28x1, and the same for the validation images. If you don't do this, you'll get an error 
#when training as the Convolutions do not recognize the shape.

