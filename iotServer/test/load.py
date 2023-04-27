import os

import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
from skimage import transform


model = keras.models.load_model("./coffeeDripper.h5")
note_classes = ['Origami Dripper', 'Kalita Wave Dripper', 'Clever Dripper', 'Flower Dripper', 'V60 Dripper']

# load the image
from PIL import Image
import io



# load the image
from PIL import Image
import io
with open('origami.jpg', 'rb') as file:
    image_bytes = file.read()
    pillow_img = Image.open(io.BytesIO(image_bytes)).convert('L')



# transform image, same as for training!
data = np.asarray(pillow_img)
data = data / 255.0
data = data[np.newaxis, ..., np.newaxis]
# --> [1, x, y, 1]
data = tf.image.resize(data, [32, 32])
print(data.shape)

predictions =  model.predict(data)
print (predictions)
pred0 = predictions[0]
label0 = np.argmax(pred0)
print(label0)
# important part is this (bc it prints the classification)
print(note_classes[predictions.argmax()])


# data = poop(pillow_img)
#
# model.predict(data)
# predict
# predictions = model(data)
# predictions = tf.nn.softmax(predictions)
# print (predictions)
# pred0 = predictions[0]
# label0 = np.argmax(pred0)
# print(label0)