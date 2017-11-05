import pygame, sys
from pygame.locals import *
import time
from sys import exit

#colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
hit = False
coeff = 1
bg = pygame.image.load("images/grid.png")

#Player class
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

    #def move_player(self):
        #key = pygame.key.get_pressed()
        #if key[pygame.K_DOWN]:

# Enemy class
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

#start pygame & set display
pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption('Level 1')
#create sprites group
sprites = pygame.sprite.Group()
hitsprites = pygame.sprite.Group()

#add player to group
for i in range(50):
    player = Player(RED, 20, 15)
    player.rect.x = 10
    player.rect.y = 768-45-120
    sprites.add(player)

#add enemy to group
for i in range(50):
    enemy = Enemy(RED, 20, 15)
    enemy.rect.x = 1024-10-44
    enemy.rect.y = 768-45-120
    sprites.add(enemy)

#add ball to group
for i in range(50):
    ball = Ball(RED, 20, 15)
    ball.rect.x = 10+44-20+5
    ball.rect.y = 768-45-44-30-20
    sprites.add(ball)


    def showFire():
        for i in range(50):
            enemy_hit = Enemy_Hit(RED, 20, 15)
            enemy_hit.rect.x = 1024 - 95
            enemy_hit.rect.y = 768 - 45 - 120
            hitsprites.add(enemy_hit)
            hitsprites.draw(screen)
            pygame.display.update()
            pygame.display.flip()
            pygame.time.delay(3000)
            screen.fill(WHITE)
            screen.blit(bg, (0, 0))
            pygame.draw.rect(screen, (0, 0, 0), (0, 768 - 45, 1024, 45))
            sprites.draw(screen)
            pygame.display.update()

    def line(ball, enemy, coeff):
        screen.fill(WHITE)
        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (0, 768 - 45, 1024, 45))
        sprites.draw(screen)
        pygame.display.update()
        go = True
        while go:
            if time < 0.021184*2:
                ball.rect.x += 1
                ball.rect.y += -coeff
            elif time >= 0.021184*2:
                ball.rect.x = 100
                ball.rect.y = 100
            else:
                break
            screen.fill(WHITE)
            screen.blit(bg, (0, 0))
            pygame.draw.rect(screen, (0, 0, 0), (0, 768 - 45, 1024, 45))
            sprites.draw(screen)
            pygame.display.update()
            pygame.display.flip()
            if (ball.rect.x >= enemy.rect.x and ball.rect.x<= enemy.rect.x+44) and (ball.rect.y >= enemy.rect.y and ball.rect.y <= enemy.rect.y+120):
                go = False
                return True


while True:
    while hit == False: # main game loop
        time = time.clock()
        screen.fill(WHITE)
        screen.blit(bg, (0,0))
        pygame.draw.rect (screen, (0, 0, 0), (0, 768-45, 1024, 45))
        hit = line(ball, enemy, coeff)
        if hit:
            showFire()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()



