

def play_game():
	done = False
	#initialize players
	print ("WELCOME TO BERKELEY POKEMON BATTLE!")

	player1_class = str(input("Choose your Pokemon: Instructor, Teaching Assistant, or Reader?"))
	if player1_class == "Instructor":
		player1_name = str(input("Choose your instructor: Rohin or Andrew"))
		if player1_name == "Rohin":
			player1 = Instructor("Rohin")
		else:
			player1 = Instructor("Andrew")
	elif player1_class == "Teaching Assistants":
		player1_name = str(input("Choose your teaching assistant: Jonathan, Matthew, Ajeya, Davis, Jessica, Angela, Jeffrey, \
		Beth, Youri, Alana, Dickson?"))
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
		player1_name == str(input("Choose your reader: Justin, Kevin, Richard, Cem, Jocelyn, George, Anna, Michelle,\
		Daniel")
		if player1_name == "Justin":
			#create Justin
		elif player1_name == "Kevin":
			#create Kevin
		elif player1_name == "Richard":
			#create Richard
		elif player1_name == "Cem":
			#create Cem
		elif player1_name == "Jocelyn":
			#create Jocelyn
		elif player1_name == "George":
			# create George
		elif player1_name == "Anna":
			#create Anna
		elif player1_name == "Michelle":
			#create Michelle
		else:
			#create Daniel
	who = 0 # assign current vs opponent player
	while not done:
		player(who)
		take_turn(current_player, opponent_player)
		
		if player1.life <= 0 or player2.life <= 0:
			done = True
		who = other(who)


	
	
def other(who):
	return 1- who

def player(who):
	if who == 0:
			current_player, opponent_player = player1, player2
	else: #if who == 1
		current_player, opponent_player = player2, player1



def take_turn(current_player, opponent_player):
	
		


		
		

	



play_game()