# Word Scramble Game
# Version: 1.0.1
# Written by: Anna Vahtera
# Last Updated: 2021-10-07
# This program is a word scramble game. The program reads a list of words from a file, selects a random word,
# shuffles the letters, and asks the user to guess the word. The user has a limited number of turns to guess the word.
# The program then reveals the correct word and the points scored by the user.
# The program uses ANSI escape codes to color the text.

import random
import string
from os import system
random.seed()
fileName = "english.lst" # File Name to Read the Words from
turns = 3 # Number of turns to play
points = 5 # Default Points for Correct Answer on First Try

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

def shuffle_word(word): # Function to Shuffle the Word
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

with open(fileName, "r", encoding="utf-8") as f: # Open the File and Read the Lines into an Array
    arrWord = [line.strip() for line in f]

r = random.randint(0, len(arrWord) - 1) # Randomly select a word from the list

ansWord = arrWord[r] # Get the word from the list
scrWord = shuffle_word(ansWord) # Shuffle the word
points = len(ansWord) # Set the points to the length of the word

def GameRound(): # Function to Play a Round of the Game
    global points
    global ansWord
    global scrWord
    system('cls') # Clear the screen
    print(BOLD + GREEN + "\n  Guess the word!" + ENDC + " You have " + YELLOW + str(turns + 1) + ENDC + " turns to guess!") # Print the game title
    print(BOLD + BLACK + "\n  Scrambled Word: " + CYAN, scrWord.lower() + ENDC) # Print the scrambled word

    for l in range(turns): # Loop through the number of turns
        inputWord = input("\n\n  Guess " + str(l + 1) + ": " + WHITE) # Get the user input

        if inputWord.lower() == ansWord.lower(): # Check if the input word is the same as the answer
            print( GREEN + "\n\n  Correct!\n" + ENDC) # Print correct if the input is correct
            print("  You scored " + YELLOW + str(points) + ENDC + " points!\n") # Print the points
            exit() # Exit the program   
        else:
            print(RED + "\n\n  Incorrect. " + ENDC + "The correct word begins with:" + GREEN, ansWord[:l + 1].capitalize() + ENDC) # Print the correct word if the input is incorrect
            points -= 1 

    inputWord = input("\n\n  Guess " + str(turns + 1) + ": " + WHITE) # Get the user input
    if inputWord.lower() == ansWord.lower(): # Check if the input word is the same as the answer
        print( GREEN + "\n\n  Correct!" + ENDC) # Print correct if the input is correct
    else:
        print(RED + "\n\n  Incorrect. " + ENDC + "The correct word is: " + GREEN, ansWord.capitalize() + ENDC) # Print the correct word
        points = 0

GameRound() # Play a Round of the Game
print("\n  You scored " + YELLOW + str(points) + ENDC + " points!\n") # Print the points
print("\n") # Print a newline