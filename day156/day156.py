import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌿 Plant Care Reminder")

font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

plants = []  # List of plants: dict with name, interval in hours, and last watered time
input_text = ""
input_active = False
input_mode = None  # 'name' or 'interval'
current_plant = {}

def draw_text(text, x, y, font, color=(0,0,0)):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

def add_plant(name, interval_hours):
    plants.append({
        "name": name,
        "interval": interval_hours * 3600,  # convert to seconds
        "last_watered": time.time()
    })

def get_time_left(plant):
    elapsed = time.time() - plant["last_watered"]
    left = plant["interval"] - elapsed
    return max(left, 0)

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h}h {m}m {s}s"

running = True
message = ""
while running:
    screen.fill((230, 255, 230))

    draw_text("🌿 Plant Care Reminder", 180, 10, big_font)

    # Draw the list of plants
    y = 60
    for plant in plants:
        left = get_time_left(plant)
        status = "💧 Water now!" if left == 0 else f"Next in: {format_time(left)}"
        draw_text(f"{plant['name']} — {status}", 30, y, font, (0,100,0) if left>0 else (200,0,0))
        y += 30

    # Instructions and current input status
    if not input_active:
        draw_text("Press 'N' to add a new plant", 30, HEIGHT - 70, font)
    else:
        prompt = "Enter plant name:" if input_mode == "name" else "Enter watering interval (hours):"
        draw_text(prompt, 30, HEIGHT - 100, font)
        draw_text(input_text, 30, HEIGHT - 70, font)

    # Error or confirmation message
    if message:
        draw_text(message, 30, HEIGHT - 40, font, (200, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if not input_active:
                if event.key == pygame.K_n:
                    input_active = True
                    input_mode = "name"
                    input_text = ""
                    current_plant = {}
                    message = ""
            else:
                if event.key == pygame.K_RETURN:
                    if input_mode == "name":
                        if input_text.strip():
                            current_plant["name"] = input_text.strip()
                            input_mode = "interval"
                            input_text = ""
                            message = ""
                        else:
                            message = "Name cannot be empty!"
                    elif input_mode == "interval":
                        try:
                            interval = float(input_text.strip())
                            if interval <= 0:
                                raise ValueError
                            current_plant["interval"] = interval
                            add_plant(current_plant["name"], current_plant["interval"])
                            input_active = False
                            message = f"Added plant '{current_plant['name']}'"
                        except ValueError:
                            message = "Please enter a positive number for interval!"
                        input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
