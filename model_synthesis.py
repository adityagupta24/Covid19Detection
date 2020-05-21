import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

session = tf.Session()
keras.backend.set_session(session)

model = keras.models.load_model("./home/final_model.hdf5")
model._make_predict_function()


def make_predictions(path):

    img = keras.preprocessing.image.load_img(path, target_size=(224, 224))
    img = keras.preprocessing.image.img_to_array(img)/255.0
    img = img.reshape((1, 224, 224, 3))
    with session.as_default():
        with session.graph.as_default():
            pred = model.predict(img)
    return pred[0][0]
