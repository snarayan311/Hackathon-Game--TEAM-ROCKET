def other(who):
	return 1- who

def play_game():
	done = False
	#initialize players
	print ("WELCOME TO BERKELEY POKEMON BATTLE!")

	player1_class = str(input("Player 1, choose your Pokemon: Instructor, Teaching Assistant, or Reader?"))
	if player1_class == "Instructor:"
		player1_name = str(input("Choose your instructor: Rohin or Andrew"))
		if player1_name == "Rohin":
			player1 = Instructor("Rohin")
		else:
			player1 = Instructor("Andrew")
	elif player1_class == "Teaching Assistants":
		player1_name = str(input("Player 1, choose your Pokemon: Jonathan, Matthew, Ajeya, Davis, Jessica, Angela, Jeffrey, \
		Beth, Youri, Alana, Dickson?")
		if player1_name == 'Jonathan':
			#create Jonathan
		elif player1_name == Matthew:
			#create Matthew
		elif player1_name == Ajeya:
			#create Ajeya
		elif player1_name == Davis:
			#create Davis
		elif player1_name == Jessica:
			#create Jessica
		elif player1_name == Angela:
			#create Angela
		elif player1_name == Jeffrey:
			#create Jeffrey
		elif player1_name == Beth:
			#create Beth
		elif player1_name == Youri:
			#create Youri
		elif player1_name == Alana:
			#create Alana
		else:
			#create Dickson
	else:
		player1_name == str(input("Choose your Pokemon: Justin, Kevin, Richard, Cem, Jocelyn, George, Anna, Michelle,\
		Daniel")
		if player1_name == Justin:
			#create Justin
		elif player1_name == Kevin:
			#create Kevin
		elif player1_name == Richard:
			#create Richard
		elif player1_name == Cem:
			#create Cem
		elif player1_name == Jocelyn:
			#create Jocelyn
		elif player1_name == George:
			# create George
		elif player1_name == Anna:
			#create Anna
		elif player1_name == Michelle:
			#create Michelle
		else:
			#create Daniel

	#repeat for player2


	who = 0 # assign current vs opponent player

	while not done:
		take_turn(current_player, opponent_player)

		if player1.life <= 0 or player2.life <= 0:
			done = True

	def take_turn(current_player, opponent_player):
		#attacks, point drains etc. 
		


		who = other(who)
		

	
		if who == 0:
			current_player, opponent_player = player1, player2
		else: #if who == 1
			current_player, opponent_player = player2, player1


play_game()