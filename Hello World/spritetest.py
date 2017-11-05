import pygame, sys
from pygame.locals import *
from sys import exit

#colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)

bg = pygame.image.load("grid.png")

#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
    #find image
        self.image = pygame.image.load("Player.png").convert()
    #background?
        self.image.set_colorkey(WHITE)
    #scale attempt
        #pygame.transform.scale2x(self.image)
    #define rect
        self.rect = self.image.get_rect()
        def drawplayer(self,surface):
            self = pygame.transform.scale2x(self.image)
            surface.blit(self.image, (self.rect.x, self.rect.y))

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

#class Ground(pygame.sprite.Sprite):
 #   def __init__(self, color, width, height):
  #      super().__init__()
   #     self.image = pygame.image.load("Ground.png").convert()
    #    self.image.set_colorkey(WHITE)
     #   self.rect = self.image.get_rect()
#start pygame & set display
pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption('Sprite Test')
#create sprites group
sprites = pygame.sprite.Group()

#add player to group
#for i in range(50):
 #   ground = Ground(RED, 20, 15)
    #ground.rect.x = 0
   # ground.rect.y = 0
  #  sprites.add(ground)

for i in range(50):
    p1 = Player(RED, 20, 15)
    p1.rect.x = 10
    p1.rect.y = 768-45-120
    sprites.add(p1)

#add enemy to group
for i in range(50):
    p1 = Enemy(RED, 20, 15)
    p1.rect.x = 1024-10-44
    p1.rect.y = 768-45-120
    sprites.add(p1)

#add ball to group
for i in range(50):
    p1 = Ball(RED, 20, 15)
    p1.rect.x = 10+44-20+5
    p1.rect.y = 768-45-44-30-20
    sprites.add(p1)

while True: # main game loop
    screen.fill(WHITE)
    screen.blit(bg, (0,0))
    pygame.draw.rect (screen, (0, 0, 0), (0, 768-45, 1024, 45))
    sprites.draw(screen)
    #test.move_player()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()