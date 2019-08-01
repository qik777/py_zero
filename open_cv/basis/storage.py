
import cv2
import handle_file

path = 'data/storage/'
src_file = 'data/rs_image_640_480.jpg'
dst_file = path+'cp_image_640_480.jpg'
handle_file.mk_dir(path)
handle_file.cp_file(src_file, dst_file)

# 读取一张400x600分辨率的图像
color_img = cv2.imread(dst_file)
print(color_img.shape)

# 直接读取单通道
gray_img = cv2.imread(dst_file, cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)

# 把单通道图片保存后，再读取，仍然是3通道，相当于把单通道值复制到3个通道保存
cv2.imwrite('data/storage/test_grayscale.jpg', gray_img)
reload_grayscale = cv2.imread('data/storage/test_grayscale.jpg')
print(reload_grayscale.shape)

# cv2.IMWRITE_JPEG_QUALITY指定jpg质量，范围0到100，默认95，越高画质越好，文件越大
cv2.imwrite('data/storage/test_imwrite.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 80))

# cv2.IMWRITE_PNG_COMPRESSION指定png质量，范围0到9，默认3，越高文件越小，画质越差
cv2.imwrite('data/storage/test_imwrite.png', color_img, (cv2.IMWRITE_PNG_COMPRESSION, 5))