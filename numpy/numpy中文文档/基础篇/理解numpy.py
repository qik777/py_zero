# NumPy是一个功能强大的Python库，主要用于对多维数组执行计算。NumPy这个词来源于两个单词-- Numerical和Python。
# NumPy提供了大量的库函数和操作，可以帮助程序员轻松地进行数值计算。这类数值计算广泛用于以下任务：
#
# 机器学习模型：在编写机器学习算法时，需要对矩阵进行各种数值计算。例如矩阵乘法、换位、加法等。NumPy提供了一个非常
# 好的库，用于简单(在编写代码方面)和快速(在速度方面)计算。NumPy数组用于存储训练数据和机器学习模型的参数。
#
# 图像处理和计算机图形学：计算机中的图像表示为多维数字数组。NumPy成为同样情况下最自然的选择。实际上，NumPy提供了
# 一些优秀的库函数来快速处理图像。例如，镜像图像、按特定角度旋转图像等。
#
# 数学任务：NumPy对于执行各种数学任务非常有用，如数值积分、微分、内插、外推等。因此，当涉及到数学任务时，它形成了
# 一种基于Python的MATLAB的快速替代。

import numpy as np
import matplotlib.pyplot as plt

my_array = np.array([1, 2, 3, 4, 5])
print (my_array)
print (my_array.shape)

my_new_array = np.zeros((5))
print (my_new_array)

my_random_array = np.random.random((5))
print (my_random_array)

# 创建二维数组
my_2d_array = np.zeros((2, 3))
print (my_2d_array)
my_2d_array = np.random.random((2, 3))
print (my_2d_array)

my_array = np.array([[4, 5], [6, 1]])
print (my_array[0][1])
print (my_array.shape)

# 提取第二列的所有元素
my_array_column_2 = my_array[:, 1]
print (my_array_column_2)


# 使用数组进行计算
a = np.array([[1.0, 2.0],
              [3.0, 4.0]])
b = np.array([[5.0, 6.0],
              [7.0, 8.0]])
sum = a + b
difference = a - b
product = a * b
quotient = a / b
print ("Sum = \n", sum)
print ("Difference = \n", difference)
print ("Product = \n", product)
print ("Quotient = \n", quotient)

# 上面乘法运算符执行逐元素乘法而不是矩阵乘法。 要执行矩阵乘法，你可以执行以下操作：
matrix_product = a.dot(b)
print ("Matrix Product = ", matrix_product)