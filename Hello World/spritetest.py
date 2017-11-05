import pygame, sys
from pygame.locals import *
from sys import exit

#colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)

#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
    #find image
        self.image = pygame.image.load("Player.png").convert()
    #background?
        self.image.set_colorkey(WHITE)
<<<<<<< HEAD
=======
    #scale attempt
        #pygame.transform.scale2x(self.image)
    #define rect
        self.rect = self.image.get_rect()
        def drawplayer(self,surface):
            self = pygame.transform.scale2x(self.image)
            surface.blit(self.image, (self.rect.x, self.rect.y))
>>>>>>> 5d5cae072ccd47948e5ce13f3207f3f984411288
        #def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([30,30])
        #self.image.fill([255,0,0])
        self.rect = self.image.get_rect()

    #def move_player(self):
        #key = pygame.key.get_pressed()
        #if key[pygame.K_DOWN]:

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
    # find image
        self.image = pygame.image.load("Enemy.png").convert()
    # background?
        self.image.set_colorkey(WHITE)
    # scale attempt
        # pygame.transform.scale2x(self.image)
    # define rect
        self.rect = self.image.get_rect()

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # find image
        self.image = pygame.image.load("Ball.png").convert()
        # background?
        self.image.set_colorkey(WHITE)
        # scale attempt
        # pygame.transform.scale2x(self.image)
        # define rect
        self.rect = self.image.get_rect()

#start pygame & set display
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Sprite Test')
#create sprites group
sprites = pygame.sprite.Group()

#add player to group
for i in range(50):
    p1 = Player(RED, 20, 15)
    p1.rect.x = 10
    p1.rect.y = 10
    sprites.add(p1)

#add enemy to group
for i in range(50):
    p1 = Enemy(RED, 20, 15)
    p1.rect.x = 10
    p1.rect.y = 210
    sprites.add(p1)

#add ball to group
for i in range(50):
    p1 = Ball(RED, 20, 15)
    p1.rect.x = 10
    p1.rect.y = 410
    sprites.add(p1)

while True: # main game loop
    screen.fill(WHITE)
    sprites.draw(screen)
    #test.move_player()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()