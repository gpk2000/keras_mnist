## Introduction

This repo consists of codes which are useful in predicting the handwritten digits. The dataset used is from the keras MNIST dataset. Although this is the "Hello world" of deep learning, this model achieves an accuracy of about 98% which is pretty cool for a basic model. There are many ways to improve this model which would be done in the future.

**UPD**: I added the convolution network code which acheives 99% accuracy. Awesome!!

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

---

## Usage in Google Colab
* Google colab is an excellent resource for running deep learning modules.
* Goto [this](https://colab.research.google.com/notebooks/intro.ipynb) page and signup.

![](https://github.com/1CH1GO/keras_mnist/blob/master/images/image_1.jpg?raw=true)

* After signing up go to File > New Notebook. A new window will pop up.

![](https://github.com/1CH1GO/keras_mnist/blob/master/images/image_2.jpg?raw=true)

* The new window will look like this

![](https://github.com/1CH1GO/keras_mnist/blob/master/images/image_3.jpg?raw=true)

* Now type the commands as shown in the picture and execute each of them individually by clicking the play button of the cell or `Ctrl + Enter`.

![](https://github.com/1CH1GO/keras_mnist/blob/master/images/image_4.jpg?raw=true)


## Predicting your own handwritten digits
* You can also predict your own handwritten digits too.
* The first step is to create a grayscale image of size 28 x 28 and save the file in the `keras_mnist` directory.
* For creating such images you can either use GIMP or similar softwares.</br>
**NOTE**: The image must have 28 x 28 size.
* After that you can open the source code of `image_prediction.py` and edit the line below `STEP 3:` and replace the filename with name of the image you created.
* After doing that you can just execute the file as mentioned in Usage.

---

