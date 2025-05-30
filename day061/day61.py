from colorama import init, Fore, Style
init(autoreset=True)

def is_leap_year(year):
    """
    Checks if a given year is a leap year.
    Returns True if leap year, else False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage
if __name__ == "__main__":
    print(Fore.CYAN + Style.BRIGHT + "🔍 Leap Year Checker 🔎")
    print("-" * 30)

    try:
        year = int(input(Fore.YELLOW + "Enter a year: " + Style.RESET_ALL))
        if is_leap_year(year):
            print(Fore.GREEN + f"✅ Yes! {year} is a leap year.")
        else:
            print(Fore.RED + f"❌ No, {year} is not a leap year.")
    except ValueError:
        print(Fore.RED + "⚠️ Please enter a valid number!")
