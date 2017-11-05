import pygame

pygame.init()

DISPLAY = pygame.display.set_mode((1024,768))
pygame.display.set_caption('Arena')

while True:


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    pygame.display.flip()