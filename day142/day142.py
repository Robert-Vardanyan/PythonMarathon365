import pygame
import sys
import time

# --- Initialization ---
pygame.init()
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⏲️ Cooking Timer")
font = pygame.font.SysFont("Arial", 40)
emoji_font = pygame.font.SysFont("Segoe UI Emoji", 60)
small_font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

# --- Variables ---
minutes = 0
seconds = 0
timer_running = False
show_start_preview = False
start_preview_time = 0
start_time = 0
remaining_time = 0
blink = False
blink_visible = True
last_blink_time = 0

# --- Functions ---
def format_time(t):
    mins = int(t) // 60
    secs = int(t) % 60
    return f"{mins:02}:{secs:02}"

def draw_screen():
    screen.fill((250, 240, 230))

    emoji = emoji_font.render("🍳", True, (0, 0, 0))
    screen.blit(emoji, (WIDTH // 2 - 30, 20))

    if not blink or blink_visible:
        time_display = font.render(format_time(remaining_time), True, (0, 0, 0))
        screen.blit(time_display, (WIDTH // 2 - 60, HEIGHT // 2 - 20))

    instructions = small_font.render("↑/↓ Min  |  →/← Sec  |  SPACE Start/Stop  |  R Reset", True, (80, 80, 80))
    screen.blit(instructions, (20, HEIGHT - 40))

# --- Main Loop ---
running = True
remaining_time = 0

while running:
    current_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if not timer_running and not show_start_preview:
                if event.key == pygame.K_UP:
                    minutes = min(minutes + 1, 59)
                elif event.key == pygame.K_DOWN:
                    minutes = max(minutes - 1, 0)
                elif event.key == pygame.K_RIGHT:
                    seconds = (seconds + 10) % 60
                elif event.key == pygame.K_LEFT:
                    seconds = (seconds - 10) % 60

                # ✅ Update display time immediately
                remaining_time = minutes * 60 + seconds

            if event.key == pygame.K_SPACE:
                if not timer_running and not show_start_preview:
                    remaining_time = minutes * 60 + seconds
                    if remaining_time > 0:
                        show_start_preview = True
                        start_preview_time = current_time
                        blink = False  # Disable blink before starting
                elif timer_running:
                    timer_running = False
                    blink = False

            elif event.key == pygame.K_r:
                timer_running = False
                show_start_preview = False
                minutes = 0
                seconds = 0
                remaining_time = 0
                blink = False

    if show_start_preview:
        if current_time - start_preview_time >= 1:
            show_start_preview = False
            timer_running = True
            start_time = current_time
            blink = True  # Enable blinking now
            last_blink_time = current_time
        else:
            remaining_time = minutes * 60 + seconds

    elif timer_running:
        elapsed = current_time - start_time
        remaining_time = max(0, remaining_time - elapsed)
        start_time = current_time

        # Blink every 0.5s
        if current_time - last_blink_time >= 0.5:
            blink_visible = not blink_visible
            last_blink_time = current_time

        if remaining_time <= 0:
            timer_running = False
            blink = False
            blink_visible = True
            print("⏰ Time's up!")

    draw_screen()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
