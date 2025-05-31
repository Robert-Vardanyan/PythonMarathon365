import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock-Paper-Scissors")

FONT = pygame.font.SysFont(None, 40)
SMALL_FONT = pygame.font.SysFont(None, 30)

# Colors
BG_COLOR = (30, 30, 30)
BUTTON_COLOR = (70, 70, 200)
BUTTON_HOVER = (100, 100, 255)
TEXT_COLOR = (255, 255, 255)
WIN_COLOR = (0, 255, 0)       # Green for win
LOSE_COLOR = (255, 0, 0)      # Red for lose
TIE_COLOR = (255, 255, 0)     # Yellow for tie

choices = ["Rock", "Paper", "Scissors"]

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, surface, mouse_pos):
        color = BUTTON_HOVER if self.rect.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        txt_surf = FONT.render(self.text, True, TEXT_COLOR)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def is_clicked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed

def determine_winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

def main():
    clock = pygame.time.Clock()

    button_width, button_height = 130, 50
    spacing = 20
    start_x = (WIDTH - (button_width * 3 + spacing * 2)) // 2
    buttons = []
    for i, choice in enumerate(choices):
        x = start_x + i * (button_width + spacing)
        y = HEIGHT - button_height - 40
        buttons.append(Button(x, y, button_width, button_height, choice))

    player_choice = None
    computer_choice = None
    result_text = "Make your choice!"
    result_color = TEXT_COLOR  # default color

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pressed = True

        screen.fill(BG_COLOR)

        instruction_surf = SMALL_FONT.render("Choose Rock, Paper, or Scissors:", True, TEXT_COLOR)
        screen.blit(instruction_surf, (WIDTH//2 - instruction_surf.get_width()//2, 20))

        for button in buttons:
            button.draw(screen, mouse_pos)
            if button.is_clicked(mouse_pos, mouse_pressed):
                player_choice = button.text
                computer_choice = random.choice(choices)
                result_text = determine_winner(player_choice, computer_choice)
                # Set result text color based on outcome
                if result_text == "You Win!":
                    result_color = WIN_COLOR
                elif result_text == "You Lose!":
                    result_color = LOSE_COLOR
                else:
                    result_color = TIE_COLOR

        if player_choice:
            player_surf = FONT.render(f"Your choice: {player_choice}", True, TEXT_COLOR)
            comp_surf = FONT.render(f"Computer choice: {computer_choice}", True, TEXT_COLOR)
            result_surf = FONT.render(result_text, True, result_color)

            screen.blit(player_surf, (WIDTH//2 - player_surf.get_width()//2, 100))
            screen.blit(comp_surf, (WIDTH//2 - comp_surf.get_width()//2, 150))
            screen.blit(result_surf, (WIDTH//2 - result_surf.get_width()//2, 220))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
