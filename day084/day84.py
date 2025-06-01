import pygame
import requests
import textwrap

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Fact Generator")
FONT = pygame.font.SysFont('arial', 28)
BUTTON_FONT = pygame.font.SysFont('arial', 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)

# Fetch a random fact from API
def get_random_fact():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        if response.status_code == 200:
            return response.json().get("text", "No fact found.")
        else:
            return "Could not fetch a fact."
    except:
        return "Error connecting to fact server."

# Draw multiline text centered
def draw_text_centered(surface, text, font, color, y_start):
    wrapped_lines = textwrap.wrap(text, width=60)
    total_height = len(wrapped_lines) * font.get_height()
    y_offset = y_start - total_height // 2
    for line in wrapped_lines:
        line_surface = font.render(line, True, color)
        x = (WIDTH - line_surface.get_width()) // 2
        surface.blit(line_surface, (x, y_offset))
        y_offset += font.get_height()

# Button class
class Button:
    def __init__(self, text, x, y, w, h, color, text_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        text_surf = BUTTON_FONT.render(self.text, True, self.text_color)
        surface.blit(
            text_surf,
            (
                self.rect.centerx - text_surf.get_width() // 2,
                self.rect.centery - text_surf.get_height() // 2,
            ),
        )

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Setup
fact = "Click the button to get a random fact!"
button = Button("New Fact", WIDTH//2 - 75, HEIGHT - 100, 150, 50, BLUE, WHITE)

# Main loop
running = True
while running:
    SCREEN.fill(WHITE)
    draw_text_centered(SCREEN, fact, FONT, BLACK, HEIGHT//2 - 30)
    button.draw(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_clicked(event.pos):
                fact = get_random_fact()

    pygame.display.flip()

pygame.quit()
