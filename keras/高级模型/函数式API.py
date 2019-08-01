import tensorflow as tf
from tensorflow.keras import layers

inputs = tf.keras.Input(shape=(32,))  # Returns a placeholder tensor

# A layer instance is callable on a tensor, and returns a tensor.
x = layers.Dense(64, activation='relu')(inputs)
x = layers.Dense(64, activation='relu')(x)
predictions = layers.Dense(10, activation='softmax')(x)


import numpy as np

x = np.array([[1,2,3,4],
              [5,6,7,8]])
y = np.array([1,2,3,4])


print(y.shape)
print(y.ndim)
