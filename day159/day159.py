import pygame
import sys
import random
import time

pygame.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⌨️ Basic Keyboard Trainer")

font = pygame.font.SysFont(None, 80)
small_font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
current_letter = random.choice(letters)
score = 0
start_time = time.time()
reaction_times = []

input_active = True
message = ""

def draw_text(text, x, y, font, color=(0, 0, 0)):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

running = True
while running:
    screen.fill((200, 230, 255))

    draw_text("Type the letter shown:", 30, 20, small_font)
    draw_text(current_letter, WIDTH//2 - 20, HEIGHT//2 - 40, font, (50, 100, 200))
    draw_text(f"Score: {score}", 30, HEIGHT - 80, small_font)
    if reaction_times:
        avg_react = sum(reaction_times) / len(reaction_times)
        draw_text(f"Avg Reaction: {avg_react:.2f} sec", 30, HEIGHT - 50, small_font)

    if message:
        draw_text(message, 30, HEIGHT - 110, small_font, (200, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and input_active:
            pressed_char = event.unicode.upper()
            if pressed_char == current_letter:
                reaction = time.time() - start_time
                reaction_times.append(reaction)
                score += 1
                current_letter = random.choice(letters)
                start_time = time.time()
                message = ""
            else:
                message = f"Wrong key! You pressed '{event.unicode}'"

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
