import tkinter as tk
from tkinter import messagebox

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("600x500")
        
        # Initialize data
        self.cards = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
            {"question": "What is the capital of Japan?", "answer": "Tokyo"}
        ]
        self.current_card = 0
        self.show_answer = False
        
        # UI Elements
        self.card_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
        self.card_frame.place(relx=0.5, rely=0.4, anchor="center", width=400, height=200)

        self.card_text = tk.Label(self.card_frame, text="", font=("Arial", 16), wraplength=300, justify="center")
        self.card_text.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Buttons
        self.next_button = tk.Button(root, text="⏩", command=self.next_card, font=("Arial", 20))
        self.next_button.place(relx=0.7, rely=0.9, anchor="center")
        
        self.flip_button = tk.Button(root, text="🔃", command=self.flip_card, font=("Arial", 20))
        self.flip_button.place(relx=0.5, rely=0.9, anchor="center")
        
        self.previous_button = tk.Button(root, text="⏪", command=self.previous_card, font=("Arial", 20))
        self.previous_button.place(relx=0.3, rely=0.9, anchor="center")
        
        # Cards button in the top-right corner
        self.cards_button = tk.Button(root, text="All", command=self.show_cards, font=("Arial", 12))
        self.cards_button.place(relx=0.95, rely=0.05, anchor="ne")
        
        # Card number display
        self.card_number_label = tk.Label(root, text="1/4", font=("Arial", 12))
        self.card_number_label.place(relx=0.5, rely=0.7, anchor="center")
        
        self.update_card()

    def update_card(self):
        if self.show_answer:
            self.card_text.config(text=self.cards[self.current_card]["answer"])
            self.card_frame.config(bg="lightgreen")
        else:
            self.card_text.config(text=self.cards[self.current_card]["question"])
            self.card_frame.config(bg="white") 

        # Update card number label
        self.card_number_label.config(text=f"{self.current_card + 1}/{len(self.cards)}")

    def next_card(self):
        if self.current_card < len(self.cards) - 1:
            self.current_card += 1
        else:
            messagebox.showinfo("End", "You have reached the end of the flashcards!")
        self.show_answer = False
        self.update_card()

    def previous_card(self):
        if self.current_card > 0:
            self.current_card -= 1
        else:
            messagebox.showinfo("Start", "You are at the beginning of the flashcards!")
        self.show_answer = False
        self.update_card()

    def flip_card(self):
        self.show_answer = not self.show_answer
        self.update_card()

    def show_cards(self):
        messagebox.showinfo("All Cards", "\n".join([card["question"] for card in self.cards]))

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
