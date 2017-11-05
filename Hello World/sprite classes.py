import pygame
from pygame.locals import *
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill([0,0,0])
        self.rect = self.image.get_rect()
