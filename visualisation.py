import matplotlib.pyplot as plt 
import numpy as np 



def plot_single_image(data=None, index=None):
    if not index:
        index = np.random.randint(len(data))
    # Do i need to clear plt?
    plt.figure()
    plt.imshow(data[index], cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.show()


def plot_25_images(data=None, label=None, index=None):
    plt.figure(figsize=(8, 8))
    if not index:
        index = np.random.randint(len(data) - 25)
    else: 
        index = index
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(data[i + index], cmap='gray')
        plt.xlabel(str(label[i + index]))
    plt.show()