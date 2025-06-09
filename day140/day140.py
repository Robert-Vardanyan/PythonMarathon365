import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Stopwatch")

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set font
font = pygame.font.SysFont(None, 72)
info_font = pygame.font.SysFont(None, 28)

# Variables to track time
start_time = 0
elapsed_time = 0
running = False

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Start
                if not running:
                    start_time = time.time() - elapsed_time
                    running = True
            elif event.key == pygame.K_p:  # Pause
                if running:
                    elapsed_time = time.time() - start_time
                    running = False
            elif event.key == pygame.K_r:  # Reset
                running = False
                elapsed_time = 0
                start_time = 0
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Update elapsed time
    if running:
        elapsed_time = time.time() - start_time

    # Format time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time * 100) % 100)

    time_text = f"{minutes:02}:{seconds:02}:{milliseconds:02}"

    # Render timer
    time_surface = font.render(time_text, True, BLACK)
    info_surface = info_font.render("S: Start  P: Pause  R: Reset  ESC: Exit", True, BLACK)

    screen.blit(time_surface, (WIDTH // 2 - time_surface.get_width() // 2, HEIGHT // 2 - 40))
    screen.blit(info_surface, (WIDTH // 2 - info_surface.get_width() // 2, HEIGHT - 40))

    pygame.display.flip()
    clock.tick(30)
