
import pygame
pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
BLUE = ( 0, 0, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

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
	screen.fill(WHITE)

	pygame.draw.line(screen, GREEN, [0,0], [100, 100], 5)

	pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

	font = pygame.font.SysFont('Calibri', 25, True, False)
	text = font.render("My text", True, BLACK)
	screen.blit(text, [250, 250])

	clock.tick(60)



	pygame.display.flip()

class Player:
	life = 500
	damage = 75
	def __init__(self, name):
		self.name = name

class Instructor(Player):
	life = 1000
	damage = 100 
	
	def __init__(self, name):
		Player.__init__(self, name)

	def instructor_attack():
		return none

class TA(Player):
	life = 750

	def __init__(self, name):
		Player.__init__(self, name)

	def ta_attack():
		return none

class Reader(Player):
	damage = 50

	def __init__(self, name):
		Player.__init__(self, name)

	def reader_attack():
		return none


pygame.quit()
	

