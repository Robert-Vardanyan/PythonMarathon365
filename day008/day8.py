import re
from termcolor import colored
from pyfiglet import figlet_format

def check_password_strength(password):
    score = 0
    criteria = [
        (len(password) >= 8, "Password must be at least 8 characters long."),
        (bool(re.search(r"[a-z]", password)), "Must contain at least one lowercase letter."),
        (bool(re.search(r"[A-Z]", password)), "Must contain at least one uppercase letter."),
        (bool(re.search(r"[0-9]", password)), "Must contain at least one digit."),
        (bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)), "Must contain at least one special character.")
    ]
    
    print(colored(figlet_format("Password Check", font="slant"), "cyan"))
    print(colored("Checking your password strength...\n", "yellow"))
    
    for passed, message in criteria:
        if passed:
            score += 1
            print(colored(f"[+]", "green"), message)
        else:
            print(colored(f"[-]", "red"), message)
    
    return score

def main():
    password = input(colored("Enter your password for validation: ", "blue"))
    score = check_password_strength(password)
    
    print("\n" + "-" * 40)
    if score == 5:
        print(colored("Your password is very strong! 🔒", "green"))
    elif 3 <= score < 5:
        print(colored("Your password is average. Consider improving it.", "yellow"))
    else:
        print(colored("Your password is weak! Change it immediately.", "red"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\nExiting the program. Goodbye!", "cyan"))
