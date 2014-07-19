def other(who):
	return 1 - who

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


	while not done:
		#game-play

play_game()