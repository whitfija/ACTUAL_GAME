import pygame
import random
import math
import sys
from pygame.locals import *
 
pygame.init()

screen = pygame.display.set_mode((1024, 768))
screen.fill((255,255,255))
font = pygame.font.SysFont(None, 36)

def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0, 0, 0))
    surface.blit(text_display, (x_pos, y_pos))

#Variables
gamestate = 0

main_clock = pygame.time.Clock()

while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if game_state == 0 or game_state == 3:
                    game_state = 1
            if event.key == K_RETURN:
                if game_state == 3:
                    game_state = 1
    if gamestate == 0:
        draw_text('Press Space to Play', font, screen, 135, 354)
    elif gamestate == 1:
        print ("GS 1!!!!!")
 
    main_clock.tick(50)
    screen.fill((255, 255, 255))
    pygame.display.update()
 
