# filter() 接收的函数必须判断出一个数的平方根是否是整数，而 math.sqrt()返回结果是浮点数。

import math
def is_sqr(x):
    r = int(math.sqrt(x))
    return r*r==x

# return 3.0
print(math.sqrt(9))

# result: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(list(range(1,21)))

# 打印出501以内平方根是整数的数
# result: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484]
print(list(filter(is_sqr, range(1, 501))))

# result: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
for count in range(1,31):
    print(count,end=' ')