import pygame
import random
import sys

pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sentence Unscrambler")

# Fonts and Colors
FONT = pygame.font.SysFont("arial", 24)
BIG_FONT = pygame.font.SysFont("arial", 32, bold=True)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 180, 0)
RED = (180, 0, 0)
BLUE = (0, 100, 255)

# Sentences to unscramble
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Pygame makes game development fun and easy",
    "Artificial intelligence is changing the world",
    "Practice makes perfect in programming",
    "Python is a versatile and powerful language"
]

def scramble_sentence(sentence):
    """Scramble words of the sentence randomly."""
    words = sentence.split()
    scrambled = words[:]
    while True:
        random.shuffle(scrambled)
        if scrambled != words:
            break
    return scrambled

# Button class for reusability
class Button:
    def __init__(self, rect, text, color, text_color=WHITE):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = FONT
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=6)
        text_surf = self.font.render(self.text, True, self.text_color)
        surface.blit(text_surf, (self.rect.centerx - text_surf.get_width()//2,
                                 self.rect.centery - text_surf.get_height()//2))
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Initialize game state
current_sentence = random.choice(sentences)
scrambled_words = scramble_sentence(current_sentence)
selected_words = []

# Word button positions
word_buttons = []
margin_x, margin_y = 20, 120  # отступ снизу от заголовка увеличен до 120
padding = 10
x, y = margin_x, margin_y
max_width = WIDTH - 40

for word in scrambled_words:
    text_surf = FONT.render(word, True, BLACK)
    rect = pygame.Rect(x, y, text_surf.get_width()+20, text_surf.get_height()+15)
    word_buttons.append({"word": word, "rect": rect, "selected": False})
    x += rect.width + padding
    if x > max_width:
        x = margin_x
        y += rect.height + padding

# Buttons
check_btn = Button((WIDTH//2 - 150, HEIGHT - 60, 120, 40), "Check", BLUE)
reset_btn = Button((WIDTH//2 + 30, HEIGHT - 60, 120, 40), "Reset", GRAY, BLACK)

# Feedback message
feedback = ""
feedback_color = BLACK

def draw_selected_sentence():
    """Draw the sentence built by user centered below title."""
    sentence_str = " ".join(selected_words)
    text_surf = BIG_FONT.render(sentence_str, True, BLACK)
    # Center horizontally, place below title (~70px from top)
    rect_bg_width = min(text_surf.get_width() + 40, WIDTH - 40)
    rect_bg = pygame.Rect((WIDTH - rect_bg_width) // 2, 60, rect_bg_width, 50)
    pygame.draw.rect(screen, GRAY, rect_bg, border_radius=8)
    screen.blit(text_surf, (rect_bg.x + 20, rect_bg.y + (rect_bg.height - text_surf.get_height()) // 2))

running = True
while running:
    screen.fill(WHITE)
    # Draw title
    title_surf = BIG_FONT.render("Sentence Unscrambler", True, BLACK)
    screen.blit(title_surf, (WIDTH//2 - title_surf.get_width()//2, 10))

    # Draw selected sentence area below title (centered)
    draw_selected_sentence()

    # Draw scrambled word buttons
    for btn in word_buttons:
        color = GREEN if btn["selected"] else GRAY
        pygame.draw.rect(screen, color, btn["rect"], border_radius=6)
        text_surf = FONT.render(btn["word"], True, BLACK)
        screen.blit(text_surf, (btn["rect"].x + 10, btn["rect"].y + 5))

    # Draw buttons
    check_btn.draw(screen)
    reset_btn.draw(screen)

    # Draw feedback
    feedback_surf = FONT.render(feedback, True, feedback_color)
    screen.blit(feedback_surf, (WIDTH//2 - feedback_surf.get_width()//2, HEIGHT - 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            # Check word button clicks (only select if not already selected)
            for btn in word_buttons:
                if btn["rect"].collidepoint(pos) and not btn["selected"]:
                    btn["selected"] = True
                    selected_words.append(btn["word"])
                    feedback = ""
                    break

            # Check check button
            if check_btn.is_clicked(pos):
                user_sentence = " ".join(selected_words)
                if user_sentence == current_sentence:
                    feedback = "Correct! Well done! 🎉"
                    feedback_color = GREEN
                else:
                    feedback = "Incorrect. Try again."
                    feedback_color = RED

            # Check reset button
            if reset_btn.is_clicked(pos):
                selected_words.clear()
                feedback = ""
                for btn in word_buttons:
                    btn["selected"] = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
