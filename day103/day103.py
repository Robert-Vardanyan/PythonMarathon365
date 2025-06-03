import pygame
import sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 600, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")

# Colors
BG_COLOR = (245, 230, 200)
TEXT_COLOR = (60, 40, 10)
BUTTON_COLOR = (210, 180, 140)
HIGHLIGHT_COLOR = (180, 150, 110)

# Fonts
font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 22)

# Load cookie image
cookie_img = pygame.image.load("cookie.png")
cookie_img = pygame.transform.scale(cookie_img, (150, 150))
cookie_rect = cookie_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))

# Game state
cookies = 0
cookies_per_click = 1
auto_cookies = 0
upgrade_cost = 50

# Button
upgrade_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 100, 300, 50)

clock = pygame.time.Clock()

# Game loop
while True:
    win.fill(BG_COLOR)

    # Draw cookie
    win.blit(cookie_img, cookie_rect)

    # Draw stats
    cookie_text = font.render(f"Cookies: {int(cookies)}", True, TEXT_COLOR)
    win.blit(cookie_text, (WIDTH // 2 - cookie_text.get_width() // 2, 30))

    # Draw upgrade button
    pygame.draw.rect(win, BUTTON_COLOR, upgrade_rect, border_radius=10)
    upgrade_text = small_font.render(f"Buy Upgrade (+1/sec) - {upgrade_cost}", True, TEXT_COLOR)
    win.blit(upgrade_text, (upgrade_rect.centerx - upgrade_text.get_width() // 2,
                            upgrade_rect.centery - upgrade_text.get_height() // 2))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if cookie_rect.collidepoint(event.pos):
                cookies += cookies_per_click
            elif upgrade_rect.collidepoint(event.pos):
                if cookies >= upgrade_cost:
                    cookies -= upgrade_cost
                    auto_cookies += 1
                    upgrade_cost = int(upgrade_cost * 1.5)

    # Auto cookies income
    cookies += auto_cookies * (clock.get_time() / 1000)

    pygame.display.flip()
    clock.tick(60)
