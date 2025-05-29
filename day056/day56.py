import random
from colorama import init, Fore

init(autoreset=True)

def love_calculator(name1, name2):
    # Пример простой "магии" совместимости: сумма кодов символов % 101
    combined = name1.lower() + name2.lower()
    score = sum(ord(c) for c in combined) % 101  # от 0 до 100
    return score

def main():
    print(Fore.MAGENTA + "❤️ Love Compatibility Calculator ❤️")
    name1 = input(Fore.YELLOW + "Enter the first name: ")
    name2 = input(Fore.YELLOW + "Enter the second name: ")

    compatibility = love_calculator(name1, name2)

    if compatibility > 80:
        color = Fore.GREEN
        message = "Great match! 💖"
    elif compatibility > 50:
        color = Fore.YELLOW
        message = "Not bad! 😊"
    else:
        color = Fore.RED
        message = "Better luck next time! 💔"

    print(color + f"Compatibility between {name1} and {name2}: {compatibility}%")
    print(color + message)

if __name__ == "__main__":
    main()
