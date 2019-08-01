import tensorflow as tf
from tensorflow.keras import layers

layer = layers.Dense(32)
config = layer.get_config()
reconstructed_layer = layers.Dense.from_config(config)
print(layer)
print(config)
print(reconstructed_layer)