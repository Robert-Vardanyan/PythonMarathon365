import pygame
import sys
import re

pygame.init()

WIDTH, HEIGHT = 500, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("📧 Email Format Validator")

font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

input_text = ""
input_active = True
message = ""

def draw_text(text, x, y, font, color=(0,0,0)):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

def is_valid_email(email):
    # Simple email format check using regular expression
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

running = True
while running:
    screen.fill((230, 230, 255))

    draw_text("📧 Enter email to validate:", 30, 20, big_font)
    draw_text(input_text, 30, 70, font)

    if message:
        color = (0, 150, 0) if message == "Valid email!" else (200, 0, 0)
        draw_text(message, 30, 120, font, color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                if is_valid_email(input_text.strip()):
                    message = "Valid email!"
                else:
                    message = "Invalid email format!"
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
