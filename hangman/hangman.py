#This script runs a simple "Hang Man" game through the Windows command window
#This is a good starter assignment that includes looping, conditionals, simple built-in functions, and work with lists
#Author: Daniel Kuhman
#Contact: danielkuhman@gmail.com
#Date created: 1/27/2020

import random
import re

file_handle = open('hangman_words.txt','r') #This file contains words that will be selected randomly
print('Welcome to Hang Man!')

#Compile the words in the imported file
list_of_words = list()
for line in file_handle:
    list_of_words.append(line.rstrip())

#Select a random word from the list
game_word = random.choice(list_of_words)
print(game_word)

#Show the user the number of letters in the game word
display_word = list()
for i in range(len(game_word)):
    display_word.append('_ ')

print(display_word)
print('Your word:',''.join(display_word))

#Start the game
list_of_guesses = list()
misses = 0 #The user gets 6 misses before the game ends
while misses < 6:
    user_guess = input('Guess a letter:')
    user_guess = user_guess.lower()
    if len(user_guess) > 1:
        print('Your guess must be a single letter!')
    else:
        if user_guess in list_of_guesses: #See if the letter was already guessed
            print('You already guessed that letter!')
        elif user_guess.isalpha() == False: #Ensure input is alphabetical
            print('Your guess must be a letter!')
        else:
            list_of_guesses.append(user_guess)
            if user_guess not in game_word:
                misses = misses + 1
                print('Oh no! That letter is not in this word!')
                print('You have', 6 - misses, 'left!')
                if misses == 6:
                    print('Oh no! You lost!')
                    break
            else:
                print('Nice guess!')
                #correct_list = list()
                for match in re.finditer(user_guess,game_word): #Needed to see if the letter appears more than once
                    display_word[match.start()] = user_guess
                    print('Your word:',''.join(display_word))
                if ''.join(display_word) == game_word:
                    print('Congratulations! You won!')
                    break
