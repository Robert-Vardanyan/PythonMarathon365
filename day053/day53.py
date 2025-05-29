import math
from colorama import init, Fore, Style

init(autoreset=True)

def calculate_area():
    print(Fore.CYAN + "📐 Area Calculator for Shapes")
    print(Fore.YELLOW + "Choose a shape to calculate area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Triangle")
    print("5. Trapezoid")

    choice = input(Fore.GREEN + "Enter your choice (1-5): ")

    try:
        if choice == '1':
            r = float(input("Enter the radius: "))
            area = math.pi * r ** 2
            print(Fore.MAGENTA + f"Area of Circle = {area:.2f}")

        elif choice == '2':
            l = float(input("Enter the length: "))
            w = float(input("Enter the width: "))
            area = l * w
            print(Fore.MAGENTA + f"Area of Rectangle = {area:.2f}")

        elif choice == '3':
            side = float(input("Enter the side length: "))
            area = side ** 2
            print(Fore.MAGENTA + f"Area of Square = {area:.2f}")

        elif choice == '4':
            b = float(input("Enter the base: "))
            h = float(input("Enter the height: "))
            area = 0.5 * b * h
            print(Fore.MAGENTA + f"Area of Triangle = {area:.2f}")

        elif choice == '5':
            a = float(input("Enter base 1: "))
            b = float(input("Enter base 2: "))
            h = float(input("Enter the height: "))
            area = 0.5 * (a + b) * h
            print(Fore.MAGENTA + f"Area of Trapezoid = {area:.2f}")

        else:
            print(Fore.RED + "Invalid choice. Please enter a number from 1 to 5.")

    except ValueError:
        print(Fore.RED + "Please enter valid numeric values.")


if __name__ == "__main__":
    calculate_area()
