import pygame
import datetime
import json
import os

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("📘 Habit Tracker")

font = pygame.font.SysFont("arial", 24)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (210, 210, 210)
BLACK = (0, 0, 0)
GREEN = (100, 200, 100)
BLUE = (100, 150, 255)

input_width = 300
input_height = 32
input_x = WIDTH // 2 - input_width // 2
input_y = 30
input_box = pygame.Rect(input_x, input_y, input_width, input_height)

input_text = ""
input_active = False

habits = []
DATA_FILE = "habits.json"

def load_habits():
    global habits
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            habits = json.load(f)

def save_habits():
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=2)

def draw_text(text, x, y, color=BLACK):
    screen.blit(font.render(text, True, color), (x, y))

def draw_habits():
    y = 100
    for i, habit in enumerate(habits):
        draw_text(habit["name"], 60, y)
        for j in range(7):  # 7 days
            date = (datetime.date.today() - datetime.timedelta(days=6-j)).isoformat()
            rect = pygame.Rect(300 + j * 50, y, 30, 30)
            color = GREEN if date in habit["dates"] else GRAY
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)
        y += 50

def toggle_habit(habit_idx, day_idx):
    date = (datetime.date.today() - datetime.timedelta(days=6-day_idx)).isoformat()
    if date in habits[habit_idx]["dates"]:
        habits[habit_idx]["dates"].remove(date)
    else:
        habits[habit_idx]["dates"].append(date)
    save_habits()

load_habits()

running = True
while running:
    screen.fill(WHITE)
    draw_text("📘 Habit Tracker", 50, 0, BLUE)

    pygame.draw.rect(screen, WHITE, input_box)
    pygame.draw.rect(screen, BLUE if input_active else GRAY, input_box, 2)
    screen.blit(font.render(input_text, True, BLACK), (input_box.x + 5, input_box.y + 5))
    
    # Draw the label to the left of input box
    label = "New Habit:"
    label_surface = font.render(label, True, BLACK)
    screen.blit(label_surface, (input_box.x - label_surface.get_width() - 10, input_box.y + 5))

    draw_habits()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                input_active = True
            else:
                input_active = False

            y = 100
            for i, habit in enumerate(habits):
                for j in range(7):
                    rect = pygame.Rect(300 + j * 50, y, 30, 30)
                    if rect.collidepoint(event.pos):
                        toggle_habit(i, j)
                y += 50

        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                if input_text.strip():
                    habits.append({"name": input_text.strip(), "dates": []})
                    save_habits()
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
