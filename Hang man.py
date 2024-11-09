#hangman project
import random

life = 5
words = ['apple','ball','cat','hello','ecstacy']
random_word = random.choice(words)
empty_list = ['_']*len(random_word)

while life>0:

    print(*empty_list,sep='')
    guess = input('Guess a letter: ')

    if guess in random_word:
        for i in range(0,len(empty_list)):
            if guess == random_word[i]:
                empty_list[i] = guess
    else:
        life -= 1
        print("you have guessed that letter is not in the word")

    if empty_list == random_word:
        print('you have won the game')
        break

    if life == 0:
        print('you lose')
