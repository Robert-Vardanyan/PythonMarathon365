import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Roll Animation with Cube")

clock = pygame.time.Clock()

# Colors for dice faces
DICE_COLORS = [
    (255, 0, 0),     # 1 - red
    (0, 255, 0),     # 2 - green
    (0, 0, 255),     # 3 - blue
    (255, 255, 0),   # 4 - yellow
    (255, 0, 255),   # 5 - purple
    (0, 255, 255)    # 6 - cyan
]

FONT = pygame.font.SysFont(None, 100)
SMALL_FONT = pygame.font.SysFont(None, 30)
BG_COLOR = (30, 30, 30)

def draw_dice_face(number):
    """Create a surface with the dice face — color and number"""
    surf = pygame.Surface((150, 150))
    surf.fill((240, 240, 240))
    pygame.draw.rect(surf, (50, 50, 50), surf.get_rect(), 4, border_radius=20)
    # Fill circle with color corresponding to the number
    color = DICE_COLORS[number - 1]
    pygame.draw.circle(surf, color, (75, 75), 60)
    # Draw the number on the dice face
    text = FONT.render(str(number), True, (255, 255, 255))
    text_rect = text.get_rect(center=(75, 75))
    surf.blit(text, text_rect)
    return surf

def roll_dice_animation(duration=1500):
    """Animate dice roll by cycling random faces for a given duration (ms)"""
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Show random dice face quickly to simulate rolling
        face = random.randint(1, 6)
        dice_surf = draw_dice_face(face)
        screen.fill(BG_COLOR)
        screen.blit(dice_surf, ((WIDTH - dice_surf.get_width()) // 2, (HEIGHT - dice_surf.get_height()) // 2))
        pygame.display.flip()
        clock.tick(20)  # animation speed (frames per second)

    # Return final dice roll result
    return random.randint(1, 6)

def main():
    dice_number = 1
    rolling = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Start rolling animation when spacebar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not rolling:
                    rolling = True
                    dice_number = roll_dice_animation()
                    rolling = False

        screen.fill(BG_COLOR)

        # Draw the dice with the current number
        dice_surf = draw_dice_face(dice_number)
        screen.blit(dice_surf, ((WIDTH - dice_surf.get_width()) // 2, (HEIGHT - dice_surf.get_height()) // 2))

        # Show hint text
        hint_text = "Press SPACE to roll the dice"
        hint = SMALL_FONT.render(hint_text, True, (200, 200, 200))
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 40))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
