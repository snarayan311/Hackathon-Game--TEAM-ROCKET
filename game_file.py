
import pygame, random
pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
BLUE = ( 0, 0, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

size = (800, 600)
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


		elif event.key == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				#move cursor square to left, cursor.move(x,y)
			elif event.key == pygame.K_RIGHT:
				#move cursor square to right
			elif event.key == pygame.K_UP:

			elif event.key == pygame.K_DOWN:

		elif event.key == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				#move cursor square to left, cursor.move(x,y)
			elif event.key == pygame.K_RIGHT:
				#move cursor square to right
			elif event.key == pygame.K_UP:

			elif event.key == pygame.K_DOWN:	


	all_object_list.update()
	

	screen.fill(WHITE)

	pygame.draw.line(screen, GREEN, [0,0], [100, 100], 5)

	pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

	font = pygame.font.SysFont('Calibri', 30, True, False)
	text = font.render("Select your pokemon", True, BLACK)
	screen.blit(text, [0, 300])

	clock.tick(60)



	pygame.display.flip()

# class Cursor:

# 	def __init__(self, color, x_coord, y_coord):
# 		self.color = color
# 		self.x_coord = x_coord
# 		self.y_coord = y_coord

# 	def move(self, ):






class Player:
	life = 500
	damage = 75
	def __init__(self, name, x_coord, y_coord):
		self.name = name
		self.x_coord = x_coord
		self.y_coord = y_coord

	def reduce_health(self, hit_points):
		if self.life <= hit_points:
			print ("You're dead!!!")
		else:
			self.life -= hit_points

	def attack(self, opponent):
		print (self.name, " has attacked ", opponent, " with ", self.damage, " damage !")
		opponent.reduce_health(self.damage)
		print(opponent.name, " has ", opponent.life, " life.")
		

	


class Instructor(Player):
	life = 1000
	damage = random.choice(range(60-100))
	
	def __init__(self, name):
		Player.__init__(self, name)

	def instructor_attack(self, opponent):
		Player.attack(self, opponent)
		if self.damage == 100:
			print("SURPRISE EXAM! SUPER EFFECTIVE!!!")
		elif self.damage == 60:
			print("Nobody shows up for lecture. Not so effective. :(")
		else:
			print("INSTRUCTOR ATTACK!")
		
		


class TA(Player):
	life = 750

	def __init__(self, name):
		Player.__init__(self, name)

	def ta_attack(self, opponent):
		Player.attack(self, opponent)
		print("GUERILLA ATTACK!")
		
class Reader(Player):
	damage = random.choice(range(50-90))

	def __init__(self, name):
		Player.__init__(self, name)

	def reader_attack(self, opponent):
		Player.attack(self, opponent)


pygame.quit()
	

