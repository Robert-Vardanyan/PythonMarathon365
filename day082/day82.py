import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def is_even(number):
    return number % 2 == 0

def main():
    print(Fore.CYAN + "\n=== Odd/Even Number Checker ===\n" + Style.RESET_ALL)
    
    try:
        num = int(input("Enter an integer: "))
        
        if is_even(num):
            print(Fore.GREEN + f"\n✅ The number {num} is EVEN.\n")
        else:
            print(Fore.MAGENTA + f"\n🔹 The number {num} is ODD.\n")

    except ValueError:
        print(Fore.RED + "\n❌ Invalid input. Please enter a valid integer.\n")

    print(Style.RESET_ALL)

if __name__ == "__main__":
    main()
