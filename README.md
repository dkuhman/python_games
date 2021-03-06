# Welcome to Python Games
This repository contains Python scripts that allow users to play simple games.

## Hangman
The user plays "hangman" in the command prompt, guessing a word randomly selected by the computer from a .txt file. This is a good 
starter assignment that includes looping, conditionals, simple built-in functions, and work with lists.

To launch the game from the command window:
`...python_games/hangman/hangman.py`

---

## Rock, Paper, Scissors
The user plays rock, paper, scissors against the "computer" in the command prompt. This script is a good starter assignment to work with
loops, conditional statements, and simple built-in functions.

To launch the game from the command window:
`...python_games/rock_paper_scissors/rock_paper_scissors.py`

---

## Tanks
### Currently under construction!
The user plays tanks! At the moment, the game only includes a single level where the useer controls a tank and fires missiles to collect coins. I am building this into a classic game of tanks (player vs cpu and player vs player). There is still a lot of work to do on this game!

---

## Motor Adapt
The user plays a game designed to demonstrate motor adaptation. The user moves a virtual ball upward toward a goal (horizontal line) using the up arrow key. When the user releases the up arrow, the ball's release height is stored and the ball returns to the bottom of the screen. Error is calculated as the vertical position of the line and the center of ball at release height. After a set of 50 virtual ball tosses, the upward velocity of the ball doubles. This velocity change should cause increased error initially, however, over subsequent tosses, the user should adapt to the new velocity and gradually reduce error. 

<img src="https://github.com/dkuhman/python_games/blob/master/motor_adapt/game_screenshot.jpg" height="300">

You can toggle feedback by pressing "f" at any point during the game:

<img src="https://github.com/dkuhman/python_games/blob/master/motor_adapt/game_screenshot_feedback.jpg" height="300">

At the end of the game, the user has the option to export error data to a .csv file for further analysis!

To launch the game from the command window:
`...python_games/motor_adapt/main.py`
