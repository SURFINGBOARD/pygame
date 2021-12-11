# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:48:49 2021

@author: 78528
"""
import pygame
import role
import tools
from constant import w,h
import monster

class Game():
    def __init__(self):
        self.pause = False
        
        self.mode = 'game'
        #clock
        self.clock = pygame.time.Clock()
        
        # animation controler
        self.count = 0
        
        pygame.init()
        
        # 设置窗口
        pygame.display.set_mode((w, h))
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("PIXCEL KNIGHT")
        
        
        
        # load background picture,transform
        bgpic = pygame.image.load("图片/背景/bg.jpg")
        self.bgpic = pygame.transform.scale(bgpic, (w, h))
        
        #construct role role
        self.main_role = role.Role()
        self.monster1 = monster.slime(3/4*w, h/2)
        self.menu_pic = tools.load_pictures('图片/菜单')
        
    
    # mian loop of game
    def run(self):
        while True:
            self.menu()
            self.game()
            
            
    def game(self):
        while self.mode == 'game':
            if self.pause == True:
                continue
            self.count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.main_role.read_event(event)
                self.monster1.read_event(event)
                #事件相关加这里
            
            
            #   改变位置
            self.main_role.update(self.count)
            self.monster1.update_pos()
            self.monster1.update(self.count)
            # 准备当前帧加这里
        
            # rendering
            self.screen.blit(self.bgpic, (0, 0))
            self.screen.blit(self.main_role.image, (self.main_role.x, self.main_role.y))
            self.screen.blit(self.monster1.image, (self.monster1.x, self.monster1.y))
            # 渲染窗口加这里
            pygame.display.update()
            self.clock.tick(60)
      
    def menu(self):
        while self.mode == 'menu':
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            # code of menu
            