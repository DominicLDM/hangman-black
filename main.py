#In this program, the user is given the option to either play hangman or to quit the program. They are then given multiple different hangman categories to choose from and have the option of choosing the game's difficulty. They then have the option to receive a hint or to guess the entire word. Once all the characters of the mystery word have been guessed the player is then given the option to either play again or quit. If they quit, the program lists how many times they won or lost and if they earned a record amount of points their name will then be displayed the next time someone plays the game.

#Importing different functions and files
import random
import os
import string
import hangmanEasy
import hangmanMedium
import hangmanHard
string.ascii_letters
#Global Variables
#These lists are used for the different categories that the user can select
dictionary = open("dictionary.txt").read().splitlines()
wordListCountries = ["canada", "china", "australia", "japan", "ireland", "spain", "france", "uganda", "kenya", "brazil", "vietnam", "tuvalu", "bahamas", "kuwait", "israel", "philippines"]
wordListColours = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "teal", "brown", "grey", "beige"]
wordListItems = ["table", "chair", "computer", "pencil", "desk", "fridge", "couch", "plate", "hammer", "ladder", "plunger", "towel", "blanket", "sock"]
wordListFood = ["pasta", "pizza", "hamburger", "sandwich", "egg", "bacon", "steak", "salad", "tomato", "broccoli", "fish", "sushi"]
wordListGreekAlpha = ["alpha", "beta","gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega"]
wordListSigma = ["sigma", "brogle", "harambe", "chirag", "gigachad", "pepega"]
lettersGlobal = []
difficultyPoints = 0
points = 0
#The mainCode function is where all the code for the main hangman game is placed. It loops depending on if the user chooses to play again in the menu function.
def mainCode():	
	#Local Variables
	global lettersGlobal
	global difficultyPoints
	global points
	underScores = []
	lettersGuessed = []
	word = []
	incorrectLettersGuessed = []
	incorrectFullWordGuesses = []
	global hangman
	#The user selects which category of hangman they would like to play
	while True:
		category = input("\n1.English Dictionary\n2.Countries\n3.Colours\n4.Household Items\n5.Food\n6.Greek Alphabet\nPlease choose a category: ")
		if category == "1":	
			secretWord = random.choice(dictionary)
			break
		if category == "2":
			secretWord = random.choice(wordListCountries)
			break
		if category == "3":
			secretWord = random.choice(wordListColours)
			break
		if category == "4":
			secretWord = random.choice(wordListItems)
			break
		if category == "5":
			secretWord = random.choice(wordListFood)
			break
		if category == "6":
			secretWord = random.choice(wordListGreekAlpha)
			break
		if category == "sigma":
			secretWord = random.choice(wordListSigma)
			break
		else: print("Please enter a valid input")
	#The underscores list is created using the previously selected secret word.
	pos = (len(secretWord)-1)
	for num in range(len(secretWord)):
		word.insert(0,secretWord[pos])
		pos = pos - 1
	for num in range(len(secretWord)):
		underScores.append("_")
	incorrectGuesses = 0
	print("Word for testing:",*word)
	#The user selects the difficulty of the game.
	while True:
		difficulty = input("Please choose a difficulty: easy 1 point, medium 2 points, hard 3 points: ")
		if difficulty == "easy" or difficulty == "e":
			guessCount = 9
			hangman = hangmanEasy.hangmanEasy
			difficultyPoints = 1
			break
		elif difficulty == "medium" or difficulty == "m":
			guessCount = 7
			hangman = hangmanMedium.hangmanMedium
			difficultyPoints = 2
			break
		elif difficulty == "hard" or difficulty == "h":
			guessCount = 5
			hangman = hangmanHard.hangmanHard
			difficultyPoints = 3
			break
		else: print("Please enter a valid option")
	#This while loop is where the actual hangman game takes place. It loops until there are no more underscores left in the underscores list or if the user guesses the entire word correctly.
	while incorrectGuesses < guessCount:
		os.system('clear')
		print(hangman[incorrectGuesses])
		print(*underScores)
		print("Letters Guessed:",*lettersGuessed)
		print("Incorrect Guesses:",*incorrectLettersGuessed)
		print("Incorrect Full Word Guesses:",*incorrectFullWordGuesses)
		if "_" not in underScores:
			break
		#The user has the option to guess the entire word
		while True:
			wordGuess = input("Would you like to guess the full word? (y/n): ")
			if wordGuess == "y" or wordGuess == "n":
				break
			else: print("Please enter a valid input")
		if wordGuess == "y":
			fullGuess = input("Enter what you think the word is: ")
			if fullGuess == secretWord:
				underScores = word
				break
			else: 
				incorrectGuesses += 1
				incorrectFullWordGuesses.insert(0,fullGuess)
		else:
			# The user is given the option to use a hint. The hint returns a character not in the mystery word.
			while True:
				hintCheck = input("Would you like a hint? (y/n): ")
				if hintCheck == "y":
					while True:
						randomLetter = random.choice(string.ascii_letters)
						if randomLetter.islower() and randomLetter not in lettersGuessed and randomLetter not in word: break
					print("The word does not have", randomLetter)
					break
				elif hintCheck == "n":
					break
				else: "Please enter a valid input"
			#The user inputs the character they believe is in the mystery word. If it is not alphabetical or lower case then an error message is returned.
			while True:
				guess = input("Please enter a lowercase letter: ")
				if guess not in lettersGuessed:
					if guess.isalpha() and guess.islower() and len(guess) == 1:
						break
				else: print('You have already entered this letter')
			#The program checks if the guess is in the mystery word or not. 
			if guess not in word:
				incorrectGuesses += 1
				lettersGuessed.insert(0,guess)
				lettersGlobal.insert(0,guess)
				incorrectLettersGuessed.insert(0,guess)
			else: 
				lettersGuessed.insert(0,guess)
				lettersGlobal.insert(0,guess)
				for num in range(len(secretWord)):
					if word[num] == guess:
						underScores[num] = guess
	#The program checks if the user won or lost.
	if incorrectGuesses == guessCount:
		os.system('clear')
		print(hangman[-1])
		print("\nGG YOU LOST!\nThe secret word was", secretWord)
		result = "lose"
		return result
	else: 
		print("\nGG YOU WON!\n")
		result = "win"
		points += difficultyPoints
		return result

#The choice function returns the option that the user selects to the menu function.
def choice():
	print("\nPlease select an option:\n1. Play Hangman\n2. Quit")
	option = (input("Option: "))
	return option

#The menu function gives the user the option to play again or quit using the mainCode and choice functions. It is also where the highscore of the game is shown and where the user inputs their name
def menu():
	lettersAscii = 97
	wins = 0
	losses = 0
	print("Welcome to hangman. In this game you have to guess the letters of a mystery word in a certain amount of tries.")
	#The user inputs their name. When the user quits this name is added along with their score to a text file.
	name = input("Please enter your name: ")
	#The program reads the scores text file and prints the largest score along with its relative name
	pointsListString = open('scores.txt').read().split()
	highPoints = 0
	pointsList = [int(s.split()[0])for s in pointsListString]
	if len(pointsList) > 0:
		highPoints = max(pointsList)
		pos = 0
		while True:
			if pointsList[pos] == highPoints:
				break
			pos += 1
	namesList = open('names.txt').read().splitlines()
	if len(namesList) > 0:
		highNames = namesList[pos]
	else: highNames = "invalid"
	print("High score made by", highNames + ":", highPoints)
	#This loop continues to loop the main hangman game until the user decides to quit.
	while True:
		playerChoice = choice()
		if playerChoice == "1":
			gameResult = mainCode()
			if gameResult == "win":
				wins += 1
				print("\nAmount of wins:", wins,"\nAmount of losses:", losses)
			else: 
				losses += 1
		elif playerChoice == "2":
			print("\nAmount of wins:", wins,"\nAmount of losses:", losses)
			#This loop prints out how many times each letter was guessed
			while lettersAscii < 123:
				characterCount = 0
				for item in lettersGlobal:
					if item == chr(lettersAscii):
						characterCount += 1
				if characterCount != 0:
					if characterCount == 1:
						print((chr(lettersAscii)), "was guessed", characterCount, "time")
					else: print((chr(lettersAscii)),"was guessed", characterCount, "times")
				lettersAscii += 1
			#The program writes the score and name of the user to the names text file and scores text file.
			file_scores = open(r"scores.txt", "a")
			file_scores.write("\n")
			file_scores.write(str(points))
			file_scores.close()
			file_names = open(r"names.txt", "a")
			file_names.write("\n")
			file_names.write(name)
			file_names.close()
			print("Thank you for playing!")
			break
		else: print("Please enter a valid input")
menu()
