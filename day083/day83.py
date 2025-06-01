import pygame
import json
import os

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz with Leaderboard")
font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (70, 130, 180)

leaderboard_file = "leaderboard.json"

# Sample quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which element has the chemical symbol O?",
        "options": ["Gold", "Oxygen", "Osmium", "Iron"],
        "answer": "Oxygen"
    },
    {
        "question": "Who wrote 'Macbeth'?",
        "options": ["Tolstoy", "Shakespeare", "Hemingway", "Dante"],
        "answer": "Shakespeare"
    }
]

# Load leaderboard from file
def load_leaderboard():
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as file:
            return json.load(file)
    return []

# Save leaderboard to file
def save_leaderboard(leaderboard):
    with open(leaderboard_file, "w") as file:
        json.dump(leaderboard, file)

# Draw text centered
def draw_text(text, x, y, color=BLACK, center=True, fnt=font):
    txt_surface = fnt.render(text, True, color)
    rect = txt_surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(txt_surface, rect)

# Display question and options
def show_question(q, selected):
    screen.fill(WHITE)
    draw_text(f"Question {q_index + 1}/{len(questions)}", WIDTH // 2, 40, BLUE, fnt=big_font)
    draw_text(q['question'], WIDTH // 2, 100, BLACK, fnt=font)
    
    for i, option in enumerate(q["options"]):
        color = GREEN if selected == i else GRAY
        pygame.draw.rect(screen, color, (150, 160 + i * 60, 500, 40), 0, 5)
        draw_text(option, 400, 180 + i * 60, BLACK)

# Ask user for name
def ask_name(score):
    user_text = ""
    input_active = True
    while input_active:
        screen.fill(WHITE)
        draw_text("Quiz Complete!", WIDTH // 2, 100, BLUE, fnt=big_font)
        draw_text(f"Your Score: {score}/{len(questions)}", WIDTH // 2, 160, GREEN)
        draw_text("Enter your name:", WIDTH // 2, 230, BLACK)
        pygame.draw.rect(screen, GRAY, (250, 270, 300, 40), 0, 5)
        draw_text(user_text, 400, 290, BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user_text.strip() != "":
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        pygame.display.update()
        clock.tick(30)
    return user_text

# Show leaderboard
def show_leaderboard():
    lb = load_leaderboard()
    screen.fill(WHITE)
    draw_text("Leaderboard", WIDTH // 2, 50, BLUE, fnt=big_font)
    y = 120
    for i, entry in enumerate(lb[:10]):
        draw_text(f"{i+1}. {entry['name']} - {entry['score']}", WIDTH // 2, y, BLACK)
        y += 40
    draw_text("Press any key to quit", WIDTH // 2, HEIGHT - 50, RED)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            elif event.type == pygame.KEYDOWN:
                waiting = False

# Main quiz logic
score = 0
q_index = 0
selected = -1
waiting_for_click = True

while q_index < len(questions):
    show_question(questions[q_index], selected)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and waiting_for_click:
            mx, my = pygame.mouse.get_pos()
            for i in range(4):
                rect = pygame.Rect(150, 160 + i * 60, 500, 40)
                if rect.collidepoint(mx, my):
                    selected = i
                    waiting_for_click = False
                    if questions[q_index]["options"][i] == questions[q_index]["answer"]:
                        score += 1

        elif event.type == pygame.KEYDOWN and not waiting_for_click:
            if event.key == pygame.K_RETURN:
                selected = -1
                q_index += 1
                waiting_for_click = True

pygame.time.delay(500)
user_name = ask_name(score)

# Update and save leaderboard
leaderboard = load_leaderboard()
leaderboard.append({"name": user_name, "score": score})
leaderboard.sort(key=lambda x: x["score"], reverse=True)
save_leaderboard(leaderboard)

# Show leaderboard
show_leaderboard()
pygame.quit()
