import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Syntax Quiz")
font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

WHITE, BLACK, BLUE, GREEN, RED, GRAY = (255, 255, 255), (0, 0, 0), (100, 149, 237), (0, 200, 0), (200, 0, 0), (230, 230, 230)

questions = [
    {
        "question": "What does 'len()' do in Python?",
        "options": ["Returns length", "Returns last element", "Returns type", "None of the above"],
        "answer": 0
    },
    {
        "question": "Which of these is a valid Python comment?",
        "options": ["// comment", "# comment", "<!-- comment -->", "/* comment */"],
        "answer": 1
    },
    {
        "question": "Which keyword is used for a function?",
        "options": ["def", "func", "function", "lambda"],
        "answer": 0
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".pt", ".pyt", ".py", ".p"],
        "answer": 2
    },
    {
        "question": "What does '==' mean?",
        "options": ["Assign", "Equal", "Compare", "Check"],
        "answer": 1
    },
]

current_question = 0
score = 0
selected = -1
show_result = False

def draw_question():
    screen.fill(WHITE)
    q = questions[current_question]
    question_surface = big_font.render(q["question"], True, BLACK)
    screen.blit(question_surface, (WIDTH//2 - question_surface.get_width()//2, 50))

    for i, option in enumerate(q["options"]):
        color = BLUE if i == selected else GRAY
        option_rect = pygame.Rect(150, 150 + i*70, 500, 50)
        pygame.draw.rect(screen, color, option_rect, border_radius=8)
        text = font.render(option, True, BLACK)
        screen.blit(text, (option_rect.x + 10, option_rect.y + 10))

    next_text = font.render("Next", True, WHITE)
    next_button = pygame.Rect(WIDTH//2 - 60, 480, 120, 40)
    pygame.draw.rect(screen, GREEN, next_button, border_radius=6)
    screen.blit(next_text, (next_button.x + 25, next_button.y + 8))
    return next_button

def draw_result():
    screen.fill(WHITE)
    title = big_font.render("Quiz Completed!", True, BLACK)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
    result = font.render(f"Your Score: {score} / {len(questions)}", True, BLUE)
    screen.blit(result, (WIDTH//2 - result.get_width()//2, 200))

    restart_btn = pygame.Rect(WIDTH//2 - 75, 300, 150, 40)
    pygame.draw.rect(screen, RED, restart_btn, border_radius=6)
    restart_text = font.render("Restart", True, WHITE)
    screen.blit(restart_text, (restart_btn.x + 35, restart_btn.y + 8))
    return restart_btn

running = True
while running:
    if show_result:
        restart_button = draw_result()
    else:
        next_button = draw_question()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if show_result:
                if restart_button.collidepoint(event.pos):
                    current_question = 0
                    score = 0
                    selected = -1
                    show_result = False
            else:
                for i in range(4):
                    rect = pygame.Rect(150, 150 + i * 70, 500, 50)
                    if rect.collidepoint(event.pos):
                        selected = i
                if next_button.collidepoint(event.pos) and selected != -1:
                    if selected == questions[current_question]["answer"]:
                        score += 1
                    current_question += 1
                    selected = -1
                    if current_question >= len(questions):
                        show_result = True

    clock.tick(30)

pygame.quit()
sys.exit()
