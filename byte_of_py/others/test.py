import tensorflow as tf
from PIL import Image

print(tf.__version__)

im = Image.open('image.jpg')
im_new = im.resize((320,240),Image.ANTIALIAS)
im_new.show()
im_new.save('resize_image.jpg')

