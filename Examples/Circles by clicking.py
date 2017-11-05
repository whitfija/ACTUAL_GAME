import pygame
import random
import math
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 460))
font = pygame.font.SysFont(None, 36)

main_clock = pygame.time.Clock()
circles = []

def create_circle(mouse_x, mouse_y):
    circle = pygame.draw.circle((screen), (0,0,0), (mouse_x, mouse_y), 15, 2)
    circle.append(circle)

def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0,0,0))
    surface.blit(text_display, (x_pos, y_pos))

while True:
    main_clock.tick(40)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            create_circle(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        for circle in circles:
            circle = pygame.draw.circle((screen), (0,0,0), (circle.x, circle.y), 15, 2)
            
    main_clock.tick(50)
    screen.fill((255,255,255))
    pygame.display.update()
