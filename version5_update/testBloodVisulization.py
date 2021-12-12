import pygame as gm
import Status
import tools
from constant import w, h

gm.init()
screen = gm.display.set_mode((w, h))
gm.display.set_caption('blood visualization')
bgpic = gm.image.load("Pictures/backgrounds/bg.jpg").convert()
bgpicView = gm.transform.scale(bgpic, (w, h))
bloodView = gm.image.load("Pictures/backgrounds/bloodvisualization.jpg").convert()
bloodView = tools.get_image(bloodView, 0, 0, 80, 16, (255, 255, 255), h/15/16)
testrole = Status.Status()
while True:
    for event in gm.event.get():
        if event.type == gm.QUIT:
            gm.quit()
    screen.blit(bgpicView, (0, 0))
    # testrole as mainrole
    gm.draw.rect(screen, (250, 0, 0), (w/11, h/16, bloodView.get_width()/65*testrole.blood, h/22), 0)
    screen.blit(bloodView, (w/20, h/20))
    gm.display.update()



