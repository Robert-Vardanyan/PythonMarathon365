import pygame
import sys

pygame.init()

# Setup
WIDTH, HEIGHT = 700, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Encryption Tool")

# Fonts and colors
FONT = pygame.font.SysFont(None, 28)
BIG_FONT = pygame.font.SysFont(None, 38)
WHITE = (255, 255, 255)
GRAY = (230, 230, 230)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
GREEN = (34, 139, 34)
RED = (200, 50, 50)
PURPLE = (138, 43, 226)

# Encryption methods
def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

def reverse_encrypt(text):
    return text[::-1]

def reverse_decrypt(text):
    return text[::-1]

def xor_encrypt(text, key=7):
    return ''.join([chr(ord(c) ^ key) for c in text])

def xor_decrypt(text, key=7):
    return xor_encrypt(text, key)  # symmetric

# State
input_text = ""
output_text = ""
active = False
method = "Caesar"
mode = "Encrypt"  # or "Decrypt"

# Rects
input_box = pygame.Rect(50, 50, 600, 40)
run_btn = pygame.Rect(50, 110, 100, 40)
method_btn = pygame.Rect(170, 110, 160, 40)
mode_btn = pygame.Rect(350, 110, 120, 40)
clear_btn = pygame.Rect(490, 110, 100, 40)

# Main loop
clock = pygame.time.Clock()
while True:
    screen.fill(WHITE)

    # Input box
    pygame.draw.rect(screen, GRAY if active else (210, 210, 210), input_box, 0, border_radius=5)
    pygame.draw.rect(screen, BLACK, input_box, 2, border_radius=5)
    input_surf = FONT.render(input_text, True, BLACK)
    screen.blit(input_surf, (input_box.x + 5, input_box.y + 8))

    # Buttons
    pygame.draw.rect(screen, BLUE, run_btn, border_radius=5)
    screen.blit(FONT.render(mode, True, WHITE), (run_btn.x + 20, run_btn.y + 10))

    pygame.draw.rect(screen, GREEN, method_btn, border_radius=5)
    screen.blit(FONT.render(f"Method: {method}", True, WHITE), (method_btn.x + 5, method_btn.y + 10))

    pygame.draw.rect(screen, PURPLE, mode_btn, border_radius=5)
    screen.blit(FONT.render("Toggle Mode", True, WHITE), (mode_btn.x + 5, mode_btn.y + 10))

    pygame.draw.rect(screen, RED, clear_btn, border_radius=5)
    screen.blit(FONT.render("Clear", True, WHITE), (clear_btn.x + 20, clear_btn.y + 10))

    # Output
    screen.blit(BIG_FONT.render("Result:", True, BLACK), (50, 180))
    pygame.draw.rect(screen, GRAY, (50, 220, 600, 40), border_radius=5)
    output_surf = FONT.render(output_text, True, BLACK)
    screen.blit(output_surf, (60, 230))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False

            if run_btn.collidepoint(event.pos):
                if method == "Caesar":
                    output_text = caesar_encrypt(input_text) if mode == "Encrypt" else caesar_decrypt(input_text)
                elif method == "Reverse":
                    output_text = reverse_encrypt(input_text)
                elif method == "XOR":
                    output_text = xor_encrypt(input_text)
                if mode == "Decrypt" and method == "Reverse":
                    output_text = reverse_decrypt(input_text)
                if mode == "Decrypt" and method == "XOR":
                    output_text = xor_decrypt(input_text)

            if method_btn.collidepoint(event.pos):
                method = "Reverse" if method == "Caesar" else "XOR" if method == "Reverse" else "Caesar"

            if mode_btn.collidepoint(event.pos):
                mode = "Decrypt" if mode == "Encrypt" else "Encrypt"

            if clear_btn.collidepoint(event.pos):
                input_text = ""
                output_text = ""

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif len(input_text) < 100:
                input_text += event.unicode

    pygame.display.flip()
    clock.tick(60)
