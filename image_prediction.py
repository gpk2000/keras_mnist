"""
This script is for predicting the handwritten digits of our own
handwritten image which is produced using gimp or any other software
the only restriction is that you create the image in the resolution
of 28 * 28 since our model is trained for such type
"""

# STEP 1: IMPORTING THE LIBRARIES 
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# STEP 2: LOAD THE TRAINED MODEL
network = load_model('trained_network.h5')

# STEP 3: IMAGE OPENING AND CHANGES
img = Image.open('img4.png')
data = list(img.getdata())
# Inverting the image
for i in range(len(data)):
    data[i] = 255 - data[i]

data = np.array(data)
data = data.astype('float32') / 255
data = data.reshape((1, 784))

# STEP 4: PREDICTING THE DIGIT
pred = network.predict(data)
pred = np.argmax(pred)
print("The predicted digit is : ", pred)