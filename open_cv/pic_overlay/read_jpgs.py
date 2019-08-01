import os
from itertools import cycle
import cv2
import time

folder = 'data'

# 列出frames文件夹下的所有图片
filenames = os.listdir(folder)

# 通过itertools.cycle生成一个无限循环的迭代器，每次迭代都输出下一张图像对象
img_iter = cycle([cv2.imread(os.sep.join([folder, x])) for x in filenames])

key = 0
while key & 0xFF != 27:
    cv2.imshow('Animation', next(img_iter))
    # time.sleep(1)
    key = cv2.waitKey(42)