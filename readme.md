## Introduction

This repo consists of codes which are useful in predicting the handwritten digits. The dataset used is from the keras MNIST dataset. Although this is the "Hello world" of deep learning, this model achieves an accuracy of about 98% which is pretty cool for a basic model. There are many ways to improve this model which would be done in the future.

I added the convolution network code which acheives 99% accuracy. Awesome!!.

Added **GUI**. Thanks and credit goes to the author of [this](https://medium.com/analytics-vidhya/handwritten-digit-recognition-gui-app-46e3d7b37287) article. 


---

## Usage on Local Machine
* The first thing you need to do is to clone this repository by typing the following command :-

`git clone https://github.com/1CH1GO/keras_mnist.git`

* Then you need to change the directory to `keras_mnist`.

* Before executing the code you need to install some packages. You can use a virtual environment or install globally. Virtual environment is the preferred one.

* The packages can be installed by the following command :-

`pip3 install -r requirements.txt`

* After that you can execute the file `image_prediction.py` using the follwing command :-

`python3 image_prediction.py`

* Dont worry your system is not going to heat up if you think that you are training the model. The model is already trained and is saved as `convnet_mnist.h5`. We will resuse this model to get our predictions.

---

## Screenshots of GUI

![](https://github.com/1CH1GO/keras_mnist/blob/master/images/Screenshot%20from%202020-06-27%2019-35-14.png?raw=true)



![](https://github.com/1CH1GO/keras_mnist/blob/master/images/Screenshot%20from%202020-06-27%2019-35-34.png?raw=true)

---

## How did i train this model

* I learnt how to do this by reading a Book on deep learning (i am still learning things from it :smile:).

* The book can be found in deep_learning_resources repository along with many cool things that i found interesting while i am on my adventure.

* I coded and trained my code on Google Colab which offers decent service in executing and training our models. My local machine literally becomes a hot pan when i try to train a model.

---

## Some predictions dont make sense :thinking:

* Yes thats true if you try to play with the model for sometime you will see that the model gives weird predictions.

* The reasons that i think for these weird predictions might be:
  - The image that you draw on the GUI is scaled down to a 28 x 28 image and then it is fed into the model for prediction.
  
  - Why 28 x 28 you ask? Thats because the MNIST dataset uses 28 x 28 format and the model is trained for such shape.
  
* So i think one way to improve accuracy might be drawing large digits. Then the 28 x 28 image might be distinguishable by the model.

---

## TODO

* Improve the models accuracy current(99%) and state-of-art(100%).

* Improve GUI? I dont have any opinions on this.

---
