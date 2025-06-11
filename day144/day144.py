import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("English to Morse Code Quiz")

font = pygame.font.SysFont("Consolas", 32)
small_font = pygame.font.SysFont("Consolas", 24)
clock = pygame.time.Clock()

# Morse code dictionary for letters and digits
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..', 'E': '.',    'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',   'J': '.---','K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.','Q': '--.-', 'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',  'V': '...-','W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---','3': '...--','4': '....-',
    '5': '.....', '6': '-....', '7': '--...','8': '---..','9': '----.'
}

# Quiz words
words = ["HELLO", "WORLD", "PYTHON", "MORSE", "CODE", "QUIZ", "TEST", "SOS", "OPENAI"]
current_index = 0
score = 0

user_input = ""
feedback = ""
show_feedback_time = 0

def draw_text(text, font, color, x, y):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

def get_morse(word):
    return " ".join(MORSE_CODE_DICT.get(ch, '') for ch in word)

running = True
while running:
    screen.fill((230, 230, 230))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                # Check user input
                correct_morse = get_morse(words[current_index])
                if user_input.strip() == correct_morse:
                    feedback = "✅ Correct!"
                    score += 1
                else:
                    feedback = f"❌ Wrong! Correct: {correct_morse}"
                show_feedback_time = pygame.time.get_ticks()
                user_input = ""
                current_index += 1
                if current_index >= len(words):
                    current_index = 0  # Restart quiz
                    feedback += " Quiz restarted!"
                    score = 0
            else:
                if event.unicode in ['.', '-', ' ']:
                    user_input += event.unicode

    # Draw quiz UI
    draw_text("English to Morse Code Quiz", font, (0, 0, 50), 50, 20)
    draw_text(f"Translate this word into Morse:", small_font, (0, 0, 0), 50, 80)
    draw_text(words[current_index], font, (10, 10, 70), 50, 120)
    draw_text("Type Morse code using '.' '-' and space", small_font, (100, 100, 100), 50, 180)

    input_box = pygame.Rect(50, 220, 500, 40)
    pygame.draw.rect(screen, (255, 255, 255), input_box)
    pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
    draw_text(user_input, font, (0, 0, 0), 60, 225)

    draw_text(f"Score: {score}", small_font, (0, 100, 0), 50, 280)

    # Show feedback for 2 seconds
    if feedback and pygame.time.get_ticks() - show_feedback_time < 2000:
        draw_text(feedback, font, (200, 0, 0) if "Wrong" in feedback else (0, 150, 0), 50, 320)
    elif pygame.time.get_ticks() - show_feedback_time >= 2000:
        feedback = ""

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
