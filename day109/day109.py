import pygame
import sys
import random
import time

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arithmetic Quiz Game")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("Arial", 50)
font_med = pygame.font.SysFont("Arial", 32)
font_small = pygame.font.SysFont("Arial", 24)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 180, 50)
RED = (220, 50, 50)
YELLOW = (255, 200, 0)

TIME_PER_QUESTION = 15  # seconds


def generate_question():
    operations = ['+', '-', '*', '/']
    op = random.choice(operations)

    if op == '+':
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        question = f"{a} + {b}"
        answer = a + b
    elif op == '-':
        a = random.randint(1, 50)
        b = random.randint(1, a)  # no negative results
        question = f"{a} - {b}"
        answer = a - b
    elif op == '*':
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        question = f"{a} * {b}"
        answer = a * b
    else:  # division
        b = random.randint(1, 12)
        answer = random.randint(1, 12)
        a = b * answer
        question = f"{a} / {b}"

    return question, answer


def draw_text_center(text, font, color, y):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(WIDTH // 2, y))
    screen.blit(rendered, rect)


def main():
    score = 0
    input_text = ""
    question, correct_answer = generate_question()
    question_start_time = time.time()
    game_over = False
    message = ""

    while True:
        screen.fill(WHITE)

        # Timer
        elapsed = time.time() - question_start_time
        time_left = max(0, TIME_PER_QUESTION - elapsed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        # Проверяем ответ
                        try:
                            user_answer = float(input_text)
                            if abs(user_answer - correct_answer) < 0.001:
                                message = "Correct!"
                                score += 1
                            else:
                                message = f"Wrong! Correct: {correct_answer}"
                            # Новый вопрос
                            question, correct_answer = generate_question()
                            input_text = ""
                            question_start_time = time.time()
                        except ValueError:
                            message = "Invalid input!"
                            input_text = ""
                    else:
                        # Разрешаем цифры, точку и минус (для отрицательных)
                        if event.unicode.isdigit() or event.unicode in ['.', '-']:
                            input_text += event.unicode

            else:
                # После game over можно нажать R для рестарта
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        score = 0
                        input_text = ""
                        question, correct_answer = generate_question()
                        question_start_time = time.time()
                        game_over = False
                        message = ""

        if not game_over and time_left <= 0:
            message = f"Time's up! Correct: {correct_answer}"
            game_over = True

        # Отрисовка
        draw_text_center("Arithmetic Quiz Game", font_big, BLACK, 60)
        draw_text_center(f"Score: {score}", font_med, GREEN, 120)
        draw_text_center(f"Time left: {int(time_left)}s", font_med, RED if time_left <= 5 else BLACK, 160)
        draw_text_center("Question:", font_med, BLACK, 210)
        draw_text_center(question, font_big, BLACK, 260)

        # Input box
        input_box_rect = pygame.Rect(WIDTH//2 - 100, 300, 200, 50)
        pygame.draw.rect(screen, BLACK, input_box_rect, 2)

        input_render = font_big.render(input_text, True, BLACK)
        screen.blit(input_render, (input_box_rect.x + 10, input_box_rect.y + 5))

        # Message
        draw_text_center(message, font_med, RED if "Wrong" in message or "Invalid" in message or "Time's up" in message else GREEN, 370)

        if game_over:
            draw_text_center("Game Over! Press R to Restart", font_med, YELLOW, 330)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
