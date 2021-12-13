# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:36:50 2021

@author: 78528
"""
import pygame
import os
# tools 

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


def get_image(picture, x, y, width, height, colorkey, scale):
    image = pygame.Surface((width,height))
    image.blit(picture, (0,0), (x, y, width, height))
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image, (int(width * scale),int(height * scale)))
    return image


def change_pic(pic_num):
    if pic_num == 0 or pic_num == 1 or pic_num == 2:
        return (pic_num + 1) % 3
    elif pic_num == 3 or pic_num == 4 or pic_num == 5:
        return ((pic_num-3)+1) % 3 +3


def animation_change_pic(pic_num, num):
    return (pic_num + 1)% num


def dead_pic(pic_num):
    if pic_num == 0 or pic_num == 1 or pic_num == 2:
        return 6
    elif pic_num == 3 or pic_num == 4 or pic_num == 5:
        return 7


def caculate_distance(pos1,pos2):
    return int(pow(pow(abs(pos1[0]-pos2[0]),2) + pow(abs(pos1[1]-pos2[1]),2), 0.5))