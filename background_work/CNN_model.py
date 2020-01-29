from keras.models import Sequential
from keras.layers import *
from keras.preprocessing.image import *
import numpy as np
import matplotlib.pyplot as pyt

def model():
    model = Sequential()
    model.add(Conv2D(32,(3,3), activation = 'relu', input_shape = (124,124,3) ))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32,(3,3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64,(3,3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64, activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation = 'sigmoid'))

    model.compile(optimizer = 'adam',loss = 'binary_crossentropy')
    return model
