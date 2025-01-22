import requests
import time
import sys
import os
from termcolor import colored

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to simulate typing text in the terminal
def typewriter(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Function to get a joke from the API
def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    joke_data = response.json()

    # If the joke consists of two parts (setup and delivery)
    if joke_data.get("type") == "twopart":
        setup = joke_data["setup"]
        delivery = joke_data["delivery"]
        
        # Adding emoji and color to joke parts
        typewriter(colored(setup, 'cyan') + " 😆")
        time.sleep(1)  # Pause before delivery
        typewriter(colored(delivery, 'yellow') + " 🚀")
    # If the joke consists of one part
    else:
        # Adding emoji and color
        typewriter(colored(joke_data["joke"], 'magenta') + " 😂")

# Main function to run the application
def main():
    while True:
        clear_screen()  # Clear the screen before each new joke
        get_joke()  # Get and display the joke
        response = input("\nDo you want another joke? (yes/no): ").lower()
        if response != "yes":
            print("Goodbye! 😎")
            break

# Run the program
if __name__ == "__main__":
    main()
