import pygame
import sys

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 200, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚦 Traffic Light Simulation")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (100, 0, 0)
YELLOW = (255, 255, 0)
DARK_YELLOW = (100, 100, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
GRAY = (50, 50, 50)

# Positions of lights
center_x = WIDTH // 2
radius = 50
positions = [
    (center_x, 120),  # Red light
    (center_x, 260),  # Yellow light
    (center_x, 400),  # Green light
]

# Traffic light states and durations (milliseconds)
states = ["RED", "GREEN", "YELLOW"]
durations = {"RED": 3000, "GREEN": 3000, "YELLOW": 1000}

current_state_index = 0
state_start_time = pygame.time.get_ticks()

# Main loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Time management
    now = pygame.time.get_ticks()
    elapsed = now - state_start_time
    current_state = states[current_state_index]

    # Switch state if duration exceeded
    if elapsed > durations[current_state]:
        current_state_index = (current_state_index + 1) % len(states)
        state_start_time = now
        current_state = states[current_state_index]

    # Draw background
    screen.fill(GRAY)

    # Draw traffic light housing
    pygame.draw.rect(screen, BLACK, (center_x - 70, 50, 140, 420), border_radius=20)

    # Draw lights with bright/dim color depending on current state
    # Red light
    color_red = RED if current_state == "RED" else DARK_RED
    pygame.draw.circle(screen, color_red, positions[0], radius)

    # Yellow light
    color_yellow = YELLOW if current_state == "YELLOW" else DARK_YELLOW
    pygame.draw.circle(screen, color_yellow, positions[1], radius)

    # Green light
    color_green = GREEN if current_state == "GREEN" else DARK_GREEN
    pygame.draw.circle(screen, color_green, positions[2], radius)

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit to 60 FPS
