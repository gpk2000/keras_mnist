"""
This script is for predicting the handwritten digits of our own
handwritten image which is produced using gimp or any other software
the only restriction is that you create the image in the resolution
of 28 * 28 since our model is trained for such type
"""

# STEP 1: IMPORTING THE LIBRARIES 
from keras.models import load_model
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import numpy as np
from PIL import Image
import pyscreenshot as ImageGrab

# STEP 2: LOAD THE TRAINED MODEL
model = load_model('convnet_mnist.h5')

# STEP 3: IMAGE OPENING AND CHANGES
def predict(img):
    img = Image.open(img)
    img = img.convert('L')
    img = img.resize((28, 28))
    data = list(img.getdata())
    for i in range(len(data)):
        data[i] = 255 - data[i]
    
    data = np.array(data)
    data = data.astype('float32') / 255
    data = data.reshape((1, 28, 28, 1))
    pred = model.predict(data, verbose=False)
    return np.argmax(pred)

# STEP 4: GUI PART

def clear_all():
    global cv
    cv.delete('all')

def activate_event(event):
    global lastx, lasty
    cv.bind('<B1-Motion>', draw_lines)
    lastx, lasty = event.x, event.y

def draw_lines(event):
    global lastx, lasty
    x, y = event.x, event.y
    cv.create_line((lastx, lasty, x, y), width = 34, fill = 'black', capstyle = ROUND, smooth = True)
    lastx, lasty = x, y

def predict_img():
    filename =  f'image.png'
    widget = cv
    
    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()

    ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
    dig = predict(filename)
    messagebox.showinfo("Prediction", "I think it is " + str(dig))
    clear_all()
    
root = Tk()


root.resizable(0, 0)
root.title("Handwritten Digit Recognition GUI App")

lastx, lasty = None, None
image_number = 0

cv = Canvas(root, width=640, height=480, bg='white', cursor="cross")
pred_btn = Button(root, text="Predict!", command=predict_img)
clear_btn = Button(root, text='Clear All', command=clear_all)

cv.grid(row=0, column=0, pady=2, sticky=W, columnspan=2)
pred_btn.grid(row=1, column=1, pady=2, padx=2)
clear_btn.grid(row=1, column=0, pady=2)

cv.bind('<Button-1>', activate_event)


root.mainloop()

