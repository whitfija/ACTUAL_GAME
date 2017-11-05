import pygame
from pygame.locals import *
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self = pygame.image.load
