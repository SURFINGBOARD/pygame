# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 07:45:56 2021

@author: CharlieYang
"""
import sys,time,random,math,pygame
from pygame.locals import *
from Mylibrary import *
global Bullet_type
Bullet_type=0
def angular_velocity(angle): #to calculate the angular velocity for chaseing the mouse direction
    vel=Point(0,0)
    vel.x=math.cos(math.radians(angle))
    vel.y=math.sin(math.radians(angle))
    return vel


class Weapon(MySprite):
    def __init__(self,Bullet_type=0,weapon_file="Pictures/weapons/weapon_0.png"):
        MySprite.__init__(self,screen)
        self.Bullet_type=Bullet_type

        self.load(weapon_file,19,29,1)

        
        
        
        self.rotation=0
        self.float_pos=Point(0,0)
        self.fire_timer=0
        

        
    def update(self,ticks):
        MySprite.update(self,ticks,100)
        self.float_pos.x+=self.velocity.x
        self.float_pos.y+=self.velocity.y
        self.X=int(self.float_pos.x)
        self.Y=int(self.float_pos.y)
        self.position=(self.X,self.Y)
        self.last_frame=0
        self.rotation=wrap_angle(self.rotation)
        angle=self.rotation+90
        self.scratch=pygame.transform.rotate(self.master_image, -angle)
        
        
    def draw(self,surface):
        width,height=self.scratch.get_size()
        center=Point(width/2,height/2)
        self.scratch=pygame.transform.scale(self.scratch, (int(width * 2),int(height * 2)))
        surface.blit(self.scratch,(self.X-center.x,self.Y-center.y))
        
        
class Bullet():
    
    def __init__(self,position,Bullet_type=0):      
        self.Bullet_type=Bullet_type
        if self.Bullet_type==0:              #to get more weapons, create more class Bullet_1,Bullet_2... 
            self.alive=True
            self.color=(250,20,20)
            self.position=Point(position.x,position.y)
            self.velocity=Point(0,0)
            self.rect=Rect(0,0,4,4)
            self.owner=""
        elif self.Bullet_type==1:
            self.alive=True
            self.color=(20,20,20)
            self.position=Point(position.x,position.y)
            self.velocity=Point(0,0)
            self.rect=Rect(0,0,8,8)
            self.owner=""
        elif self.Bullet_type==2:
            self.alive=True
            self.color=(250,20,20)
            self.position=Point(position.x,position.y)
            self.velocity=Point(0,0)
            self.rect=Rect(0,0,4,4)
            self.owner=""
        elif self.Bullet_type==3:
            self.alive=True
            self.color=(250,20,20)
            self.position=Point(position.x,position.y)
            self.velocity=Point(0,0)
            self.rect=Rect(0,0,4,4)
            self.owner=""
    def update(self,ticks):
        if self.Bullet_type==0:
            self.position.x+=self.velocity.x*10.0
            self.position.y+=self.velocity.y*10.0
            if self.position.x<0 or self.position.x>900\
                or self.position.y<0 or self.position.y>600:
                self.alive=False
            self.rect=Rect(self.position.x,self.position.y,4,4)
        elif self.Bullet_type==1:
            self.position.x+=self.velocity.x*10.0
            self.position.y+=self.velocity.y*10.0
            if self.position.x<0 or self.position.x>900\
                or self.position.y<0 or self.position.y>600:
                self.alive=False
            self.rect=Rect(self.position.x,self.position.y,8,8) 
            
        elif self.Bullet_type==2:
            self.position.x+=self.velocity.x*20.0
            self.position.y+=self.velocity.y*20.0
            if self.position.x<0 or self.position.x>900\
                or self.position.y<0 or self.position.y>600:
                self.alive=False
            self.rect=Rect(self.position.x,self.position.y,4,4)
        elif self.Bullet_type==3:
            self.position.x+=self.velocity.x*20.0
            self.position.y+=self.velocity.y*20.0
            if self.position.x<0 or self.position.x>900\
                or self.position.y<0 or self.position.y>600:
                self.alive=False
            self.rect=Rect(self.position.x,self.position.y,4,4)
            
    def draw(self,surface):
        if self.Bullet_type==0:
            pos=(int(self.position.x),int(self.position.y))
            pygame.draw.circle(surface,self.color,pos,4,0)
        elif self.Bullet_type==1:
            pos=(int(self.position.x),int(self.position.y))
            pygame.draw.circle(surface,self.color,pos,8,0)
        elif self.Bullet_type==2:
            pos=(int(self.position.x),int(self.position.y))
            pygame.draw.circle(surface,self.color,pos,4,0)       
        elif self.Bullet_type==3:
            pos=(int(self.position.x),int(self.position.y))
            pygame.draw.circle(surface,self.color,pos,4,0)       
            

class BulletSP(MySprite):
    
    def __init__(self,position,w,h,Bullet_type=0,bullet_file="Pictures/weapons/bullet_0.png"):
        MySprite.__init__(self,screen)
        self.Bullet_type=Bullet_type
        self.load(bullet_file,12,11,1)
        if self.Bullet_type==0:
            self.load(bullet_file,12,11,1)
        elif self.Bullet_type==1:
            self.load("Pictures/weapons/bullet_1.png",16,24,1)
        elif self.Bullet_type==2:
            self.load("Pictures/weapons/bullet_2.png",7,39,1)
        elif self.Bullet_type==3:
            self.load("Pictures/weapons/bullet_3.png",15,42,1)
            
        self.rotation=0
        self.float_pos=Point(position.x,position.y)
        self.alive=True
        self.velocity=Point(0,0)
        self.owner=""
        
        self.w=w
        self.h=h
        
    def update(self,ticks):
        
        if self.Bullet_type==0:
            
            self.float_pos.x+=self.velocity.x*10.0
            self.float_pos.y+=self.velocity.y*10.0
            if self.float_pos.x<0 or self.float_pos.x>9000\
                or self.float_pos.y<0 or self.float_pos.y>6000:
                self.alive=False
            self.rotation=wrap_angle(self.rotation)
            angle=self.rotation+90
            self.scratch=pygame.transform.rotate(self.master_image, -angle)
        elif self.Bullet_type==1:
            self.float_pos.x+=self.velocity.x*10.0
            self.float_pos.y+=self.velocity.y*10.0
            if self.float_pos.x<0 or self.float_pos.x>9000\
                or self.float_pos.y<0 or self.float_pos.y>6000:
                self.alive=False
            self.rotation=wrap_angle(self.rotation)
            angle=self.rotation+90
            self.scratch=pygame.transform.rotate(self.master_image, -angle)
            
        elif self.Bullet_type==2:
            self.float_pos.x+=self.velocity.x*40.0
            self.float_pos.y+=self.velocity.y*40.0
            if self.float_pos.x<0 or self.float_pos.x>9000\
                or self.float_pos.y<0 or self.float_pos.y>6000:
                self.alive=False
            self.rotation=wrap_angle(self.rotation)
            angle=self.rotation+90
            self.scratch=pygame.transform.rotate(self.master_image, -angle)
            
        elif self.Bullet_type==3:
            self.float_pos.x+=self.velocity.x*20.0
            self.float_pos.y+=self.velocity.y*20.0
            if self.float_pos.x<0 or self.float_pos.x>9000\
                or self.float_pos.y<0 or self.float_pos.y>6000:
                self.alive=False
            self.rotation=wrap_angle(self.rotation)
            angle=self.rotation+90
            self.scratch=pygame.transform.rotate(self.master_image, -angle)
        self.X=int(self.float_pos.x)
        self.Y=int(self.float_pos.y) 
        
    def draw(self,surface):
        if self.Bullet_type==0:
           
            width,height=self.scratch.get_size()
            center=Point(width/2,height/2)
            self.scratch=pygame.transform.scale(self.scratch, (self.w//400*width,self.w//400*height))
            surface.blit(self.scratch,(self.X-center.x,self.Y-center.y))
        elif self.Bullet_type==1:
            width,height=self.scratch.get_size()
            center=Point(width/2,height/2)
            self.scratch=pygame.transform.scale(self.scratch, (self.w//300*width,self.w//300*height))
            surface.blit(self.scratch,(self.X-center.x,self.Y-center.y))
        elif self.Bullet_type==2:
            width,height=self.scratch.get_size()
            center=Point(width/2,height/2)
            self.scratch=pygame.transform.scale(self.scratch, (self.w//400*width,self.w//400*height))
            surface.blit(self.scratch,(self.X-center.x,self.Y-center.y))       
        elif self.Bullet_type==3:
            width,height=self.scratch.get_size()
            center=Point(width/2,height/2)
            self.scratch=pygame.transform.scale(self.scratch, (self.w//400*width,self.w//400*height))
            surface.blit(self.scratch,(self.X-center.x,self.Y-center.y))     


def read_event():
        global Bullet_type
        b1,b2,b3=pygame.mouse.get_pressed()
        keys=pygame.key.get_pressed()#press1/2/3/4/5/6  and change Bullets_i parameter
        if keys[K_ESCAPE]:
            going=False
        elif keys[K_0]:
            Bullet_type=0
        elif keys[K_1]:
            Bullet_type=1
        elif keys[K_2]:
            Bullet_type=2
        elif keys[K_3]:
            Bullet_type=3 
            
        if keys[K_SPACE] or mouse_up>0 and (Bullet_type==0 or Bullet_type==1):
            if ticks>weapon.fire_timer+500:
                weapon.fire_timer=ticks
                Bullet.player_fire_cannon()
        
        elif keys[K_SPACE] or mouse_up>0 and (Bullet_type==2):
            if ticks>weapon.fire_timer+200:
                weapon.fire_timer=ticks
                Bullet.player_fire_cannon()
            
        elif keys[K_SPACE] or b1>0 and (Bullet_type==3):
            if ticks>weapon.fire_timer+5:        
                weapon.fire_timer=ticks
                Bullet.player_fire_cannon()

            
def game_init():
    global screen,backbuffer,font,timer,player_group,weapon,\
            enemy,crosshair,crosshair_group,bullets
    pygame.init()
    screen=pygame.display.set_mode((900,600))
    backbuffer=pygame.Surface((900,600))
    bgpic=pygame.image.load("data/bg.jpg").convert()
    
    pygame.display.set_caption("Weapon example")
    font=pygame.font.Font(None,30)
    timer=pygame.time.Clock()
    pygame.mouse.set_visible(False)
    
    weapon=Weapon()
    weapon.float_pos=Point(200,100)
        
        
    crosshair=MySprite(screen)
    crosshair.load("data/crosshair_1.png",16,16,1)
    crosshair_group=pygame.sprite.GroupSingle()
    crosshair_group.add(crosshair)

game_init()
bullets=list()
game_over=False
last_time=0

mouse_x=mouse_y=0    


going=False


while going:
    
    timer.tick(30)
    ticks=pygame.time.get_ticks()
    
    
    mouse_up=mouse_down=0
    mouse_up_x=mouse_up_y=0
    mouse_down_x=mouse_down_y=0
        
    for event in pygame.event.get():
        if event.type==QUIT:
            going=False
        elif event.type==MOUSEMOTION:
            mouse_x,mouse_y=event.pos
            move_x,move_y=event.rel
        elif event.type==MOUSEBUTTONDOWN:
            mouse_down=event.button
            mouse_down_x,mouse_down_y=event.pos
        elif event.type==MOUSEBUTTONUP:
            mouse_up=event.button
            mouse_up_x,mouse_up_y=event.pos
    
    
    Bullet.read_event()
    if not game_over:
        crosshair.position=(mouse_x,mouse_y)
        crosshair_group.update(ticks)
        
    angle=target_angle(weapon.X,weapon.Y,crosshair.X+crosshair.frame_width/2,
                       crosshair.Y+crosshair.frame_height/2)
    weapon.rotation=angle
    weapon.update(ticks)
    for bullet in bullets:
        bullet.update(ticks)
        '''
        if bullet.owner=="weapon":
            if pygame.sprite.collide_rect(bullet, enemy):
                bullet.alive=False
                if Bullet_type==1:
                    bullet.alive=True'''
    backbuffer.fill((0,0,0))
    for bullet in bullets:
        bullet.draw(backbuffer)
            
    weapon.draw(backbuffer)
    crosshair_group.draw(backbuffer)
    for bullet in bullets:
        if bullet.alive==False:
            bullets.remove(bullet)          
    
    
    screen.blit(backbuffer,(0,0))    
    pygame.display.update()

pygame.quit()