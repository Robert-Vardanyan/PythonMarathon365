import random

dice_faces = {
    1: ["+-------+",
        "|       |",
        "|   ●   |",
        "|       |",
        "+-------+"],
    2: ["+-------+",
        "| ●     |",
        "|       |",
        "|     ● |",
        "+-------+"],
    3: ["+-------+",
        "| ●     |",
        "|   ●   |",
        "|     ● |",
        "+-------+"],
    4: ["+-------+",
        "| ●   ● |",
        "|       |",
        "| ●   ● |",
        "+-------+"],
    5: ["+-------+",
        "| ●   ● |",
        "|   ●   |",
        "| ●   ● |",
        "+-------+"],
    6: ["+-------+",
        "| ●   ● |",
        "| ●   ● |",
        "| ●   ● |",
        "+-------+"],
}

print("Welcome to the Dice Rolling Simulator!")

while True:
    user_input = input("Press Enter to roll the dice (or 'q' to quit): ").strip().lower()
    if user_input == 'q':
        print("Thank you for playing! Goodbye.")
        break
    number = random.randint(1, 6)
    print(f"The dice rolled: {number}")
    print("\n".join(dice_faces[number]))
    print("-" * 20)
