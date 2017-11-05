import pygame, sys
from pygame.locals import *
from sys import exit
from sprite_classes import player

pygame.init()
screen = pygame.display.set_mode((500,500))

def screen():
    pygame.draw.rect(screen, (250, 250, 250), (0, 0, 500, 500))

def drawplayer():
    pygame.draw.player(drawplayer, (0,0,0), ())

while True: # main game loop
    drawplayer()
    drawscreen()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
