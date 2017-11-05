import pygame
import sys
from Player import Player
from Bubble import Bubble
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,460))
screen.fill((255,255,255))
pygame.display.set_caption('Bubble Buster')
font = pygame.font.SysFont(None, 36)

main_clock = pygame.time.Clock()

score = 0

#Adding Lives and Being God
lives = 3
alive = True

#create and set up values for the player
player = Player()
player.rect.x = 285
player_speed = player.speed

player2 = Player()
player2.rect.x = 285 - 640

player3 = Player()
player3.rect.x = 285 + 640

draw_group = pygame.sprite.Group()
draw_group.add(player)
draw_group.add(player2)
draw_group.add(player3)

bubble_group = pygame.sprite.Group()

move_left = False
move_right = False

p1OnScreen = True
p2OnScreen = False
p3OnScreen = False

def draw_screen():
    screen.fill((255, 255, 255))

def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (0,0,0))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)

#ball
x_position = 320
y_position = 380
last_x = x_position
last_y = y_position
ball = pygame.draw.circle(screen, (0,0,0), (x_position, y_position), 5,0)
ball_can_move = False

speed = [5, -5]

#BUBBLES
all_bubbles = []
number_of_bubbles = 30
bubble_radius = 20
bubble_edge = 1
initial_bubble_position = 30
bubble_spacing = 60

def create_bubbles():
    bubble_x = initial_bubble_position
    bubble_y = initial_bubble_position

    for rows in range(0,3):
        for columns in range(0,10):
            bubble = Bubble(bubble_x,  bubble_y)
            bubble_x += bubble_spacing
            bubble_group.add(bubble)
        bubble_y += bubble_spacing
        bubble_x = initial_bubble_position



create_bubbles()

def draw_bubbles():
    for bubble in all_bubbles:
        bubble = pygame.draw.circle(screen, (0,0,0), (bubble.rect.x, bubble.y), bubble_radius, bubble_edge)

while True:
    #check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #KEYBOARD INPUTS
        if event.type == KEYDOWN:
            if event.key == K_a:
                move_left = True
                move_right = False
            if event.key == K_d:
                move_left = False
                move_right = True
        if event.type == KEYUP:
            if event.key == K_a:
                move_left = False
            if event.key == K_d:
                move_right = False
            if alive:
                if event.key == K_SPACE:
                    ball_can_move = True
            if not alive:
                if event.key == K_RETURN:
                    lives = 3
                    alive = True
                    score = 0
                    ball_can_move = False
                    for x in range(0, len(all_bubbles)):
                        all_bubbles.pop()
                    create_bubbles()

    #Ensure consistant clock speed
    main_clock.tick(50)

    #MOVING THE PLAYER
    if move_left:
        player.rect.x -= player_speed
        player2.rect.x -= player_speed
        player3.rect.x -= player_speed
    if move_right:
        player.rect.x += player_speed
        player2.rect.x += player_speed
        player3.rect.x += player_speed
        
        #Teleportation
    if player.rect.right < 0 and p1OnScreen == True:
        player2.rect.x = 640+640
        p1OnScreen = False
        p3OnScreen = True
        p2OnScreen = False

    if player2.rect.right < 0 and p2OnScreen == True:
        player3.rect.x = 640+640
        p1OnScreen = True
        p2OnScreen = False
        p3OnScreen = False

    if player3.rect.right < 0 and p3OnScreen == True:
        player.rect.x = 640+640
        p1OnScreen = False
        p2OnScreen = True
        p3OnScreen = False
        
    if player.rect.x >640 and p1OnScreen == True:
        player3.rect.x = -60-640
        p1OnScreen = False
        p2OnScreen = True
        p3OnScreen = False

    if player2.rect.x >640 and p2OnScreen == True:
        player.rect.x = -60-640
        p1OnScreen = False
        p2OnScreen = False
        p3OnScreen = True

    if player3.rect.x >640 and p3OnScreen == True:
        player2.rect.x = -60-640
        p1OnScreen = True
        p2OnScreen = False
        p3OnScreen = False

    #MOVING THE BALL
    if ball_can_move:
        last_x = x_position
        last_y = y_position

        x_position += speed[0]
        y_position += speed[1]
        if ball.x <= 0:
            x_position = 15
            speed[0] = -speed[0]
        elif ball.x >= 640:
            x_position = 625
            speed[0] = -speed[0]
        if ball.y <= 0:
            y_position = 15
            speed[1] = -speed[1]
        #Subtracting Lives and being God
        elif ball.y >= 460:
            lives -= 1
            ball_can_move = False

        #Test collisions with the player
        if ball.colliderect(player.rect)or ball.colliderect(player2.rect) or ball.colliderect(player3.rect):
            y_position -= 15
            speed[1] = -speed[1]
            
        #Move direction
        move_direction = ((x_position - last_x), (y_position - last_y))

        #Test collision with bubbles
        for bubble in bubble_group:
            if ball.colliderect(bubble.rect):
                if move_direction[1] > 0:
                    speed[1] = -speed[1]
                    y_position -= 10
                elif move_direction[1] < 0:
                    speed[1] = -speed[1]
                    y_position += 10
                bubble_group.remove(bubble)
                score += 100
                break
    else:
        if p1OnScreen == True:
            x_position = position = player.rect.x + 30
            y_position = 380
        if p2OnScreen == True:
            x_position = position = player2.rect.x + 30
            y_position = 380
        if p3OnScreen == True:
            x_position = position = player3.rect.x + 30
            y_position = 380
        
    if lives <= 0:
        alive = False
    
    draw_screen()
    draw_group.draw(screen)
    bubble_group.draw(screen)
    ball = pygame.draw.circle(screen, (0,0,0), (x_position, y_position), 5, 0)

    if alive:
        draw_text('Score: %s' % (score), font, screen, 5, 5)
        draw_text('Lives: %s' % (lives), font, screen, 540, 5)
    else:
        draw_text('Get_Rect', font, screen, 255, 5)
        draw_text('Press Enter to Play Again', font, screen, 180, 50)
    
    pygame.display.update()
