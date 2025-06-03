import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Trivia Quiz")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 180, 0)
RED = (180, 0, 0)
BLUE = (0, 0, 180)
YELLOW = (240, 200, 0)

font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 36)

clock = pygame.time.Clock()

# Sample questions (replace or extend)
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": 1
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "choices": ["Leo Tolstoy", "William Shakespeare", "Mark Twain", "Charles Dickens"],
        "answer": 1
    },
    {
        "question": "What is the boiling point of water at sea level?",
        "choices": ["100°C", "90°C", "80°C", "70°C"],
        "answer": 0
    },
    {
        "question": "What language is primarily spoken in Brazil?",
        "choices": ["Spanish", "Portuguese", "French", "English"],
        "answer": 1
    },
]

random.shuffle(questions)

class Button:
    def __init__(self, rect, text):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = GRAY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=8)
        label = font.render(self.text, True, BLACK)
        surface.blit(label, (self.rect.centerx - label.get_width()//2, self.rect.centery - label.get_height()//2))

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)

def draw_text_center(surface, text, y, font, color=BLACK):
    label = font.render(text, True, color)
    surface.blit(label, (WIDTH//2 - label.get_width()//2, y))

def main():
    question_index = 0
    score = 0
    selected = -1
    show_result = False
    result_timer = 0
    TIME_LIMIT = 15  # seconds for each question
    start_ticks = pygame.time.get_ticks()

    btn_w, btn_h = 300, 50
    btn_x = WIDTH//2 - btn_w//2
    btn_y_start = 250
    btn_gap = 20

    def load_buttons(choices):
        btns = []
        for i, choice in enumerate(choices):
            rect = (btn_x, btn_y_start + i*(btn_h + btn_gap), btn_w, btn_h)
            btns.append(Button(rect, choice))
        return btns

    if questions:
        buttons = load_buttons(questions[question_index]["choices"])
    else:
        buttons = []

    running = True
    while running:
        win.fill(WHITE)
        elapsed_sec = (pygame.time.get_ticks() - start_ticks) / 1000
        time_left = max(0, TIME_LIMIT - elapsed_sec)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not show_result and question_index < len(questions):
                pos = event.pos
                for i, btn in enumerate(buttons):
                    if btn.is_hovered(pos):
                        selected = i
                        show_result = True
                        result_timer = pygame.time.get_ticks()
                        if i == questions[question_index]["answer"]:
                            score += 1
                        break

        # Check if quiz is finished
        if question_index >= len(questions):
            # Final screen
            draw_text_center(win, "Quiz Complete!", 200, big_font, BLUE)
            draw_text_center(win, f"Your score: {score} / {len(questions)}", 260, big_font, BLACK)
            accuracy = score / len(questions) * 100 if questions else 0
            draw_text_center(win, f"Accuracy: {accuracy:.2f}%", 320, big_font, BLACK)
            draw_text_center(win, "Press ESC to quit", 400, font, RED)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
        else:
            # Draw question
            draw_text_center(win, f"Question {question_index + 1} / {len(questions)}", 20, font, BLUE)
            question_text = questions[question_index]["question"]
            draw_text_center(win, question_text, 80, big_font)

            # Draw buttons
            for i, btn in enumerate(buttons):
                if show_result:
                    if i == questions[question_index]["answer"]:
                        btn.color = GREEN
                    elif i == selected:
                        btn.color = RED
                    else:
                        btn.color = GRAY
                else:
                    btn.color = GRAY
                btn.draw(win)

            # Timer bar
            pygame.draw.rect(win, GRAY, (150, 550, 500, 20), border_radius=10)
            timer_width = int(500 * (time_left / TIME_LIMIT))
            timer_color = YELLOW if time_left < 5 else BLUE
            pygame.draw.rect(win, timer_color, (150, 550, timer_width, 20), border_radius=10)
            draw_text_center(win, f"Time left: {int(time_left)} sec", 520, font)

            # After showing result, wait 2 seconds then next question
            if show_result:
                if pygame.time.get_ticks() - result_timer > 2000:
                    question_index += 1
                    if question_index < len(questions):
                        buttons = load_buttons(questions[question_index]["choices"])
                        selected = -1
                        show_result = False
                        start_ticks = pygame.time.get_ticks()
            else:
                if time_left <= 0:
                    # Time's up, mark as wrong and show correct
                    selected = -1
                    show_result = True
                    result_timer = pygame.time.get_ticks()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
