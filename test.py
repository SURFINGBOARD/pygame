#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 19:55:47 2021

@author: chenkanyu
"""
import pygame
import map_comp


pygame.init() #初始化pygame类
screen = pygame.display.set_mode((600,800)) 
pygame.display.set_caption('动画测试') 
candle = map_comp.candle(0,0,"图片/背景","candle")
fps=30
clock = pygame.time.Clock()
count=0

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255,255,255))  
    candle.update(count,([],False))  
    screen.blit(candle.image,(0,0))
    count = count+1
    clock.tick(fps)
    
    pygame.display.flip()
    






