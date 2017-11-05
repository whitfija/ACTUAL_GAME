import pygame, sys
from pygame.locals import *
from sys import exit

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

def drawscreen():
    pygame.draw.rect(screen, WHITE, (0, 0, 250, 250))

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.image.load("Player.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()


pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Sprite Test')
sprites = pygame.sprite.Group()

for i in range(50):
    test = Player(BLACK, 20, 15)
    Player.rect.x = 0
    Player.rect.y = 0
    sprites.add(test)



while True: # main game loop
    drawscreen()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
