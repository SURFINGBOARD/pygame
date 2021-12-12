import pygame as gm
import Status
from constant import w, h

# clock = gm.time.Clock()
gm.init()
screen = gm.display.set_mode((w, h))
# screen = gm.display.get_surface()
gm.display.set_caption('blood visualization')
bgpic = gm.image.load("Pictures/backgrounds/bg.jpg").convert()
bgpicView = gm.transform.scale(bgpic, (w, h))
blood = gm.image.load("Pictures/backgrounds/bloodvisualization.jpg").convert()
bloodView = gm.transform.scale(blood, (w/5, h/10))
testrole = Status.Status()
while True:
    for event in gm.event.get():
        if event.type == gm.QUIT:
            gm.quit()
    screen.blit(bgpicView, (0, 0))
    screen.blit(bloodView, (0, 0))

    gm.draw.rect(screen, (250, 0, 0), (60, 20, w/30*testrole.blood, h/21), 0)
    gm.display.update()
    # clock.tick(60)



