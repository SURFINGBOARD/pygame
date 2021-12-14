#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:08:18 2021

@author: chenkanyu
"""

import pygame
import tools
from constant import w, h
import obj


class candle(obj.obj):
    def __init__(self,x,y,pic_group,pic):
        super().__init__(x,y,pic_group,pic)
        
    def update(self,count,pos1):
        self.update_pos()
        if not pos1[0] == []:
            if (tools.caculate_distance(pos1[1],self.rect.center)) > (tools.caculate_distance(pos1[1],(self.x+self.rect.width/2,self.y + self.rect.height/2))):
               self.undo_update_pos()
        if count % 6 == 0:
            
            self.image = tools.get_image(self.PIC['candle'], self.pic_count*16, 0, 16, 16, (0,0,0), self.size)    
            #计算下一帧图片的标号
            self.pic_count = tools.animation_change_pic(self.pic_count,6)
            
        
        
        self.rect.x = self.x
        self.rect.y = self.y
        
            
        
        