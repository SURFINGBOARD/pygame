# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:41:52 2021

@author: 78528
"""
import tools
import pygame
from constant import w, h
import Status

class Role(pygame.sprite.Sprite, Status.Status):
   
    
    size = w / 16 / 16

    #pos
    x,y = w/2 - 32*3/2, h/2 - 32*3/2
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Status.Status.__init__(self, 50)
        self.PIC = tools.load_pictures('Pictures/roleMoving')
        self.image = tools.get_image(self.PIC['knight'],0 , 0, 16, 16, (0,0,0), self.size)
        #direction
        self.direction = 'right'
        
        self.run = 0
        
        self.pic_count = 0
        # press
        self.long_press = 0 
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
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
            if event.key == pygame.K_w:
                self.press_move()
            if event.key == pygame.K_s:
                self.press_move()
            if event.key == pygame.K_a:
                self.press_move()
                self.direction = 'left'
            if event.key == pygame.K_d:
                self.press_move()
                self.direction = 'right'

                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.release_move()
            if event.key == pygame.K_s:
                self.release_move()
            if event.key == pygame.K_a:
                self.release_move()
            if event.key == pygame.K_d:
                self.release_move()
            
            

    

    def update(self,count):
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