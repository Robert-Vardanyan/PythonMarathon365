import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 400, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stop Signal Visualizer")

# Colors
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
RED = (220, 0, 0)
YELLOW = (240, 200, 0)
GREEN = (0, 180, 0)
DARK_GRAY = (70, 70, 70)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

signals = ["RED", "YELLOW", "GREEN"]
current_index = 0

def draw_signal(surface, state):
    surface.fill(BLACK)
    center_x = WIDTH // 2
    radius = 60
    spacing = 50
    # Calculate positions to be vertically centered and symmetrical
    total_height = 3 * (2 * radius) + 2 * spacing
    start_y = (HEIGHT - total_height) // 2 + radius

    # Draw the housing rectangle around the circles
    rect_height = total_height + 40
    rect_top = start_y - radius - 20
    pygame.draw.rect(surface, GRAY, (center_x - 80, rect_top, 160, rect_height), border_radius=20)

    # Positions of the circles
    positions = [start_y + i * (2 * radius + spacing) for i in range(3)]

    colors = [RED, YELLOW, GREEN]

    for i, y in enumerate(positions):
        color = colors[i] if signals[current_index] == signals[i] else DARK_GRAY
        pygame.draw.circle(surface, color, (center_x, y), radius)

    # Draw the text for current signal centered at bottom
    font = pygame.font.SysFont("Arial", 40, bold=True)
    text = font.render(signals[current_index], True, WHITE)
    text_rect = text.get_rect(center=(center_x, rect_top + rect_height + 40))
    surface.blit(text, text_rect)

def main():
    global current_index
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_index = (current_index + 1) % len(signals)

        draw_signal(win, signals[current_index])
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
