from colorama import init, Fore, Style

init(autoreset=True)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return Fore.CYAN + "Underweight 😟"
    elif 18.5 <= bmi < 25:
        return Fore.GREEN + "Normal weight 🙂"
    elif 25 <= bmi < 30:
        return Fore.YELLOW + "Overweight 😐"
    else:
        return Fore.RED + "Obesity 😟"

def main():
    print(Fore.LIGHTBLUE_EX + "🧮 Welcome to the BMI Calculator!\n")
    while True:
        try:
            weight = float(input(Fore.WHITE + "Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))
            bmi = calculate_bmi(weight, height)
            category = interpret_bmi(bmi)

            print(Fore.LIGHTMAGENTA_EX + f"\nYour BMI is: {bmi}")
            print("Category:", category)

        except ValueError:
            print(Fore.RED + "❌ Invalid input. Please enter numbers only.")

        again = input(Fore.CYAN + "\nDo you want to calculate again? (y/n): ").strip().lower()
        if again != 'y':
            print(Fore.LIGHTRED_EX + "👋 Goodbye! Stay healthy!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
