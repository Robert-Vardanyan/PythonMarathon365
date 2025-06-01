import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Periodic Table Quiz")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (210, 210, 210)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 215, 0)

# Fonts
FONT = pygame.font.SysFont("arial", 28)
BIGFONT = pygame.font.SysFont("arial", 40)

# Dictionary of element symbols and their full names
elements = {
    "H": "hydrogen", "He": "helium", "Li": "lithium", "Be": "beryllium", "B": "boron",
    "C": "carbon", "N": "nitrogen", "O": "oxygen", "F": "fluorine", "Ne": "neon",
    "Na": "sodium", "Mg": "magnesium", "Al": "aluminum", "Si": "silicon", "P": "phosphorus",
    "S": "sulfur", "Cl": "chlorine", "Ar": "argon", "K": "potassium", "Ca": "calcium"
}
symbols = list(elements.keys())

# Game state variables
score = 0
wrong = 0
current_symbol = random.choice(symbols)
user_input = ""
quiz_done = False
total_questions = 10
asked = 0

# Helper function to render text
def draw_text(text, font, color, x, y, center=True):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(x, y) if center else (x, y))
    screen.blit(rendered, rect)

# Load a new question
def new_question():
    global current_symbol, user_input
    current_symbol = random.choice(symbols)
    user_input = ""

# Finish the quiz
def end_quiz():
    global quiz_done
    quiz_done = True

# Draw all elements on the screen
def draw_interface():
    screen.fill(WHITE)

    if quiz_done:
        accuracy = round(score / total_questions * 100)
        draw_text("Quiz Finished!", BIGFONT, BLACK, WIDTH // 2, 60)
        draw_text(f"Correct: {score}", FONT, GREEN, WIDTH // 2, 130)
        draw_text(f"Incorrect: {wrong}", FONT, RED, WIDTH // 2, 180)
        draw_text(f"Accuracy: {accuracy}%", FONT, BLACK, WIDTH // 2, 230)
        draw_text("Press ESC to quit", FONT, GRAY, WIDTH // 2, 300)
    else:
        draw_text("What is the name of element with symbol:", FONT, BLACK, WIDTH // 2, 50)
        draw_text(current_symbol, BIGFONT, YELLOW, WIDTH // 2, 110)

        # Input box
        pygame.draw.rect(screen, GRAY, (150, 180, 400, 50), 2)
        draw_text(user_input, FONT, BLACK, WIDTH // 2, 205)

        draw_text(f"Question {asked + 1} / {total_questions}", FONT, GRAY, WIDTH // 2, 280)

    pygame.display.flip()

# Main game loop
def main():
    global user_input, score, wrong, asked

    clock = pygame.time.Clock()
    running = True

    while running:
        draw_interface()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if quiz_done:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    continue

                if event.key == pygame.K_RETURN:
                    if user_input.strip().lower() == elements[current_symbol]:
                        score += 1
                    else:
                        wrong += 1
                    asked += 1
                    if asked >= total_questions:
                        end_quiz()
                    else:
                        new_question()

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

                elif event.unicode.isalpha() or event.unicode == " ":
                    user_input += event.unicode

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
