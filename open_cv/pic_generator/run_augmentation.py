# 图片数据增加小工具
# running cmd：
#   python run_augmentation.py imagenet_samples more_samples 1000 --rotate_angle_vari 180 --p_rotate_crop 0.5

import os
import argparse
import random
import math
from multiprocessing import Process
from multiprocessing import cpu_count

import cv2

# 导入image_augmentation.py为一个可调用模块
import image_augmentation as ia


# 利用Python的argparse模块读取输入输出和各种扰动参数
def parse_args():
    parser = argparse.ArgumentParser(
        description='A Simple Image Data Augmentation Tool',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_dir',
                        help='Directory containing images')
    parser.add_argument('output_dir',
                        help='Directory for augmented images')
    parser.add_argument('num',
                        help='Number of images to be augmented',
                        type=int)

    parser.add_argument('--num_procs',
                        help='Number of processes for paralleled augmentation',
                        type=int, default=cpu_count())

    parser.add_argument('--p_mirror',
                        help='Ratio to mirror an image',
                        type=float, default=0.5)

    parser.add_argument('--p_crop',
                        help='Ratio to randomly crop an image',
                        type=float, default=1.0)
    parser.add_argument('--crop_size',
                        help='The ratio of cropped image size to original image size, in area',
                        type=float, default=0.8)
    parser.add_argument('--crop_hw_vari',
                        help='Variation of h/w ratio',
                        type=float, default=0.1)

    parser.add_argument('--p_rotate',
                        help='Ratio to randomly rotate an image',
                        type=float, default=1.0)
    parser.add_argument('--p_rotate_crop',
                        help='Ratio to crop out the empty part in a rotated image',
                        type=float, default=1.0)
    parser.add_argument('--rotate_angle_vari',
                        help='Variation range of rotate angle',
                        type=float, default=10.0)

    parser.add_argument('--p_hsv',
                        help='Ratio to randomly change gamma of an image',
                        type=float, default=1.0)
    parser.add_argument('--hue_vari',
                        help='Variation of hue',
                        type=int, default=10)
    parser.add_argument('--sat_vari',
                        help='Variation of saturation',
                        type=float, default=0.1)
    parser.add_argument('--val_vari',
                        help='Variation of value',
                        type=float, default=0.1)

    parser.add_argument('--p_gamma',
                        help='Ratio to randomly change gamma of an image',
                        type=float, default=1.0)
    parser.add_argument('--gamma_vari',
                        help='Variation of gamma',
                        type=float, default=2.0)

    args = parser.parse_args()
    args.input_dir = args.input_dir.rstrip('/')
    args.output_dir = args.output_dir.rstrip('/')

    return args


'''
根据进程数和要增加的目标图片数，
生成每个进程要处理的文件列表和每个文件要增加的数目
'''


def generate_image_list(args):
    # 获取所有文件名和文件总数
    filenames = os.listdir(args.input_dir)
    num_imgs = len(filenames)

    # 计算平均处理的数目并向下取整
    num_ave_aug = int(math.floor(args.num / num_imgs))

    # 剩下的部分不足平均分配到每一个文件，所以做成一个随机幸运列表
    # 对于幸运的文件就多增加一个，凑够指定的数目
    rem = args.num - num_ave_aug * num_imgs
    lucky_seq = [True] * rem + [False] * (num_imgs - rem)
    random.shuffle(lucky_seq)

    # 根据平均分配和幸运表策略，
    # 生成每个文件的全路径和对应要增加的数目并放到一个list里
    img_list = [
        (os.sep.join([args.input_dir, filename]), num_ave_aug + 1 if lucky else num_ave_aug)
        for filename, lucky in zip(filenames, lucky_seq)
    ]

    # 文件可能大小不一，处理时间也不一样，
    # 所以随机打乱，尽可能保证处理时间均匀
    random.shuffle(img_list)

    # 生成每个进程的文件列表，
    # 尽可能均匀地划分每个进程要处理的数目
    length = float(num_imgs) / float(args.num_procs)
    indices = [int(round(i * length)) for i in range(args.num_procs + 1)]
    return [img_list[indices[i]:indices[i + 1]] for i in range(args.num_procs)]


# 每个进程内调用图像处理函数进行扰动的函数
def augment_images(filelist, args):
    # 遍历所有列表内的文件
    for filepath, n in filelist:
        img = cv2.imread(filepath)
        filename = filepath.split(os.sep)[-1]
        dot_pos = filename.rfind('.')

        # 获取文件名和后缀名
        imgname = filename[:dot_pos]
        ext = filename[dot_pos:]

        print('Augmenting {} ...'.format(filename))
        for i in range(n):
            img_varied = img.copy()

            # 扰动后文件名的前缀
            varied_imgname = '{}_{:0>3d}_'.format(imgname, i)

            # 按照比例随机对图像进行镜像
            if random.random() < args.p_mirror:
                # 利用numpy.fliplr(img_varied)也能实现
                img_varied = cv2.flip(img_varied, 1)
                varied_imgname += 'm'

            # 按照比例随机对图像进行裁剪
            if random.random() < args.p_crop:
                img_varied = ia.random_crop(
                    img_varied,
                    args.crop_size,
                    args.crop_hw_vari)
                varied_imgname += 'c'

            # 按照比例随机对图像进行旋转
            if random.random() < args.p_rotate:
                img_varied = ia.random_rotate(
                    img_varied,
                    args.rotate_angle_vari,
                    args.p_rotate_crop)
                varied_imgname += 'r'

            # 按照比例随机对图像进行HSV扰动
            if random.random() < args.p_hsv:
                img_varied = ia.random_hsv_transform(
                    img_varied,
                    args.hue_vari,
                    args.sat_vari,
                    args.val_vari)
                varied_imgname += 'h'

            # 按照比例随机对图像进行Gamma扰动
            if random.random() < args.p_gamma:
                img_varied = ia.random_gamma_transform(
                    img_varied,
                    args.gamma_vari)
                varied_imgname += 'g'

            # 生成扰动后的文件名并保存在指定的路径
            output_filepath = os.sep.join([
                args.output_dir,
                '{}{}'.format(varied_imgname, ext)])
            cv2.imwrite(output_filepath, img_varied)


# 主函数
def main():
    # 获取输入输出和变换选项
    args = parse_args()
    params_str = str(args)[10:-1]

    # 如果输出文件夹不存在，则建立文件夹
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    print('Starting image data augmentation for {}\n'
          'with\n{}\n'.format(args.input_dir, params_str))

    # 生成每个进程要处理的列表
    sublists = generate_image_list(args)

    # 创建进程
    processes = [Process(target=augment_images, args=(x, args,)) for x in sublists]

    # 并行多进程处理
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print('\nDone!')


if __name__ == '__main__':
    main()