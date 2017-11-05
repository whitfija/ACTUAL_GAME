import pygame
import random
import math
import sys
from pygame.locals import *
from Enemy import Enemy
from Elephant import Elephant

pygame.init()

screen = pygame.display.set_mode((640, 460))
background = pygame.Surface((640, 460), 0, screen)
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
font = pygame.font.SysFont(None, 36)

def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1(0,0,0))
    surface.blit(text_display, (x_pos, y_pos))

main_clock = pygame.time.Clock()

rock = Enemy()
enemy_group = pygame.sprite.Group()
enemy_group.add(rock)

pet = Elephant()
all_sprites = pygame.sprite.Group()
all_sprites.add(pet)
all_sprites.add(rock)

while True:
    #check for events
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    main_clock.tick(50)
    #adding the collision_hit_list
    collision_hit_list = pygame.sprite.spritecollide(pet, enemy_group, False)
    all_sprites.clear(screen, background)
    all_sprites.draw(screen)
    enemy_group.update()
    pygame.display.update()
























    
