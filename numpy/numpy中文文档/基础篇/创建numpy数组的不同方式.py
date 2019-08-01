# Numpy库的核心是数组对象或ndarray对象（n维数组）。你将使用Numpy数组执行逻辑，统计和傅里叶变换等运算。作为使用Numpy的一部分，
# 你要做的第一件事就是创建Numpy数组。本指南的主要目的是帮助数据科学爱好者了解可用于创建Numpy数组的不同方式。
#
# 创建Numpy数组有三种不同的方法：
#
# 使用Numpy内部功能函数
# 从列表等其他Python的结构进行转换
# 使用特殊的库函数

# 使用Numpy内部功能函数
import numpy as np


# 创建一维数组
array = np.arange(20)
print(array)
print(array.shape)

# 创建二维数组
array = np.arange(20).reshape(4,5)
print(array)
print(array.shape)

# 创建三维数组
array = np.arange(27).reshape(3,3,3)
print(array)
print(array.shape)

# 以5为间隔,从10到35的数
array = np.arange(10, 35, 5)
print(array)

array = np.zeros((3,2))
print(array)

array = np.ones((2,3))
print(array)

# 填入随机数
array = np.empty((3,4))
print(array)

# 填入给定值
print(np.full((2,3),5))

# 对角线为给定值,其他均为0
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]
print(np.eye(5,5))

# 返回0~10之间均匀分布的5个数
print(np.linspace(0,10,num=5))


# 从Python列表转换:
# 除了使用Numpy函数之外，你还可以直接从Python列表创建数组。将Python列表传递给数组函数以创建Numpy数组

# 创建一位数组
array = np.array([4,5,6])
print(array)
print(array.shape)

# 创建二位数组
array = np.array([(1,2,3), (4,5,6)])
print(array)
print(array.shape)


# 使用特殊的库函数
# 你还可以使用特殊库函数来创建数组。例如，要创建一个填充0到1之间随机值的数组，请使用random函数。

print(np.random.random((2,2)))