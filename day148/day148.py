import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("💸 Simple Budget Planner")

font = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)

income = 0
expenses = []
input_active = None
input_boxes = {
    "income": {"rect": pygame.Rect(180, 50, 200, 32), "text": "", "surface": None},
    "category": {"rect": pygame.Rect(180, 150, 140, 32), "text": "", "surface": None},
    "amount": {"rect": pygame.Rect(340, 150, 100, 32), "text": "", "surface": None},
}

def draw_text(text, x, y, color=BLACK):
    surf = font.render(text, True, color)
    screen.blit(surf, (x, y))

def draw_input(name, label):
    box = input_boxes[name]
    rect = box["rect"]
    pygame.draw.rect(screen, WHITE, rect)
    pygame.draw.rect(screen, BLUE if input_active == name else GRAY, rect, 2)

    draw_text(label, rect.x - 110, rect.y + 5)

    text_surface = font.render(box["text"], True, BLACK)
    text_width = text_surface.get_width()
    max_width = rect.width - 10

    if text_width > max_width:
        offset = text_width - max_width
        text_surface = text_surface.subsurface((offset, 0, max_width, text_surface.get_height()))

    screen.blit(text_surface, (rect.x + 5, rect.y + 5))

def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect)
    draw_text(text, rect.x + 10, rect.y + 8)

def reset_inputs():
    for box in input_boxes.values():
        box["text"] = ""

add_button = pygame.Rect(460, 150, 100, 32)

def draw_ui():
    screen.fill(WHITE)
    draw_text("💸 Simple Budget Planner", 180, 10, BLUE)
    draw_input("income", "Monthly Income:")
    draw_input("category", "Category:")
    draw_input("amount", "Amount:")

    draw_button("Add", add_button, GREEN)

    draw_text("🧾 Expenses:", 50, 220)
    y = 250
    total_expense = 0
    for cat, amt in expenses:
        draw_text(f"{cat}: -${amt}", 60, y, RED)
        y += 30
        total_expense += amt

    balance = income - total_expense
    draw_text(f"Total Income: ${income}", 60, HEIGHT - 100, GREEN)
    draw_text(f"Total Expenses: ${total_expense}", 60, HEIGHT - 70, RED)
    draw_text(f"Balance: ${balance}", 60, HEIGHT - 40, BLUE)

running = True
while running:
    screen.fill(WHITE)
    draw_ui()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = None
            for name, box in input_boxes.items():
                if box["rect"].collidepoint(event.pos):
                    input_active = name
            if add_button.collidepoint(event.pos):
                try:
                    cat = input_boxes["category"]["text"]
                    amt = float(input_boxes["amount"]["text"])
                    if cat:
                        expenses.append((cat, amt))
                        reset_inputs()
                except:
                    pass

        elif event.type == pygame.KEYDOWN and input_active:
            box = input_boxes[input_active]
            if event.key == pygame.K_RETURN:
                if input_active == "income":
                    try:
                        income = float(box["text"])
                    except:
                        income = 0
                input_active = None
            elif event.key == pygame.K_BACKSPACE:
                box["text"] = box["text"][:-1]
            else:
                if len(box["text"]) < 100:  # just in case
                    box["text"] += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
