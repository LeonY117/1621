import tensorflow as tf
from tensorflow import keras

import numpy as np
# tensorflow supports version of numpy as 1.16.4 (april 21st)
import matplotlib.pyplot as plt

# How to organize functions in a file?


def plotSingleImage(index=None):
    if not index:
        index = np.random.randint(6000)

    # Do i need to clear plt?
    plt.figure()
    plt.imshow(train_images[index], cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.show()


def plot25Images():
    plt.figure(figsize=(8, 8))
    index = np.random.randint(6000 - 25)
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i + index], cmap='gray')
        plt.xlabel(str(train_labels[i + index]))
    plt.show()


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
model.fit(train_images, train_labels, epochs=10)

# 6. EVALUATE
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)


# DATA VISUALIZATION

# plot25Images()
# plotSingleImage()
