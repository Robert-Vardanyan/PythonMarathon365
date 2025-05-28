import tkinter as tk
import random

class MealPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Meal Planner")  # Set window title
        self.root.geometry("400x300")           # Set window size
        self.root.resizable(False, False)       # Disable resizing

        # List of meals to choose from
        self.meals = [
            "Spaghetti Carbonara",
            "Chicken Stir Fry",
            "Vegetable Curry",
            "Beef Tacos",
            "Grilled Salmon",
            "Margherita Pizza",
            "Caesar Salad",
            "Sushi Rolls",
            "Pancakes with Syrup",
            "Quinoa Salad"
        ]

        # Title label at the top of the window
        self.title_label = tk.Label(root, text="🍽️ Random Meal Planner", font=("Arial", 18))
        self.title_label.pack(pady=15)

        # Button to generate a random meal
        self.generate_button = tk.Button(root, text="Get Random Meal", font=("Arial", 14), command=self.show_meal)
        self.generate_button.pack(pady=20)

        # Label to display the selected meal
        self.meal_label = tk.Label(root, text="", font=("Arial", 16), fg="blue")
        self.meal_label.pack(pady=10)

    def show_meal(self):
        # Select a random meal from the list
        meal = random.choice(self.meals)
        # Update the label to show the selected meal
        self.meal_label.config(text=meal)

def main():
    root = tk.Tk()           # Create main window
    app = MealPlannerApp(root)  # Initialize the app
    root.mainloop()          # Start the GUI event loop

if __name__ == "__main__":
    main()
