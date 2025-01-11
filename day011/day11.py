import random
import string
import time

# Function to generate a password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function for stylish output
def stylish_print(message, delay=0.1):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Main function
def main():
    stylish_print("Hello! Welcome to the Password Generator.\n", 0.05)
    time.sleep(1)
    
    # Ask for password length
    stylish_print("How many characters should the password have?", 0.05)
    length = input("Enter the password length (default is 12): ")
    length = int(length) if length else 12
    
    stylish_print("\nGenerating password...", 0.1)
    time.sleep(1)
    
    password = generate_password(length)
    
    # Stylish output of the password
    stylish_print(f"\nYour generated password: {password}", 0.05)
    
if __name__ == "__main__":
    main()
