import pygame
import sys
import random
import time

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 20, 20
CELL_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
GREEN = (50, 200, 50)
RED = (255, 50, 50)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Maze Game")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("Arial", 60)
font_med = pygame.font.SysFont("Arial", 30)

# Directions for maze generation and movement (row, col)
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def generate_maze(rows, cols):
    # Maze with walls between cells:
    # 1 means wall, 0 means path
    maze = [[1 for _ in range(cols*2+1)] for _ in range(rows*2+1)]

    def carve_passages(r, c):
        maze[r*2+1][c*2+1] = 0
        dirs = DIRS[:]
        random.shuffle(dirs)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr*2+1][nc*2+1] == 1:
                # Remove wall between current and next cell
                maze[r*2+1 + dr][c*2+1 + dc] = 0
                carve_passages(nr, nc)

    carve_passages(0, 0)
    return maze

def draw_maze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            rect = pygame.Rect(col*CELL_SIZE//2, row*CELL_SIZE//2, CELL_SIZE//2, CELL_SIZE//2)
            color = BLACK if maze[row][col] == 1 else WHITE
            pygame.draw.rect(screen, color, rect)

def maze_coords_to_grid(r, c):
    # Convert maze coordinates (on expanded grid) to player position grid
    return r, c

def can_move(maze, r, c):
    if 0 <= r < len(maze) and 0 <= c < len(maze[0]):
        return maze[r][c] == 0
    return False

def draw_player(r, c):
    rect = pygame.Rect(c*CELL_SIZE//2, r*CELL_SIZE//2, CELL_SIZE//2, CELL_SIZE//2)
    pygame.draw.rect(screen, RED, rect)

def draw_goal(r, c):
    rect = pygame.Rect(c*CELL_SIZE//2, r*CELL_SIZE//2, CELL_SIZE//2, CELL_SIZE//2)
    pygame.draw.rect(screen, GREEN, rect)

def draw_text_center(text, font, color, y_offset=0):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(WIDTH//2, HEIGHT//2 + y_offset))
    screen.blit(rendered, rect)

def button(rect, text, font, inactive_color, active_color, action=None):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, active_color, rect)
        if click[0] == 1 and action is not None:
            pygame.time.delay(200)
            action()
    else:
        pygame.draw.rect(screen, inactive_color, rect)

    text_render = font.render(text, True, BLACK)
    text_rect = text_render.get_rect(center=rect.center)
    screen.blit(text_render, text_rect)

def main():
    # Generate a new maze each time
    maze = generate_maze(ROWS, COLS)

    # Player start position on maze grid (coordinates for the expanded maze grid)
    player_pos = [1, 1]  # top-left corner in expanded maze grid (must be open)
    goal_pos = [ROWS*2-1, COLS*2-1]  # bottom-right corner in expanded maze grid

    start_time = time.time()
    time_limit = 120  # seconds to solve maze

    game_state = "playing"  # can be: playing, won, lost

    def restart_game():
        nonlocal maze, player_pos, game_state, start_time
        maze = generate_maze(ROWS, COLS)
        player_pos[:] = [1, 1]
        game_state = "playing"
        start_time = time.time()

    while True:
        screen.fill(BLACK)

        # Draw maze, player, goal
        draw_maze(maze)
        draw_goal(*goal_pos)
        draw_player(*player_pos)

        # Timer display
        elapsed = int(time.time() - start_time)
        time_left = max(time_limit - elapsed, 0)
        timer_text = font_med.render(f"Time left: {time_left}s", True, GREEN)
        screen.blit(timer_text, (10, 10))

        if game_state == "playing":
            if player_pos == goal_pos:
                game_state = "won"
            elif time_left <= 0:
                game_state = "lost"

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and game_state == "playing":
                r, c = player_pos
                if event.key == pygame.K_UP:
                    if can_move(maze, r-1, c):
                        player_pos = [r-1, c]
                elif event.key == pygame.K_DOWN:
                    if can_move(maze, r+1, c):
                        player_pos = [r+1, c]
                elif event.key == pygame.K_LEFT:
                    if can_move(maze, r, c-1):
                        player_pos = [r, c-1]
                elif event.key == pygame.K_RIGHT:
                    if can_move(maze, r, c+1):
                        player_pos = [r, c+1]

        if game_state == "won":
            # Overlay semi-transparent black
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            overlay.fill(BLACK)
            screen.blit(overlay, (0,0))

            draw_text_center("You Win!", font_big, GREEN, -40)
            btn_rect = pygame.Rect(WIDTH//2 - 75, HEIGHT//2 + 30, 150, 50)
            button(btn_rect, "Restart", font_med, WHITE, GRAY, restart_game)

        elif game_state == "lost":
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            overlay.fill(BLACK)
            screen.blit(overlay, (0,0))

            draw_text_center("Time's Up! You Lose!", font_big, RED, -40)
            btn_rect = pygame.Rect(WIDTH//2 - 75, HEIGHT//2 + 30, 150, 50)
            button(btn_rect, "Restart", font_med, WHITE, GRAY, restart_game)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
