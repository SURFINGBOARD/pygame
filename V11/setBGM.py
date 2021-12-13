import pygame
import sys
pygame.mixer.init()
global music,sound
music=['BGM/login.wav',"BGM/fight2.ogg"]
sound=['BGM/success.ogg','BGM/failure.ogg']
def play_music(i):
    pygame.mixer.music.load(music[i])
    pygame.mixer.music.play(loops=-1)
    # pygame.mixer.music.set_volume(0.6)

def play_sound(i):
    pygame.mixer.music.load(sound[i])
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.6)

def stop_sound():
    pygame.mixer.music.stop()

# play_sound(1)
# play_music(0)
# # screen=pygame.display.set_mode([300,300])
# while 1:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             sys.exit()
