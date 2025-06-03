import pygame
import sys
import re

pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("String Pattern Finder")

# Colors
BG_COLOR = (240, 240, 240)
TEXT_COLOR = (0, 0, 0)
INPUT_BG = (255, 255, 255)
ACTIVE_BG = (220, 220, 255)
BUTTON_COLOR = (100, 149, 237)
BUTTON_HOVER = (65, 105, 225)

font = pygame.font.SysFont("Arial", 24)
small_font = pygame.font.SysFont("Arial", 18)

# Input fields
input_text = ""
pattern = ""
active_input = "text"
result_matches = []

text_rect = pygame.Rect(50, 50, 700, 40)
pattern_rect = pygame.Rect(50, 120, 700, 40)
button_rect = pygame.Rect(300, 180, 200, 40)

clock = pygame.time.Clock()

def draw_textbox(rect, text, active):
    pygame.draw.rect(win, ACTIVE_BG if active else INPUT_BG, rect, border_radius=6)
    rendered_text = font.render(text, True, TEXT_COLOR)
    win.blit(rendered_text, (rect.x + 10, rect.y + 8))
    pygame.draw.rect(win, TEXT_COLOR, rect, 2, border_radius=6)

def draw_button(rect, text, hover=False):
    color = BUTTON_HOVER if hover else BUTTON_COLOR
    pygame.draw.rect(win, color, rect, border_radius=8)
    text_surf = font.render(text, True, (255, 255, 255))
    win.blit(text_surf, (rect.centerx - text_surf.get_width() // 2, rect.centery - text_surf.get_height() // 2))

def highlight_matches(base_text, matches, x, y, width):
    words = base_text.split()
    offset = 0
    display_line = ''
    line_height = 0
    for word in words:
        space = ' ' if display_line else ''
        new_line = display_line + space + word
        line_surface = small_font.render(new_line, True, TEXT_COLOR)
        if line_surface.get_width() > width:
            rendered = small_font.render(display_line, True, TEXT_COLOR)
            win.blit(rendered, (x, y + line_height))
            line_height += 25
            display_line = word
        else:
            display_line = new_line
    rendered = small_font.render(display_line, True, TEXT_COLOR)
    win.blit(rendered, (x, y + line_height))

running = True
while running:
    win.fill(BG_COLOR)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]

    # Labels
    win.blit(font.render("Enter text:", True, TEXT_COLOR), (50, 20))
    win.blit(font.render("Enter pattern (regex):", True, TEXT_COLOR), (50, 95))

    # Textboxes
    draw_textbox(text_rect, input_text, active_input == "text")
    draw_textbox(pattern_rect, pattern, active_input == "pattern")

    # Button
    hovered = button_rect.collidepoint(mouse)
    draw_button(button_rect, "Find Pattern", hovered)

    # Display results
    if result_matches:
        win.blit(font.render(f"Matches found: {len(result_matches)}", True, TEXT_COLOR), (50, 240))
        y_offset = 280
        for match in result_matches[:5]:
            win.blit(small_font.render(f"- {match}", True, TEXT_COLOR), (60, y_offset))
            y_offset += 25
        if len(result_matches) > 5:
            win.blit(small_font.render(f"...and {len(result_matches) - 5} more", True, TEXT_COLOR), (60, y_offset))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_rect.collidepoint(event.pos):
                active_input = "text"
            elif pattern_rect.collidepoint(event.pos):
                active_input = "pattern"
            elif button_rect.collidepoint(event.pos):
                try:
                    result_matches = re.findall(pattern, input_text)
                except:
                    result_matches = ["Invalid pattern"]

        if event.type == pygame.KEYDOWN:
            if active_input == "text":
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            elif active_input == "pattern":
                if event.key == pygame.K_BACKSPACE:
                    pattern = pattern[:-1]
                else:
                    pattern += event.unicode

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
