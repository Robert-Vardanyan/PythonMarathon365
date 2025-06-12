import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 700, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("💬 Random Famous Quotes")

font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

quotes = [
    ("The only limit to our realization of tomorrow is our doubts of today.", "Franklin D. Roosevelt"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("Life is what happens when you're busy making other plans.", "John Lennon"),
    ("Do not watch the clock. Do what it does. Keep going.", "Sam Levenson"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"),
    ("You miss 100% of the shots you don’t take.", "Wayne Gretzky"),
    ("Be yourself; everyone else is already taken.", "Oscar Wilde"),
]

def draw_text_wrapped(text, x, y, font, max_width, color=(0,0,0)):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)

    for i, line in enumerate(lines):
        render = font.render(line.strip(), True, color)
        screen.blit(render, (x, y + i * font.get_height()))

current_quote, current_author = random.choice(quotes)

running = True
while running:
    screen.fill((250, 245, 230))

    draw_text_wrapped(f"“{current_quote}”", 40, 50, font, WIDTH - 80)
    draw_text_wrapped(f"— {current_author}", 40, 160, font, WIDTH - 80, (50, 50, 50))

    draw_text_wrapped("Press SPACE for a new quote", 40, HEIGHT - 40, font, WIDTH - 80, (100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_quote, current_author = random.choice(quotes)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
