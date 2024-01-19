import pygame
import sys
import random
from pygame.locals import *
from constants import *
from objects import *

def main():
    pygame.init()

    # Set up display
    FPS = pygame.time.Clock()
    FPS.tick(60)

    # Objects
    balls = []
    mousePosList = []
    clickDown = False

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Check if the left mouse button is pressed
        if pygame.mouse.get_pressed()[0]:
            if (len(mousePosList)<2):
                mousePosList = [pygame.Vector2(pygame.mouse.get_pos()) for _ in range(2)]

            clickDown = True
            mousePos = pygame.Vector2(pygame.mouse.get_pos())
            if mousePos != mousePosList[1]:
                mousePosList[0], mousePosList[1] = mousePosList[1], mousePos
                print(f"{mousePosList[1].x} {mousePosList[1].y}")

        # Check for mouse button release
        if event.type == MOUSEBUTTONUP and clickDown:
            pos = mousePosList[1]
            x = circle(SCREEN, random.randint(1, 100), pos,
                       2*(mousePosList[1] - mousePosList[0]), getRandCol())
            balls.append(x)
            mousePosList = []
            clickDown = False

        # Update objects
        
        for i in range(0, len(balls)):
            for j in range (0, i):
                balls[j].ballCollision(balls[i])

        for ball in balls:
            if ball.o.speed.y != 0 or ball.o.pos.y != SCREEN_HEIGHT - ball.radius:
                pullSpeed(ball.o.speed, GRAVITY)
            ball.updatePosScreen()

        # Update screen
        SCREEN.fill(BLACK)
        for ball in balls:
            ball.draw()

        pygame.display.update()

if __name__ == "__main__":
    main()
