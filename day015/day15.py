import random
import colorama
from colorama import Fore, Style
import os

# Initialize colorama
colorama.init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Fore.CYAN}=============================================
{Fore.GREEN}      Welcome to the Guess the Number Game!
{Fore.CYAN}=============================================
{Style.RESET_ALL}
    """
    print(banner)

def get_feedback_message(guess, number):
    if guess < number:
        return f"{Fore.YELLOW}The number is higher! Try again."
    elif guess > number:
        return f"{Fore.MAGENTA}The number is lower! Try again."
    else:
        return f"{Fore.GREEN}Congratulations! You guessed the number!"

def play_game():
    clear_screen()
    print_banner()

    number = random.randint(1, 100)
    attempts = 0

    print(f"{Fore.BLUE}I have picked a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input(f"{Fore.CYAN}Enter your guess: {Style.RESET_ALL}"))
            attempts += 1

            if guess < 1 or guess > 100:
                print(f"{Fore.RED}The number must be between 1 and 100! Try again.")
                continue

            feedback = get_feedback_message(guess, number)
            print(feedback)

            if guess == number:
                print(f"{Fore.CYAN}You guessed the number in {Fore.YELLOW}{attempts}{Fore.CYAN} attempts. Thank you for playing!")
                break

        except ValueError:
            print(f"{Fore.RED}Invalid input! Please enter an integer.")

if __name__ == "__main__":
    play_game()
