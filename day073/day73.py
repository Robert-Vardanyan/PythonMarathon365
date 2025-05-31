import pygame
import time
import random

pygame.init()

# Settings
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 197, 94)
RED = (239, 68, 68)
GRAY = (130, 130, 130)
BLUE = (59, 130, 246)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Test")

font_small = pygame.font.SysFont("consolas", 24)
font_large = pygame.font.SysFont("consolas", 32)
clock = pygame.time.Clock()

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language.",
    "Typing speed depends on practice and accuracy.",
    "Always test your code before deployment.",
    "Artificial intelligence is shaping the future.",
    "The sun sets in the west and rises in the east."
]

def draw_text(surface, text, pos, font, color=BLACK):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

def draw_colored_text(surface, text, user_text, pos, font):
    # Draw the target text in gray first
    draw_text(surface, text, pos, font, GRAY)

    x, y = pos
    # Overlay the user input with colors (green correct, red wrong)
    for i, char in enumerate(user_text):
        if i < len(text):
            color = GREEN if char == text[i] else RED
        else:
            color = RED  # extra characters are errors
        char_surf = font.render(char, True, color)
        surface.blit(char_surf, (x, y))
        x += char_surf.get_width()

def calculate_wpm(start_time, input_text):
    elapsed = time.time() - start_time
    words = len(input_text.split())
    if elapsed > 0:
        return (words / elapsed) * 60
    return 0

def calculate_accuracy(target, user_input):
    correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(target) and c == target[i])
    if len(target) == 0:
        return 0
    return (correct_chars / len(target)) * 100

def main():
    run = True
    input_text = ''
    start_time = None
    target_text = random.choice(sentences)
    wpm = 0
    accuracy = 0
    finished = False

    while run:
        win.fill(WHITE)

        draw_text(win, "Typing Speed Test", (WIDTH // 2 - 140, 20), font_large, BLUE)
        draw_text(win, "Type this sentence:", (50, 80), font_small)
        draw_text(win, target_text, (50, 110), font_small, BLACK)

        pygame.draw.rect(win, (200, 200, 200), pygame.Rect(45, 170, 710, 40), 2)

        # Draw user text with color feedback
        draw_colored_text(win, target_text, input_text, (50, 175), font_small)

        if finished:
            draw_text(win, f"⏱️ WPM: {wpm:.2f}", (50, 240), font_small, GREEN)
            draw_text(win, f"🎯 Accuracy: {accuracy:.2f}%", (50, 270), font_small, GREEN)
            draw_text(win, "Press Enter to retry", (50, 310), font_small, RED)

        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN and not finished:
                if not start_time:
                    start_time = time.time()

                if event.key == pygame.K_RETURN:
                    if input_text:
                        wpm = calculate_wpm(start_time, input_text)
                        accuracy = calculate_accuracy(target_text, input_text)
                        finished = True

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                else:
                    # Filter out non-printable characters
                    if event.unicode.isprintable():
                        input_text += event.unicode

            elif event.type == pygame.KEYDOWN and finished:
                # Restart test on Enter after finishing
                if event.key == pygame.K_RETURN:
                    input_text = ''
                    start_time = None
                    target_text = random.choice(sentences)
                    wpm = 0
                    accuracy = 0
                    finished = False

    pygame.quit()

if __name__ == "__main__":
    main()
