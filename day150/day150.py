import pygame
import sys
import datetime
import json
import os

pygame.init()
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎂 Birthday Reminder")

font = pygame.font.SysFont("arial", 24)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
GREEN = (0, 200, 100)

input_boxes = {
    "name": {"rect": pygame.Rect(150, 50, 200, 32), "text": ""},
    "date": {"rect": pygame.Rect(150, 100, 200, 32), "text": ""},  # format: YYYY-MM-DD
}
input_active = None

add_button = pygame.Rect(380, 75, 100, 40)
birthdays = []

FILE = "birthdays.json"

def load_birthdays():
    global birthdays
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            birthdays = json.load(f)

def save_birthdays():
    with open(FILE, "w") as f:
        json.dump(birthdays, f, indent=2)

def draw_text(text, x, y, color=BLACK):
    screen.blit(font.render(text, True, color), (x, y))

def draw_input(name, label):
    box = input_boxes[name]
    rect = box["rect"]
    pygame.draw.rect(screen, WHITE, rect)
    pygame.draw.rect(screen, BLUE if input_active == name else GRAY, rect, 2)
    draw_text(label, rect.x - 100, rect.y + 5)
    screen.blit(font.render(box["text"], True, BLACK), (rect.x + 5, rect.y + 5))

def draw_birthdays():
    y = 180
    today = datetime.date.today().strftime("%m-%d")
    for person in birthdays:
        try:
            date_obj = datetime.datetime.strptime(person["date"], "%Y-%m-%d").date()
            color = GREEN if date_obj.strftime("%m-%d") == today else BLACK
        except:
            color = BLACK
        text = f"{person['name']} - {person['date']}"
        draw_text(text, 60, y, color)
        y += 30

def add_birthday(name, date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")  # check format
        birthdays.append({"name": name, "date": date_str})
        save_birthdays()
        input_boxes["name"]["text"] = ""
        input_boxes["date"]["text"] = ""
    except:
        print("Invalid date format. Use YYYY-MM-DD.")

load_birthdays()

running = True
while running:
    screen.fill(WHITE)
    draw_text("🎂 Birthday Reminder", 240, 10, BLUE)

    draw_input("name", "Name:")
    draw_input("date", "Date:")

    pygame.draw.rect(screen, GREEN, add_button)
    draw_text("➕ Add", add_button.x + 15, add_button.y + 8)

    draw_text("Upcoming Birthdays:", 60, 140, BLUE)
    draw_birthdays()

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
                    add_birthday(name, date)

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
