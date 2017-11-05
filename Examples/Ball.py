from pygame.locals import *
import pygame
import math
from time import sleep

class Ball(pygame.sprite.Sprite):
    #Starting position and speed
    speed = 6

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([250, 250])
        self.image = pygame.image.load("images/Ball.png").convert_alpha()
        self.rect = self.image.get_rect(center=(10, 350))
        self.rect.bottom = 770
        self.rect.x = 269.5
        self.rect.y = 369.5
