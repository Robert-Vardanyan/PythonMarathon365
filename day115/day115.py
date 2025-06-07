import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 640, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple RPG Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
GREEN = (0, 180, 0)
BLUE = (30, 144, 255)
GRAY = (200, 200, 200)
PLAYER_COLOR = (50, 150, 255)
ENEMY_COLOR = (255, 80, 80)

# Fonts
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

# Initial stats
player_health = 100
enemy_health = 100
game_over = False
result_text = ""

clock = pygame.time.Clock()

def draw_health_bar(x, y, health, max_health, color, label):
    # Background bar
    pygame.draw.rect(screen, GRAY, (x, y, 200, 25))
    # Health bar
    health_width = int(200 * (health / max_health))
    pygame.draw.rect(screen, color, (x, y, health_width, 25))
    pygame.draw.rect(screen, BLACK, (x, y, 200, 25), 2)
    # Health text (e.g. "75 / 100")
    health_text = font.render(f"{health} / {max_health}", True, BLACK)
    text_rect = health_text.get_rect(center=(x + 100, y + 12))
    screen.blit(health_text, text_rect)
    # Label (Player or Enemy)
    label_text = font.render(label, True, BLACK)
    screen.blit(label_text, (x, y - 30))

def draw_interface():
    screen.fill(WHITE)

    # Draw health bars with labels and numbers
    draw_health_bar(50, 90, player_health, 100, GREEN, "Player")
    draw_health_bar(380, 90, enemy_health, 100, RED, "Enemy")

    # Draw player and enemy as circles
    pygame.draw.circle(screen, PLAYER_COLOR, (150, 250), 50)
    pygame.draw.circle(screen, ENEMY_COLOR, (490, 250), 50)

    # Buttons
    pygame.draw.rect(screen, BLUE, (250, 500, 140, 50))  # Attack
    screen.blit(font.render("Attack", True, WHITE), (280, 510))

    pygame.draw.rect(screen, GREEN, (410, 500, 140, 50))  # Heal
    screen.blit(font.render("Heal", True, WHITE), (450, 510))

    if game_over:
        # Display result text
        text_surface = big_font.render(result_text, True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)

        # Restart instruction
        restart_surf = font.render("Press R to Restart", True, BLACK)
        restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
        screen.blit(restart_surf, restart_rect)

def reset_game():
    global player_health, enemy_health, game_over, result_text
    player_health = 100
    enemy_health = 100
    game_over = False
    result_text = ""

running = True
while running:
    draw_interface()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Attack button
                if 250 <= mouse_pos[0] <= 390 and 500 <= mouse_pos[1] <= 550:
                    damage = random.randint(10, 30)
                    enemy_health -= damage
                    if enemy_health <= 0:
                        enemy_health = 0
                        result_text = "You Win!"
                        game_over = True
                        break

                    # Enemy counterattack
                    damage = random.randint(5, 20)
                    player_health -= damage
                    if player_health <= 0:
                        player_health = 0
                        result_text = "You Lose!"
                        game_over = True

                # Heal button
                elif 410 <= mouse_pos[0] <= 550 and 500 <= mouse_pos[1] <= 550:
                    heal = random.randint(10, 25)
                    player_health = min(player_health + heal, 100)

                    # Enemy counterattack
                    damage = random.randint(5, 20)
                    player_health -= damage
                    if player_health <= 0:
                        player_health = 0
                        result_text = "You Lose!"
                        game_over = True

        else:
            # Restart game on pressing R
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
