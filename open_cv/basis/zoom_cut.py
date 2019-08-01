# 缩放，裁剪和补边
import cv2
import handle_file

path = 'data/zoom_cut/'
src_file = 'data/rs_image_640_480.jpg'
dst_file = path+'cp_image_640_480.jpg'
handle_file.mk_dir(path)
handle_file.cp_file(src_file, dst_file)

# 读取一张四川大录古藏寨的照片
img = cv2.imread(dst_file)

# 缩放成200x200的方形图像
img_200x200 = cv2.resize(img, (200, 200))

# 不直接指定缩放后大小，通过fx和fy指定缩放比例，0.5则长宽都为原来一半
# 等效于img_200x300 = cv2.resize(img, (300, 200))，注意指定大小的格式是(宽度,高度)
# 插值方法默认是cv2.INTER_LINEAR，这里指定为最近邻插值
img_200x300 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5,
                              interpolation=cv2.INTER_NEAREST)

# 在上张图片的基础上，上下各贴50像素的黑边，生成300x300的图像
img_300x300 = cv2.copyMakeBorder(img, 50, 50, 0, 0,
                                       cv2.BORDER_CONSTANT,
                                       value=(0, 0, 0))

# 对照片中树的部分进行剪裁
patch_tree = img[20:150, -180:-50]

cv2.imwrite(path+'cropped_tree.jpg', patch_tree)
cv2.imwrite(path+'resized_200x200.jpg', img_200x200)
cv2.imwrite(path+'resized_200x300.jpg', img_200x300)
cv2.imwrite(path+'bordered_300x300.jpg', img_300x300)