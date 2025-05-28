import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def generate_story():
    characters = [
        "a brave knight", "an alien", "a robot", "a talking cat", "a pirate captain", 
        "a wizard", "a ninja", "a dragon", "a lost astronaut", "a clever raccoon"
    ]
    places = [
        "in a haunted castle", "on a mysterious island", "in outer space", 
        "in the jungle", "inside a volcano", "in a candy land", 
        "at the bottom of the ocean", "on Mars", "in a secret lab", "in a magical forest"
    ]
    actions = [
        "fought evil", "discovered a treasure", "built a time machine", 
        "danced with ghosts", "escaped from danger", "flew a rocket", 
        "became invisible", "solved a mystery", "saved the world", "found a magic stone"
    ]
    items = [
        "with a laser sword", "using a teleportation device", "with a magic wand", 
        "with the power of friendship", "with a jetpack", "with invisibility cloak", 
        "with a spell book", "with a singing banana", "with a robot dog", "with a donut cannon"
    ]

    character = Fore.CYAN + random.choice(characters) + Style.RESET_ALL
    place = Fore.GREEN + random.choice(places) + Style.RESET_ALL
    action = Fore.YELLOW + random.choice(actions) + Style.RESET_ALL
    item = Fore.MAGENTA + random.choice(items) + Style.RESET_ALL

    story = f"🌟 One day, {character} appeared {place} and {action} {item}."
    return story

def main():
    print(Fore.LIGHTBLUE_EX + "🎲 Welcome to the Random Story Generator!" + Style.RESET_ALL)
    while True:
        print("\n📖 " + generate_story())
        again = input(Fore.LIGHTWHITE_EX + "\nDo you want to create another story? (y/n): ").strip().lower()
        if again != 'y':
            print(Fore.LIGHTRED_EX + "👋 Goodbye! Thanks for playing!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
