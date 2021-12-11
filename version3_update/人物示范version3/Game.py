# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:48:49 2021

@author: Yufan Chen
@updater: Zheng Liu
"""
import pygame
import role
from constant import w, h

class Game():
    def __init__(self):
        # create a game clock
        self.clock = pygame.time.Clock()
        
        # animation controller (FPS amount)
        self.count = 0
        
        pygame.init()
        
        # windows setting
        pygame.display.set_mode((w, h))
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("testing game")

        # load background picture,transform
        bgpic = pygame.image.load("图片/背景/bg.jpg")
        self.bgpic = pygame.transform.scale(bgpic, (w, h))
        
        # construct role role
        self.main_role = role.Role()
    
    # mian loop of game
    def run(self):
        while True:
            self.count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.main_role.read_event(event)

            # change location
            self.main_role.dead(False, self.count)
            # refresh the surface
            self.main_role.update()
        
            # rendering
            self.screen.blit(self.bgpic, (0, 0))
            self.screen.blit(self.main_role.image, (self.main_role.x, self.main_role.y))
            pygame.display.update()
            # set as 60 frames per frame
            self.clock.tick(60)