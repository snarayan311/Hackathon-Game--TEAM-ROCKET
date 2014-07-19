
import pygame
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

pygame.quit()
	