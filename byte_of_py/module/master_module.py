import my_module
my_module.say_hi()
print('Version', my_module.__version__)
print()

# from my_module import say_hi, __version__
# say_hi()
# print('Version', __version__)
# print()

from my_module import *
say_hi()
print('Version', version)
# print('Version', __version__) # 不会导入 __version__名称，因为后者以双下划线开头。