
import pygame
pygame.init()

import random

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
BLUE = ( 0, 0, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cs61a pokemon")

done = False

clock = pygame.time.Clock()






x, y = 0, 0
rec_color = RED
display_text = "Select your Pokemon"
background = pygame.image.load("bg.jpg")
backgroundtRect = background.get_rect()
size = background.get_size()

background2 = pygame.image.load("bg2.jpg")

player1 = pygame.image.load("Ajeya.jpg")
player2 = pygame.image.load("Andrew.jpg")

selection_phase = True
selection_phase_choice = False
battle_phase = False


pokemon_list = ['Ajeya','Alana', 'Andrew', 'Anegla', 'Beth', 'Davis', 'Dickson', 'Jeffery', 'Jessica', 'Jonathan', 'Rohin', 'Youri', 'Matthew']

def pokemonfinder(x,y):
	if x == 0 and y ==0:
		return "Ajeya"
	if x == 150 and y ==0:
		return "Alana"
	if x == 300 and y ==0:
		return "Andrew"
	if x == 450 and y ==0:
		return "Angela"
	if x == 0 and y ==150:
		return "Beth"
	if x == 150 and y ==150:
		return "Davis"
	if x == 300 and y ==150:
		return "Dickson"
	if x == 450 and y ==150:
		return "Jeffery"
	if x == 0 and y ==300:
		return "Jessica"
	if x == 150 and y ==300:
		return "Jonathan"
	if x == 300 and y ==300:
		return "Rohin"
	if x == 450 and y ==300:
		return "Youri"
	if x == 0 and y ==450:
		return "Matthew"



#main program loop
while not done:
	#main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x, y = x-150, y
				rec_color = RED
			elif event.key == pygame.K_RIGHT:
				x, y = x+150, y
				rec_color = RED
			elif event.key == pygame.K_UP:
				x, y = x, y-150
				rec_color = RED
			elif event.key == pygame.K_DOWN:
				x, y = x, y+150
				rec_color = RED
			elif event.key == pygame.K_RETURN:
				rec_color = GREEN
				pokemon = pokemonfinder(x,y)
				display_text = "Go " + pokemon + "!"
				selection_phase_choice = True
				#player2 = random.choice(pokemon_list)
				
		
		"""elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x, y = x-75, y
			elif event.key == pygame.K_RIGHT:
				x, y = x+75, y
			elif event.key == pygame.K_UP:
				x, y = x, y-75
			elif event.key == pygame.K_DOWN:	
				x, y = x, y+75

		"""
		#all_object_list.update()
	
	if selection_phase:	

		screen.blit(background, backgroundtRect)

	#pygame.draw.line(screen, GREEN, [0,0], [100, 100], 5)

		pygame.draw.rect(screen, rec_color, [x, y, 150, 150], 5)



		font = pygame.font.SysFont('Calibri', 30, True, False)
		text = font.render(display_text, True, GREEN)
		screen.blit(text, [250, 500])

		pygame.display.flip()

		if selection_phase_choice:
			pygame.time.delay(1000)
			selection_phase = False
			battle_phase = True
			display_text = 'Ajeya VS Andrew'
				


	if battle_phase:


		screen.fill(BLACK)
		screen.blit(background2, backgroundtRect)

		font = pygame.font.SysFont('Calibri', 30, True, False)
		text = font.render(display_text, True, RED)
		screen.blit(text, [200, 250])

	
		
		screen.blit(player1,(0,350))
		screen.blit(player2,(450,0))

		pygame.display.flip()

	clock.tick(60)
	



class Player:
	life = 500
	damage = 75
	def __init__(self, name):
		self.name = name

	def reduce_health(self, hit_points):
		if self.life <= hit_points:
			print ("You're dead!!!")
		else:
			self.life -= hit_points

	def attack(self, opponent):
		opponent.reduce_health(self.damage)

class Instructor(Player):
	life = 1000
	damage = 100 
	
	def __init__(self, name):
		Player.__init__(self, name)

	

class TA(Player):
	life = 750

	def __init__(self, name):
		Player.__init__(self, name)

class Reader(Player):
	damage = 50

	def __init__(self, name):
		Player.__init__(self, name)



pygame.quit()
	

