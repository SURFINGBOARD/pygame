import pygame
import tools
from constant import w, h

class monster():

    size = w / 16 / 16
    # speed
    speed_x = 0
    speed_y = 0


class slime(monster):
    
    def __init__(self, x, y):
        self.PIC = tools.load_pictures('Pictures/monster')
        self.pic_count = 0
        self.dead = False
        self.blood = 6
        self.x, self.y = x, y
        self.active = False
        self.long_press = {'up': False, 'down': False, 'right': False, 'left': False} 
        self.speed = self.size * 16/32
        self.dead_time = 0
        self.direction = 'right'
        self.image = tools.get_image(self.PIC['slime'], 0, 0, 16, 16, (0, 0, 0), self.size)
    def active(self):
        pass
    
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
        
    def update(self,count):
        round = count//60
        if self.dead == True: 
            if count % 8 == 0 :
                if count - self.dead_time <= 48:
                    if self.direction == 'left':
                         self.image = tools.get_image(self.PIC['slime_dead_left'],(5-self.pic_count) * 16 , 0, 16, 16, (0,0,0), self.size)
                         self.pic_count = tools.animation_change_pic(self.pic_count,6)
                    else:
                         self.image = tools.get_image(self.PIC['slime_dead'],self.pic_count * 16 , 0, 16, 16, (0,0,0), self.size)
                         self.pic_count = tools.animation_change_pic(self.pic_count,6)
                else:
                    if self.direction == 'left':
                         self.image = tools.get_image(self.PIC['slime_dead_left'],5 * 16, 0, 16, 16, (0,0,0), self.size)
                    else:
                        self.image = tools.get_image(self.PIC['slime_dead'],5 * 16, 0, 16, 16, (0,0,0), self.size)    
        else:
            if count % 6 == 0 :
                if round % 4 == 0:
                    self.image = tools.get_image(self.PIC['slime_run_left'],(5-self.pic_count) * 16 , 0, 16, 16, (255,255,255), self.size)
                    self.pic_count = tools.animation_change_pic(self.pic_count,6)
                    self.x -= self.speed
                    self.direction = 'left'
                elif round % 4 == 1:
                    self.image = tools.get_image(self.PIC['slime_left'],self.pic_count * 16 , 0, 16, 16, (0,0,0), self.size)
                    self.pic_count = tools.animation_change_pic(self.pic_count,6)
                    self.direction = 'left'
                elif round % 4 == 2:
                    self.image = tools.get_image(self.PIC['slime_run'],(5-self.pic_count) * 16 , 0, 16, 16, (255,255,255), self.size)
                    self.pic_count = tools.animation_change_pic(self.pic_count,6)
                    self.direction = 'right'
                    self.x += self.speed
                elif round % 4 == 3:
                    self.image = tools.get_image(self.PIC['slime'],self.pic_count * 16 , 0, 16, 16, (0,0,0), self.size)
                    self.pic_count = tools.animation_change_pic(self.pic_count,6)
                    self.direction = 'right'
                
        
    def dead_(self, count):
        self.dead == True
        self.dead_time = count//60