# Made by MarsBars06 on Github
from random import randint
# Importing the randint function which chooses a random integer
import playsound
# Imports the playsound library, better OS compatibility than winsound
import os
dirname = os.path.dirname(__file__)
LoseSound_filename = os.path.join(dirname, 'resources/LoseSound.wav')
WinSound_filename = os.path.join(dirname, 'resources/WinSound.wav')
# These lines of code put the path of the SFX wav files into variables
# which will be used later on.
# These are based on relative paths.
print("Ghost Game")
feelingBrave = True
# The feelingBrave variable will come in use when it is used in a while loop
score = 0
# Defining the variable which will hold the score/points scored
while feelingBrave:
    ghostDoor = randint(1,3)
    # The ghost door is a random door that, when chosen by the user, ends the game.
    print("Three doors ahead...")
    print("A ghost behind one")
    print("Which door do you open?")
    doorChosen = input("1, 2, or 3? ")
    # This is a prompt to the user
    while doorChosen != '1' and doorChosen != '2' and doorChosen != '3':
    # The conditionals above make sure that the program only accepts the numbers 1, 2 or 3
        doorChosen = input("Please type a number between 1 and 3 ")
        # Makes sure that the input is 1, 2 or 3.
    doorChosenNum = int(doorChosen)
    # Converts the user input into an integer
    if doorChosenNum == ghostDoor:
        print("GHOST!!!")
        feelingBrave = False
        # Making feelingBrave False -> breaks the loop and code execution moves to
        # after the end of the while loop
    else:
        print("No ghost!")
        print("You enter the next room.")
        score += 1
        # Adds 1 point to the score counter.
# This code is executed when the user types a number that happens
# to be the ghost door.
print("Run away!")
print("Game over!/nYou scored", score, "points")
playsound.playsound(LoseSound_filename)
# SFX
input("Press Enter to exit...")
