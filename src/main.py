import pygame
import sys
from pygame.locals import *
from constants import *
from objects import *

def main():
	pygame.init()
	#set up display
	FPS = pygame.time.Clock()
	FPS.tick(240)
	SCREEN.fill(WHITE)
	x = circle(SCREEN, 50.0, pygame.Vector2(300, 500), pygame.Vector2(-20,-80))
	#game loop
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		if (x.o.speed.y != 0 or x.o.pos.y != SCREEN_HEIGHT - x.radius):
			pullSpeed(x.o.speed, GRAVITY)
		x.updatePosScreen()
		SCREEN.fill(WHITE)
		x.draw()
		pygame.display.update()

if __name__ == "__main__":
	main()