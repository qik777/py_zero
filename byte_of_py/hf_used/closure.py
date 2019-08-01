# 闭包
# 在函数内部定义的函数和外部定义的函数是一样的，只是他们无法被外部访问：

def f():
    print('f()...')
    def g():
        print('g()...')
    return g

print(f()())
print()

ls = [1,2,3,4,5,6,7]
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum

f = calc_sum(ls)
print(f())

# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
