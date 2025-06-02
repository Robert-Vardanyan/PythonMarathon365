import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BEIGE = (255, 248, 220)
BROWN = (139, 69, 19)
DARK_BROWN = (100, 40, 0)
LIGHT_BROWN = (205, 133, 63)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Fortune Cookie")

FONT = pygame.font.SysFont('arial', 22)
BIG_FONT = pygame.font.SysFont('arial', 28, bold=True)

# Fortune list
fortunes = [
    "Your future is as bright as the sun.",
    "A fresh start will put you on your way.",
    "A thrilling time is in your near future.",
    "You will conquer obstacles to achieve success.",
    "Happiness begins with facing life with a smile.",
    "Something wonderful is about to happen.",
    "You will soon embark on a new journey.",
    "A new perspective will come with the new year.",
    "Good news will come to you from far away.",
    "You will make a valuable new connection soon."
]

last_fortune = None

# Button settings
button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 200, 50)

def get_new_fortune():
    global last_fortune
    fortune = random.choice(fortunes)
    while fortune == last_fortune:
        fortune = random.choice(fortunes)
    last_fortune = fortune
    return fortune

def draw_button(mouse_pos):
    color = LIGHT_BROWN if button_rect.collidepoint(mouse_pos) else BROWN
    pygame.draw.rect(screen, color, button_rect, border_radius=8)
    pygame.draw.rect(screen, DARK_BROWN, button_rect, 3, border_radius=8)
    text = FONT.render("Crack the Cookie", True, WHITE)
    screen.blit(text, (button_rect.centerx - text.get_width() // 2,
                       button_rect.centery - text.get_height() // 2))

def main():
    running = True
    fortune_text = ""
    show_message = False

    while running:
        screen.fill(BEIGE)

        mouse_pos = pygame.mouse.get_pos()

        # Title
        title = BIG_FONT.render("Digital Fortune Cookie", True, DARK_BROWN)
        screen.blit(title, ((WIDTH - title.get_width()) // 2, 30))

        # Fortune text or hint
        if show_message:
            wrapped = []
            words = fortune_text.split()
            line = ""
            for word in words:
                if FONT.size(line + word + " ")[0] > WIDTH - 80:
                    wrapped.append(line)
                    line = word + " "
                else:
                    line += word + " "
            wrapped.append(line)

            for i, line in enumerate(wrapped):
                fortune_surface = FONT.render(line.strip(), True, BLACK)
                screen.blit(fortune_surface, ((WIDTH - fortune_surface.get_width()) // 2, 120 + i * 30))
        else:
            hint = FONT.render("Click the cookie!", True, DARK_BROWN)
            screen.blit(hint, ((WIDTH - hint.get_width()) // 2, 150))

        # Draw cookie button
        draw_button(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    fortune_text = get_new_fortune()
                    show_message = True

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
