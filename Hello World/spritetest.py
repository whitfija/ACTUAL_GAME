import pygame, sys
from pygame.locals import *
from sys import exit

#colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.image.load("Enemy.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
    #def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([30,30])
        #self.image.fill([255,0,0])
        #self.rect = self.image.get_rect()


pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Sprite Test')
sprites = pygame.sprite.Group()

for i in range(50):
    test = Player(BLACK, 20, 15)
    test.rect.x = 0
    test.rect.y = 0
    sprites.add(test)
while True: # main game loop
    screen.fill(WHITE)
    sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()