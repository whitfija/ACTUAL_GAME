from pygame.locals import *
import pygame
import math
from time import sleep

class Player(pygame.sprite.Sprite):
    #Starting position and speed
    speed = 6

    def __init__(self):
        super().__init__()

        #Create the Surface
        self.image = pygame.Surface([250, 250])

        #Load the image
        self.image = pygame.image.load("images/paddle.png").convert_alpha()

        #Create a Rectangle to handle location, collision
        self.rect = self.image.get_rect(center=(10, 350))

        #Set the horizontal starting position. This never to change
        self.rect.y = 380
