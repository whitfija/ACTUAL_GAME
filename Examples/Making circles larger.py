import pygame
import random
import math
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 460))
font = pygame.font.SysFont(None, 36)

main_clock = pygame.time.Clock()
 
pygame.key.set_repeat(100, 50)

size = 10
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                size += 10
        if event.type == KEYUP:
            if event.key == K_a:
                size = 10
 
    main_clock.tick(50)
    screen.fill((255, 255, 255))
 
    circle = pygame.draw.circle((screen), (0,0,0), (320, 230), size, 2)
    pygame.display.update()

