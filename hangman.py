import random

print("Hangman Game")

words = ['hello', 'world', 'python']
random_word = random.choice(words)

# Display the initial hidden word with underscores
print('Guess the word: ' + '_' * len(random_word))

# Create a list to store guessed letters and a variable to track remaining lives
letters = ['_'] * len(random_word)
life = 5

# Start the game loop
while life > 0:
    # Display current state of the guessed word
    print("\nCurrent word: " + ''.join(letters))

    # Get the player's guess
    guess = input("Guess a letter: ")

    # Check if the guessed letter is in the random word
    if guess in random_word:
        for index in range(len(random_word)):
            if random_word[index] == guess:
                letters[index] = guess  # Update the guessed letter in the correct position
        print("Good guess!")
    else:
        life -= 1
        print("You have guessed it wrong.")
        print(f"You have {life} lives left.")

    # Check if the player has guessed all the letters
    if ''.join(letters) == random_word:
        print("Congratulations! You guessed the word: " + random_word)
        break

# If lives run out, end the game
if life == 0:
    print("You have lost the game. The word was: " + random_word)
