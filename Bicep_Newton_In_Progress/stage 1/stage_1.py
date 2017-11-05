import pygame, sys, math, easygui, os
from easygui import enterbox
from pygame.locals import *
import time
from sys import exit
import tkinter as tk
import tkinter as tk2
import tkinter as tk3
from tkinter import *

pygame.init()

#colors
BLACK = (0,   0,   0)
RED = (255,   0,   0)
WHITE = (255,255,255)
#declarations
hit = False
coeff = 1
bg = pygame.image.load("images/grid.png")

#sprite classes
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

# start pygame & set display
screen = pygame.display.set_mode((1024, 768),0,0)
pygame.display.set_caption('Level 1')
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
time.sleep(2)
# create sprites group
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
    ball.rect.y = 768 - 45 - 44 - 30 - 20
    sprites.add(ball)

#Window Classes
class LevelSelect:
    func = 0
    def __init__(self, master):
        def funcTo(num):
            LevelSelect.func = num
            print(LevelSelect.func)
            root.withdraw()
            root.destroy()

        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text="Choose")
        self.label.pack()
        self.greet_button = Button(master, text="Level one", command=lambda: funcTo(1))
        self.greet_button.pack()
        self.greet_button = Button(master, text="Level two", command=lambda: funcTo(2))
        self.greet_button.pack()


class SelectEquation:
    func = 0

    def __init__(self, master):
        def funcTo(num):
            SelectEquation.func = num
            print(SelectEquation.func)
            root2.withdraw()
            root2.destroy()
        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text="Choose")
        self.label.pack()
        self.greet_button = Button(master, text="line", command= lambda: funcTo(1))
        self.greet_button.pack()
        self.greet_button = Button(master, text="Parabola", command= lambda: funcTo(2))
        self.greet_button.pack()
        self.greet_button = Button(master, text="Exponential", command= lambda: funcTo(3))
        self.greet_button.pack()
        self.close_button = Button(master, text="OK", command=master.quit)
        self.close_button.pack()

class TypeCoeff(object):
    value= enterbox(msg='blah',title='coe')
    print(value)
    coeff = value

class LoseWindow:
    func = 0

    def __init__(self, master):
        def funcTo(num):
            LoseWindow.func = num
            print(LoseWindow.func)
            master.quit
            root.withdraw()

        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text="Do you want to leave the game?")
        self.label.pack()
        self.greet_button = Button(master, text="Play Again!", command=lambda: funcTo(1))
        self.greet_button.pack()
        self.greet_button = Button(master, text="Quit", command=lambda: funcTo(2))
        self.greet_button.pack()


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

#playing function
def playlv1():
    hit = False
    while True:
        while hit == False:  # main game loop
            screen.fill(WHITE)
            screen.blit(bg, (0, 0))
            pygame.draw.rect(screen, (0, 0, 0), (0, 768 - 45, 1024, 45))
            root2.mainloop()

            if SelectEquation.func == 1:
                hit = line(ball, enemy, coeff)
            elif SelectEquation.func == 2:
                hit = parabola(ball, enemy, coeff)
            elif SelectEquation.func == 3:
                hit = sine(ball, enemy, coeff)
            else: continue
            if hit == True:
                showFire()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def line(ball, enemy, coeff):
    stime = pygame.time.get_ticks()
    screen.fill(WHITE)
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), (0, 768 - 45, 1024, 45))
    sprites.draw(screen)
    pygame.display.update()

    #m = TypeCoeffPt2(root3)
    #root3.mainloop()
    #coeff = m.entryValue()

    go = True
    while go:
        ltime = pygame.time.get_ticks()
        print(ltime)
        print(stime)
        if ltime-stime < 5500:
            ball.rect.x += 1
            ball.rect.y += (int)((0-coeff)*ball.rect.x)
        else:
            ball.rect.x = ball.rect.x
            ball.rect.y = ball.rect.y
            easygui.msgbox("You missed the target!", title="Wrong")
            go = False
            return False
        screen.fill(WHITE)
        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (0, 768 - 45, 1024, 45))
        sprites.draw(screen)
        pygame.display.update()
        pygame.display.flip()
        if (ball.rect.x >= enemy.rect.x and ball.rect.x<= enemy.rect.x+44) and (ball.rect.y >= enemy.rect.y and ball.rect.y <= enemy.rect.y+120):
            go = False
            return True

def parabola(ball, enemy, coeff):
    stime = pygame.time.get_ticks()
    screen.fill(WHITE)
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), (0, 768 - 45, 1024, 45))
    sprites.draw(screen)
    pygame.display.update()

    #m = TypeCoeffPt2(root3)
    #root3.mainloop()
    #coeff = m.entryValue()

    go = True
    while go:
        ltime = pygame.time.get_ticks()
        print(ltime)
        print(stime)
        if ltime-stime < 5500:
            ball.rect.x += 1
            ball.rect.y += -coeff*(ball.rect.x**2)
        else:
            ball.rect.x = ball.rect.x
            ball.rect.y = ball.rect.y
            easygui.msgbox("You missed the target!", title="Wrong")
            go = False
            return False
        screen.fill(WHITE)
        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (0, 768 - 45, 1024, 45))
        sprites.draw(screen)
        pygame.display.update()
        pygame.display.flip()
        if (ball.rect.x >= enemy.rect.x and ball.rect.x<= enemy.rect.x+44) and (ball.rect.y >= enemy.rect.y and ball.rect.y <= enemy.rect.y+120):
            go = False
            return True
root = tk.Tk()
app = LevelSelect(root)

root2 = tk2.Tk()
app2 = SelectEquation(root2)

#root3 = tk3.Tk()

started1 = False
started2 = False
started3 = False
leave = False

#Main Loop

while leave == False:
    if started1 == False:
        started1 = True
        LevelSelect.func = 1
        root.mainloop()
        if LevelSelect.func == 1:
            print(SelectEquation.func)
            playlv1()

        elif LevelSelect.func == 2:
            if SelectEquation.func == 1:
                play()
            elif SelectEquation.func == 2:
                play()
            elif SelectEquation.func == 3:
                play()

        else: print("nada")