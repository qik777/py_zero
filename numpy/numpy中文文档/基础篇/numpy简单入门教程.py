# NumPy是Python中的一个运算速度非常快的一个数学库，它非常重视数组。它允许你在Python中进行向量和矩阵计算，并且由于许多底层
# 函数实际上是用C编写的，因此你可以体验在原生Python中永远无法体验到的速度。
#
# NumPy绝对是科学Python成功的关键之一，如果你想要进入Python中的数据科学和/或机器学习，你就要必须学习它。在我看来，NumPy
# 的API设计得很好，所以我们要开始使用它并不困难。
import numpy as np
import matplotlib.pyplot as plt

# 多维数组切片
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(a[0, 1:4]) # >>>[12 13 14]
print(a[1:4, 0]) # >>>[16 21 26]
print(a[::2,::2]) # >>>[[11 13 15]
                  #     [21 23 25]
                  #     [31 33 35]]
print(a[:, 1]) # >>>[12 17 22 27 32]

print(type(a)) # >>><class 'numpy.ndarray'>
print(a.dtype) # >>>int64
print(a.size) # >>>25
print(a.shape) # >>>(5, 5)
print(a.itemsize) # >>>8
print(a.ndim) # >>>2
print(a.nbytes) # >>>200

a = np.arange(25)
print(a)
a = a.reshape((5, 5))
print(a)

b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
print(b)
b = b.reshape((5,5))
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a < b)
print(a > b)

print(a.dot(b))

# dot, sum, min, max, cumsum
a = np.arange(10)

print(a.sum()) # >>>45
print(a.min()) # >>>0
print(a.max()) # >>>9
print(a.cumsum()) # >>>[ 0  1  3  6 10 15 21 28 36 45]

# 花式索引
a = np.arange(0, 100, 10)
print(a)
indices = [1, 5, -1]
b = a[indices]
print(b)


# 缺省索引
a = np.arange(0, 100, 10)
b = a[:5]
c = a[a >= 50]
print(b) # >>>[ 0 10 20 30 40]
print(c) # >>>[50 60 70 80 90]

# Where
a = np.arange(0, 100, 10)
b = np.where(a < 50)
c = np.where(a >= 50)[0]
print(b) # >>>(array([0, 1, 2, 3, 4]),)
print(c) # >>>[5 6 7 8 9]

# 布尔屏蔽
# a = np.linspace(0, 2 * np.pi, 50)
# print(a)
# b = np.sin(a)
# plt.plot(a,b)
# mask = b >= 0
# plt.plot(a[mask], b[mask], 'bo')
# mask = (b >= 0) & (a <= np.pi / 2)
# plt.plot(a[mask], b[mask], 'go')
# plt.show()