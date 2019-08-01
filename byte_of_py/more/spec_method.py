import time
class x_method:
    def __init__(self):
        print('init')
    def __del__(self):
        print('del')
    def __str__(self):
        print('str')
    def __lt__(self,other):
        print('lt')
    def __getitem__(self, key):
        print('getitem')
    def __len__(self):
        print('len')

x = x_method();
time.sleep(3)
del x_method