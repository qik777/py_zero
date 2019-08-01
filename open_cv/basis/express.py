# form: https://zhuanlan.zhihu.com/p/24425116

import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import shutil

import cv2
import handle_file

path = 'data/express/'
src_file = 'data/rs_image_640_480.jpg'
dst_file = path+'cp_image_640_480.jpg'
handle_file.mk_dir(path)
handle_file.cp_file(src_file, dst_file)

# 图6-1中的矩阵
img = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
], dtype=np.uint8)

# print(np.size())

# 用matplotlib存储
plt.imsave(dst_file, img)

# 用OpenCV存储
cv2.imwrite(path+'re_image_cv2.jpg', img)