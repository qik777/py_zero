import sys
import os
print('The command line arguments are:')
# 查看你的程序目前所处在的目录和文件
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

# 查看你的程序目前所处在的目录
print(os.getcwd())
print()

# from..import 语句
from math import sqrt
print("Square root of 16 is", sqrt(16))