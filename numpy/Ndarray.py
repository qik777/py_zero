import numpy as np

# 一维数组
a = np.array([1,2,3])
print (a)
print (a.shape)

a_zero = np.zeros((8))
print (a_zero)

a_one = np.ones((4))
print (a_one)

# 生成0~1之间随机数
a_random = np.random.random((6))
print (a_random)

# 多于一个维度
a = np.array([[1,  2],  [3,  4]])
print (a)

# 最小维度
a = np.array([1, 2, 3, 4, 5], ndmin = 2)
print (a)

# dtype 参数
a = np.array([1,  2,  3], dtype = complex)
print (a)
