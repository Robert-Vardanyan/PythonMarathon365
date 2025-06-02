import pygame
import random
import time
import json
import os

pygame.init()

# --- Settings ---
WIDTH, HEIGHT = 650, 700
CARD_SIZE = 100
PADDING = 20
GRID_SIZE = 4
FPS = 60

# --- Colors ---
WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
BLACK = (30, 30, 30)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
BLUE = (100, 150, 255)

# --- Fonts ---
FONT = pygame.font.SysFont(None, 40)
BIG_FONT = pygame.font.SysFont(None, 60)
SMALL_FONT = pygame.font.SysFont(None, 24)

# --- Window ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Game")
clock = pygame.time.Clock()

# --- Highscore file ---
HIGHSCORE_FILE = "highscores.json"
if not os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump([], f)

# --- Game data ---
values = list(range(1, 9)) * 2
random.shuffle(values)
cards = [values[i * GRID_SIZE:(i + 1) * GRID_SIZE] for i in range(GRID_SIZE)]
revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
matched = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]

first_card = None
second_card = None
clicks = 0
matched_pairs = 0
game_over = False
start_time = time.time()
end_time = None
wait_time = 0
animating = []

def draw_cards():
    grid_width = GRID_SIZE * CARD_SIZE + (GRID_SIZE + 1) * PADDING
    grid_height = GRID_SIZE * CARD_SIZE + (GRID_SIZE + 1) * PADDING
    start_x = (WIDTH - grid_width) // 2 + PADDING
    start_y = (HEIGHT - 200 - grid_height) // 2 + PADDING

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = start_x + col * (CARD_SIZE + PADDING)
            y = start_y + row * (CARD_SIZE + PADDING)
            rect = pygame.Rect(x, y, CARD_SIZE, CARD_SIZE)

            if matched[row][col]:
                pygame.draw.rect(screen, GREEN, rect)
            elif revealed[row][col] or (row, col) in animating:
                pygame.draw.rect(screen, BLUE, rect)
                text = FONT.render(str(cards[row][col]), True, BLACK)
                screen.blit(text, (x + CARD_SIZE // 2 - text.get_width() // 2,
                                   y + CARD_SIZE // 2 - text.get_height() // 2))
            else:
                pygame.draw.rect(screen, RED, rect)


def get_card_at_pos(pos):
    x, y = pos
    grid_width = GRID_SIZE * CARD_SIZE + (GRID_SIZE + 1) * PADDING
    grid_height = GRID_SIZE * CARD_SIZE + (GRID_SIZE + 1) * PADDING
    start_x = (WIDTH - grid_width) // 2 + PADDING
    start_y = (HEIGHT - 200 - grid_height) // 2 + PADDING

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            card_x = start_x + col * (CARD_SIZE + PADDING)
            card_y = start_y + row * (CARD_SIZE + PADDING)
            rect = pygame.Rect(card_x, card_y, CARD_SIZE, CARD_SIZE)
            if rect.collidepoint(x, y):
                return row, col
    return None


def save_score(seconds, attempts):
    with open(HIGHSCORE_FILE, "r") as f:
        scores = json.load(f)
    scores.append({"time": round(seconds, 1), "attempts": attempts})
    scores.sort(key=lambda x: (x["time"], x["attempts"]))
    scores = scores[:5]
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump(scores, f)

def draw_highscores():
    with open(HIGHSCORE_FILE, "r") as f:
        scores = json.load(f)
    y = HEIGHT - 180
    screen.blit(SMALL_FONT.render("🏆 Best Results:", True, BLACK), (WIDTH // 2 - 80, y))
    for i, entry in enumerate(scores):
        text = SMALL_FONT.render(
            f"{i + 1}. {entry['time']}s, {entry['attempts']} tries", True, BLACK)
        screen.blit(text, (WIDTH // 2 - 80, y + 25 + i * 25))

# --- Game loop ---
running = True
while running:
    screen.fill(WHITE)
    draw_cards()
    draw_highscores()

    if game_over:
        msg = BIG_FONT.render(f"You won in {clicks} tries!", True, BLACK)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT - 120))

        time_msg = FONT.render(f"Time: {round(end_time - start_time, 1)}s", True, BLACK)
        screen.blit(time_msg, (WIDTH // 2 - time_msg.get_width() // 2, HEIGHT - 70))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and wait_time == 0:
            pos = pygame.mouse.get_pos()
            selected = get_card_at_pos(pos)
            if selected:
                r, c = selected
                if not revealed[r][c] and not matched[r][c]:
                    revealed[r][c] = True
                    animating.append((r, c))

                    if first_card is None:
                        first_card = (r, c)
                    elif second_card is None and (r, c) != first_card:
                        second_card = (r, c)
                        clicks += 1
                        fr, fc = first_card
                        sr, sc = second_card
                        if cards[fr][fc] == cards[sr][sc]:
                            matched[fr][fc] = True
                            matched[sr][sc] = True
                            matched_pairs += 1
                            first_card = None
                            second_card = None
                            animating = []

                            if matched_pairs == 8:
                                game_over = True
                                end_time = time.time()
                                save_score(end_time - start_time, clicks)
                        else:
                            wait_time = pygame.time.get_ticks()

    if wait_time and pygame.time.get_ticks() - wait_time > 1000:
        fr, fc = first_card
        sr, sc = second_card
        revealed[fr][fc] = False
        revealed[sr][sc] = False
        first_card = None
        second_card = None
        wait_time = 0
        animating = []

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
