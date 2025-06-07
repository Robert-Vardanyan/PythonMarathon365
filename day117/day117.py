import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prime Number Finder")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 205, 50)
RED = (220, 20, 60)
GRAY = (200, 200, 200)
BLUE = (70, 130, 180)

font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 48)

input_box = pygame.Rect(50, 100, 400, 40)
active_color = BLUE
inactive_color = GRAY

user_text = ''
active = False
result = ''
result_color = BLACK

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def draw():
    screen.fill(WHITE)
    # Title
    title = big_font.render("Prime Number Finder", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    # Input box
    color = active_color if active else inactive_color
    pygame.draw.rect(screen, color, input_box, 2)

    # User input text
    txt_surface = font.render(user_text, True, BLACK)
    screen.blit(txt_surface, (input_box.x + 10, input_box.y + 8))

    # Instructions
    instr = font.render("Enter a positive integer and press Enter", True, BLACK)
    screen.blit(instr, (WIDTH // 2 - instr.get_width() // 2, input_box.y + 60))

    # Result text
    if result:
        res_surface = font.render(result, True, result_color)
        screen.blit(res_surface, (WIDTH // 2 - res_surface.get_width() // 2, input_box.y + 110))

    pygame.display.flip()

def main():
    global active, user_text, result, result_color
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    if user_text.isdigit():
                        num = int(user_text)
                        if is_prime(num):
                            result = f"{num} is a prime number."
                            result_color = GREEN
                        else:
                            result = f"{num} is NOT a prime number."
                            result_color = RED
                    else:
                        result = "Please enter a valid positive integer."
                        result_color = RED
                    user_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if event.unicode.isdigit():
                        user_text += event.unicode

        draw()
        clock.tick(30)

if __name__ == "__main__":
    main()
