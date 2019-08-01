# 第一个字符必须是字母表中的字母（大写 ASCII 字符或小写 ASCII 字符或 Unicode 字
# 符）或下划线（ _ ）。
# 标识符的其它部分可以由字符（大写 ASCII 字符或小写 ASCII 字符或 Unicode 字符）、
# 下划线（ _ ）、数字（0~9）组成。
# 标识符名称区分大小写。例如， myname 和 myName 并不等同。要注意到前者是小写字
# 母 n 而后者是大写字母 N 。
# 有效 的标识符名称可以是 i 或 name_2_3 ，无效 的标识符名称可能是
# 2things ， this is spaced out ， my-name 和 >a1b2_c3

# 文件名：var.py
i = 5
print(i)
i = i + 1
print(i)
s = '''This is a multi-line string.
This is the second line.'''
print(s)
print()

# 逻辑行与物理行：强烈建议你对于每一行物理行最多只写入一行逻辑行
# 一个逻辑行可以由多个物理行组成
s = 'This is a string. \
This continues the string.'
print(s)
print()

# 错误的缩进会导致编译错误
i = 5
# 下面将发生错误，注意行首有一个空格
print('Value is', i)
print('I repeat, the value is', i)

