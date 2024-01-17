import pygame
import random

#random color
def getRandCol():
	return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#modify the speed of an object based on a pull vector
def pullSpeed(modified, pull):
	modified.x += pull.x/60
	modified.y += pull.y/60

#fundamental properties of objec
class object():
	def __init__(self, surface, pos = pygame.Vector2(0, 0),
			  speed = pygame.Vector2(0, 0), color = getRandCol()):
		self.surface = surface
		self.pos = pos
		self.speed = speed
		self.color = color
	
	def updatePos(self):
		self.pos.x += self.speed.x/60
		self.pos.y += self.speed.y/60

#object + radius
class circle():
	def __init__(self, surface, radius, pos = pygame.Vector2(0, 0),
			  speed = pygame.Vector2(0, 0), color = getRandCol()):
		self.o = object(surface, pos, speed, color)
		self.radius = radius
	
	def draw(self):
		pygame.draw.circle(self.o.surface, self.o.color, self.o.pos, self.radius)
