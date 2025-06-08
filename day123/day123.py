import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cipher Challenge")

# Colors and font
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
DARK = (30, 30, 30)
RED = (200, 50, 50)
GREEN = (50, 200, 100)
FONT = pygame.font.SysFont("arial", 24)

# Caesar cipher logic
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Sample sentences
sentences = [
    "hello world", "python is fun", "i love programming",
    "stay curious", "keep learning", "cipher game is cool"
]

# Generate a challenge
def generate_challenge():
    original = random.choice(sentences)
    shift = random.randint(1, 25)
    encrypted = caesar_cipher(original, shift)
    return original, encrypted, shift

# UI Elements
input_box = pygame.Rect(100, 240, 400, 40)
check_button = pygame.Rect(100, 300, 100, 40)
next_button = pygame.Rect(250, 300, 100, 40)
clear_button = pygame.Rect(400, 300, 100, 40)

input_text = ""
message = ""
color_message = DARK

original, encrypted, shift = generate_challenge()

clock = pygame.time.Clock()
active = False
running = True

while running:
    screen.fill(WHITE)

    # Draw challenge
    screen.blit(FONT.render("Decrypt this message:", True, DARK), (100, 50))
    screen.blit(FONT.render(f"🔒 {encrypted}", True, BLUE), (100, 90))

    # Input box
    pygame.draw.rect(screen, BLUE, input_box, 2)
    input_surface = FONT.render(input_text, True, DARK)
    screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))

    # Buttons
    pygame.draw.rect(screen, BLUE, check_button)
    pygame.draw.rect(screen, BLUE, next_button)
    pygame.draw.rect(screen, BLUE, clear_button)

    screen.blit(FONT.render("Check", True, WHITE), (check_button.x + 15, check_button.y + 5))
    screen.blit(FONT.render("Next", True, WHITE), (next_button.x + 15, next_button.y + 5))
    screen.blit(FONT.render("Clear", True, WHITE), (clear_button.x + 15, clear_button.y + 5))

    # Message
    if message:
        msg_surface = FONT.render(message, True, color_message)
        screen.blit(msg_surface, (100, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            active = input_box.collidepoint(event.pos)
            if check_button.collidepoint(event.pos):
                if input_text.lower().strip() == original:
                    message = "✅ Correct!"
                    color_message = GREEN
                else:
                    message = "❌ Incorrect. Try again."
                    color_message = RED

            if next_button.collidepoint(event.pos):
                original, encrypted, shift = generate_challenge()
                input_text = ""
                message = ""

            if clear_button.collidepoint(event.pos):
                input_text = ""
                message = ""

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif len(input_text) < 30 and event.unicode.isprintable():
                input_text += event.unicode

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
