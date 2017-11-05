import pygame
import random
import math
import sys
from pygame.locals import *
 
pygame.init()
 
screen = pygame.display.set_mode((640, 460))
font = pygame.font.SysFont(None, 36)
 
def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0, 0, 0))
    surface.blit(text_display, (x_pos, y_pos))
 
main_clock = pygame.time.Clock()
 
#Variables to hold our time
timer = 0.0
score = 0
 
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    #By adding the time that passes every full cycle of our while loop, we get
    #an effective timer.
    timer += main_clock.get_time()
 
    main_clock.tick(50)
 
    #If the timer's value is above 1000, we know a second has passed.
    if timer > 1000:
        score += 1
        timer = 0
 
    screen.fill((255, 255, 255))
 
    #Display and format our timer.  If it hasn't been 10 seconds, add in a zero
    #to our display.  Whenever the time is two digits, don't put a zero in.
    if score > 1:
        draw_text('Score: %s' % (score), font, screen, 50, 50)
 
    pygame.display.update()
