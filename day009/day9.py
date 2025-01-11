import random
import os
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama for Windows
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print(Fore.CYAN + Style.BRIGHT)
    print("========================================")
    print("             Hangman Game               ")
    print("========================================" + Style.RESET_ALL)

def print_hangman(tries):
    stages = [
        """
         _______
        |      |
        |      O
        |     \\
        |
        |
       _|_
        """,
        """
         _______
        |      |
        |      O
        |     /|\\
        |
        |
       _|_
        """,
        """
         _______
        |      |
        |      O
        |     /|\\
        |     / \\
        |
       _|_
        """
    ]

    print(Fore.RED + stages[min(tries, 2)] + Style.RESET_ALL)


def print_win():
    win_banner = pyfiglet.figlet_format("WIN", font="slant")
    free = """
         O
        /|\\
         |
        / \\
    """ 
    print(Fore.GREEN +  win_banner + free  + Style.RESET_ALL)

def print_lose():
    lose_banner = pyfiglet.figlet_format("LOSE", font="slant")
    print(Fore.RED + lose_banner + Style.RESET_ALL)

def get_word():
    words = ["python", "terminal", "hangman", "development", "programming", "challenge"]
    return random.choice(words).upper()

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def display_alphabet(guessed_letters, word):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        if letter in guessed_letters:
            if letter in word:
                print(Fore.GREEN + letter + Style.RESET_ALL, end=" ")
            else:
                print(Fore.RED + letter + Style.RESET_ALL, end=" ")
        else:
            print(Fore.YELLOW + letter + Style.RESET_ALL, end=" ")
    print()

def play_game():
    clear_screen()
    print_title()
    word = get_word()
    guessed_letters = []
    attempts = 3

    while attempts > 0:
        clear_screen()
        print_title()
        print(Fore.YELLOW + f"Word: {display_word(word, guessed_letters)}" + Style.RESET_ALL)
        print_hangman(3 - attempts)
        display_alphabet(guessed_letters, word)

        guess = input(Fore.GREEN + "\nEnter a letter: " + Style.RESET_ALL).strip().upper()

        if not guess.isalpha() or len(guess) != 1:
            print(Fore.RED + "Please enter a single valid letter." + Style.RESET_ALL)
            continue

        if guess in guessed_letters:
            print(Fore.RED + "Already guessed that!" + Style.RESET_ALL)
            continue

        guessed_letters.append(guess)

        if guess in word:
            if set(word) <= set(guessed_letters):
                clear_screen()
                print_title()
                print(Fore.YELLOW + f"\nWord: {word}" + Style.RESET_ALL)
                print_win()
                break
            print(Fore.BLUE + "Good!" + Style.RESET_ALL)
        else:
            attempts -= 1
            print(Fore.RED + "Missed!" + Style.RESET_ALL)

    else:
        clear_screen()
        print_title()
        print_hangman(3)
        print_lose()
        print(Fore.RED + f"\nGame Over! The word was: {word}" + Style.RESET_ALL)

if __name__ == "__main__":
    play_game()
