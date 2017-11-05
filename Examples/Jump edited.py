import pygame
import random
import math
import sys
from pygame.locals import *
from Ball import Ball
 
pygame.init()
 
screen = pygame.display.set_mode((540, 780))
screen.fill((255,255,255))
font = pygame.font.SysFont(None, 36)

def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0, 0, 0))
    surface.blit(text_display, (x_pos, y_pos))
 
#ball
ball = Ball()
draw_group = pygame.sprite.Group()
draw_group.add(ball)
ball_can_move = False
ball.rect.y = 700

generating = True
x_pos = 0
y_pos = -590
move_left = False
move_right = False
jump_state = 0
grounded = False
jump_timer = 0.0
player_speed = 6

main_clock = pygame.time.Clock()
rectangles = []
rectangles2 = []
delete = []

game_state = 0
rng = 0

timer = 0.0
score = 0
ScreenSpeed = 10
Screen = 0
ScreenMove = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                move_right = False
                move_left = True
            if event.key == K_d:
                move_right = True
                move_left = False
            if event.key == K_SPACE:
                if game_state == 0 or game_state == 3:
                    game_state = 1
                if game_state == 1:
                    if jump_state == 0 and grounded:
                        jump_state = 1
            if event.key == K_RETURN:
                if game_state == 3:
                    game_state = 1
            if event.key == K_p:
                ball.rect.y -= 5
            if event.key == K_l:
                ball.rect.y += 5
        if event.type == KEYUP:
            if event.key == K_a:
                move_left = False
            if event.key == K_d:
                move_right = False


    main_clock.tick(100)

    if game_state == 0: #Main Menu
        draw_text('Press Space to Play', font, screen, 135, 354)

    if game_state == 1:     
        if move_left:
            ball.rect.x -= player_speed
        if move_right:
            ball.rect.x += player_speed
        if ball.rect.left < 0:
            ball.rect.x += player_speed
        if ball.rect.right > 540:
            ball.rect.x -= player_speed

        if ball.rect.y < 390:
            ScreenMove = True
        if ball.rect.y >= 390:
            ScreenMove = False
            
        if generating:
            generating = False
            if rng == 0:
                y_pos = -10
                file_variable = open('Map.txt', 'r')
            else:
                rng = random.randint(1, 5)
          
                if rng == 1:
                    file_variable = open('Map2.txt', 'r')
                if rng == 2:
                    file_variable = open('Map3.txt', 'r')
                if rng == 3:
                    file_variable = open('Map4.txt', 'r')
                if rng == 4:
                    file_variable = open('Map5.txt', 'r')
                if rng == 5:
                    file_variable = open('Map6.txt', 'r')    

            for line in file_variable:
                line = line.rstrip()
                for x in range(0, len(line)):
                    if(int(line[x]) == 0):
                        x_pos += 30
                    elif(int(line[x]) == 1):
                        rectangle = pygame.Rect((x_pos, y_pos, 30, 10))
                        rectangles.append(rectangle)
                        x_pos += 30
                    elif(int(line[x]) == 2):
                        rectangle = pygame.Rect((x_pos, y_pos, 30, 10))
                        rectangles2.append(rectangle)
                        x_pos += 30
                    elif(int(line[x]) == 3):
                        rectangle = pygame.Rect((x_pos, y_pos, 30, 10))
                        delete.append(rectangle)
                        x_pos += 30
                    else:
                        pass
                    
                x_pos = 0
                y_pos += 10
            file_variable.close()
        rng = 1
        y_pos = -780
        x_pos = 0

     
        for trigger in delete:
            if trigger.y > 0:
                delete.remove(trigger)
                generating = True
            if trigger.y > 780:
                delete.remove(trigger)
            if ball.rect.colliderect(trigger):
                grounded = True
        for aRect in rectangles:
            if aRect.y >780:
                rectangles.remove(aRect)
            if ball.rect.colliderect(aRect):
                grounded = True
                if ScreenMove == True:
                    ball.rect.y = aRect.top - 34
                if ScreenMove == False:
                    ball.rect.y = aRect.top - 44
        for aRect in rectangles2:
            if aRect.y >780:
                rectangles2.remove(aRect)
            if ball.rect.colliderect(aRect):  
                groudned = True
                if ScreenMove == True:
                    ball.rect.y = aRect.top - 34
                if ScreenMove == False:
                    ball.rect.y = aRect.top - 44
        
        if jump_state == 0:
            if jump_timer == 0:
                ball.rect.y += 30
        if jump_state == 1:
            jump_timer += main_clock.get_time()
            grounded = False
            for aRect in rectangles:
                if ball.rect.colliderect(aRect):
                    grounded = False
            for aRect in rectangles2:
                if ball.rect.colliderect(aRect):
                    grounded = False
            ball.rect.y -= 10
            if jump_timer >= 150:
                jump_state = 2
        elif jump_state == 2:
            jump_timer = 0
            jump_state = 0
        
        #ball.rect.y += 5

##        if grounded:
##        #Makes sure the player is colliding with
##        #a platform
##            platList = ball.rect.collidelist(rectangles)
##            if platList != None:
##                print("groudned on rect")
##                plat_rect = rectangles[platList]
##                ball.rect.y = plat_rect.top - 25
##            platList2 = ball.rect.collidelist(rectangles2)
##            if platList2 != None:
##                plat_rect = rectangles2[platList2]
##                ball.rect.y = plat_rect.top - 25
            


        if ball.rect.y > 780:
            game_state = 3
            rectangles == []
            rectangles2 == []
            delete == []
            
        timer += main_clock.get_time()

        main_clock.tick(100)

        if timer > 250:
            score += 1
            Screen += 1
            timer = 0
                
        main_clock.tick(100)
        screen.fill((255,255,255))
        if score > 0:
            draw_text('Score: %s' % (score), font, screen, 50, 50)        
        for rectangle in rectangles:
            if ScreenMove == True:
                rectangle.y+=ScreenSpeed
            pygame.draw.rect(screen, (0,0,0), rectangle)
        for rectangle in rectangles2:
            if ScreenMove == True:
                rectangle.y+=ScreenSpeed
            pygame.draw.rect(screen, (255,255,0), rectangle)
        for rectangle in delete:
            if ScreenMove == True:
                rectangle.y+=ScreenSpeed
            pygame.draw.rect(screen, (0,255,0), rectangle)
        
        draw_group.draw(screen)
        
    if game_state == 3:    
        for trigger in delete:
            delete.remove(trigger)
        for aRect in rectangles:
            rectangles.remove(aRect)
        for aRect in rectangles2:
            rectangles2.remove(aRect)
        draw_group.remove(ball)
            
        screen.fill((255,255,255))
        draw_text('Get_Rect', font, screen, 225, 5)
        draw_text('Press Space to Play Again', font, screen, 125, 55)
        draw_text('Press Enter to Go to Main Menu', font, screen, 95, 105)
        
        ball = Ball()
        draw_group = pygame.sprite.Group()
        draw_group.add(ball)
        ball_can_move = False
        ball.rect.y = 700

        generating = True
        x_pos = 0
        y_pos = -590
        move_left = False
        move_right = False
        jump_state = 0
        grounded = False
        jump_timer = 0.0
        player_speed = 6

        main_clock = pygame.time.Clock()
        rectangles = []
        rectangles2 = []
        delete = []

        game_state = 0
        rng = 0

        timer = 0.0
        score = 0
        ScreenSpeed = 10
        Screen = 0
        ScreenMove = False
        
    pygame.display.update()











    
 

