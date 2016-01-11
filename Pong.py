import pygame
import sys
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

length, width = 150, 15

FPS = 30

font = pygame.font.SysFont("arial", 32)

gameOver = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

def ball(x,y,radius,color):
    pygame.draw.circle(gameDisplay, color, (x,y), radius)

def paddle(x,y,length, width, color):
    pygame.draw.rect(gameDisplay, color, (x,y,width,length))
    
                     
def close():
    pygame.quit()
    sys.exit()

def gameOverFunc():
    close()

def gameLoop():

    posBx, posBy = display_width//2, display_height//2
    ballX, ballY, ballRad = posBx, posBy, 5
    ball_change_x, ball_change_y = 10, 10
    posX1, posX2 = display_width//20, 19*display_width//20-width
    x1,y1 = posX1, display_height//2-length//2
    x2,y2 = posX2, display_height//2-length//2
    move_y1, move_y2 = 0, 0
    move = 30
    point1, point2 = 0, 0
        
    
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_UP:
                    move_y2 = -move
                elif event.key == pygame.K_DOWN:
                    move_y2 = move
                if event.key == pygame.K_w:
                    move_y1 = -move
                elif event.key == pygame.K_s:
                    move_y1 = move
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    move_y1 = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    move_y2 = 0
                    



        if ballX <= posX1+width and y1 <= ballY <= y1+length:
            ball_change_x *= -1
            #ball_change_y *= -1
        elif ballX >= posX2 and y2 <= ballY <= y2+length:
            ball_change_x *= -1
            #ball_change_y *= -1
        elif ballX < posX1+width:
            point2 += 1
            ballX, ballY = posBx, posBy
            time.sleep(2)
        elif ballX > posX2:
            point1 += 1
            ballX, ballY = posBx, posBy
            time.sleep(2)


        
            
        if not ballRad <= ballY <= display_height-ballRad:
            ball_change_y *= -1
        if y1 <= 0 and move_y1 < 0:
            move_y1 = 0
        elif y1 >= display_height-length and move_y1 > 0:
            move_y1 = 0
        if y2 <= 0 and move_y2 < 0:
            move_y2 = 0
        elif y2 >= display_height-length and move_y2 > 0:
            move_y2 = 0


        ballX += ball_change_x
        ballY += ball_change_y

        y1 += move_y1
        y2 += move_y2


        gameDisplay.fill(white)
        ball(ballX,ballY,ballRad,red)
        paddle(x1,y1,length,width,black)
        paddle(x2,y2,length,width,black)
        pygame.display.update()

        clock.tick(FPS)


gameLoop()
