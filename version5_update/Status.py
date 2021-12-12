# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:00:52 2021
blood

@author: Zheng Liu
"""

class Status():
    def __init__(self, blood=3, speed=10, score=0, hurt=False, dead=False):
        self.blood = blood  # at beginning: main role own 6 blood at, common monster own 3 blood, boos maybe role.blood multiple 10 times
        self.speed = speed
        self.score = score  # get 1 score when killing a monster
        self.hurt = hurt    # get hurt: True, not hurt: False
        self.dead = dead    # dead: True, alive: False

    # different roles have different movement speed
    # easy to add pick up items function
    def set_speed(self, speed):
        self.speed = speed
    def get_speed(self):
        return self.speed

    # different roles have different weapon types
    # easy to add pick up strong weapon function
    def set_weapon(self, weapon):
        self.speed = weapon
    def get_weapon(self):
        return self.weapon

    # bleed to reduce blood amount when get hurt
    def bleed(self):
        if self.hurt:   # get attack, hurt change to True, then blood-1
            self.blood -= 1

    def dead(self):
        if self.blood == 0:
            self.dead = True