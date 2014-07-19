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