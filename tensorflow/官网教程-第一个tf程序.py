# TensorFlow 是一个用于研究和生产的开源机器学习库。TensorFlow 提供了各种 API，可供初学者和专家在桌面、移动、网络和云端环境下进行开发。
# 请参阅以下几部分，了解如何开始使用。
# 高阶 Keras API 提供了用于创建和训练深度学习模型的构造块。

import tensorflow as tf

mnist = tf.keras.datasets.mnist

print(tf.keras.__version__)

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
