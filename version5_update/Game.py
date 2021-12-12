# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:48:49 2021

@author: Yufan Chen
@updater: Zheng Liu
"""
import pygame
import role
from constant import w, h
import tools
import monster


class Game():
    def __init__(self):
        self.pause = False

        self.mode = 'game'
        # create a game clock
        self.clock = pygame.time.Clock()

        # animation controller (FPS amount)
        self.count = 0

        pygame.init()

        # windows setting
        pygame.display.set_mode((w, h))
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("PIXCEL KNIGHT")

        # load background picture,transform
        bgpic = pygame.image.load("Pictures/backgrounds/bg.jpg")
        self.bgpic = pygame.transform.scale(bgpic, (w, h))

        # construct role role
        self.main_role = role.Role()
        self.monster1 = monster.slime(3 / 4 * w, h / 2)
        # self.menu_pic = tools.load_pictures('Pictures/menu')

    # mian loop of game
    def run(self):
        while True:
            self.count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.main_role.read_event(event)
                self.monster1.read_event(event)
                # add new event at here

            # change location
            self.main_role.update(self.count)
            self.monster1.update_pos()
            self.monster1.update(self.count)
            # add current frame here

            # rendering
            self.screen.blit(self.bgpic, (0, 0))
            self.screen.blit(self.main_role.image, (self.main_role.x, self.main_role.y))
            self.screen.blit(self.monster1.image, (self.monster1.x, self.monster1.y))
            # add rendering here

            pygame.display.update()
            # set as 60 frames per frame
            self.clock.tick(60)

    def menu(self):
        while self.mode == 'menu':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        # code of menu