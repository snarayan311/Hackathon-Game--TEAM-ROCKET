
import pygame 
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cs61a pokemon")

done = False

clock = pygame.time.Clock()

#main program loop
while not done:
	#main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	#game logic

	#drawing code

class Player:
	life = 500
	damage = 75
	def __init__(self, name):
		self.name = name

class Instructor(Player)
	life = 1000
	damage = 100 
	
	def __init__(self, name):
		Player.__init__(self, name)

	def instructor_attack():

class TA(Player)
	life = 750

	def __init__(self, name):
		Player.__init__(self, name)

	def ta_attack():

class Reader(Player)
	damage = 50

	def __init__(self, name):
		Player.__init__(self, name)

	def reader_attack():