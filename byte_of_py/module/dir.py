import sys
# 给出 sys 模块中的属性名称
print(dir(sys))

# 给出当前模块的属性名称
print(dir())
print()

# 创建一个新的变量 'a'
a = 5
print(dir())
print(dir().__doc__)
print()

# 删除或移除一个名称
del a
print(dir())