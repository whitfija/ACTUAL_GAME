import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption('Arena 2')
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
    #find image
        self.image = pygame.image.load("images/Player.png").convert()
    #background?
        self.image.set_colorkey(WHITE)
    #scale attempt
        #pygame.transform.scale2x(self.image)
    #define rect
        self.rect = self.image.get_rect()
        def drawplayer(self,surface):
            self = pygame.transform.scale2x(self.image)
            surface.blit(self.image, (self.rect.x, self.rect.y))

        self.rect = self.image.get_rect()

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


sprites = pygame.sprite.Group()

for i in range(50):
    player = Player(RED, 20, 15)
    player.rect.x = 10
    player.rect.y = 768 - 45 - 120-76
    sprites.add(player)

for i in range(50):
    enemy = Enemy(RED, 20, 15)
    enemy.rect.x = 1024-10-44
    enemy.rect.y = 768-45-120-200-100-100-25+2
    sprites.add(enemy)

#add ball to group
for i in range(50):
    ball = Ball(RED, 20, 15)
    ball.rect.x = 10+44-20+5
    ball.rect.y = 768-45-44-30-20-75
    sprites.add(ball)


while True:


    for event in pygame.event.get():
        pygame.draw.rect(screen, RED, (1024-200, 300, 200, 100))
        pygame.draw.rect(screen, GREEN, (0, 768, 420, -120))

        sprites.draw(screen)

        pygame.display.flip()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()







# Enemy class
