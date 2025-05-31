import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Capital Game")

FONT = pygame.font.SysFont(None, 40)
SMALL_FONT = pygame.font.SysFont(None, 30)

# Sample data: country -> capital
countries = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Canada": "Ottawa",
    "Egypt": "Cairo",
}

country_list = list(countries.keys())
index = 0

input_text = ""
message = ""
message_color = (0, 0, 0)

def draw_text(text, font, color, surface, x, y):
    txt_obj = font.render(text, True, color)
    txt_rect = txt_obj.get_rect(center=(x, y))
    surface.blit(txt_obj, txt_rect)

def next_country():
    global index, input_text, message
    index = (index + 1) % len(country_list)
    input_text = ""
    message = ""

clock = pygame.time.Clock()

while True:
    screen.fill((230, 230, 230))

    # Draw instructions
    draw_text("Guess the Capital City", FONT, (0, 0, 0), screen, WIDTH//2, 40)
    draw_text(f"Country: {country_list[index]}", FONT, (0, 0, 255), screen, WIDTH//2, 100)

    # Draw input box
    input_box = pygame.Rect(WIDTH//2 - 150, 150, 300, 40)
    pygame.draw.rect(screen, (255, 255, 255), input_box)
    pygame.draw.rect(screen, (0, 0, 0), input_box, 2)

    # Render input text
    txt_surface = FONT.render(input_text, True, (0, 0, 0))
    screen.blit(txt_surface, (input_box.x + 10, input_box.y + 5))

    # Draw message
    draw_text(message, FONT, message_color, screen, WIDTH//2, 220)

    # Draw instructions for user
    draw_text("Press ENTER to submit, BACKSPACE to delete", SMALL_FONT, (50, 50, 50), screen, WIDTH//2, 280)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Check answer ignoring case and spaces
                answer = countries[country_list[index]].lower().replace(" ", "")
                guess = input_text.lower().replace(" ", "")
                if guess == answer:
                    message = "Correct! 🎉"
                    message_color = (0, 150, 0)
                else:
                    message = f"Wrong! The capital is {countries[country_list[index]]}"
                    message_color = (200, 0, 0)
                pygame.time.set_timer(pygame.USEREVENT + 1, 2000)  # Timer to show message before next country
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                # Only accept letters and spaces
                if event.unicode.isalpha() or event.unicode == " ":
                    input_text += event.unicode

        elif event.type == pygame.USEREVENT + 1:
            next_country()
            pygame.time.set_timer(pygame.USEREVENT + 1, 0)  # Stop the timer

    pygame.display.flip()
    clock.tick(30)
