print('hello world',end=' ') #注意到 print 是一个函数

# 注意到 print 是一个函数
print('hello world')
print()

# 字面常量(Literal Constants)
# 单引号双引号效果相同
# 三引号内部可以加任意的双引号或单引号
# 字符串内容不可变
str = 'I love this game'
print(str)
str = "I love this food"
print(str)
print()


str = '''这是一段多行字符串。这是它的第一行。
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
print(str)
print()

# format
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:&^9}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('a', end='')
print('b')

print('a', end=' ')
print('b', end=' ')
print('c')
print()

# 转义序列
print('This is the first line\nThis is the second line')
print("This is the first sentence.\
This is the second sentence.")
print(r"Newlines are indicated by \n")
print()




