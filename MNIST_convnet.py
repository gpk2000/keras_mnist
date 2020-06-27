""" 
This script is an extension of the basic neural network used in
MNIST_basic.py file. Here we use convolution networks to improve
our accuracy to 99 %.
"""

# STEP 1: IMPORTING THE LIBRARIES
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import models
from keras import layers
from keras.datasets import mnist
from keras.utils import to_categorical

cwd = os.getcwd()

# STEP 2: GET THE TRAIN DATA AND TEST DATA
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# STEP 3: RESHAPING THE DATA AND FEATURE SCALING
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))

train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# STEP 4: BUILDING THE MODEL
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# STEP 5: COMPILING THE MODEL
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# STEP 6: FIT THE MODEl
model.fit(train_images, train_labels, batch_size=64, epochs=5)

# STEP 7: EVALUATE THE MODEL
test_loss, test_acc = model.evaluate(test_images, test_labels) 

print('The accuracy acquired : ', test_acc)

model.save(cwd + "cnetmodel.h5")
print("Saved to the folder in current working directory")
