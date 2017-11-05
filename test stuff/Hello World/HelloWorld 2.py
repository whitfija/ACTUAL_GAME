import pygame, sys
from pygame.locals import *
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill([255,0,0])
        self.rect = self.image.get_rect()

    def move_player(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:

            self.rect.y += 1
        elif key[pygame.K_UP]:
            self.rect.y -= 1
        elif key[pygame.K_RIGHT]:
            self.rect.x += 1
        elif key[pygame.K_LEFT]:
            self.rect.x -= 1
    def add_to_group(self):
        all_sprite_list.add(self)

    def remove_from_group(self):
        all_sprite_list.remove(self)

    def draw(self,surface):
        surface.blit(self.image,(self.rect.x, self.rect.y))

###pygame.image.load(os.path.join('player', 'Player.png'))

pygame.init()
screen = pygame.display.set_mode((500,500))

player = Player()

def drawscreen():
    pygame.draw.rect(screen, (250, 250, 250), (0, 0, 500, 500))

def drawplayer():
    player.draw(screen)

while True: # main game loop
    drawscreen()
    player.move_player()
    drawplayer()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
