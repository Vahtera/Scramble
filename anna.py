from os import system, name
def clearScreen(): # Clear Screen
    system('cls' if name == 'nt' else 'clear') # Clear Screen depending on OS