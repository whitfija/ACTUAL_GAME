import pygame, sys
background_colour = (255, 255, 255)
(width, height) = (700, 700)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.init()

WHITE = (255,255, 255)
BLACK = (0,0,0)

guyx=50
guyy=600
ammox = guyx
ammoy = guyy
AMMO = pygame.draw.circle(screen, BLACK, (ammox, ammoy), 10)

pygame.display.flip()

running = True
while running:

    for event in pygame.event.get():

        for event in pygame.event.get():
            
            pygame.display.flip()
            if event.type == pygame.QUIT:
                running = False


        AMMO
        ammox+=5
        ammoy-=5


        pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False

