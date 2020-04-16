import random


def	Congrats(nb, attempt):
	if nb == 42:
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	else:
		print ("Congratulations. you've got it!")
	if attempt == 1:
		print("Congratulations! You got it on your first try!")
	else:
		print(f"You won in {attempt} attempts!")

print ("This is an interactive guessing game!\n You have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")

nb = random.randint(1, 99)
def	Game(attempt):
	inp = input("What's your guess between 1 and 99?\n>>")
	if inp == 'exit':
		print('Goodbye!')
		exit()
	if not inp.isdigit():
		print("That's not a number.")
	else:
		inp = int(inp)
		if inp == nb:
			Congrats(nb, attempt + 1)
			exit()
		elif inp < nb:
			print("Too low!")
		elif inp > nb:
			print("Too high!")
	Game(attempt + 1)
Game(0)
