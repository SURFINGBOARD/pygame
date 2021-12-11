# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:41:52 2021

@author: 78528
"""
import tools
import pygame
from constant import w, h

class Role():
    #direction
    direction = 5
    
    # press
    long_press = {'up': False, 'down': False, 'right': False, 'left': False}
    
    # speed
    speed_x = 0
    speed_y = 0

    #pos
    x,y = 0,0
    
    def __init__(self):
        self.PIC = tools.load_pictures('图片/人物行走')
    
        
    
        
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
            if self.direction == 1 or self.direction == 2:
                self.direction = 0
            if self.direction == 3 or self.direction == 4:
                self.direction = 5
            
    # 读取按键事件 更新速度
    def change_speed(self):
        if self.long_press['up'] == True:
            self.speed_y = -5
        if self.long_press['down'] == True:
            self.speed_y = 5
        if self.long_press['right'] == True:
            self.speed_x = 5
        if self.long_press['left'] == True:
            self.speed_x = -5
    
    # 刷新role对象的image属性 主函数只要把image画到窗口就可以渲染动画
    def update(self, count):
        #绘制当前角色
        self.image = tools.get_image(self.PIC['人物行走2'],self.direction * 32 , 0, 32, 32, (255,255,255), 3)
        self.x += self.speed_x
        self.y += self.speed_y
        
        
        if self.x > w-32*3+20:
            self.x = w-32*3+20
            
        if self.y > h- 32*3+20:
            self.y = h- 32*3+20
            
        if self.x < 0:
            self.x = 0
            
        if self.y < 0:
            self.y = 0
            
    # 死亡或者存活的动画     
    def dead(self, if_dead, count):
        if if_dead == True:
            self.direction = tools.dead_pic(self.direction)
        else:
            if (self.speed_x != 0 or self.speed_y != 0) and count % 8 == 0:
                self.direction = tools.change_pic(self.direction)
        
        
    
        