import random
import time

# Introduction and game rules
print("""
Welcome to Rock, Paper, Scissors!

Game rules:
- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.

Make your choice!
""")
time.sleep(2)

# Visual representations of Rock, Scissors, and Paper
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

scissors = """
    _______
---'   ____)
      (    )
       (   )
        (  )
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
         _______)
        _______)
---.__________)
"""

while True:
    # Show player options
    print("""
    Choose:
    1. Rock
    2. Scissors
    3. Paper
    """)

    # Get player input
    while True:
        try:
            player_choice = int(input("Enter the number of your choice (1/2/3): "))
            if player_choice in [1, 2, 3]:
                break
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Please enter the number 1, 2, or 3.")

    # Generate computer's choice
    computer_choice = random.randint(1, 3)

    # Display player and computer choices
    if player_choice == 1:
        print("You chose: Rock\n", rock)
        player_choice_str = "Rock"
    elif player_choice == 2:
        print("You chose: Scissors\n", scissors)
        player_choice_str = "Scissors"
    elif player_choice == 3:
        print("You chose: Paper\n", paper)
        player_choice_str = "Paper"

    if computer_choice == 1:
        print("Computer chose: Rock\n", rock)
        computer_choice_str = "Rock"
    elif computer_choice == 2:
        print("Computer chose: Scissors\n", scissors)
        computer_choice_str = "Scissors"
    elif computer_choice == 3:
        print("Computer chose: Paper\n", paper)
        computer_choice_str = "Paper"

    # Determine winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 3) or \
         (player_choice == 3 and computer_choice == 1):
        result = "You win!"
    else:
        result = "You lose."

    print(f"Result: {result}\n")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break
