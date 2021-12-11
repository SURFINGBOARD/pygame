# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:41:52 2021

@author: 78528
"""
import tools
import pygame
from constant import w, h

class Role():
   
    
    size = w / 16 / 16

    #pos
    x,y = w/2 - 32*3/2, h/2 - 32*3/2
    
    def __init__(self):
        self.PIC = tools.load_pictures('图片/人物行走')
        self.image = tools.get_image(self.PIC['knight'],0 , 0, 16, 16, (0,0,0), self.size)
        self.blood = 6
        #direction
        self.direction = 'right'
        
        self.run = 0
        
        self.dead = False
        
        self.pic_count = 0
        # press
        self.long_press = 0 
    
    def press_move(self):
        self.long_press += 1 
        self.pic_count = 0
        self.run += 1
        
    def release_move(self):
        self.long_press -= 1 
        self.pic_count = 0
        self.run -= 1
    
        
    def read_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.press_move()
            if event.key == pygame.K_UP:
                self.press_move()
            if event.key == pygame.K_LEFT:
                self.press_move()
                self.direction = 'left'
            if event.key == pygame.K_RIGHT:
                self.press_move()
                self.direction = 'right'
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.release_move()
            if event.key == pygame.K_UP:
                self.release_move()
            if event.key == pygame.K_LEFT:
                self.release_move()
            if event.key == pygame.K_RIGHT:
                self.release_move()
            
            

    
    # 刷新role对象的image属性 主函数只要把image画到窗口就可以渲染动画
    def update(self,count):
        #绘制当前角色
       
        if self.dead == True:
            if  self.direction == 'right':
                self.image = tools.get_image(self.PIC['knight_dead_right'],self.pic_count * 16 , 0, 16, 16, (0,0,0), self.size)
            else:
                self.image = tools.get_image(self.PIC['knight_dead_left'],self.pic_count * 16 , 0, 16, 16, (0,0,0), self.size)
            
        else:
            if count % 5 == 0:
                if not self.run == 0:
                    if self.direction == 'right':
                        self.image = tools.get_image(self.PIC['knight_run'],self.pic_count * 16 , 0, 16, 16, (0,0,0), self.size)
                        self.pic_count = tools.animation_change_pic(self.pic_count,6)
                    else:
                        self.image = tools.get_image(self.PIC['knight_run_left'],(5-self.pic_count) * 16 , 0, 16, 16, (0,0,0), self.size)
                        self.pic_count = tools.animation_change_pic(self.pic_count,6)
                else:
                    if self.direction == 'right':
                        self.image = tools.get_image(self.PIC['knight'],self.pic_count * 16 , 0, 16, 16, (0,0,0), self.size)
                        self.pic_count = tools.animation_change_pic(self.pic_count,6)
                    else:
                        self.image = tools.get_image(self.PIC['knight_left'],self.pic_count * 16 , 0, 16, 16, (0,0,0), self.size)
                        self.pic_count = tools.animation_change_pic(self.pic_count,6)
        

        
        

            
    # 死亡或者存活的动画     
    def dead(self):
        self.dead = True
        
        
    
        