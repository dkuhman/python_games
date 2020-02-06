#This script runs a simple "Rock Paper Scissors" game through the Windows command window
#This is a good starter assignment that includes looping, conditionals, and simple built-in functions
#Author: Daniel Kuhman
#Contact: danielkuhman@gmail.com
#Date created: 1/28/2020

import random, os

print('Welcome to Rock, Paper, Scissors!')

game_status = 1
game_count = 0

while game_status == 1:
    game_count = game_count + 1
    #Compile wins. When one wins 3, the game ends
    user_win_count = 0
    cpu_win_count = 0

    choice_list = ['rock','paper','scissors']

    while user_win_count < 3 and cpu_win_count < 3:
        print('Next round!')

        #Let user make a suggestion
        user_input = input('Please pick a move (rock, paper, scissors):')
        user_input = user_input.lower()
        user_input = user_input.rstrip()
        while user_input not in choice_list:
            user_input = input('That is not a choice, please pick either rock, paper, or scissors:')

        #The cpu makes a random selection
        cpu_choice = random.choice(choice_list)

        print('The computer chose:',cpu_choice)
        print('The user selected:',user_input)

        if cpu_choice == user_input:
            print('Tie!')
        elif cpu_choice == 'rock' and user_input == 'scissors':
            print('CPU Wins!')
            cpu_win_count = cpu_win_count + 1
        elif cpu_choice == 'paper' and user_input == 'rock':
            print('CPU Wins!')
            cpu_win_count = cpu_win_count + 1
        elif cpu_choice == 'scissors' and user_input == 'paper':
            print('CPU Wins!')
            cpu_win_count = cpu_win_count + 1
        elif user_input == 'rock' and cpu_choice == 'scissors':
            print('You Win!')
            user_win_count = user_win_count + 1
        elif user_input == 'paper' and cpu_choice == 'rock':
            print('You Win!')
            user_win_count = user_win_count + 1
        elif user_input == 'scissors' and cpu_choice == 'paper':
            print('You Win!')
            user_win_count = user_win_count + 1

        #Provide the ongoing score
        print('Score: User:',user_win_count,'CPU:',cpu_win_count)

    if cpu_win_count > user_win_count:
        print('Oh no, the CPU won - better luck next time!')
    else:
        print('Congratulations, you won!')

    new_game_input = input('Would you like to play a new game? (y/n)')
    new_game_input = new_game_input.lower()
    if new_game_input == 'y':
        game_status = 1
        clear_cmnd_screen = lambda: os.system('cls') #Clear the command prompt
        clear_cmnd_screen()
        print('New game! Good Luck!')
    else:
        game_status = 0
