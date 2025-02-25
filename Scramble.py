#
# Word Scramble Game
# Scramble.py
#
# Version History:
# 1.0.0 - Initial Release
# 1.0.1 - Added Command Line Arguments
# 1.1.0 - Added Language Support
# 1.1.1 - Added Finnish Language Support
# 1.1.2 - Added Help Screen
# 1.1.3 - Fixed Command Line Arguments
# 
# # Written by: Anna Vahtera
#
# This program is a word scramble game.
# It reads a list of words from a file and scrambles the word.
# The players have a limited number of turns to guess the word.
# The player gets points for guessing the word correctly.
# The program uses ANSI escape codes to color the text.
#

import random
import string
import sys
from os import system

# Initialize Variables
random.seed()
turns = 3 # Number of turns to play
points = 5 # Default Points for Correct Answer on First Try
arguments = len(sys.argv) # Get the Command Line Arguments
iTurn = 0 # Player Turn
iRnd = 0 # Round Number

def displayHelp(): # Display Help Screen
    print("\n\nInstructions:\n")
    print("Usage: py Scramble.py [#players] [#rounds] [language]\n")
    print("Language is any of the following:")
    print("--english: English language. (Default)")
    print("--finnish: Finnish language.")
    print("\nCommand line arguments:")
    print("-h, --help: this Help screen.")
    #print("-r, --rules: Display rules.")
    print("-p#: Number of players.")
    print("-r#: Number of rounds.")
    print("\nIf selecting the language, make sure the required language file is present [\"language.lst\"].\n")
    exit()

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

# Translatable strings:
text = {
  "play-again?": {
    "english": "Play another round? Y/N [Y]: ",
    "finnish": "Pelataanko uusi kierros? K/E [K]: ",
  },
  "quit": {
    "english": "Thank you for playing!",
    "finnish": "Kiitos, että pelasit!",
  },
  "players": {
    "english": " players",
    "finnish": " pelaajaa",
  },
  "player": {
    "english": " Player ",
    "finnish": " Pelaaja ",
  },
  "lang": {
    "english": "English",
    "finnish": "Suomi",
  },
  "language": {
    "english": "Language",
    "finnish": "Kieli",
  },
  "wordlist": {
    "english": "Wordlist",
    "finnish": "Sanalista",
  },
    "nPlayers": {
    "english": "\n  Enter the number of players [1]: ",
    "finnish": "\n  Syötä pelaajien määrä [1]: ",
  },
    "nRounds": {
    "english": "\n  Enter the number of rounds [1]: ",
    "finnish": "\n  Syötä kierrosten määrä [1]: ",
  },
    "scrWord": {
    "english": "\n  Scrambled Word: ",
    "finnish": "\n  Sekoitettu Sana: ",
  },
    "continue": {
    "english": "  Press Enter to Continue...",
    "finnish": "  Paina Enter jatkaaksesi...",
  },
    "incorrect": {
    "english": "\n\n  Incorrect. ",
    "finnish": "\n\n  Väärin. ",
  },
    "correct": {
    "english": "\n\n  Correct!",
    "finnish": "\n\n  Oikein!",
  },
    "correctword": {
    "english": "The correct word is: ",
    "finnish": "Oikea sana on: ",
  },
    "correctwordbegins": {
    "english": "The correct word begins with:",
    "finnish": "Oikea sana alkaa:",
  },
    "scored": {
    "english": "  You scored ",
    "finnish": "  Sait ",
  },
    "points": {
    "english": " points!\n",
    "finnish": " pistettä!\n",
  },
    "youhave": {
    "english": " You have ",
    "finnish": " Sinulla on ",
  },
    "turnsleft": {
    "english": " turns to guess!",
    "finnish": " kierrosta aikaa arvata!",
  },
    "guessword": {
    "english": "\n  Guess the word!",
    "finnish": "\n  Arvaa sana!",
  },
    "thisis": {
    "english": " This is your ",
    "finnish": " Tämä on ",
  },
    "last": {
    "english": "last",
    "finnish": "viimeinen",
  },
    "turntoguess": {
    "english": " turn to guess!",
    "finnish": " kierroksesi arvata!",
  },
    "word": {
    "english": " / Word ",
    "finnish": " / Sana ",
  },
    "guess": {
    "english": ", Guess ",
    "finnish": ", Arvaus ",
  },
    "finalscores": {
    "english": "\n Final Scores for the game:\n",
    "finnish": "\n Pelin lopulliset pisteet:\n",
  },
    "fscored": {
    "english": " scored: ",
    "finnish": " sai: ",
},
}

def SetPlayers(): # Function to get the number of Players
    r = -1
    if arguments > 1: # Check if there are Command Line Arguments
        for l in range(1, arguments):
            if sys.argv[l][:2] == "-p": # Check if the Argument is for the Number of Players
                r = sys.argv[l][2:]
    if r == -1:
        r = input(text["nPlayers"][lang]) or 1 # If no input, default to 1
    return int(r)

def SetRounds(): # Function to get the number of rounds to play
    r = -1
    if arguments > 1: # Check if there are Command Line Arguments
        for l in range(1, arguments):
            if sys.argv[l][:2] == "-r": # Check if the Argument is for the Number of Rounds
                r = sys.argv[l][2:]
    if r == -1:
        r = input(text["nRounds"][lang]) or 1 # If no input, default to 1
    return int(r)

def defMode(): # Set Program Language Mode
    t = "english"
    if arguments > 1: # Check if there are Command Line Arguments
        for l in range(1, arguments):
            tStr = sys.argv[l]
            if tStr == "--finnish": # Check if the Argument is for Finnish Language
                t = "finnish"
            elif tStr == "--english": # Check if the Argument is for English Language
                t = "english"
            elif tStr == "-h" or tStr == "--help": # Check if the Argument is for Help
                displayHelp()
            #elif tStr == "-r" or tStr == "--rules":
            #    displayRules()
    return t

def shuffle_word(word): # Function to Shuffle the Word
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

system('cls') # Clear the screen
lang = defMode() # Default Language
fileName = lang + ".lst" # File Name to Read the Words from
numPlayers = SetPlayers() # Get the number of players
numRounds = SetRounds() # Get the number of rounds

with open(fileName, "r", encoding="utf-8") as f: # Open the File and Read the Lines into an Array
    arrWord = [line.strip() for line in f]

def GameRound(plrTurn, plrRnd): # Function to Play a Round of the Game
    global points
    global numPlayers
    global arrWord
    global ansWord
    global scrWord
    global turns
    global playerPoints
    global iTurn

    print(BOLD + BLACK + text["scrWord"][lang] + CYAN, scrWord.lower() + ENDC) # Print the scrambled word

    for l in range(turns): # Loop through the number of turns
        print(BOLD + GREEN + text["guessword"][lang] + ENDC + text["youhave"][lang] + YELLOW + str(3 - l) + ENDC + text["turnsleft"][lang]) # Print the game title
        inputWord = input("\n " + text["player"][lang] + str(plrTurn + 1) + text["word"][lang] + str(plrRnd + 1) + text["guess"][lang] + str(l + 1) + ": " + WHITE) # Get the user input

        if inputWord.lower() == ansWord.lower(): # Check if the input word is the same as the answer
            print( GREEN + text["correct"][lang] + "\n" + ENDC) # Print correct if the input is correct
            print(text["scored"][lang] + YELLOW + str(points) + ENDC + text["points"][lang]) # Print the points
            go = input(text["continue"][lang]) # Wait for the user to press Enter")
            break
        else:
            print(RED + text["incorrect"][lang] + ENDC + text["correctwordbegins"][lang] + GREEN, ansWord[:l + 1].capitalize() + ENDC) # Print the correct word if the input is incorrect
            points -= 1 
    
    if inputWord.lower() != ansWord.lower():
        print(BOLD + GREEN + text["guessword"][lang] + ENDC + text["thisis"][lang] + YELLOW + text["last"][lang] + ENDC + text["turntoguess"][lang]) # Print the game title
        inputWord = input("\n\n  Guess " + str(turns + 1) + ": " + WHITE) # Get the user input
        if inputWord.lower() == ansWord.lower(): # Check if the input word is the same as the answer
            print( GREEN + text["correct"][lang] + ENDC) # Print correct if the input is correct
        else:
            print(RED + text["incorrect"][lang] + ENDC + text["correctword"][lang] + GREEN, ansWord.capitalize() + ENDC) # Print the correct word
            points = 0
            go = input(text["continue"][lang]) # Wait for the user to press Enter")

# Set all player's points to 0 to start
playerPoints = [0] * numPlayers

for iTurn in range(numPlayers): # Loop through the number of players
    for iRnd in range(numRounds): # Loop through the number of rounds
        system('cls') # Clear the screen
        r = random.randint(0, len(arrWord) - 1) # Randomly select a word from the list
        ansWord = arrWord[r] # Get the word from the list
        scrWord = shuffle_word(ansWord) # Shuffle the word
        points = len(ansWord) # Set the points to the length of the word
        GameRound(iTurn, iRnd) # Play a Round of the Game
        playerPoints[iTurn] += points # Add the points to the player's total points

# Display Final Scores
system('cls') # Clear the screen
print(text["finalscores"][lang]) # Print a newline
for n in range(numPlayers):
    print(text["player"][lang] + str(n + 1) + text["fscored"][lang] + YELLOW + str(playerPoints[n]) + ENDC + text["points"][lang]) # Print the points
print("\n") # Print a newline