import pygame, sys
from pygame.locals import *
from sys import exit
from tkinter import Tk, Label, Button

class App:
    func = 0

#if func == 1:
    #x ** 1/2

    def __init__(self, master):
        def funcTo(num):
            App.func = num
            print(App.func)
            root.withdraw()
        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text="Choose")
        self.label.pack()
        self.greet_button = Button(master, text="SQRT", command= lambda: funcTo(1))
        self.greet_button.pack()
        self.greet_button = Button(master, text="Parabola", command= lambda: funcTo(2))
        self.greet_button.pack()
        self.greet_button = Button(master, text="Exponential", command= lambda: funcTo(3))
        self.greet_button.pack()
        self.close_button = Button(master, text="OK", command=master.quit)
        self.close_button.pack()

#colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)

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

#start pygame & set display
pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption('Level 1')
#create sprites group
sprites = pygame.sprite.Group()

#add player to group
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

started = False

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
    if started == False:
        root = Tk()
        app = App(root)
        root.mainloop()
        started = True
    root.withdraw()