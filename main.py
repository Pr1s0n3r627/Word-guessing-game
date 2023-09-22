import random
# it's use is in it's name so comeone

name = input("What is your name? >>\n")

print("Good Luck ", name, " <3 ")

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks','sunshine', 
	    'guitar', 'butterfly', 'exploration', 'adventure',
	    'whisper', 'journey', 'silence', 'sapphire', 
	    'fragrance', 'breeze', 'moonlight', 'stellar', 
        'diamond', 'wanderlust', 'equation', 'sunset', 
        'symphony', 'galaxy', 'reflection', 'velvet', 
        'serenity', 'alchemy', 'ocean']

# this will choose one random word from this list of words
# like no shit it will
word = random.choice(words)


print("Guess the characters")

guesses = ''

turns = 10


while turns > 0:

	# counts the number of times a user fails
	failed = 0

	# all characters from the input word taking one at a time
	for char in word:

		# comparing that character with the character in guesses
		if char in guesses:
			print(char, end=" ")

		else:
			print("_", end = "")

			# for every failure 1 will be incremented in failure
			failed += 1

	if failed == 0:
		# user will win the game if failure is 0 and 'You Win' will be given as output
		print("\nFine, You Win")

		# this print the correct word
		print("The word was: ", word,"\n\n")
		break

	# if user has input the wrong alphabet then it will ask user to enter another alphabet
	print()
	g = input("guess a character:")
	guess = g[0]

	# every input character will be stored in guesses
	guesses += guess

	# check input with the character in word
	if guess not in word:

		turns -= 1

		# if the character doesn’t match the word then “Wrong” will be given as output
		print("Skill Issue")

		# this will print the number of turns left for the user
		print("You have", + turns, 'tries')

		if turns == 0:
			print("AHAHAHAHAHAHAHAHA\nYOU LOST\nLMAO")
