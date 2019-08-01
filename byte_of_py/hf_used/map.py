#       map()是 Python 内置的高阶函数，它接收一个函数 f 和一个list，并通过把函数 f
# 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
#       map()函数不改变原有的 list，而是返回一个新的 list
#       利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数

# example 1: 对list中每个数字取平方
ls = [1,2,3,4,5,6,7,8,9]

def f(x):
    x*x

# def f(x):
#     print(x*x)

# bad output
rs = map(f,ls)
print(list(rs))

rs=map(str,ls)
print(list(rs))

rs=map(int,ls)
print(list(rs))

# 正确的打印map()的方式
new_ls = map(lambda x:x*x, ls)
print(list(new_ls))
print()


# 由于list包含的元素可以是任何类型，因此，map() 不仅 y仅可以处理只包含数值的 list，
# 事实上它可以处理包含任意类型的 list，只要传入的函数f可以处理这种数据类型。

#  example 2: 将书写不规范的名字按首字母大写后面字母小写的方式更改
name = ['adam', 'LISA', 'barT', 'lily', 'KEN', 'KIVen']

# def format_name(s):
#     return s[0].upper() + s[1:].lower()

new_name = map(lambda s:s[0].upper() + s[1:].lower(), name)
print(list(new_name))