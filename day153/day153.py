import pygame
import random
import time

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⌨️ Python Shortcuts Quiz")
font = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 200, 100)
RED = (200, 50, 50)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)

# Quiz questions
questions = [
    {
        "question": "How to comment a line in Python?",
        "options": ["Ctrl + /", "Ctrl + C", "Ctrl + K"],
        "answer": 0
    },
    {
        "question": "Duplicate a line in VSCode?",
        "options": ["Alt + Shift + Down", "Ctrl + Shift + D", "Ctrl + D"],
        "answer": 0
    },
    {
        "question": "Find in file?",
        "options": ["Ctrl + F", "Ctrl + H", "Ctrl + Shift + P"],
        "answer": 0
    },
    {
        "question": "Run Python file?",
        "options": ["Ctrl + Shift + B", "F5", "Alt + R"],
        "answer": 1
    },
    {
        "question": "Open Command Palette in VSCode?",
        "options": ["Ctrl + Shift + P", "Ctrl + K", "Ctrl + Alt + P"],
        "answer": 0
    }
]

random.shuffle(questions)
current_question = 0
selected = -1
score = 0
answered = False
answer_time = None  # Time when answer was selected

def draw_text(text, x, y, color=BLACK):
    rendered = font.render(text, True, color)
    screen.blit(rendered, (x, y))

def draw_question():
    q = questions[current_question]
    draw_text(f"Question {current_question + 1} of {len(questions)}", 50, 30)
    draw_text(q["question"], 50, 80)
    for i, option in enumerate(q["options"]):
        rect = pygame.Rect(50, 130 + i * 60, 700, 50)
        color = GRAY
        if answered:
            if i == q["answer"]:
                color = GREEN
            elif i == selected:
                color = RED
        elif i == selected:
            color = BLUE
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        draw_text(option, rect.x + 10, rect.y + 10)

def next_question():
    global current_question, selected, answered, answer_time
    current_question += 1
    selected = -1
    answered = False
    answer_time = None

running = True
while running:
    screen.fill(WHITE)

    if current_question < len(questions):
        draw_question()

        # Auto-advance after 2 seconds
        if answered and answer_time and time.time() - answer_time > 1:
            next_question()
    else:
        draw_text(f"Quiz complete! 🎉 Your score: {score} / {len(questions)}", 200, 300)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not answered and current_question < len(questions):
            for i in range(3):
                rect = pygame.Rect(50, 130 + i * 60, 700, 50)
                if rect.collidepoint(event.pos):
                    selected = i
                    answered = True
                    answer_time = time.time()
                    if selected == questions[current_question]["answer"]:
                        score += 1

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
