import pygame
import tools
from constant import w, h
import obj
import Status



class slime(obj.obj, Status.Status):
    
    def __init__(self,x,y,pic_group,pic):
        obj.obj.__init__(self,x,y,pic_group,pic)
        Status.Status.__init__(self)
        self.active = False
        self.dead_time = 0
        self.direction = 'right'
        self.blood = 65
        self.size = w * 5 / 16 / 16
        self.rect = pygame.Rect(self.x, self.y, 16*self.size, 16*self.size)
    def active(self):
        pass
    
    
        
    def update(self,count,pos1):
        self.update_pos()
        if pos1[2] == True:
            self.undo_update_pos()
        if not pos1[0] == []:
            if (tools.caculate_distance(pos1[1],self.rect.center)) > (tools.caculate_distance(pos1[1],(self.x+self.rect.width/2,self.y + self.rect.height/2))):
               self.undo_update_pos()
            
        
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
                    if pos1[0] == []:
                        self.x -= 3*self.speed
                    
                    self.direction = 'left'
                elif round % 4 == 1:
                    self.image = tools.get_image(self.PIC['slime_left'],self.pic_count * 16 , 0, 16, 16, (0,0,0), self.size)
                    self.pic_count = tools.animation_change_pic(self.pic_count,6)
                    self.direction = 'left'
                    self.y -= 3*self.speed
                elif round % 4 == 2:
                    self.image = tools.get_image(self.PIC['slime_run'],(5-self.pic_count) * 16 , 0, 16, 16, (255,255,255), self.size)
                    self.pic_count = tools.animation_change_pic(self.pic_count,6)
                    self.direction = 'right'
                    if pos1[0] == []:
                        self.x += 3*self.speed
                elif round % 4 == 3:
                    self.image = tools.get_image(self.PIC['slime'],self.pic_count * 16 , 0, 16, 16, (0,0,0), self.size)
                    self.pic_count = tools.animation_change_pic(self.pic_count,6)
                    self.direction = 'right'
                    self.y += 3*self.speed
               
        self.rect.x = self.x
        self.rect.y = self.y
        
    def dead_(self, count):
        self.dead == True
        self.dead_time = count//60