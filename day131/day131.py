import pygame
import sys
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock-Paper-Scissors")
font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
BLUE = (100, 100, 255)
GREEN = (100, 255, 100)
RED = (255, 100, 100)

# Game data
choices = ['Rock', 'Paper', 'Scissors']
player_score = 0
computer_score = 0
draws = 0
result_text = ""

# Button setup
button_rects = {
    "Rock": pygame.Rect(50, 300, 150, 50),
    "Paper": pygame.Rect(225, 300, 150, 50),
    "Scissors": pygame.Rect(400, 300, 150, 50)
}

def draw_buttons():
    for name, rect in button_rects.items():
        pygame.draw.rect(screen, BLUE, rect)
        text = font.render(name, True, WHITE)
        screen.blit(text, (rect.x + 30, rect.y + 10))

def get_winner(player, computer):
    if player == computer:
        return "Draw"
    if (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        return "Player"
    return "Computer"

# Game loop
running = True
while running:
    screen.fill(GRAY)
    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            player_score = 0
            computer_score = 0
            draws = 0
            result_text = ""

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for choice, rect in button_rects.items():
                if rect.collidepoint(pos):
                    computer_choice = random.choice(choices)
                    winner = get_winner(choice, computer_choice)
                    if winner == "Player":
                        player_score += 1
                        result_text = f"You Win! {choice} beats {computer_choice}"
                    elif winner == "Computer":
                        computer_score += 1
                        result_text = f"You Lose! {computer_choice} beats {choice}"
                    else:
                        draws += 1
                        result_text = "It's a Draw!"

    # Display result
    result_surface = big_font.render(result_text, True, WHITE)
    screen.blit(result_surface, (WIDTH // 2 - result_surface.get_width() // 2, 50))

    # Display score
    score_text = f"Player: {player_score}  Computer: {computer_score}  Draws: {draws}"
    score_surface = font.render(score_text, True, WHITE)
    screen.blit(score_surface, (WIDTH // 2 - score_surface.get_width() // 2, 120))

    # Instructions
    instruction = font.render("Press R to reset scores", True, WHITE)
    screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, 160))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
