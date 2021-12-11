# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:36:50 2021

@author: 78528
"""
import pygame
import os
# tools 

# 把文件夹中的所有图片加载到一个个surface然后存一个字典，方便读取
# path: 文件夹位置
# 返回一个image对象的list
def load_pictures(path, accept = ('.jpg','.png','.bmp','.gif')):
    pictures = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img.convert()
            pictures[name] = img
    return pictures

# 把一个surface画到另一个surface但是提供了获取部分图片，挖出背景色，缩放的功能
# picture：组图
# x, y: 图片截取起始点
# width, height: 帧大小 
# colorkey：快速抠图的底色
# scale: 放大倍数
#返回： 一个image对象
def get_image(picture, x, y, width, height, colorkey, scale):
    image = pygame.Surface((width,height))
    image.blit(picture, (0,0), (x, y, width, height))
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image, (int(width * scale),int(height * scale)))
    return image


# 在六图的组合图中循环切换图片的数字来实现动画
# pic_num： 当前图片的标号
# return： 下一帧的图片标号
def change_pic(pic_num):
    if pic_num == 0 or pic_num == 1 or pic_num == 2:
        return (pic_num + 1) % 3
    elif pic_num == 3 or pic_num == 4 or pic_num == 5:
        return ((pic_num-3)+1) % 3 +3
    