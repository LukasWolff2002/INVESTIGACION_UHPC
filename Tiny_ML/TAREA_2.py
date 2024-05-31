# Load libraries
import sys
import tensorflow as tf

# This script requires TensorFlow 2 and Python 3.
if sys.version_info.major < 3:
    raise Exception((f"The script is developed and tested for Python 3. "
                     f"Current version: {sys.version_info.major}"))

if tf.__version__.split('.')[0] != '2':
    raise Exception((f"The script is developed and tested for tensorflow 2. "
                     f"Current version: {tf.__version__}"))

# Load in fashion MNIST
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# Define the base model
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)), 
                                    tf.keras.layers.Dense(512, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

training_images  = training_images/255.0 #YOUR CODE HERE
test_images = test_images/255.0 #YOUR CODE HERE#

# compile the model
model.compile(optimizer = tf.keras.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

# fit the model to the training data
model.fit(training_images, training_labels, epochs=5)

# test the model on the test data
model.evaluate(test_images, test_labels)


#Once it's done training -- you should see an accuracy value at the end of the final epoch. 
#It might look something like 0.8648. This tells you that your neural network is about 86% accurate 
#in classifying the training data. I.E., it figured out a pattern match between the image and the labels 
#that worked 86% of the time. But how would it work with unseen data? That's why we have the test images. 
#We can call model.evaluate, and pass in the two sets, and it will report back the loss for each. 
#This should reach about .8747 or thereabouts, showing about 87% accuracy. Not Bad!

#But what did it actually learn? If we inference on the model using model.
#predict we get out the following list of values. What does it represent?

#A hint: trying running print(test_labels[0])

classifications = model.predict(test_images)
print(classifications[0])
