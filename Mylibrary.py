# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 00:41:33 2021

@author: CharlieYang,psxcy3
reference to “More python programming for the absolute beginer” by Jonathan S.Harbour 


"""

import random,math,pygame,sys,time
from pygame.locals import *


def print_text(font,x,y,text,color=(255,255,255)):   #print text on the screen
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))
def wrap_angle(angle):
    return abs(angle%360)

def target_angle(x1,y1,x2,y2):           #calculate angle of two point
    delta_x=x2-x1
    delta_y=y2-y1
    angle_radians=math.atan2(delta_y,delta_x)#atan2 function for calculation radian
    angle_degrees=math.degrees(angle_radians)#transform radian into degrees
    return angle_degrees

def distance(point1,point2):#distance between 2 points
    delta_x=point1.x-point2.x
    delta_y=point1.y-point2.y
    dist=math.sqrt(delta_x*delta_x+delta_y*delta_y)
    return dist

class Point(object):#a basic class used as position and velocity(vector)
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        
    def getx(self):
        return self.__x
    def setx(self,x):
        self.__x=x
    x=property(getx,setx)
    
    
    def gety(self):
        return self.__y
    def sety(self,y):
        self.__y=y
    y=property(gety,sety)
    
    def __str__(self):
        return "(X:"+"(:.0F)".format(self.__x)+\
            ",Y:"+"(:.0f".format(self.__y)+")"


class MySprite(pygame.sprite.Sprite):#a basic class derived from sprite
    def __init__(self, target):#target is like where would you draw your instance on e.g. screen,backbuffer
        pygame.sprite.Sprite.__init__(self)#derive the __init__ of pygame.sprite.Sprite 
        self.master_image=None#  the image of instance                    add  or change attributes of MySprite 
        self.frame=0            #set the current anime frame
        self.old_frame=-1       #set the anime frame before
        self.frame_width=1      #set the default frame width
        self.frame_height=1     #set the default frame height
        self.first_frame=0      #set the beginning frame of the anime
        self.last_frame=0       #set the ending frame of the anime
        self.columns=1          #get the number of colums of the anime picture
        self.last_time=0        # an intermediate parameter for currenet_time
        self.direction=0
        self.velocity=Point(0,0)
              
    
    def _getx(self):
        return self.rect.x
    def _setx(self,value):
        self.rect.x=value
    X=property(_getx,_setx)
    
    
    def _gety(self):
        return self.rect.y
    def _sety(self,value):
        self.rect.y=value
    Y=property(_gety,_sety)

    def _getpos(self):
        return self.rect.topleft

    def _setpos(self,pos):
        self.rect.topleft=pos
    position=property(_getpos,_setpos)
    
    
    def load(self,filename,width,height,columns):#set the animation of the instance
        self.master_image=pygame.image.load(filename).convert_alpha()
        self.frame_width=width
        self.frame_height=height
        self.rect=Rect(0,0,width,height)
        self.columns=columns
        
        rect=self.master_image.get_rect()
        self.last_frame=(rect.width//width)*(rect.height//height)-1
        self.set_image(self.master_image,width,height,columns)
        
    def set_image(self,image,width=0,height=0,columns=1):
        self.master_image=image
        if width==0 and height==0:
            self.frame_width=image.get_width()
            self.frame_height=image.get_height()
        else:
            self.frame_width=width
            self.frame_height=height
            rect=self.master_image.get_rect()
            self.last_frame=(rect.width//width)*(rect.height//height)-1
        self.rect=Rect(0,0,self.frame_width,self.frame_height)
        self.columns=columns


    def update(self,current_time,rate=8):
        if self.last_frame>self.first_frame:# for most time
            if current_time>self.last_time+rate:
                self.frame+=1
                if self.frame>self.last_frame:
                    self.frame=self.first_frame#change current frame to the first frame to start next recycle
                self.last_time=current_time
            else:
                self.frame=self.first_frame
        if self.frame!=self.old_frame:
            frame_x=(self.frame%self.columns)*self.frame_width
            frame_y=(self.frame//self.columns)*self.frame_height
            rect=Rect(frame_x,frame_y,self.frame_width,self.frame_height)
            self.image=self.master_image.subsurface(rect)
            self.old_frame=self.frame
    def __str__(self):
        return str(self.frame)+"."+str(self.first_frame)+\
            ","+str(self.last_frame)+","+str(self.frame_width)+\
            ","+str(self.frame_height)+","+str(self.columns)+\
                ","+str(self.rect)