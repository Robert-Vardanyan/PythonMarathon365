import random

# Grid size
SIZE = 10

# Words with clues
words_with_clues = {
    "python": "A popular programming language.",
    "loop": "Used to repeat code.",
    "bug": "An error in a program.",
    "list": "A collection of elements.",
    "dict": "Key-value pair structure.",
    "class": "Defines object behavior.",
    "try": "Starts exception handling.",
    "code": "Set of instructions.",
    "set": "Unordered unique elements.",
    "if": "Starts a conditional block."
}

grid = [[" " for _ in range(SIZE)] for _ in range(SIZE)]
placed_words = []

def can_place(word, row, col, direction):
    if direction == "across":
        if col + len(word) > SIZE:
            return False
        for i in range(len(word)):
            ch = grid[row][col + i]
            if ch != " " and ch != word[i]:
                return False
    else:
        if row + len(word) > SIZE:
            return False
        for i in range(len(word)):
            ch = grid[row + i][col]
            if ch != " " and ch != word[i]:
                return False
    return True

def place_word(word, row, col, direction):
    if direction == "across":
        for i in range(len(word)):
            grid[row][col + i] = word[i]
    else:
        for i in range(len(word)):
            grid[row + i][col] = word[i]
    placed_words.append((word, row, col, direction))

def generate_crossword():
    words = list(words_with_clues.keys())
    random.shuffle(words)
    for word in words:
        placed = False
        for _ in range(100):
            row = random.randint(0, SIZE - 1)
            col = random.randint(0, SIZE - 1)
            direction = random.choice(["across", "down"])
            if can_place(word, row, col, direction):
                place_word(word, row, col, direction)
                placed = True
                break
        if not placed:
            print(f"❌ Could not place: {word}")

def display_grid():
    print("\n🧩 Crossword Grid:\n")
    print("   " + " ".join(str(i) for i in range(SIZE)))
    for idx, row in enumerate(grid):
        print(f"{idx:2} " + " ".join(ch if ch != " " else "." for ch in row))

def display_clues():
    print("\n📜 Clues:\n")
    for i, (word, row, col, direction) in enumerate(placed_words, 1):
        print(f"{i}. ({direction.title()} @ {row},{col}) - {words_with_clues[word]}")

if __name__ == "__main__":
    generate_crossword()
    display_grid()
    display_clues()
