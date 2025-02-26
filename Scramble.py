''' Word Scramble Game '''
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
# 1.1.4 - OS compatibilty for clearing screen.
# 1.1.5 - Added functionality to determine winner.
# 1.1.6 - Changed to using libAnna for common functions.
# 1.1.7 - Formatted code to conform to PEP 8. Mostly.
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
import sys
from libAnna.anna import clear_screen, open_file

# Initialize Variables
random.seed()
TURNS = 3  # Number of turns to play
POINTS = 5  # Default Points for Correct Answer on First Try
ARGUMENTS = len(sys.argv)  # Get the Command Line Arguments
I_TURN = 0  # Player Turn
I_RND = 0  # Round Number


def display_help():
    '''Display Help Screen'''
    print("\n\nInstructions:\n")
    print("Usage: py Scramble.py [#players] [#rounds] [language]\n")
    print("Language is any of the following:")
    print("--english: English language. (Default)")
    print("--finnish: Finnish language.")
    print("\nCommand line arguments:")
    print("-h, --help: this Help screen.")
    # print("-r, --rules: Display rules.")
    print("-p#: Number of players.")
    print("-r#: Number of rounds.")
    print("\nIf selecting the language, make sure the required language file is present [\"language.lst\"].\n")
    sys.exit()


# Color Definitions
WHITE = "\033[37m"  # White Text Color
BLUE = "\033[34m"  # Blue Text Color
YELLOW = "\033[33m"  # Yellow Text Color
GREEN = "\033[32m"  # Green Text Color
RED = "\033[31m"  # Red Text Color
CYAN = "\033[36m"  # Cyan Text Color
PURPLE = "\033[35m"  # Purple Text Color
BLACK = "\033[30m"  # Black Text Color
BOLD = "\033[1m"  # Bold Text
NOBOLD = "\033[22m"  # No Bold Text
ENDC = "\033[0m"  # Reset Text Color

# Translatable strings:
TEXT = {
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
    "winner": {
        "english": "Winner is",
        "finnish": "Voittaja on",
    },
    "congratulations": {
        "english": "\n Congratulations!",
        "finnish": "\n Onneksi olkoon!",
    }
}


def set_players():
    '''Function to get the number of Players'''
    p = -1
    if ARGUMENTS > 1:  # Check if there are Command Line Arguments
        for l in range(1, ARGUMENTS):
            if sys.argv[l][:2] == "-p" and len(sys.argv[l]) > 2:  # Check if the Argument is for the Number of Players
                p = sys.argv[l][2:]
    if p == -1:
        p = input(TEXT["nPlayers"][LANG]) or 1  # If no input, default to 1
    return int(p)


def set_rounds():
    '''Function to get the number of rounds to play'''
    k = -1
    if ARGUMENTS > 1:  # Check if there are Command Line Arguments
        for l in range(1, ARGUMENTS):
            if sys.argv[l][:2] == "-r" and len(sys.argv[l]) > 2:  # Check if the Argument is for the Number of Rounds
                k = sys.argv[l][2:]
    if k == -1:
        k = input(TEXT["nRounds"][LANG]) or 1  # If no input, default to 1
    return int(k)


def def_mode():
    '''Set Program Language Mode'''
    t = "english"
    if ARGUMENTS > 1:  # Check if there are Command Line Arguments
        for l in range(1, ARGUMENTS):
            t_str = sys.argv[l]
            if t_str == "--finnish":  # Check if the Argument is for Finnish Language
                t = "finnish"
            elif t_str == "--english":  # Check if the Argument is for English Language
                t = "english"
            elif t_str in('-h', '--help'):  # Check if the Argument is for Help
                display_help()
            # elif t_str == "-r" or t_str == "--rules":
            #    displayRules()
    return t


def shuffle_word(word):
    '''Function to Shuffle the Word'''
    word = list(word)
    random.shuffle(word)
    return ''.join(word)


clear_screen()  # Clear the screen
LANG = def_mode()  # Default Language
FILE_NAME = LANG + ".lst"  # File Name to Read the Words from
NUM_PLAYERS = set_players()  # Get the number of players
NUM_ROUNDS = set_rounds()  # Get the number of rounds

ARR_WORD = open_file(FILE_NAME)


def game_round(plr_turn, plr_rnd):
    '''Function to Play a Round of the Game'''
    global POINTS
    global NUM_PLAYERS
    global ARR_WORD
    global ANS_WORD
    global SCR_WORD
    global TURNS
    global PLAYER_POINTS
    global I_TURN

    print(BOLD + BLACK + TEXT["scrWord"][LANG] + CYAN, SCR_WORD.lower() + ENDC)  # Print the scrambled word

    for l in range(TURNS):  # Loop through the number of turns
        print(BOLD + GREEN + TEXT["guessword"][LANG] + ENDC + TEXT["youhave"][LANG] + YELLOW + str(3 - l) + ENDC + TEXT["turnsleft"][LANG])  # Print the game title
        input_word = input("\n " + TEXT["player"][LANG] + str(plr_turn + 1) + TEXT["word"][LANG] + str(plr_rnd + 1) + TEXT["guess"][LANG] + str(l + 1) + ": " + WHITE)  # Get the user input

        if input_word.lower() == ANS_WORD.lower():  # Check if the input word is the same as the answer
            print(GREEN + TEXT["correct"][LANG] + "\n" + ENDC)  # Print correct if the input is correct
            print(TEXT["scored"][LANG] + YELLOW + str(POINTS) + ENDC + TEXT["points"][LANG])  # Print the points
            input(TEXT["continue"][LANG])  # Wait for the user to press Enter")
            break

        print(RED + TEXT["incorrect"][LANG] + ENDC + TEXT["correctwordbegins"][LANG] + GREEN, ANS_WORD[:l + 1].capitalize() + ENDC)  # Print the correct word if the input is incorrect
        POINTS -= 1

    if input_word.lower() != ANS_WORD.lower():
        print(BOLD + GREEN + TEXT["guessword"][LANG] + ENDC + TEXT["thisis"][LANG] + YELLOW + TEXT["last"][LANG] + ENDC + TEXT["turntoguess"][LANG])  # Print the game title
        input_word = input("\n\n  Guess " + str(TURNS + 1) + ": " + WHITE)  # Get the user input
        if input_word.lower() == ANS_WORD.lower():  # Check if the input word is the same as the answer
            print(GREEN + TEXT["correct"][LANG] + ENDC)  # Print correct if the input is correct
        else:
            print(RED + TEXT["incorrect"][LANG] + ENDC + TEXT["correctword"][LANG] + GREEN, ANS_WORD.capitalize() + ENDC)  # Print the correct word
            POINTS = 0
            input(TEXT["continue"][LANG])  # Wait for the user to press Enter")

# Set all player's points to 0 to start
PLAYER_POINTS = [0] * NUM_PLAYERS

for I_TURN in range(NUM_PLAYERS):  # Loop through the number of players
    for I_RND in range(NUM_ROUNDS):  # Loop through the number of rounds
        clear_screen()  # Clear the screen
        r = random.randint(0, len(ARR_WORD) - 1)  # Randomly select a word from the list
        ANS_WORD = ARR_WORD[r]  # Get the word from the list
        SCR_WORD = shuffle_word(ANS_WORD)  # Shuffle the word
        POINTS = len(ANS_WORD)  # Set the points to the length of the word
        game_round(I_TURN, I_RND)  # Play a Round of the Game
        PLAYER_POINTS[I_TURN] += POINTS  # Add the points to the player's total points

# Display Final Scores
clear_screen()  # Clear the screen
print(BOLD + BLACK + TEXT["finalscores"][LANG] + ENDC)  # Print a newline
for n in range(NUM_PLAYERS):
    print(TEXT["player"][LANG] + str(n + 1) + TEXT["fscored"][LANG] + YELLOW + str(PLAYER_POINTS[n]) + ENDC + TEXT["points"][LANG])  # Print the points

# Display winner
WINNER = PLAYER_POINTS.index(max(PLAYER_POINTS)) + 1
print("\n " + TEXT["winner"][LANG] + BOLD + RED + TEXT["player"][LANG] + str(WINNER) + ENDC + "!")
print(BOLD + YELLOW + TEXT["congratulations"][LANG] + ENDC)
print("\n")  # Print a newline
