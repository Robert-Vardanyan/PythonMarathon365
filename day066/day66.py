import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set window size and title
WIDTH, HEIGHT = 400, 150
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🕒 Digital Clock")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)

# Set font and size
font = pygame.font.SysFont("Arial", 72, bold=True)

# Main loop
while True:
    # Handle events (like closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get current time string
    current_time = time.strftime("%H:%M:%S")

    # Render the text
    text_surface = font.render(current_time, True, BLUE)

    # Fill background
    screen.fill(BLACK)

    # Get text rectangle and center it
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Draw text on the screen
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Wait for 1 second before updating time again
    pygame.time.wait(1000)
