import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption('Arena 3')
bg = pygame.image.load("images/grid.png")


#constants representing colours
BLACK = (0,   0,   0)
BROWN = (153, 76,  0)
GREEN = (0,   255, 0)
BLUE  = (0,   0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
screen.fill(WHITE)
screen.blit(bg, (0, 0))


class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # find image
        self.image = pygame.image.load("images/Player.png").convert()
        # background?
        self.image.set_colorkey(WHITE)
        # scale attempt
        # pygame.transform.scale2x(self.image)
        # define rect
        self.rect = self.image.get_rect()

        def drawplayer(self, surface):
            self = pygame.transform.scale2x(self.image)
            surface.blit(self.image, (self.rect.x, self.rect.y))

        self.rect = self.image.get_rect()

        # def move_player(self):
        # key = pygame.key.get_pressed()
        # if key[pygame.K_DOWN]:


class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # find image
        self.image = pygame.image.load("images/Enemy.png").convert()
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
        self.image = pygame.image.load("images/Ball.png").convert()
        # background?
        self.image.set_colorkey(WHITE)
        # scale attempt
        # pygame.transform.scale2x(self.image)
        # define rect
        self.rect = self.image.get_rect()


# Enemy_Hit class
class Enemy_Hit(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # find image
        self.image = pygame.image.load("images/fire.png").convert()
        # background?
        self.image.set_colorkey(WHITE)
        # scale attempt
        # pygame.transform.scale2x(self.image)
        # define rect
        self.rect = self.image.get_rect()


# Enemy_Hit class
class Enemy_Hit(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # find image
        self.image = pygame.image.load("images/fire.png").convert()
        # background?
        self.image.set_colorkey(WHITE)
        # scale attempt
        # pygame.transform.scale2x(self.image)
        # define rect
        self.rect = self.image.get_rect()


sprites = pygame.sprite.Group()

#add player to group
for i in range(50):
   player = Player(RED, 20, 15)
   player.rect.x = 10
   player.rect.y = 768-45-120-300+50-5
   sprites.add(player)

#add enemy to group
for i in range(50):
   enemy = Enemy(RED, 20, 15)
   enemy.rect.x = 1024-10-44-20-20
   enemy.rect.y = 768-45-120-300+50-5
   sprites.add(enemy)

#add ball to group
for i in range(50):
    ball = Ball(RED, 20, 15)
    ball.rect.x = 10+44-20+5
    ball.rect.y = 768 - 45 - 44 - 30 - 20-300+50-5
    sprites.add(ball)


while True:


   for event in pygame.event.get():
       pygame.draw.rect(screen, BLUE, (1024-250, 768-100, 200, -200))
       pygame.draw.circle(screen, (255, 255, 0), (1024-800, 480), 80)
       pygame.draw.circle(screen, (255, 0, 255), (1024-550, 250), 80)
       pygame.draw.circle(screen, (0, 255, 255), (1024-300, 480), 80)
       pygame.draw.rect(screen, BLUE, (0, 768-100, 200, -200))

       sprites.draw(screen)
       pygame.display.flip()
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()


   pygame.display.update()



