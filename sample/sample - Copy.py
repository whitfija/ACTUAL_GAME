import pygame, sys, easygui, math
from pygame.locals import *
import time
from sys import exit
from tkinter import Tk, Label, Button



#colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
hit = False
coeff = 0
bg = pygame.image.load("i
#Player classmages/grid.png")

#gamestate
gamestate = 0


#Main

while leave == False:
    if gamestate == 0:
        screen.fill(WHITE)
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Some text!", 1, (255, 255, 0))
        screen.blit(label, (100, 100))

    elif gamestate == 1:
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


        class App1:
            func = 0

            def __init__(self, master):
                def funcTo(num):
                    App1.func = num
                    print(App1.func)
                    master.quit
                    root.withdraw()

                self.master = master
                master.title("A simple GUI")
                self.label = Label(master, text="Choose")
                self.label.pack()
                self.greet_button = Button(master, text="level one", command=lambda: funcTo(1))
                self.greet_button.pack()
                self.greet_button = Button(master, text="level two", command=lambda: funcTo(2))
                self.greet_button.pack()


        class App2:
            func = 0

            def __init__(self, master):
                def funcTo(num):
                    App2.func = num
                    print(App2.func)
                    master.quit
                    root.withdraw()

                self.master = master
                master.title("A simple GUI")
                self.label = Label(master, text="Choose")
                self.label.pack()
                self.greet_button = Button(master, text="line", command=lambda: funcTo(1))
                self.greet_button.pack()
                self.greet_button = Button(master, text="Parabola", command=lambda: funcTo(2))
                self.greet_button.pack()
                self.greet_button = Button(master, text="Exponential", command=lambda: funcTo(3))
                self.greet_button.pack()
                self.close_button = Button(master, text="OK", command=master.quit)
                self.close_button.pack()


        class App3:
            func = 0

            def __init__(self, master):
                def funcTo(num):
                    App3.func = num
                    print(App3.func)
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

        # add player to group
        pygame.init()
        screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption('Level 1')
        # create sprites group
        sprites = pygame.sprite.Group()
        hitsprites = pygame.sprite.Group()
        for i in range(50):
            player = Player(RED, 20, 15)
            player.rect.x = 10
            player.rect.y = 768 - 45 - 120
            sprites.add(player)

        # add enemy to group
        for i in range(50):
            enemy = Enemy(RED, 20, 15)
            enemy.rect.x = 1024 - 10 - 44
            enemy.rect.y = 768 - 45 - 120
            sprites.add(enemy)

        # add ball to group
        for i in range(50):
            ball = Ball(RED, 20, 15)
            ball.rect.x = 10 + 44 - 20 + 5
            ball.rect.y = 768 - 45 - 44 - 30 - 20
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
                starttime = pygame.time.get_ticks()
                screen.fill(WHITE)
                screen.blit(bg, (0, 0))
                pygame.draw.rect(screen, (0, 0, 0), (0, 768 - 45, 1024, 45))
                sprites.draw(screen)
                pygame.display.update()
                go = True
                while go:
                    currenttime = pygame.time.get_ticks()
                    if currenttime - starttime < 6000:
                        ball.rect.x += 1
                        ball.rect.y += -coeff
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
                    if (ball.rect.x >= enemy.rect.x and ball.rect.x <= enemy.rect.x + 44) and (
                            ball.rect.y >= enemy.rect.y and ball.rect.y <= enemy.rect.y + 120):
                        go = False
                        return True

        started1 = False
        started2 = False
        started3 = False
        leave = False
        while hit == False: # main game loop
            screen.fill(WHITE)
            screen.blit(bg, (0,0))
            pygame.draw.rect (screen, (0, 0, 0), (0, 768-45, 1024, 45))

            #if started1 == False:
                #root = Tk()
                #app = App1(root)
                #root.mainloop()
                #started1 = True
            #root.withdraw()

            #if started2 == False:
                #root = Tk()
                #app = App2(root)
                #root.mainloop()
                #started2 = True
            #root.withdraw()

            #if App1.func == 1:
            hit = line(ball, enemy, coeff)
            #elif App1.func == 2:
            #    hit = line(ball, enemy, coeff)
            #else: continue

            if hit:
                showFire()
                root = Tk()
                app = App3(root)
                root.mainloop()
                started3 = True
                root.withdraw()

        if App3.func == 1:
            leave = False
        elif App3.func == 2:
            leave = True
        else: continue

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()


