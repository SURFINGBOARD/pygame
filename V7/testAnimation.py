#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 19:55:47 2021

@author: chenkanyu
"""
import pygame
import animation


pygame.init() #初始化pygame类
screen = pygame.display.set_mode((600,800)) 
pygame.display.set_caption('动画测试') 
# treasures = animation.picToAnim(0,0,"static/things","treasures",(255, 255, 255),8,16,16)
# candle = animation.picToAnim(0,0,"static/things","candles",(255, 255, 255),6,16,16)
# boom = animation.picToAnim(0,0,"static/things","boom",(0, 0, 0),7,32,32)
coin = animation.picToAnim(0,0,"static/things","coins",(0, 0, 0),6,16,16,True)
fps=30
clock = pygame.time.Clock()
count=0

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255,255,255))
    # play loop
    # treasures.update(count,([],False))
    # screen.blit(treasures.image,(0,0))
    # candle.update(count,([],False))
    # screen.blit(candle.image,(0,0))
    coin.update(count,([],False))
    screen.blit(coin.image,(0,0))


    # play once
    # group = pygame.sprite.Group(boom)
    # group.update(count,([],False))
    # if boom.killing == True:
    #     boom.kill()
    # group.draw(screen)
    count = count+1
    clock.tick(fps)
    
    pygame.display.flip()
    






