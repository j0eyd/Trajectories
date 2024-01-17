import pygame
import sys
from pygame.locals import *
from constants import *
from objects import *


def main():
	pygame.init()
	#set up display
	FPS = pygame.time.Clock()
	FPS.tick(60)
	SCREEN.fill(WHITE)
	x = circle(SCREEN, 10.0, pygame.Vector2(200, 200), pygame.Vector2(-0.1,0))
	#game loop
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		if ((x.o.pos.x + x.radius/2 > SCREEN_WIDTH) or (x.o.pos.x - x.radius/2 < 0)):
			x.o.speed.x *= -1
		if ((x.o.pos.y + x.radius/2 > SCREEN_HEIGHT) or (x.o.pos.y - x.radius/2 < 0)):
			x.o.speed.y *= -1
		gravity(x.o.speed, )
		x.o.updatePos()
		SCREEN.fill(WHITE)
		x.draw()
		pygame.display.update()

if __name__ == "__main__":
	main()