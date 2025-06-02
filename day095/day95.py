import pygame
import random
import sys

pygame.init()

# Window setup
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Poem Generator")

# Fonts
FONT = pygame.font.SysFont("georgia", 24)
TITLE_FONT = pygame.font.SysFont("georgia", 32, bold=True)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
DARK_BLUE = (30, 60, 90)

# Poem data
lines_part1 = [
    "The winds of time whisper low",
    "Beneath the sky's eternal dome",
    "Shadows walk where sunlight sleeps",
    "Through silent trees, the moon aglow",
    "When oceans breathe in midnight tones",
]

lines_part2 = [
    "Hearts that dream, forever yearn",
    "And hopes like embers softly turn",
    "Memories echo through the dust",
    "Stars collapse in silver trust",
    "Eyes reflect the soul’s deep fire",
]

lines_part3 = [
    "Moments pass like falling rain",
    "Love engraved in fleeting flame",
    "Time unwinds without a sound",
    "The void replies with no refrain",
    "While ashes of the stars still burn",
]

def generate_poem():
    return random.sample(lines_part1, 1) + random.sample(lines_part2, 1) + random.sample(lines_part3, 2)

# Buttons
button_rect = pygame.Rect(WIDTH//2 - 80, HEIGHT - 70, 160, 40)

# Initial poem
poem_lines = generate_poem()

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # Title
    title_surf = TITLE_FONT.render("Random Poem Generator", True, DARK_BLUE)
    screen.blit(title_surf, (WIDTH//2 - title_surf.get_width()//2, 30))

    # Display poem
    for i, line in enumerate(poem_lines):
        text_surf = FONT.render(line, True, BLACK)
        screen.blit(text_surf, (WIDTH//2 - text_surf.get_width()//2, 120 + i * 40))

    # Draw button
    pygame.draw.rect(screen, DARK_BLUE, button_rect, border_radius=5)
    btn_text = FONT.render("New Poem", True, WHITE)
    screen.blit(btn_text, (button_rect.x + 30, button_rect.y + 8))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                poem_lines = generate_poem()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
