from colorama import init, Fore

def print_multiplication_table():
    init(autoreset=True)  # Initialize colorama

    # Size of the multiplication table
    size = 10

    # Print the table header
    print("   ", end="")
    for i in range(1, size + 1):
        print(f"{Fore.YELLOW}{i:4}", end="")
    print("\n" + "    " + "----" * size)

    # Print the rows of the table
    for i in range(1, size + 1):
        print(f"{Fore.CYAN}{i:2} |", end="")  # Print the row number in color
        for j in range(1, size + 1):
            # Alternate colors for the multiplication results
            if (i * j) % 2 == 0:
                print(f"{Fore.GREEN}{i * j:4}", end="")
            else:
                print(f"{Fore.RED}{i * j:4}", end="")
        print()  # Move to the next line

# Call the function to print the multiplication table
print_multiplication_table()
