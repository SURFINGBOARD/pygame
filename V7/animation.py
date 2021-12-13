#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:08:18 2021

@author: chenkanyu
@updater: ZhengLiu
"""

import tools
from constant import w, h
import obj
import pygame


class picToAnim(obj.obj):
    def __init__(self, x, y, pic_group, pic, howmany):
        super().__init__(x, y, pic_group, pic)
        self.howmany = howmany
        self.pic = pic
        
    def update(self, count, pos1):
        # get coordinate as a tuple based on bk map, x:pos[0],y:pos[1]
        self.update_pos()
        if not pos1[0] == []:
            if (tools.caculate_distance(pos1[1], self.rect.center)) > (tools.caculate_distance(pos1[1], (self.x + self.rect.width / 2, self.y + self.rect.height / 2))):
                self.undo_update_pos()
        # update the 16 pixel as a picture per frame
        if count % 8 == 0:
            self.image = tools.get_image(self.PIC[self.pic], self.pic_count * 16, 0, 16, 16, (255, 255, 255), self.size)
            self.pic_count = tools.animation_change_pic(self.pic_count, self.howmany)
        self.rect.x = self.x
        self.rect.y = self.y