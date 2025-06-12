import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎵 Music Genre Recommender")

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

# Mood to genre mapping
mood_genres = {
    "😊 Happy": "Pop",
    "😢 Sad": "Blues",
    "🔥 Energetic": "Rock",
    "😴 Relaxed": "Lo-fi",
    "💭 Thoughtful": "Jazz"
}

selected_genre = None

# Button class
class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        text_surface = font.render(self.text, True, BLACK)
        surface.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create buttons
buttons = []
y = 100
for mood in mood_genres:
    buttons.append(Button(mood, 150, y, 300, 50))
    y += 70

# Function to draw genre recommendation centered below buttons
def draw_genre(genre):
    genre_text = f"🎧 You should listen to: {genre}"
    text_surface = font.render(genre_text, True, DARK_GRAY)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, y + 30))
    screen.blit(text_surface, text_rect)

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Title
    title = font.render("What's your mood?", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    # Buttons
    for button in buttons:
        button.draw(screen)

    # Genre output
    if selected_genre:
        draw_genre(selected_genre)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.is_clicked(event.pos):
                    selected_genre = mood_genres[button.text]

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
