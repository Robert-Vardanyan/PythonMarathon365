import pygame
import sys
import json
import os

# --- Initialization ---
pygame.init()
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 12, 16
CELL_SIZE = WIDTH // COLS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌱 Virtual Garden Planner")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
emoji_font = pygame.font.SysFont("Segoe UI Emoji", CELL_SIZE - 10)

# --- Constants ---
SAVE_FILE = "garden_save.json"

# Plant types mapped to emojis
PLANT_TYPES = {
    1: ("Tree", "🌳"),
    2: ("Flower", "🌸"),
    3: ("Bush", "🌿")
}
current_plant = 1

# Colors
GRAY = (200, 200, 200)
SEASON_BACKGROUNDS = {
    "summer": (144, 238, 144),
    "autumn": (255, 228, 181),
    "winter": (220, 220, 255)
}
current_season = "summer"

# --- Garden Grid ---
garden = [[None for _ in range(COLS)] for _ in range(ROWS)]

# --- Functions ---
def draw_garden():
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)
            plant = garden[row][col]
            if plant:
                plant_type = plant["type"]
                emoji = PLANT_TYPES[plant_type][1]
                emoji_surface = emoji_font.render(emoji, True, (0, 0, 0))
                screen.blit(emoji_surface, rect.topleft)

def draw_info():
    text = f"Current Plant: {PLANT_TYPES[current_plant][0]} (1-3) | Season: {current_season.title()} (S/A/W)"
    img = font.render(text, True, (0, 0, 0))
    screen.blit(img, (10, HEIGHT - 30))

def save_garden():
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(garden, f, ensure_ascii=False)

def load_garden():
    global garden
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            loaded = json.load(f)
            for r in range(ROWS):
                for c in range(COLS):
                    cell = loaded[r][c]
                    if cell and "type" in cell:
                        garden[r][c] = {"type": cell["type"]}
                    else:
                        garden[r][c] = None

# --- Main Loop ---
load_garden()
running = True

while running:
    screen.fill(SEASON_BACKGROUNDS[current_season])
    draw_garden()
    draw_info()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_garden()
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            if 0 <= row < ROWS and 0 <= col < COLS:
                if event.button == 1:  # Left click
                    garden[row][col] = {"type": current_plant}
                elif event.button == 3:  # Right click
                    garden[row][col] = None

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_plant = 1
            elif event.key == pygame.K_2:
                current_plant = 2
            elif event.key == pygame.K_3:
                current_plant = 3
            elif event.key == pygame.K_s:
                current_season = "summer"
            elif event.key == pygame.K_a:
                current_season = "autumn"
            elif event.key == pygame.K_w:
                current_season = "winter"
            elif event.key == pygame.K_q:
                save_garden()
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
