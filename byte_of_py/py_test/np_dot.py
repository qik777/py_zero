import numpy as np

x_data = np.float32(np.random.rand(2,10))
print(x_data)
print("\n")
y_data = np.dot([1,2], x_data)
print(y_data)
