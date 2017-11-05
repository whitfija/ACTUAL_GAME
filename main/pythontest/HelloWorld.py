import pygame, sys
from Tkinter import *


background_colour = (255, 255, 255)
(width, height) = (700, 700)
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

guyx = 50
guyy = 600
ammox = guyx
ammoy = guyy
AMMO = pygame.draw.circle(screen, BLACK, (ammox, ammoy), 10)

pygame.display.flip()

running = True
while running:




    root = Tk()
    v = IntVar()

    Label(root, text="Choose a function:", justify=LEFT, padx=20).pack()
    Radiobutton(root, text="Python", padx=20, variable=v, value=1).pack(anchor=W)
    Radiobutton(root, text="Perl", padx=20, variable=v, value=2).pack(anchor=W)

    #btn = tkinter.Button(window, text="Ok", command=pygame.QUIT)
    #btn.pack()

    #def quit(root):
     #   root.destroy()



    mainloop()



    #if user press ok then close box and prompt eq

    for event in pygame.event.get():

        AMMO
        ammox += 5
        ammoy -= 5



    pygame.display.flip()
    if event.type == pygame.QUIT:
        running = False