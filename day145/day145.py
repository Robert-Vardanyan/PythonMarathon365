import pygame
import sys
import json
import os

pygame.init()

WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Daily Goal Tracker")

font = pygame.font.SysFont("Arial", 24)
small_font = pygame.font.SysFont("Arial", 18)
clock = pygame.time.Clock()

GOALS_FILE = "daily_goals.json"

# Load goals from file or empty list
if os.path.exists(GOALS_FILE):
    with open(GOALS_FILE, "r") as f:
        goals = json.load(f)
else:
    goals = []  # list of dicts: {"text": str, "done": bool}

input_text = ""
input_active = False
error_message = ""

def save_goals():
    with open(GOALS_FILE, "w") as f:
        json.dump(goals, f)

def draw_text(text, font, color, x, y):
    rendered = font.render(text, True, color)
    screen.blit(rendered, (x, y))

def draw_goals():
    y = 80
    for i, goal in enumerate(goals):
        color = (0, 150, 0) if goal["done"] else (0, 0, 0)
        checkbox = "✅" if goal["done"] else "⬜"
        draw_text(f"{checkbox} {goal['text']}", font, color, 50, y)
        y += 35

running = True
while running:
    screen.fill((240, 240, 240))
    draw_text("Daily Goal Tracker", font, (20, 20, 60), 50, 20)

    # Input box
    input_box = pygame.Rect(50, 50, 500, 30)
    pygame.draw.rect(screen, (255, 255, 255), input_box)
    pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
    draw_text(input_text, font, (0, 0, 0), input_box.x + 5, input_box.y + 3)

    # Instructions
    draw_text("Type a goal and press Enter to add", small_font, (80, 80, 80), 50, 90)

    # Draw goals
    draw_goals()

    # Draw progress
    done_count = sum(1 for g in goals if g["done"])
    total_count = len(goals)
    draw_text(f"Progress: {done_count} / {total_count}", font, (0, 100, 0), 400, 20)

    if error_message:
        draw_text(error_message, small_font, (200, 0, 0), 50, HEIGHT - 40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_goals()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            # Check if clicked on any goal
            y = 80
            for goal in goals:
                rect = pygame.Rect(50, y, 500, 30)
                if rect.collidepoint(mx, my):
                    goal["done"] = not goal["done"]
                    save_goals()
                    break
                y += 35
            # Check if input box clicked
            if input_box.collidepoint(mx, my):
                input_active = True
            else:
                input_active = False
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                if input_text.strip() == "":
                    error_message = "Goal cannot be empty!"
                else:
                    goals.append({"text": input_text.strip(), "done": False})
                    input_text = ""
                    error_message = ""
                    save_goals()
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if len(input_text) < 50:
                    input_text += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
