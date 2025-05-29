import re
from colorama import init, Fore

init(autoreset=True)

def check_password_strength(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[\W_]', password))  # спецсимволы

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    return score

def main():
    print(Fore.CYAN + "🔒 Random Password Strength Checker 🔒")
    password = input(Fore.YELLOW + "Enter your password to check: ")

    score = check_password_strength(password)

    if score == 5:
        color = Fore.GREEN
        strength = "Very Strong"
    elif score >= 3:
        color = Fore.YELLOW
        strength = "Moderate"
    else:
        color = Fore.RED
        strength = "Weak"

    print(color + f"Password strength: {strength} ({score}/5)")

if __name__ == "__main__":
    main()
