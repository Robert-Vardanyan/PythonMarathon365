import pygame
import random
import time

pygame.init()

# Размеры окна и сетки
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4, 4
CARD_SIZE = WIDTH // COLS

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
GRAY = (200, 200, 200)
BLUE = (100, 100, 255)

# Шрифт
FONT = pygame.font.SysFont(None, 72)

# Окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Card Game")

# Создание карточек
def create_cards():
    numbers = list(range(1, (ROWS * COLS // 2) + 1)) * 2
    random.shuffle(numbers)
    return [numbers[i * COLS:(i + 1) * COLS] for i in range(ROWS)]

cards = create_cards()
revealed = [[False] * COLS for _ in range(ROWS)]

# Переменные состояния
first_click = None
second_click = None
matched_pairs = 0
running = True
clock = pygame.time.Clock()

def draw_board():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CARD_SIZE, row * CARD_SIZE, CARD_SIZE - 5, CARD_SIZE - 5)
            pygame.draw.rect(screen, BLUE if revealed[row][col] else GRAY, rect)
            if revealed[row][col]:
                text = FONT.render(str(cards[row][col]), True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            row = y // CARD_SIZE
            col = x // CARD_SIZE

            if not revealed[row][col]:
                if first_click is None:
                    first_click = (row, col)
                    revealed[row][col] = True
                elif second_click is None and (row, col) != first_click:
                    second_click = (row, col)
                    revealed[row][col] = True

    if first_click and second_click:
        row1, col1 = first_click
        row2, col2 = second_click

        if cards[row1][col1] != cards[row2][col2]:
            pygame.display.flip()
            pygame.time.delay(800)
            revealed[row1][col1] = False
            revealed[row2][col2] = False
        else:
            matched_pairs += 1

        first_click = None
        second_click = None

    if matched_pairs == (ROWS * COLS) // 2:
        screen.fill(WHITE)
        msg = FONT.render("You Win!", True, GREEN)
        msg_rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(msg, msg_rect)
        pygame.display.flip()
        pygame.time.delay(3000)
        cards = create_cards()
        revealed = [[False] * COLS for _ in range(ROWS)]
        matched_pairs = 0
        first_click = second_click = None

    clock.tick(30)

pygame.quit()
