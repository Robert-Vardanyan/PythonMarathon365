def is_prime(num):
    """
    Check if a number is a prime number.

    Parameters:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    print("Prime Number Checker")
    while True:
        try:
            user_input = input("Enter a number (or type 'exit' to quit): ").strip()
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break

            number = int(user_input)
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
