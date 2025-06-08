import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Scrambler")

# Colors
WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)

# Fonts
FONT = pygame.font.SysFont(None, 36)

# Input and output
input_text = ""
scrambled_text = ""

# Input box
input_box = pygame.Rect(50, 50, 400, 40)

# Buttons
scramble_button = pygame.Rect(50, 110, 180, 40)
clear_button = pygame.Rect(270, 110, 180, 40)

clock = pygame.time.Clock()

def scramble_word(word):
    chars = list(word)
    random.shuffle(chars)
    return ''.join(chars)

running = True
active = False

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if user clicked inside the input box
            active = input_box.collidepoint(event.pos)

            if scramble_button.collidepoint(event.pos):
                scrambled_text = scramble_word(input_text)

            if clear_button.collidepoint(event.pos):
                input_text = ""
                scrambled_text = ""

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif len(input_text) < 30 and event.unicode.isprintable():
                input_text += event.unicode

    # Draw input box
    pygame.draw.rect(screen, GRAY if active else BLUE, input_box, 2)
    input_surface = FONT.render(input_text, True, BLACK)
    screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))

    # Draw buttons
    pygame.draw.rect(screen, BLUE, scramble_button)
    scramble_label = FONT.render("Scramble", True, WHITE)
    screen.blit(scramble_label, (scramble_button.x + 30, scramble_button.y + 5))

    pygame.draw.rect(screen, BLUE, clear_button)
    clear_label = FONT.render("Clear", True, WHITE)
    screen.blit(clear_label, (clear_button.x + 60, clear_button.y + 5))

    # Show scrambled result
    if scrambled_text:
        label = FONT.render(f"Scrambled: {scrambled_text}", True, BLACK)
        screen.blit(label, (50, 180))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
