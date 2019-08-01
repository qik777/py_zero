
import tensorflow as tf
from tensorflow.keras import layers

# 创建序列模型
model = tf.keras.Sequential([
# Adds a densely-connected layer with 64 units to the model:
layers.Dense(64, activation='relu'),
# Add another:
layers.Dense(64, activation='relu'),
# Add a softmax layer with 10 output units:
layers.Dense(10, activation='softmax')])


model.compile(optimizer=tf.train.AdamOptimizer(0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

import numpy as np

print(np.random.random((4, 3)))
data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))
model.fit(data, labels, epochs=10, batch_size=32)

# data = np.random.random((1000, 32))
# labels = np.random.random((1000, 10))
#
# val_data = np.random.random((100, 32))
# val_labels = np.random.random((100, 10))
#
# model.fit(data, labels, epochs=10, batch_size=32,
#           validation_data=(val_data, val_labels))



# # Instantiates a toy dataset instance:
# data = np.random.random((1000, 32))
# labels = np.random.random((1000, 10))
# dataset = tf.data.Dataset.from_tensor_slices((data, labels))
# dataset = dataset.batch(32)
# dataset = dataset.repeat()
#
# # Don't forget to specify `steps_per_epoch` when calling `fit` on a dataset.
# model.fit(dataset, epochs=10, steps_per_epoch=30)

data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))

model.evaluate(data, labels, batch_size=32)

result = model.predict(data, batch_size=32)
print(result)
print(result.shape)



