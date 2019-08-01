import tensorflow as tf
from PIL import Image

print(tf.__version__)

im = Image.open('data/timg.jpeg')
# im.show()
im_new = im.resize((192,192),Image.ANTIALIAS)
# im_new.show()
im_new.save('data/rs_timg_192_192.png')

def start(self):
    print('')
    if __name__ == '__main__':
        print(self)

