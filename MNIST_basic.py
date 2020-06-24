"""
This script demonstrates the basic building of a neural network
that can detect handwritten images with >=97 % of accuracy. This
code uses Keras deep learning library and TensorFlow as its backened.
We will use the MNIST dataset which comes inbuilt with keras datasets.

The neural network that we constructed has input layer of size 784
and hidden layer of size 512 and output layer of size 10.
"""

# STEP: 1 IMPORTING THE LIBRARIES
import numpy as np   
import os 
import pandas as pd
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras import models, layers
from keras.utils import to_categorical

cwd = os.getcwd()

# STEP:2 GET THE TRAIN DATA AND TEST DATA
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# STEP 3: RESHAPING THE DATA AND SCALING
train_images = train_images.reshape((60000, 784))
test_images = test_images.reshape((10000, 784))

train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

# STEP 4: CHANGING LABELS TO CATEGORIES
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# STEP 5: BUILD THE NETWORK
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape = (784, )))
network.add(layers.Dense(10, activation='softmax'))

# STEP 6: COMPILE THE NETWORK
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# STEP 7: FIT THE NETWORK
network.fit(train_images, train_labels, batch_size=128, epochs=10, verbose=0)

# STEP 8: EVALUATE THE NETWORKS
train_loss, train_acc = network.evaluate(test_images, test_labels)
print("The accuracy achieved: ", train_acc)

# STEP 9: SAVING THE MODEL AS A H5
network.save(cwd + "/trained_network.h5")
print("Saved to the folder in current working directory")

