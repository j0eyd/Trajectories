import pygame

#colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SOFT_PURPLE = (115, 50, 180)

#display

SCREEN_HEIGHT = 888; SCREEN_WIDTH = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

GRAVITY = pygame.Vector2(0, 9.8)

#physics

BOUNCE_DAMP = 0.5