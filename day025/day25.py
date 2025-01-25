import time
import os
from termcolor import colored

def reverse_text(text):
    """
    Function to reverse the text.
    """
    return text[::-1]

def print_with_delay(text, delay=0.1):
    """
    Function to print text with a delay to simulate typing effect.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    """
    Function to clear the screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """
    Main function that takes user input and prints the reversed text with a typing effect.
    """
    clear_screen()  # Clear the screen before starting

    print(colored("Hello! This is a text reverser program. 🌀", "cyan"))
    
    text = input(colored("Enter the text to reverse: ", "green"))
    
    print_with_delay("\nPlease wait...", 0.1)
    
    reversed_text = reverse_text(text)
    
    print_with_delay(colored("\nReversed text: ", "yellow"), 0.1)
    print_with_delay(colored(reversed_text, "magenta"), 0.1)
    
    print_with_delay("\nThank you for using the program! 👋", 0.1)

if __name__ == "__main__":
    main()
