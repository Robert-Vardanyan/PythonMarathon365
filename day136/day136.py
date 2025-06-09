import pygame
import time

pygame.init()

WIDTH, HEIGHT = 540, 540
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver (Visual)")

FONT = pygame.font.SysFont("comicsans", 40)
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
HIGHLIGHT_COLOR = (50, 205, 50)

board = [
    [5, 1, 7, 6, 0, 0, 0, 3, 4],
    [2, 8, 9, 0, 0, 4, 0, 0, 0],
    [3, 4, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 3, 8, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def draw_grid():
    WIN.fill(BG_COLOR)
    for i in range(10):
        line_width = 3 if i % 3 == 0 else 1
        pygame.draw.line(WIN, LINE_COLOR, (0, i * 60), (WIDTH, i * 60), line_width)
        pygame.draw.line(WIN, LINE_COLOR, (i * 60, 0), (i * 60, HEIGHT), line_width)

def draw_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = FONT.render(str(board[i][j]), True, (0, 0, 0))
                WIN.blit(text, (j * 60 + 20, i * 60 + 15))

def highlight_cell(row, col):
    pygame.draw.rect(WIN, HIGHLIGHT_COLOR, (col * 60, row * 60, 60, 60))
    pygame.display.update()

def update_board(board, row, col, num):
    highlight_cell(row, col)
    board[row][col] = num
    draw_grid()
    draw_board(board)
    pygame.display.update()
    time.sleep(0.03)

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid(board, num, pos):
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve_visual(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if valid(board, num, (row, col)):
            update_board(board, row, col, num)
            if solve_visual(board):
                return True
            update_board(board, row, col, 0)
    return False

def main():
    run = True
    draw_grid()
    draw_board(board)
    pygame.display.update()

    solving = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solving = True

        if solving:
            solve_visual(board)
            solving = False

    pygame.quit()

if __name__ == "__main__":
    main()
