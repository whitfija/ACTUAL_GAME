import pygame
from pygame.locals import *
from sys import exit

class player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self = pygame.image.load(os.path.join('player', 'Player.png'))
