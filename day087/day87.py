import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Higher or Lower Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GRAY = (200, 200, 200)

# Fonts
FONT = pygame.font.SysFont("arial", 30)
FONT_SMALL = pygame.font.SysFont("arial", 22)

# Button class for easy button creation and handling
class Button:
    def __init__(self, text, x, y, w, h, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        text_surf = FONT.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

# Game variables
current_number = random.randint(1, 100)
score = 0
game_over = False
message = "Will the next number be higher or lower?"

# Buttons
higher_btn = Button("Higher", 100, 300, 120, 50, GREEN, (0,255,0))
lower_btn = Button("Lower", 280, 300, 120, 50, RED, (255,0,0))
restart_btn = Button("Restart", 190, 360, 120, 40, BLUE, (0,0,255))

def draw_text_center(text, y, font, color=BLACK):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(WIDTH // 2, y))
    screen.blit(text_surf, text_rect)

running = True
while running:
    screen.fill(WHITE)

    # Draw current number
    draw_text_center(f"Current Number: {current_number}", 100, FONT)

    # Draw message
    draw_text_center(message, 180, FONT_SMALL)

    # Draw score
    draw_text_center(f"Score: {score}", 40, FONT)

    # Draw buttons
    if not game_over:
        higher_btn.draw(screen)
        lower_btn.draw(screen)
    else:
        restart_btn.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if higher_btn.is_clicked(event) or lower_btn.is_clicked(event):
                next_number = random.randint(1, 100)
                guess_higher = event.pos[0] > 0 and higher_btn.rect.collidepoint(event.pos)

                # Check guess
                if (next_number > current_number and higher_btn.is_clicked(event)) or (next_number < current_number and lower_btn.is_clicked(event)):
                    score += 1
                    message = f"Correct! Next number was {next_number}. Will the next be higher or lower?"
                    current_number = next_number
                else:
                    message = f"Wrong! Next number was {next_number}. Game Over!"
                    game_over = True

        else:
            if restart_btn.is_clicked(event):
                # Reset game
                current_number = random.randint(1, 100)
                score = 0
                game_over = False
                message = "Will the next number be higher or lower?"

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
