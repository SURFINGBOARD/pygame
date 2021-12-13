import pygame
pygame.mixer.init()
global music,sound
music=['BGM/menu.ogg',"BGM/fight2.ogg"]
sound=['BGM/failure.ogg','BGM/success.ogg']
def play_music(i):
    pygame.mixer.music.load(music[i])
    pygame.mixer.music.play(loops=-1)

def play_sound(i):
    pygame.mixer.music.load(sound[i])
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.6)

def stop_sound():
    pygame.mixer.music.stop()