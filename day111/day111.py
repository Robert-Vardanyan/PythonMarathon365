import pygame
import random
import time
import sys

pygame.init()

# --- Config ---
WIDTH, HEIGHT = 600, 600
FPS = 60
BUTTON_SIZE = 250
DELAY = 700  # milliseconds
HIGHLIGHT_TIME = 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (180, 0, 0)
BLUE = (0, 0, 180)
YELLOW = (180, 180, 0)
LIGHT_GREEN = (0, 255, 0)
LIGHT_RED = (255, 0, 0)
LIGHT_BLUE = (0, 0, 255)
LIGHT_YELLOW = (255, 255, 0)

COLOR_MAP = {
    "green": (GREEN, LIGHT_GREEN),
    "red": (RED, LIGHT_RED),
    "blue": (BLUE, LIGHT_BLUE),
    "yellow": (YELLOW, LIGHT_YELLOW)
}

# --- Init ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simon Says")
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()

# --- Rects ---
green_rect = pygame.Rect(25, 25, BUTTON_SIZE, BUTTON_SIZE)
red_rect = pygame.Rect(325, 25, BUTTON_SIZE, BUTTON_SIZE)
yellow_rect = pygame.Rect(25, 325, BUTTON_SIZE, BUTTON_SIZE)
blue_rect = pygame.Rect(325, 325, BUTTON_SIZE, BUTTON_SIZE)

buttons = {
    "green": green_rect,
    "red": red_rect,
    "yellow": yellow_rect,
    "blue": blue_rect
}


def draw_buttons(active=None):
    for color, rect in buttons.items():
        base, highlight = COLOR_MAP[color]
        current_color = highlight if active == color else base
        pygame.draw.rect(screen, current_color, rect)
    pygame.display.flip()


def show_message(text):
    screen.fill(BLACK)
    render = font.render(text, True, WHITE)
    screen.blit(render, (WIDTH // 2 - render.get_width() // 2, HEIGHT // 2 - render.get_height() // 2))
    pygame.display.flip()


def flash_sequence(sequence):
    for color in sequence:
        draw_buttons(color)
        pygame.time.delay(HIGHLIGHT_TIME)
        draw_buttons()
        pygame.time.delay(DELAY)


def get_click(pos):
    for color, rect in buttons.items():
        if rect.collidepoint(pos):
            return color
    return None


def main():
    running = True
    level = 1
    sequence = []
    waiting_input = False

    while running:
        screen.fill(BLACK)
        draw_buttons()
        show_message(f"Level {level}")
        pygame.time.delay(1000)

        sequence.append(random.choice(list(buttons.keys())))
        flash_sequence(sequence)

        input_index = 0
        waiting_input = True

        while waiting_input:
            draw_buttons()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = get_click(event.pos)
                    if clicked:
                        draw_buttons(clicked)
                        pygame.time.delay(HIGHLIGHT_TIME)
                        draw_buttons()
                        if clicked == sequence[input_index]:
                            input_index += 1
                            if input_index == len(sequence):
                                level += 1
                                waiting_input = False
                                pygame.time.delay(500)
                        else:
                            show_message("Wrong! Game Over")
                            pygame.time.delay(2000)
                            sequence = []
                            level = 1
                            waiting_input = False
                            pygame.time.delay(1000)
            clock.tick(FPS)


if __name__ == "__main__":
    main()
