import pygame
import random
import time

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction Timer Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 48)

# Game state
waiting_for_green = False
green_shown = False
too_soon = False
reaction_time = 0
start_time = 0

# Clock
clock = pygame.time.Clock()

# Timer management
delay_timer_started = False
delay_start_time = 0
delay_duration = 0

running = True
while running:
    screen.fill(WHITE)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click handling
        if event.type == pygame.MOUSEBUTTONDOWN:
            if green_shown:
                reaction_time = (time.time() - start_time)
                green_shown = False
            elif waiting_for_green:
                # Too early
                waiting_for_green = False
                delay_timer_started = False
                too_soon = True

        # Keyboard: SPACE to restart
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            waiting_for_green = True
            delay_timer_started = True
            delay_start_time = current_time
            delay_duration = random.randint(2000, 4000)  # 2-4 seconds
            green_shown = False
            too_soon = False
            reaction_time = 0

    # Delay before showing green
    if waiting_for_green and delay_timer_started:
        if current_time - delay_start_time >= delay_duration:
            waiting_for_green = False
            green_shown = True
            start_time = time.time()

    # Drawing UI
    if green_shown:
        screen.fill(GREEN)
        text = font.render("CLICK!", True, BLACK)
        screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    elif waiting_for_green:
        screen.fill(RED)
        text = font.render("WAIT FOR GREEN...", True, WHITE)
        screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    elif too_soon:
        text1 = font.render("Too soon! 😬", True, RED)
        text2 = font.render("Press SPACE to retry", True, BLACK)
        screen.blit(text1, text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
        screen.blit(text2, text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))
    elif reaction_time > 0:
        text1 = font.render(f"Reaction time: {reaction_time:.3f} sec", True, BLACK)
        text2 = font.render("Press SPACE to retry", True, RED)
        screen.blit(text1, text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
        screen.blit(text2, text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))
    else:
        text1 = font.render("Reaction Timer", True, BLACK)
        text2 = font.render("Press SPACE to start", True, RED)
        screen.blit(text1, text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
        screen.blit(text2, text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
