import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // COLS
NUM_MINES = 10

# Colors
BG_COLOR = (30, 30, 30)
GRID_COLOR = (50, 50, 50)
REVEALED_COLOR = (200, 200, 200)
MINE_COLOR = (255, 50, 50)
TEXT_COLOR = (0, 0, 0)
WIN_COLOR = (50, 255, 50)
LOSE_COLOR = (255, 0, 0)

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
font = pygame.font.SysFont(None, 40)

def generate_grid(rows, cols, num_mines):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    mines = set()

    while len(mines) < num_mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if (r, c) not in mines:
            grid[r][c] = -1
            mines.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == -1:
                continue
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == -1:
                        count += 1
            grid[r][c] = count
    return grid

def draw_grid():
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if revealed[r][c]:
                pygame.draw.rect(win, REVEALED_COLOR, rect)
                if grid[r][c] > 0:
                    text = font.render(str(grid[r][c]), True, TEXT_COLOR)
                    win.blit(text, (c * CELL_SIZE + 15, r * CELL_SIZE + 10))
                elif grid[r][c] == -1:
                    pygame.draw.circle(win, MINE_COLOR, rect.center, CELL_SIZE // 4)
            else:
                pygame.draw.rect(win, GRID_COLOR, rect)
            pygame.draw.rect(win, BG_COLOR, rect, 1)

def reveal(r, c):
    if r < 0 or r >= ROWS or c < 0 or c >= COLS or revealed[r][c]:
        return
    revealed[r][c] = True
    if grid[r][c] == 0:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                reveal(r + dr, c + dc)

def show_message(text, color):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    win.blit(overlay, (0, 0))
    message = font.render(text, True, color)
    rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    win.blit(message, rect)
    pygame.display.update()

def check_win():
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != -1 and not revealed[r][c]:
                return False
    return True

def reset_game():
    global grid, revealed, game_over, win_game
    grid = generate_grid(ROWS, COLS, NUM_MINES)
    revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
    game_over = False
    win_game = False

# Game state
reset_game()

# Main loop
running = True
while running:
    win.fill(BG_COLOR)
    draw_grid()

    if game_over:
        show_message("Game Over! Press R to restart.", LOSE_COLOR)
    elif win_game:
        show_message("You Win! Press R to restart.", WIN_COLOR)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and not win_game:
            x, y = pygame.mouse.get_pos()
            c, r = x // CELL_SIZE, y // CELL_SIZE
            if grid[r][c] == -1:
                revealed[r][c] = True
                game_over = True
            else:
                reveal(r, c)
                if check_win():
                    win_game = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

pygame.quit()
sys.exit()
