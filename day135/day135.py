import random
import string

SIZE = 12
WORDS = ["python", "loop", "bug", "list", "class", "code", "input", "while", "true", "false"]

grid = [[" " for _ in range(SIZE)] for _ in range(SIZE)]

DIRECTIONS = [
    (0, 1),    # right
    (1, 0),    # down
    (1, 1),    # diagonal down-right
    (-1, 1),   # diagonal up-right
]

def can_place(word, r, c, dr, dc):
    for i in range(len(word)):
        nr, nc = r + dr*i, c + dc*i
        if not (0 <= nr < SIZE and 0 <= nc < SIZE):
            return False
        if grid[nr][nc] != " " and grid[nr][nc] != word[i]:
            return False
    return True

def place_word(word):
    random.shuffle(DIRECTIONS)
    for _ in range(100):
        r, c = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
        for dr, dc in DIRECTIONS:
            if can_place(word, r, c, dr, dc):
                for i in range(len(word)):
                    grid[r + dr*i][c + dc*i] = word[i]
                return True
    return False

def fill_grid():
    for word in WORDS:
        if not place_word(word):
            print(f"⚠️ Couldn't place: {word}")
    for r in range(SIZE):
        for c in range(SIZE):
            if grid[r][c] == " ":
                grid[r][c] = random.choice(string.ascii_lowercase)

def display_grid():
    print("\n🧩 Word Search Grid:\n")
    print("   " + " ".join(f"{i:2}" for i in range(SIZE)))
    for i, row in enumerate(grid):
        print(f"{i:2} " + " ".join(row))

def play_game():
    found = set()
    print("\n📝 Find these words:\n", ", ".join(WORDS))
    while len(found) < len(WORDS):
        word = input("\n🔎 Enter found word (or 'quit'): ").lower()
        if word == 'quit':
            break
        elif word in WORDS and word not in found:
            print("✅ Found!")
            found.add(word)
        elif word in found:
            print("🔁 Already found.")
        else:
            print("❌ Not in word list.")
    print("\n🎉 Game Over! You found:", ", ".join(found))

if __name__ == "__main__":
    fill_grid()
    display_grid()
    play_game()
