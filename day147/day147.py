import pygame
import requests
import sys

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🤓 Random Fun Fact Generator")

# Colors
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
LIGHT_GREEN = (0, 255, 0)

font = pygame.font.SysFont(None, 28)
title_font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def fetch_fact():
    try:
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["text"]
        else:
            return "⚠️ Could not load fact."
    except Exception as e:
        return "❌ Error: " + str(e)

def draw_button(text, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action:
            pygame.time.delay(150)  # prevent double click
            return action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))

    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + w/2, y + h/2))
    screen.blit(text_surf, text_rect)
    return None

def wrap_text(text, font, max_width):
    """Split text into lines that fit within max_width"""
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())
    return lines

current_fact = "Click the button to get a random fact!"

# Game loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    title = title_font.render("🤓 Random Fun Fact Generator", True, BLUE)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))

    result = draw_button("Generate Fact", WIDTH//2 - 80, HEIGHT - 80, 160, 50, GREEN, LIGHT_GREEN, fetch_fact)
    if result:
        current_fact = result

    # Draw fact text wrapped
    lines = wrap_text(current_fact, font, WIDTH - 40)
    y_offset = 120
    for line in lines:
        rendered_line = font.render(line, True, BLACK)
        screen.blit(rendered_line, (20, y_offset))
        y_offset += 30

    pygame.display.flip()
    clock.tick(30)
