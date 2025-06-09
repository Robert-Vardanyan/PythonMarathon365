import pygame
import random
import sys
import time

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Operations Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (180, 0, 0)
GRAY = (220, 220, 220)

# Fonts
font_big = pygame.font.SysFont(None, 60)
font_small = pygame.font.SysFont(None, 32)

# Game variables
score = 0
input_text = ""
feedback = ""
feedback_color = BLACK
time_limit = 60  # 60 seconds to play
start_time = time.time()

# Function to create a new math question
def generate_question():
    b = random.randint(1, 10)
    op = random.choice(["+", "-", "*", "/"])
    if op == "/":
        a = b * random.randint(1, 10)  # ensures division with no remainder
        result = a // b
    else:
        a = random.randint(1, 20)
        result = eval(f"{a}{op}{b}")
    return f"{a} {op} {b}", int(result)

# Generate the first question
question, answer = generate_question()

clock = pygame.time.Clock()

# Function to draw text on the screen
def draw_text(text, x, y, font, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, time_limit - elapsed_time)

    # Stop the game if time runs out
    if remaining_time <= 0:
        feedback = f"Time's up! Final Score: {score}"
        feedback_color = RED
        running = False

    # Handle user input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    if int(input_text) == answer:
                        score += 1
                        feedback = "Correct!"
                        feedback_color = GREEN
                    else:
                        feedback = f"Wrong! Answer: {answer}"
                        feedback_color = RED
                    question, answer = generate_question()
                    input_text = ""
                except:
                    feedback = "Invalid input"
                    feedback_color = RED
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_MINUS and len(input_text) == 0:
                input_text += "-"
            elif event.unicode.isdigit():
                input_text += event.unicode

    # Draw question and input field
    draw_text("Solve:", 50, 40, font_big)
    draw_text(question, 200, 40, font_big)

    pygame.draw.rect(screen, GRAY, (200, 120, 200, 60))
    draw_text(input_text, 210, 130, font_big)

    # Display score, time, and feedback
    draw_text("Score: " + str(score), 50, 300, font_small)
    draw_text("Time Left: " + str(remaining_time), 50, 340, font_small)
    draw_text(feedback, 50, 200, font_small, feedback_color)

    pygame.display.flip()
    clock.tick(30)

# Show final score for 3 seconds before quitting
pygame.time.delay(3000)
pygame.quit()
