import pygame
import string

# Functions
def to_pig_latin(text):
    vowels = "aeiou"
    words = text.lower().split()
    translated = []

    for word in words:
        punct = ''
        if word[-1] in string.punctuation:
            punct = word[-1]
            word = word[:-1]

        if not word:
            continue

        if word[0] in vowels:
            new_word = word + "way"
        else:
            new_word = word[1:] + word[0] + "ay"

        translated.append(new_word + punct)

    return " ".join(translated)


def from_pig_latin(text):
    words = text.lower().split()
    translated = []

    for word in words:
        punct = ''
        if word[-1] in string.punctuation:
            punct = word[-1]
            word = word[:-1]

        if word.endswith("way"):
            new_word = word[:-3]
        elif word.endswith("ay") and len(word) > 2:
            core = word[:-2]
            new_word = core[-1] + core[:-1]
        else:
            new_word = word

        translated.append(new_word + punct)

    return " ".join(translated)

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pig Latin Translator")

# Fonts and colors
FONT = pygame.font.SysFont('arial', 24)
BIG_FONT = pygame.font.SysFont('arial', 30, bold=True)
WHITE = (255, 255, 255)
LIGHT_GRAY = (230, 230, 230)
ACTIVE_GRAY = (200, 200, 255)
DARK_GRAY = (50, 50, 50)
BLUE = (70, 130, 180)
RED = (200, 60, 60)
GREEN = (60, 160, 90)

# Input field
input_box = pygame.Rect(100, 90, 600, 40)
input_active = False
input_text = ""
translated_text = ""

# Buttons
translate_btn = pygame.Rect(150, 160, 150, 50)
reverse_btn = pygame.Rect(325, 160, 150, 50)
clear_btn = pygame.Rect(500, 160, 150, 50)

def draw_button(rect, text, color):
    pygame.draw.rect(screen, color, rect, border_radius=7)
    label = FONT.render(text, True, WHITE)
    screen.blit(label, (rect.centerx - label.get_width() // 2, rect.centery - label.get_height() // 2))

running = True
while running:
    screen.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()

    # Title
    title = BIG_FONT.render("Pig Latin Translator", True, DARK_GRAY)
    screen.blit(title, ((WIDTH - title.get_width()) // 2, 20))

    # Input box
    color = ACTIVE_GRAY if input_active else LIGHT_GRAY
    pygame.draw.rect(screen, color, input_box, border_radius=5)
    pygame.draw.rect(screen, DARK_GRAY, input_box, 2, border_radius=5)
    input_surface = FONT.render(input_text, True, DARK_GRAY)
    screen.blit(input_surface, (input_box.x + 10, input_box.y + 8))

    # Buttons
    draw_button(translate_btn, "Translate", BLUE)
    draw_button(reverse_btn, "Reverse", GREEN)
    draw_button(clear_btn, "Clear", RED)

    # Output
    if translated_text:
        lines = []
        words = translated_text.split()
        line = ''
        for word in words:
            if FONT.size(line + word)[0] < 600:
                line += word + ' '
            else:
                lines.append(line.strip())
                line = word + ' '
        lines.append(line.strip())

        for i, l in enumerate(lines):
            output_surface = FONT.render(l, True, DARK_GRAY)
            screen.blit(output_surface, (100, 240 + i * 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                input_active = True
            else:
                input_active = False

            if translate_btn.collidepoint(event.pos):
                translated_text = to_pig_latin(input_text)

            if reverse_btn.collidepoint(event.pos):
                translated_text = from_pig_latin(input_text)

            if clear_btn.collidepoint(event.pos):
                input_text = ""
                translated_text = ""

        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                translated_text = to_pig_latin(input_text)
            else:
                if len(input_text) < 100:
                    input_text += event.unicode

    pygame.display.flip()

pygame.quit()
