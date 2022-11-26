import numpy as np
import PIL.Image as Image
import sys
import matplotlib.pyplot as plt


def GenAutolevelMapping( fn, ConvertToArray = True ): #hist is the histogram of a 8 bit gray scale image
    try:
        image = Image.open(fn)
    except IOError as err:
        print(err)  # output the err
        raise  # raise again

        # if image.mode == 'RGB' or image.mode == 'RGBA':
    if image.mode != 'L':
        image = image.convert('L')

    if ConvertToArray == True:
        image = np.asarray(image)

    return image

def ImageAutolevel( f,H,L ): # f is the input image, as Image object or numpy array
    g = np.round(255 * ((f - L) / (H - L)))
    g = Image.fromarray(g)
    if g.mode == 'F':
        g = g.convert('L')
    return g

    # return g #g is the auto-level-processed image


def Main(fn1,fn2):
    try:
        f = GenAutolevelMapping(fn1)

        img_array = np.asarray(f)  #
        h = np.max(img_array)  #
        l = np.min(img_array)  #
    except:
        return
    g = ImageAutolevel(f,h,l)
    g.save(fn2)

    fig, axeslist = plt.subplots(1, 2)  # 2 columns and 1 row
    axeslist.ravel()[0].imshow(f, cmap='gray')
    axeslist.ravel()[1].imshow(g, cmap='gray')
    axeslist.ravel()[0].set_axis_off()
    axeslist.ravel()[1].set_axis_off()

    plt.show()


if __name__=='__main__':
    fn1 = r'E:\课程文件\python图像处理\auto-level-Zhangyq2086-main\Lenna.jpg'
    # image_name = 'ALenna'#'E:/课程文件/python图像处理/auto-level-Zhangyq2086-main/' + image_name + '.bmp'
    fn2 = r'E:\课程文件\python图像处理\auto-level-Zhangyq2086-main\ALenna.bmp'
    Main(fn1, fn2)

