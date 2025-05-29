from colorama import init, Fore, Style

init(autoreset=True)

# Transaction list
transactions = []

def add_transaction():
    print(Fore.CYAN + "\nAdd a Transaction")
    t_type = input("Is it income or expense? (i/e): ").lower()
    if t_type not in ['i', 'e']:
        print(Fore.RED + "Invalid type. Use 'i' for income or 'e' for expense.")
        return

    try:
        amount = float(input("Enter the amount: "))
        desc = input("Enter a description: ")
    except ValueError:
        print(Fore.RED + "Invalid amount.")
        return

    transactions.append({
        'type': 'Income' if t_type == 'i' else 'Expense',
        'amount': amount if t_type == 'i' else -amount,
        'desc': desc
    })

    print(Fore.GREEN + "Transaction added successfully!")

def view_balance():
    balance = sum(t['amount'] for t in transactions)
    print(Fore.YELLOW + f"\nCurrent Balance: {Fore.GREEN if balance >= 0 else Fore.RED}${balance:.2f}")

def view_history():
    if not transactions:
        print(Fore.RED + "\nNo transactions yet.")
        return

    print(Fore.MAGENTA + "\nTransaction History:")
    for i, t in enumerate(transactions, 1):
        color = Fore.GREEN if t['amount'] > 0 else Fore.RED
        sign = "+" if t['amount'] > 0 else "-"
        print(f"{i}. {color}{t['type']:7} {sign}${abs(t['amount']):.2f} - {Style.BRIGHT}{t['desc']}")

def main():
    print(Fore.CYAN + "💰 Simple Budget Tracker")
    while True:
        print(Fore.BLUE + "\nMenu:")
        print("1. Add Transaction")
        print("2. View Balance")
        print("3. View History")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_balance()
        elif choice == '3':
            view_history()
        elif choice == '4':
            print(Fore.CYAN + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select 1–4.")

if __name__ == "__main__":
    main()
