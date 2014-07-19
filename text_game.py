
import random

def play_game():

	def other(who):
		return 1- who

	def player(who):
		if who == 0:
			current_player, opponent_player = player1, player2
		else: #if who == 1
			current_player, opponent_player = player2, player1

	done = False
	#initialize players
	print ("WELCOME TO BERKELEY POKEMON BATTLE!")

	player1_class = str(input("Choose your Pokemon: Instructor, Teaching Assistant, or Reader? "))
	if player1_class == "Instructor":
		player1_name = str(input("Choose your instructor: Rohin or Andrew. "))
		if player1_name == "Rohin":
			player1 = Instructor("Rohin")
		else:
			player1 = Instructor("Andrew")
	elif player1_class == "Teaching Assistants":
		player1_name = str(input("Choose your teaching assistant: Jonathan, Matthew, Ajeya, Davis, Jessica, Angela, Jeffrey, \
		Beth, Youri, Alana, Dickson? "))
		if player1_name == "Jonathan":
			player1 = TA("Jonathan")
		elif player1_name == "Matthew":
			player1 = TA("Matthew")
		elif player1_name == "Ajeya":
			player1 = TA("Ajeya")
		elif player1_name == "Davis":
			player1 = TA("Davis")
		elif player1_name == "Jessica":
			player1 = TA("Jessica")
		elif player1_name == "Angela":
			player1 = TA("Angela")
		elif player1_name == "Jeffrey":
			player1 = TA("Jeffrey")
		elif player1_name == "Beth":
			player1 = TA("Beth")
		elif player1_name == "Youri":
			player1 = TA("Youri")
		elif player1_name == "Alana":
			player1 = TA("Alana")
		else:
			player1 = TA("Dickson")
	else:
		player1_name = str(input("Choose your reader: Justin, Kevin, Richard, Cem, Jocelyn, George, Anna, Michelle,\
		Daniel. "))
		if player1_name == "Justin":
			player1 = Reader("Justin")
		elif player1_name == "Kevin":
			player1 = Reader("Kevin")
		elif player1_name == "Richard":
			player1 = Reader("Richard")
		elif player1_name == "Cem":
			player1 = Reader("Cem")
		elif player1_name == "Jocelyn":
			player1 = Reader("Jocelyn")
		elif player1_name == "George":
			player1 = Reader("George")
		elif player1_name == "Anna":
			player1 = Reader("Anna")
		elif player1_name == "Michelle":
			player1 = Reader("Michelle")
		else:
			player1 = Reader("Daniel")

	x = ["Instructor" , "Teaching Assistant", "Reader"]
	player2_class = random.choice(x)
	if player2_class == "Instructor":
		y = ["Andrew", "Rohin"]
		player2_name = random.choice(y)
		if player2_name == "Rohin":
			player2 = Instructor("Rohin")
		else:
			player2 = Instructor("Andrew")
	elif player2_class == "Teaching Assistants":
		z = ["Jonathan", "Matthew", "Ajeya", "Davis", "Jessica", "Angela", "Jeffrey", \
		"Beth", "Youri", "Alana", "Dickson"]
		player2_name = random.choice(z)
		if player2_name == "Jonathan":
			player2 = TA("Jonathan")
		elif player2_name == "Matthew":
			player2 = TA("Matthew")
		elif player2_name == "Ajeya":
			player2 = TA("Ajeya")
		elif player2_name == "Davis":
			player2 = TA("Davis")
		elif player2_name == "Jessica":
			player2 = TA("Jessica")
		elif player2_name == "Angela":
			player2 = TA("Angela")
		elif player2_name == "Jeffrey":
			player2 = TA("Jeffrey")
		elif player2_name == "Beth":
			player2 = TA("Beth")
		elif player2_name == "Youri":
			player2 = TA("Youri")
		elif player2_name == "Alana":
			player2 = TA("Alana")
		else:
			player2 = TA("Dickson")
	else:
		a = ["Justin", "Kevin", "Richard", "Cem", "Jocelyn", "George", "Anna", "Michelle",\
		"Daniel"]
		player2_name = random.choice(a)
		if player2_name == "Justin":
			player2 = Reader("Justin")
		elif player2_name == "Kevin":
			player2 = Reader("Kevin")
		elif player2_name == "Richard":
			player2 = Reader("Richard")
		elif player2_name == "Cem":
			player2 = Reader("Cem")
		elif player2_name == "Jocelyn":
			player2 = Reader("Jocelyn")
		elif player2_name == "George":
			player2 = Reader("George")
		elif player2_name == "Anna":
			player2 = Reader("Anna")
		elif player2_name == "Michelle":
			player2 = Reader("Michelle")
		else:
			player2 = Reader("Daniel")



	
	who, current_player, opponent_player = 0, player1, player2
	while not done:
		player(who)
		input("Press enter to continue: ")
		take_turn(current_player, opponent_player)
		
		if player1.life <= 0 or player2.life <= 0:
			done = True
		who = other(who)
	print("GAME OVER!")


	
	

def take_turn(player, opponent):
	player.attack(opponent, player.damage)
	

######################

class Player:
	life = 500
	damage = 75
	def __init__(self, name):
		self.name = name

	def reduce_health(self, hit_points):
		if self.life <= hit_points:
			print ("You're dead!!!")
		
		self.life -= hit_points

	def attack(self, opponent, damage):
		print (self.name, " has attacked ", opponent, " with ", damage, " damage !")
		opponent.reduce_health(damage)
		print(opponent.name, " has ", opponent.life, " life.")

	def __str__(self):
		return self.name
		

class Instructor(Player):
	life = 1000
	damage = range(60,100)
	
	def __init__(self, name):
		Player.__init__(self, name)
		self.turn_damage = 0

	def attack(self, opponent, damage):
		self.turn_damage = random.choice(self.damage)
		Player.attack(self, opponent, self.turn_damage)
		if self.turn_damage in range(90, 100):
			print("SURPRISE EXAM! SUPER EFFECTIVE!!!")
		elif self.turn_damage in range(60,70):
			print("Nobody shows up for lecture. Not so effective.")
		else:
			print("INSTRUCTOR ATTACK!")
		
		
class TA(Player):
	life = 750

	def __init__(self, name):
		Player.__init__(self, name)

	def attack(self, opponent,damage):
		Player.attack(self, opponent, Player.damage)
		print("GUERILLA ATTACK!")

		
class Reader(Player):
	damage = range(50,90)

	def __init__(self, name):
		Player.__init__(self, name)
		self.damage = 0



	def attack(self, opponent, damage):
		self.turn_damage = random.choice(self.damage)
		Player.attack(self, opponent, self.turn_damage)
		if self.turn_damage in range(50,60):
			print("Oh no! This midterm is really long!")
		elif self.turn_damage in range(80,90):
			print("SUPER READER READS ALL THE EXAMS!")
		else:
			print('Reader attack!')