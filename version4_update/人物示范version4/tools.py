# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:36:50 2021
tools

@author: Yufan Cheng
@update: Zheng Liu
"""
import pygame
import os


def load_pictures(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    """
    feed a list of pictures in a folder into a dict called pictures
    :param path: a relative path or absolute path
    :param accept: a list of types can accept
    :return: a list of pictures
    """
    pictures = {}
    for pic in os.listdir(path):  # get a list of pictures in variable path
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            # accelerate rendering
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img.convert()
            pictures[name] = img
    return pictures


def get_image(picture, x, y, width, height, colorkey, scale):
    """
    draw a surface which provide get picture, get back-color and get scaling times into another surface
    :param picture: a list of pictures about one role
    :param x: coordinate x
    :param y: coordinate y
    :param width: frame width
    :param height: frame height
    :param colorkey: the back-color
    :param scale: how many times scaling up
    :return:
    """
    image = pygame.Surface((width, height))
    image.blit(picture, (0, 0), (x, y, width, height))
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    return image


def change_pic(pic_num):
    """
    impelemnt an influence animation by changing the index of pictures
    :param pic_num: current picture index
    :return: the index of picture of next frame
    """
    if pic_num == 0 or pic_num == 1 or pic_num == 2:
        return (pic_num + 1) % 3
    elif pic_num == 3 or pic_num == 4 or pic_num == 5:
        return ((pic_num - 3) + 1) % 3 + 3


def animation_change_pic(pic_num, num):
    """
    change the numbers of special effects pictures
    :param pic_num: current picture index
    :param num: how many pictures in list
    :return: the index of picture of next frame
    """
    return (pic_num + 1) % num


def dead_pic(pic_num):
    """
    get the index of dead picture through calculating the index of current picture
    :param pic_num: the index of current picture
    :return: the index of dead picture of next frame
    """
    if pic_num == 0 or pic_num == 1 or pic_num == 2:
        return 6
    elif pic_num == 3 or pic_num == 4 or pic_num == 5:
        return 7
