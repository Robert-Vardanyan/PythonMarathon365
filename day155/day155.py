import pygame
import sys
import time

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("♟️ Chess Clock Simulator")

# Fonts and colors
font = pygame.font.SysFont(None, 60)
small_font = pygame.font.SysFont(None, 30)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Players' time (5 minutes)
start_time = 5 * 60
time1 = start_time
time2 = start_time

active_player = 1
last_switch = time.time()
running = True
game_over = False

# Load beep.wav sound — put your file next to this script
try:
    beep = pygame.mixer.Sound("beep.wav")
    beep.set_volume(1.0)
except pygame.error:
    beep = None
    print("Failed to load beep.wav")

def draw_time(seconds, y, color, label):
    minutes = int(seconds) // 60
    sec = int(seconds) % 60
    time_str = f"{minutes:02}:{sec:02}"
    text = font.render(time_str, True, color)
    rect = text.get_rect(center=(WIDTH // 2, y))
    screen.blit(text, rect)

    label_text = small_font.render(label, True, color)
    label_rect = label_text.get_rect(center=(WIDTH // 2, y - 40))
    screen.blit(label_text, label_rect)

while running:
    screen.fill(WHITE)
    now = time.time()
    elapsed = now - last_switch

    if not game_over:
        if active_player == 1:
            time1 -= elapsed
            if time1 <= 0:
                time1 = 0
                game_over = True
                if beep:
                    print("Playing beep sound for Player 1")
                    beep.play()
        else:
            time2 -= elapsed
            if time2 <= 0:
                time2 = 0
                game_over = True
                if beep:
                    print("Playing beep sound for Player 2")
                    beep.play()

    last_switch = now

    draw_time(time1, 100, GREEN if active_player == 1 else BLACK, "Player 1")
    draw_time(time2, 220, GREEN if active_player == 2 else BLACK, "Player 2")

    if game_over:
        over_text = small_font.render("⏳ Time's up!", True, RED)
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT - 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            active_player = 2 if active_player == 1 else 1
            if beep:
                beep.play()


    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
sys.exit()
