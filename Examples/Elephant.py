import pygame
import random

class Elephant(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/elephant.png").convert_alpha()
        self.rect = self.image.get_rect(center=(500, 350))
