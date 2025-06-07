import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Sorting Visualizer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (160, 160, 160)
RED = (255, 60, 60)
GREEN = (60, 255, 60)
BLUE = (60, 60, 255)

# Fonts
font = pygame.font.SysFont(None, 30)
large_font = pygame.font.SysFont(None, 50)

# Generate random list
NUM_COUNT = 50
numbers = [random.randint(10, HEIGHT - 50) for _ in range(NUM_COUNT)]

# Variables to control sorting
i = 0
j = 0
swapped = False
sorting = True
sorted_completed = False

clock = pygame.time.Clock()
FPS = 60

def draw_bars(numbers, highlight_indices=None, swapped_indices=None):
    screen.fill(WHITE)
    bar_width = WIDTH // len(numbers)
    
    for idx, val in enumerate(numbers):
        x = idx * bar_width
        y = HEIGHT - val
        color = GRAY
        if highlight_indices and idx in highlight_indices:
            color = BLUE
        if swapped_indices and idx in swapped_indices:
            color = RED
        pygame.draw.rect(screen, color, (x, y, bar_width - 2, val))
    
    # Draw status text
    if sorted_completed:
        text = large_font.render("Sorting Completed!", True, GREEN)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))
    elif sorting:
        text = font.render("Sorting... (Bubble Sort)", True, BLACK)
        screen.blit(text, (10, 10))
    else:
        text = font.render("Press R to Reset", True, BLACK)
        screen.blit(text, (10, 10))

def bubble_sort_step(numbers, i, j):
    swapped = False
    if j < len(numbers) - i - 1:
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
        j += 1
    else:
        i += 1
        j = 0
    return i, j, swapped

def main():
    global i, j, swapped, sorting, sorted_completed
    
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and sorted_completed:
                    # Reset
                    reset()
        
        if sorting and not sorted_completed:
            i, j, swapped = bubble_sort_step(numbers, i, j)
            if i >= len(numbers) - 1:
                sorting = False
                sorted_completed = True

        # Highlight current comparison
        highlight = [j, j + 1] if sorting else None
        draw_bars(numbers, highlight_indices=highlight)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def reset():
    global numbers, i, j, swapped, sorting, sorted_completed
    numbers = [random.randint(10, HEIGHT - 50) for _ in range(NUM_COUNT)]
    i = 0
    j = 0
    swapped = False
    sorting = True
    sorted_completed = False

if __name__ == "__main__":
    main()

