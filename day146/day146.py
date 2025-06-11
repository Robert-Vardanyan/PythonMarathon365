import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Board - 2D list to store moves: 0 empty, 1 player 1 (X), 2 player 2 (O)
board = [[0]*BOARD_COLS for _ in range(BOARD_ROWS)]

# Draw grid lines
def draw_lines():
    # Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                # Draw X
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
            elif board[row][col] == 2:
                # Draw O
                center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True

def check_win(player):
    # Check rows
    for row in range(BOARD_ROWS):
        if all([spot == player for spot in board[row]]):
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(BOARD_ROWS)]):
        return True
    if all([board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS)]):
        return True
    return False

def draw_winner_line(player):
    # Draw line on the winning combination
    # Rows
    for row in range(BOARD_ROWS):
        if all([spot == player for spot in board[row]]):
            y = row * SQUARE_SIZE + SQUARE_SIZE // 2
            pygame.draw.line(screen, (255, 0, 0), (15, y), (WIDTH - 15, y), 10)
            return
    # Columns
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):
            x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            pygame.draw.line(screen, (255, 0, 0), (x, 15), (x, HEIGHT - 15), 10)
            return
    # Diagonal top-left to bottom-right
    if all([board[i][i] == player for i in range(BOARD_ROWS)]):
        pygame.draw.line(screen, (255, 0, 0), (15, 15), (WIDTH - 15, HEIGHT - 15), 10)
        return
    # Diagonal top-right to bottom-left
    if all([board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS)]):
        pygame.draw.line(screen, (255, 0, 0), (WIDTH - 15, 15), (15, HEIGHT - 15), 10)
        return

def restart():
    global board, current_player, game_over
    board = [[0]*BOARD_COLS for _ in range(BOARD_ROWS)]
    current_player = 1
    game_over = False
    screen.fill(BG_COLOR)
    draw_lines()

current_player = 1
game_over = False
draw_lines()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, current_player)
                if check_win(current_player):
                    game_over = True
                    draw_winner_line(current_player)
                elif is_board_full():
                    game_over = True
                current_player = 2 if current_player == 1 else 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    draw_figures()
    pygame.display.update()
