import os
import shutil

def mk_dir(dir):
    folder = os.path.exists(dir)
    if not folder:
        os.mkdir(dir)
        print('mkdir:'+dir)
    else:
        print('the folder is exist!')

def cp_file(src,dst):
    is_file = os.path.isfile(src)
    if is_file:
        shutil.copy(src, dst)
        print('cp file successful')
    else:
        print('the src file is not exist,cp file fail!')
