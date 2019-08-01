# 匿名函数
# 高阶函数可以接收函数做参数，有些时候，我们不需要显式地定义函数，直接传入匿名函数更方便。
# 在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算 f(x)=x2 时，除了定义
# 一个f(x)的函数外，还可以直接传入匿名函数：

import math

# example 2: 关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x * x, ls)))

# 匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。
# 使用匿名函数，可以不必定义函数名，直接创建一个函数对象，很多时候可以简化代码：
# sorted([1, 3, 9, 5, 0], lambda x,y: -cmp(x,y))//python 3.x取消了cmp

# sorted(ls, lambda x,y: -cmp(x,y))

#  example 2: 将书写不规范的名字按首字母大写后面字母小写的方式更改
name = ['adam', 'LISA', 'barT', 'lily', 'KEN', 'KEvin']

for n in name:
    print(n, end=' ')
print()

new_name = map(lambda s:s[0].upper() + s[1:].lower(), name)
print(list(new_name))

str = ['I','Love','This','Game','!']

for s in str:
    print(s, end=' ')