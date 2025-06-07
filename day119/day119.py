import pygame
import sys
import random

# --- Инициализация Pygame ---
pygame.init()
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = SQUARE_SIZE // 4

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe AI")
font = pygame.font.SysFont(None, 40)

# --- Игровое поле ---
board = [["" for _ in range(3)] for _ in range(3)]
game_over = False
current_player = "X"

def draw_lines():
    screen.fill(WHITE)
    # Горизонтальные
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    # Вертикальные
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "O":
                pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                 row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == "X":
                start = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, BLACK, start, end, CROSS_WIDTH)
                pygame.draw.line(screen, BLACK, (start[0], end[1]), (end[0], start[1]), CROSS_WIDTH)

def check_winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full():
    return all(all(cell != "" for cell in row) for row in board)

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    elif is_board_full():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "O"
                    score = minimax(False)
                    board[row][col] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "X"
                    score = minimax(True)
                    board[row][col] = ""
                    best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -float("inf")
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = "O"
                score = minimax(False)
                board[row][col] = ""
                if score > best_score:
                    best_score = score
                    move = (row, col)
    if move:
        board[move[0]][move[1]] = "O"

def restart_game():
    global board, game_over, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    game_over = False
    current_player = "X"
    draw_lines()

draw_lines()

# --- Главный цикл игры ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                restart_game()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and current_player == "X":
            x, y = event.pos
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE
            if board[row][col] == "":
                board[row][col] = "X"
                if check_winner("X"):
                    game_over = True
                elif is_board_full():
                    game_over = True
                else:
                    current_player = "O"

    if current_player == "O" and not game_over:
        ai_move()
        if check_winner("O") or is_board_full():
            game_over = True
        else:
            current_player = "X"

    draw_lines()
    draw_figures()

    if game_over:
        if check_winner("X"):
            text = font.render("You Win! Press R", True, RED)
        elif check_winner("O"):
            text = font.render("AI Wins! Press R", True, RED)
        else:
            text = font.render("Draw! Press R", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.update()
