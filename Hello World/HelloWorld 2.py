import pygame, sys
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500,500))

pygame.sprite.Sprite.add

def screen():
    pygame.draw.rect(screen, (250, 250, 250), (0, 0, 500, 500))

def drawplayer():


#pygame.display.set_caption('Hello World!')
while True: # main game loop


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
