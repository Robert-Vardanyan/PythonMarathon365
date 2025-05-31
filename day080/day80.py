import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Drawing Application")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# List of available colors for the palette
colors = [BLACK, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]

# Current drawing color
current_color = BLACK

# Brush size
brush_size = 5

# Create a surface for drawing (white background)
canvas = pygame.Surface((WIDTH, HEIGHT - 60))
canvas.fill(WHITE)

# Font for buttons and text
font = pygame.font.SysFont(None, 24)

def draw_color_palette():
    """Draw color selection boxes."""
    for i, color in enumerate(colors):
        rect = pygame.Rect(10 + i*50, HEIGHT - 50, 40, 40)
        pygame.draw.rect(screen, color, rect)
        # Draw border around selected color
        if color == current_color:
            pygame.draw.rect(screen, (0,0,0), rect, 3)
        else:
            pygame.draw.rect(screen, (100,100,100), rect, 1)

def draw_clear_button():
    """Draw the clear button."""
    rect = pygame.Rect(WIDTH - 110, HEIGHT - 50, 100, 40)
    pygame.draw.rect(screen, (180, 180, 180), rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)
    text = font.render("Clear", True, (0, 0, 0))
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)
    return rect

def draw_save_button():
    """Draw the save button."""
    rect = pygame.Rect(WIDTH - 220, HEIGHT - 50, 100, 40)
    pygame.draw.rect(screen, (180, 180, 180), rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)
    text = font.render("Save", True, (0, 0, 0))
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)
    return rect

def main():
    global current_color

    clock = pygame.time.Clock()
    drawing = False
    last_pos = None

    clear_button_rect = None
    save_button_rect = None

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Mouse button down: start drawing or select color/button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    # Check if clicked on color palette
                    for i, color in enumerate(colors):
                        rect = pygame.Rect(10 + i*50, HEIGHT - 50, 40, 40)
                        if rect.collidepoint(mouse_pos):
                            current_color = color
                            break
                    else:
                        # Check if clicked clear button
                        if clear_button_rect and clear_button_rect.collidepoint(mouse_pos):
                            canvas.fill(WHITE)
                        # Check if clicked save button
                        elif save_button_rect and save_button_rect.collidepoint(mouse_pos):
                            pygame.image.save(canvas, "drawing.png")
                            print("Drawing saved as drawing.png")
                        else:
                            # Start drawing on canvas only if click inside canvas area
                            if mouse_pos[1] < HEIGHT - 60:
                                drawing = True
                                last_pos = mouse_pos

            # Mouse button up: stop drawing
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    last_pos = None

            # Mouse motion: draw if drawing
            elif event.type == pygame.MOUSEMOTION:
                if drawing and last_pos:
                    # Draw line on the canvas surface from last_pos to current mouse_pos
                    pygame.draw.line(canvas, current_color, last_pos, mouse_pos, brush_size)
                    last_pos = mouse_pos

        # Fill background for the whole window
        screen.fill(GRAY)

        # Draw the canvas surface
        screen.blit(canvas, (0,0))

        # Draw color palette
        draw_color_palette()

        # Draw buttons
        clear_button_rect = draw_clear_button()
        save_button_rect = draw_save_button()

        # Draw current color info
        info_text = font.render(f"Current Color", True, (0,0,0))
        screen.blit(info_text, (10, HEIGHT - 80))
        pygame.draw.rect(screen, current_color, pygame.Rect(110, HEIGHT - 80, 40, 20))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(110, HEIGHT - 80, 40, 20), 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
