```
# Word Scramble Game
# Scramble.py
#
# Version History:
# 1.0.0 - Initial Release
# 1.0.1 - Added Command Line Arguments
# 1.1.0 - Added Language Support
# 1.1.1 - Added Finnish Language Support
# 1.1.2 - Added Help Screen
# 
# # Written by: Anna Vahtera
#
# This program is a word scramble game.
# It reads a list of words from a file and scrambles the word.
# The players have a limited number of turns to guess the word.
# The player gets points for guessing the word correctly.
# The program uses ANSI escape codes to color the text.
#
```

```
Instructions:

Usage: py Scramble.py [#players] [#rounds] [language]

Language is any of the following:
--english: English language. (Default)
--finnish: Finnish language.

Command line arguments:
-h, --help: this Help screen.
-p#: Number of players.
-r#: Number of rounds.

If selecting the language, make sure the required language file is present ["language.lst"].

(If no arguments are given, program will ask for # of players and # of rounds on startup.)
The Program will display a scrambled word, and it's the players' job to guess the correct word
from the letters. Points are awareded based on the length of the word.
```
