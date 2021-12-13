# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:07:51 2021

@author: 78528
"""
import pygame
import tools
import monster
import obj
from constant import w,h
class bg(obj.obj):
    size = h / 800
    stop = False
    def __init__(self,x,y,pic_group,pic):
        super().__init__(x,y,pic_group,pic)
        
    def update(self,pos1):
        if pos1[1] == [] and pos1[2] == [] and pos1[0] == []:
            self.update_pos()
            if not (self.x >= -1920*h/800+w*3/5 and self.x <= w*2/5 and self.y >= -1280*h/800+h*5/6 and self.y <= h/4):
                self.undo_update_pos()
                self.stop = True
            else:
                self.stop = False
            
        self.rect.x = self.x
        self.rect.y = self.y