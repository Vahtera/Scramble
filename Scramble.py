# Word Scramble Game
# Version: 1.0.1
# Written by: Anna Vahtera
# Last Updated: 2021-10-07
# This program is a word scramble game. The program reads a list of words from a file, selects a random word,
# shuffles the letters, and asks the user to guess the word. The user has a limited number of turns to guess the word.
# The program then reveals the correct word and the points scored by the user.
# The program uses ANSI escape codes to color the text.

from json.scanner import NUMBER_RE
import random
import string
import sys
from os import system
random.seed()
fileName = "english.lst" # File Name to Read the Words from
turns = 3 # Number of turns to play
points = 5 # Default Points for Correct Answer on First Try
arguments = len(sys.argv) # Get the Command Line Arguments
iTurn = 0 # Player Turn
iRnd = 0 # Round Number

# Color Definitions
WHITE = "\033[37m" # White Text Color
BLUE = "\033[34m" # Blue Text Color
YELLOW = "\033[33m" # Yellow Text Color
GREEN = "\033[32m" # Green Text Color
RED = "\033[31m" # Red Text Color
CYAN = "\033[36m" # Cyan Text Color
PURPLE = "\033[35m" # Purple Text Color
BLACK = "\033[30m" # Black Text Color
BOLD = "\033[1m" # Bold Text
NOBOLD = "\033[22m" # No Bold Text
ENDC = "\033[0m" # Reset Text Color

def SetPlayers(): # Function to get the number of Players
    if arguments > 1:
        for l in range(1, arguments):
            if sys.argv[l][:2] == "-p":
                r = sys.argv[l][2:]
    else:
        r = input("Enter the number of players [1]: ") or 1
    
    return int(r)

def SetRounds(): # Function to get the number of rounds to play
    if arguments > 1:
        for l in range(1, arguments):
            if sys.argv[l][:2] == "-r":
                r = sys.argv[l][2:]
    else:
        r = input("Enter the number of rounds [1]: ") or 1
    
    return int(r)


def shuffle_word(word): # Function to Shuffle the Word
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

with open(fileName, "r", encoding="utf-8") as f: # Open the File and Read the Lines into an Array
    arrWord = [line.strip() for line in f]

numPlayers = SetPlayers() # Get the number of players
numRounds = SetRounds() # Get the number of rounds

def GameRound(plrTurn, plrRnd): # Function to Play a Round of the Game
    global points
    global numPlayers
    global arrWord
    global ansWord
    global scrWord
    global turns
    global playerPoints
    global iTurn

    print(BOLD + BLACK + "\n  Scrambled Word: " + CYAN, scrWord.lower() + ENDC) # Print the scrambled word

    for l in range(turns): # Loop through the number of turns
        print(BOLD + GREEN + "\n  Guess the word!" + ENDC + " You have " + YELLOW + str(3 - l) + ENDC + " turns to guess!") # Print the game title
        inputWord = input("\n\n  Player " + str(plrTurn + 1) + " / Word " + str(plrRnd + 1) + ", Guess " + str(l + 1) + ": " + WHITE) # Get the user input

        if inputWord.lower() == ansWord.lower(): # Check if the input word is the same as the answer
            print( GREEN + "\n\n  Correct!\n" + ENDC) # Print correct if the input is correct
            print("  You scored " + YELLOW + str(points) + ENDC + " points!\n") # Print the points
            go = input("  Press Enter to Continue...") # Wait for the user to press Enter")
            break
        else:
            print(RED + "\n\n  Incorrect. " + ENDC + "The correct word begins with:" + GREEN, ansWord[:l + 1].capitalize() + ENDC) # Print the correct word if the input is incorrect
            points -= 1 
    
    if inputWord.lower() != ansWord.lower():
        print(BOLD + GREEN + "\n  Guess the word!" + ENDC + " This is your " + YELLOW + "last" + ENDC + " turn to guess!") # Print the game title
        inputWord = input("\n\n  Guess " + str(turns + 1) + ": " + WHITE) # Get the user input
        if inputWord.lower() == ansWord.lower(): # Check if the input word is the same as the answer
            print( GREEN + "\n\n  Correct!" + ENDC) # Print correct if the input is correct
        else:
            print(RED + "\n\n  Incorrect. " + ENDC + "The correct word is: " + GREEN, ansWord.capitalize() + ENDC) # Print the correct word
            points = 0
            go = input("  Press Enter to Continue...") # Wait for the user to press Enter")

# Set all player's points to 0 to start
playerPoints = [0] * numPlayers

for iTurn in range(numPlayers):
    for iRnd in range(numRounds):
        system('cls') # Clear the screen
        r = random.randint(0, len(arrWord) - 1) # Randomly select a word from the list
        ansWord = arrWord[r] # Get the word from the list
        scrWord = shuffle_word(ansWord) # Shuffle the word
        points = len(ansWord) # Set the points to the length of the word
        GameRound(iTurn, iRnd) # Play a Round of the Game
        playerPoints[iTurn] += points # Add the points to the player's total points

# Final Scores
system('cls') # Clear the screen
print("  Final Scores for the game:\n") # Print a newline
for n in range(numPlayers):
    print("  Player " + str(n + 1) + " scored: " + YELLOW + str(playerPoints[n]) + ENDC + " points!") # Print the points
print("\n") # Print a newline