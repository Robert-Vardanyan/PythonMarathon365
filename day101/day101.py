import pygame
import random
import time
import sys

# Setup
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quick Typing Game")
clock = pygame.time.Clock()

# Fonts and Colors
FONT = pygame.font.SysFont("consolas", 40)
SMALL_FONT = pygame.font.SysFont("consolas", 24)
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
CORRECT_COLOR = (0, 255, 0)
WRONG_COLOR = (255, 0, 0)

# Word bank
WORDS = ["banana", "keyboard", "python", "development", "intelligence", "universe", "synthesis", "project", "success", "power", "performance", "type", "game", "graphics"]

def draw_text_centered(text, font, color, y_offset=0):
    """Draws text centered on the screen."""
    text_surf = font.render(text, True, color)
    rect = text_surf.get_rect(center=(WIDTH//2, HEIGHT//2 + y_offset))
    screen.blit(text_surf, rect)

def main():
    running = True
    user_text = ""
    start_time = None
    game_over = False

    target_word = random.choice(WORDS)
    correct_chars = 0

    while running:
        screen.fill(BG_COLOR)

        # Draw instruction or result
        if not game_over:
            draw_text_centered("Type the word:", SMALL_FONT, TEXT_COLOR, -60)
            draw_text_centered(target_word, FONT, TEXT_COLOR, -10)

            # Render typed text with color feedback
            rendered = ""
            for i, char in enumerate(user_text):
                if i < len(target_word):
                    color = CORRECT_COLOR if char == target_word[i] else WRONG_COLOR
                    char_surface = FONT.render(char, True, color)
                    rect = char_surface.get_rect()
                    rect.topleft = (WIDTH//2 - len(target_word)*12 + i*24, HEIGHT//2 + 40)
                    screen.blit(char_surface, rect)
        else:
            total_time = round(end_time - start_time, 2)
            accuracy = (correct_chars / len(target_word)) * 100 if target_word else 0
            draw_text_centered(f"Time: {total_time}s", FONT, CORRECT_COLOR, -20)
            draw_text_centered(f"Accuracy: {accuracy:.1f}%", FONT, CORRECT_COLOR, 30)
            draw_text_centered("Press R to play again or ESC to quit", SMALL_FONT, TEXT_COLOR, 80)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    if start_time is None:
                        start_time = time.time()
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.unicode.isprintable():
                        user_text += event.unicode
                        if len(user_text) == len(target_word):
                            end_time = time.time()
                            correct_chars = sum(1 for i in range(len(target_word)) if user_text[i] == target_word[i])
                            game_over = True
                else:
                    if event.key == pygame.K_r:
                        main()
                        return
                    elif event.key == pygame.K_ESCAPE:
                        running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
