import pygame
import sys
import json
import os
import datetime

pygame.init()
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⏳ Event Countdown Tracker")

font = pygame.font.SysFont("arial", 24)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
BLACK = (0, 0, 0)
BLUE = (0, 120, 215)
GREEN = (0, 200, 100)
RED = (200, 50, 50)

input_boxes = {
    "name": {"rect": pygame.Rect(150, 50, 220, 32), "text": ""},
    "date": {"rect": pygame.Rect(150, 100, 220, 32), "text": ""},
}
input_active = None
add_button = pygame.Rect(390, 75, 100, 40)

events = []
DATA_FILE = "events.json"

def load_events():
    global events
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            events = json.load(f)

def save_events():
    with open(DATA_FILE, "w") as f:
        json.dump(events, f, indent=2)

def draw_text(text, x, y, color=BLACK):
    screen.blit(font.render(text, True, color), (x, y))

def draw_input(name, label):
    box = input_boxes[name]
    rect = box["rect"]
    pygame.draw.rect(screen, WHITE, rect)
    pygame.draw.rect(screen, BLUE if input_active == name else GRAY, rect, 2)
    draw_text(label, rect.x - 100, rect.y + 5)
    screen.blit(font.render(box["text"], True, BLACK), (rect.x + 5, rect.y + 5))

def draw_events():
    y = 180
    today = datetime.date.today()
    for event in events:
        try:
            date_obj = datetime.datetime.strptime(event["date"], "%Y-%m-%d").date()
            days_left = (date_obj - today).days
            color = GREEN if days_left == 0 else BLACK
            label = f"{event['name']} - {event['date']} ({'Today!' if days_left == 0 else str(days_left) + ' days left'})"
            draw_text(label, 60, y, color)
            y += 30
        except:
            continue

def add_event(name, date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")  # validate
        events.append({"name": name, "date": date_str})
        save_events()
        input_boxes["name"]["text"] = ""
        input_boxes["date"]["text"] = ""
    except:
        print("Invalid date format")

load_events()

running = True
while running:
    screen.fill(WHITE)
    draw_text("⏳ Event Countdown Tracker", 200, 10, BLUE)

    draw_input("name", "Event:")
    draw_input("date", "Date:")

    pygame.draw.rect(screen, GREEN, add_button)
    draw_text("➕ Add", add_button.x + 20, add_button.y + 8)

    draw_text("Upcoming Events:", 60, 140, BLUE)
    draw_events()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = None
            for name, box in input_boxes.items():
                if box["rect"].collidepoint(event.pos):
                    input_active = name
            if add_button.collidepoint(event.pos):
                name = input_boxes["name"]["text"]
                date = input_boxes["date"]["text"]
                if name and date:
                    add_event(name, date)

        elif event.type == pygame.KEYDOWN and input_active:
            box = input_boxes[input_active]
            if event.key == pygame.K_BACKSPACE:
                box["text"] = box["text"][:-1]
            elif event.key == pygame.K_RETURN:
                input_active = None
            else:
                if input_active == "date":
                    if event.unicode.isdigit() and len(box["text"].replace("-", "")) < 8:
                        clean = box["text"].replace("-", "") + event.unicode
                        if len(clean) >= 5:
                            box["text"] = clean[:4] + "-" + clean[4:6]
                            if len(clean) > 6:
                                box["text"] += "-" + clean[6:]
                        elif len(clean) >= 4:
                            box["text"] = clean[:4] + "-" + clean[4:]
                        else:
                            box["text"] = clean
                else:
                    box["text"] += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
