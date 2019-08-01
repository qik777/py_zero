# 返回函数
# Python的函数不但可以返回int、str、list、dict等数据类型，还可以返回函数！
# 例如，定义一个函数 f()，我们让它返回一个函数 g，可以这样写：
from functools import reduce
def f():
    print('call f()...')
    def g():
        print('call g()...')
    return g

x = f()
print()
print('f():',f())
print()
print('x:',x)
print()
print('x():',x())
print()
print('f()():',f()())
print()

# 请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积
def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod([1, 2, 3, 4, 5])
print(f())
