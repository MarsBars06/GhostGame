# Made by MarsBars06 on Github
from random import randint
# Importing the randint function which chooses a random integer
from time import sleep
# Imports the sleep function from the time library.
import os
try:
    SFX_enabled = True
    # If you want to disable the sound effects played, change this line to:
    # SFX_enabled = False
    import playsound
    # Imports the playsound library, better OS compatibility than winsound
except:
    print("The module 'playsound' is not installed")
    sleep(0.5)
    print("Please run the command 'pip install playsound' in the system terminal")
    sleep(0.5)
    SFX_enabled = False
    print("SFX will not be played\n")
    sleep(0.5)
if SFX_enabled:
    dirname = os.path.dirname(__file__)
    LoseSound_filename = os.path.join(dirname, 'resources/LoseSound.wav')
    WinSound_filename = os.path.join(dirname, 'resources/WinSound.wav')
    DoorSound_filename = os.path.join(dirname, 'resources/DoorSound.wav')
    # These lines of code put the relative path of the SFX wav files into variables
    # which will be used later on.  This only runs if the SFX_enabled variable is True.
# These are based on relative paths.
print("Ghost Game - Made by MarsBars06 at Github.")
sleep(0.5)
feelingBrave = True
# The feelingBrave variable will come in use when it is used in a while loop
score = 0
# Defining the variable which will hold the score/points scored
while feelingBrave:
    ghostDoor = randint(1,3)
    # The ghost door is a random door that, when chosen by the user, ends the game.
    print("Three doors ahead...")
    sleep(0.5)
    print("A ghost behind one")
    sleep(0.5)
    print("Which door do you open?")
    doorChosen = input("1, 2, or 3? ")
    # This is a prompt to the user
    while doorChosen != '1' and doorChosen != '2' and doorChosen != '3':
    # The conditionals above make sure that the program only accepts the numbers 1, 2 or 3
        doorChosen = input("Please type a number between 1 and 3 ")
        # Makes sure that the input is 1, 2 or 3.
    doorChosenNum = int(doorChosen)
    # Converts the user input into an integer
    print("You open the door...")
    playsound.playsound(DoorSound_filename, True)
    if doorChosenNum == ghostDoor:
        print("GHOST!!!")
        feelingBrave = False
        # Making feelingBrave False -> breaks the loop and code execution moves to
        # after the end of the while loop
    else:
        print("No ghost!")
        if SFX_enabled:
            playsound.playsound(WinSound_filename, True)
            # Only plays the sound effect if the SFX_enabled variable is True.
        print("You enter the next room.")
        score += 1
        sleep(0.5)
        # Adds 1 point to the score counter.
# This code is executed when the user types a number that happens
# to be the ghost door.
print("Run away!")
sleep(0.5)
print("Game over!\nYou scored", score, "points")
if SFX_enabled:
    playsound.playsound(LoseSound_filename, True)
    # Only plays the sound effect if the SFX_enabled variable is true.
input("Press Enter to exit...")
