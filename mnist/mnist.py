import tensorflow as tf
from tensorflow import keras

import numpy as np
# tensorflow supports version of numpy as 1.16.4 (april 21st)
import matplotlib.pyplot as plt

import visualisation 


# 1. DATA IMPORT & PREPROCESS
mnist = keras.datasets.mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# train_images: (60000, 28, 28)
# test_images: (10000, 28, 28)

# 2. Normalize data
train_images = train_images / 255
test_images = test_images / 255

# 3. MODEL
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])

# 4. COMPILE
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(
                  from_logits=True),
              metrics=['accuracy'])

# 5. TRAIN
# model.fit(train_images, train_labels, epochs=10)

# 6. EVALUATE
# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)


# DATA VISUALIZATION

# plot25Images()
# plotSingleImage()
