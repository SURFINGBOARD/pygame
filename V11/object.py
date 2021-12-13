# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:12:42 2021

@author: 78528
"""

import pygame
import tools
from constant import w, h

class obj(pygame.sprite.Sprite):
    def __init__(self,x,y,pic_group,pic):
        super().__init__()
        self.PIC = tools.load_pictures(pic_group)
        self.pic_count = 0
        self.x, self.y = x, y
        self.long_press = {'up': False, 'down': False, 'right': False, 'left': False} 
        self.speed = self.size * 16/32
        self.image = tools.get_image(self.PIC[pic],0 , 0, 16, 16, (0,0,0), self.size)
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        
    def read_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.long_press['down'] = True
                
            if event.key == pygame.K_UP:
                self.long_press['up'] = True
                
            if event.key == pygame.K_LEFT:
                self.long_press['left'] = True
                self.direction = 0
               
            if event.key == pygame.K_RIGHT:
                self.long_press['right'] =True
                self.direction = 5
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.long_press['up'] = False
                
            if event.key == pygame.K_DOWN:
                self.long_press['down'] = False
                
            if event.key == pygame.K_RIGHT:
                self.long_press['right'] = False
                
            if event.key == pygame.K_LEFT:
                self.long_press['left'] = False
            self.speed_x, self.speed_y = 0, 0
           
        if self.long_press['up'] == True:
            self.speed_y =+ self.speed * 1.2
        if self.long_press['down'] == True:
            self.speed_y =- self.speed * 1.2
        if self.long_press['right'] == True:
            self.speed_x =- self.speed * 1.2
        if self.long_press['left'] == True:
            self.speed_x =+ self.speed * 1.2
            
    def update_pos(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
    def undo_update_pos(self):
        self.x -= self.speed_x
        self.y -= self.speed_y
        
    def update(self,count,pos1):
        
        self.update_pos()
        if not pos1[0] == []:
            if (tools.caculate_distance(pos1[1],self.rect.center)) > (tools.caculate_distance(pos1[1],(self.x+self.rect.width/2,self.y + self.rect.height/2))):
               
                self.undo_update_pos()
        self.rect.x = self.x
        self.rect.y = self.y