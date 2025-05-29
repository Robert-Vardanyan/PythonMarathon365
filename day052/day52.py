from colorama import init, Fore, Style

def find_pythagorean_triplets(limit):
    triplets = []

    for a in range(1, limit):
        for b in range(a, limit):  # Avoid duplicates
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= limit:
                triplets.append((a, b, int(c)))

    return triplets


def main():
    init(autoreset=True)  # Enable colorama

    print(Fore.CYAN + "🔺 Pythagorean Triplets Finder 🔺" + Style.RESET_ALL)
    
    try:
        limit = int(input(Fore.YELLOW + "Enter the maximum value for c: " + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + "Please enter a valid integer.")
        return

    triplets = find_pythagorean_triplets(limit)

    if not triplets:
        print(Fore.RED + "No Pythagorean triplets found.")
        return

    max_len = max(len(str(num)) for triplet in triplets for num in triplet)

    print(Fore.GREEN + f"\nFound {len(triplets)} triplets:\n")

    for a, b, c in triplets:
        a_str = str(a).rjust(max_len)
        b_str = str(b).rjust(max_len)
        c_str = str(c).rjust(max_len)

        print(
            f"{Fore.BLUE}({Fore.MAGENTA}{a_str}{Fore.BLUE}, "
            f"{Fore.MAGENTA}{b_str}{Fore.BLUE}, "
            f"{Fore.MAGENTA}{c_str}{Fore.BLUE}) "
            f"{Fore.WHITE}→ "
            f"{Fore.YELLOW}{a_str}² {Fore.WHITE}+ "
            f"{Fore.YELLOW}{b_str}² {Fore.WHITE}= "
            f"{Fore.GREEN}{c_str}²"
        )


if __name__ == "__main__":
    main()
