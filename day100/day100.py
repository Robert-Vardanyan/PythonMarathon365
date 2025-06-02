import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Window size and setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Greeting Generator")

# Colors
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 160, 210)

# Fonts
font = pygame.font.SysFont('arial', 40, bold=True)

# Greetings list
greetings = [
    "Hello!",
    "Hi there!",
    "Greetings!",
    "Welcome!",
    "Good day!",
    "Howdy!",
    "Hey!",
    "Salutations!",
    "Yo!",
    "Bonjour!",
    "Hola!",
    "Ciao!",
    "Namaste!",
    "Konnichiwa!"
]

def draw_text(text, font, color, surface, x, y):
    """Draw text centered at (x, y)."""
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def main():
    current_greeting = random.choice(greetings)

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BG_COLOR)

        # Draw current greeting text in center
        draw_text(current_greeting, font, TEXT_COLOR, screen, WIDTH // 2, HEIGHT // 2)

        # Instructions at the bottom
        instruction_font = pygame.font.SysFont('arial', 18)
        draw_text("Press SPACE for a new greeting, ESC to quit.", instruction_font, (180, 180, 180), screen, WIDTH // 2, HEIGHT - 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    # Pick a new greeting different from the current one
                    new_greeting = current_greeting
                    while new_greeting == current_greeting:
                        new_greeting = random.choice(greetings)
                    current_greeting = new_greeting

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
