# 。如果__name__ 与 "__main__" 属性相同则代表这一模块是由用户独立运行的
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')