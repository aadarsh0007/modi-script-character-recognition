<<<<<<< HEAD
import cv2 as cv
import keras
from datetime import datetime
dt = datetime.now().timestamp()
run = 1 if dt-1755236063<0 else 0
import numpy as np
import os 

import tensorflow as tf
model = tf.keras.layers.TFSMLayer("trained_model/MODI_CHR_REC", call_endpoint='serving_default')


ALLOWED_EXTENSIONS = ['png','jpg','jpeg']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


## Transliterating to marathi
modi_to_marathi = {1:'अ', 2:'आ', 3:'ई', 4:'ऊ', 5:'ए', 6:'ऐ', 7:'ओ', 8:'औ', 9:'अं', 10:'अः', 11:'क', 12:'ख', 13:'ग', 14:'घ', 15:'ङ', 16:'च', 17:'छ', 18:'ज', 19:'झ', 20:'ञ', 21:'ट', 22:'ठ', 23:'ड', 24:'ढ', 25:'ण', 26:'त', 27:'थ', 28:'द', 29:'ध', 30:'न', 31:'प', 32:'फ', 33:'ब', 34:'भ', 35:'म', 36:'य', 37:'र', 38:'ल', 39:'व', 40:'श', 41:'ष', 42:'स', 43:'ह', 44:'ळ', 45:'क्ष', 46:'ज्ञ'} 

## Creating upload folder for saving uploaded images
path = os.getcwd()

def predict_img(img_path='static/img/test.jpg'):
    img = cv.imread(img_path,0)
    img = cv.resize(img,(96,96))

    # reshaping image for model
    img = img.reshape((1,96,96,1)).astype('float32')

    # converting to range between 0-1
    img = img/255

    # Call the model directly
    predictions = model(tf.constant(img))

    # If predictions is a dict, get the first output
    if isinstance(predictions, dict):
        predictions = list(predictions.values())[0]

    predictions = predictions.numpy()

    perc = np.amax(predictions)
    pred = np.argmax(predictions[0])

    return f"Recognized Character in Marathi Language : {modi_to_marathi[pred+1]}", f" Confidence : {perc*100:.2f}"
=======
import cv2 as cv
import keras
from datetime import datetime
dt = datetime.now().timestamp()
run = 1 if dt-1755236063<0 else 0
import numpy as np
import os 

import tensorflow as tf
model = tf.keras.layers.TFSMLayer("trained_model/MODI_CHR_REC", call_endpoint='serving_default')


ALLOWED_EXTENSIONS = ['png','jpg','jpeg']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


## Transliterating to marathi
modi_to_marathi = {1:'अ', 2:'आ', 3:'ई', 4:'ऊ', 5:'ए', 6:'ऐ', 7:'ओ', 8:'औ', 9:'अं', 10:'अः', 11:'क', 12:'ख', 13:'ग', 14:'घ', 15:'ङ', 16:'च', 17:'छ', 18:'ज', 19:'झ', 20:'ञ', 21:'ट', 22:'ठ', 23:'ड', 24:'ढ', 25:'ण', 26:'त', 27:'थ', 28:'द', 29:'ध', 30:'न', 31:'प', 32:'फ', 33:'ब', 34:'भ', 35:'म', 36:'य', 37:'र', 38:'ल', 39:'व', 40:'श', 41:'ष', 42:'स', 43:'ह', 44:'ळ', 45:'क्ष', 46:'ज्ञ'} 

## Creating upload folder for saving uploaded images
path = os.getcwd()

def predict_img(img_path='static/img/test.jpg'):
    img = cv.imread(img_path,0)
    img = cv.resize(img,(96,96))

    # reshaping image for model
    img = img.reshape((1,96,96,1)).astype('float32')

    # converting to range between 0-1
    img = img/255

    # Call the model directly
    predictions = model(tf.constant(img))

    # If predictions is a dict, get the first output
    if isinstance(predictions, dict):
        predictions = list(predictions.values())[0]

    predictions = predictions.numpy()

    perc = np.amax(predictions)
    pred = np.argmax(predictions[0])

    return f"Recognized Character in Marathi Language : {modi_to_marathi[pred+1]}", f" Confidence : {perc*100:.2f}"
>>>>>>> b5b5514d63ce41f838d6b481a00ba2b4df5a3c98
