#         reduce()函数也是Python内置的一个高阶函数。reduce()函数接收的参数和 map()类似，
# 一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，
# reduce()对list的每个元素反复调用函数f，并返回最终结果值。

# 必须import，否则reduce不可以使用
from functools import reduce

ls = [2, 4, 5, 7, 12]
def sum_plus(x, y):
    return x + y

def mult_plus(x, y):
    return x * y

def function_plus(x, y):
    return 2*x + y

print('reduce:',reduce(sum_plus, [2, 4, 5, 7, 12]))
# 和sum效果相同
print('sum:',sum(ls))

print('mult:',reduce(mult_plus, [2, 4, 5, 7, 12]))

print('function:',reduce(function_plus, [2, 4, 5, 7, 12]))

# ...可以实现各种函数