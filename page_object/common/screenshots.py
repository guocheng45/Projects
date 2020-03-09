# coding=utf-8

from PIL import ImageGrab


def screenshot_PC(name):
    pic = ImageGrab.grab()  # 实现截屏功能
    im = pic.convert('RGB')
    im.save(name + '.png')
    # im.save('F:\src\Image\image//' + str(c) + '.jpg', 'JPEG')  # 设置保存路径和图片格式
