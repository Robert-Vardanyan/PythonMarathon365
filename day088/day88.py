import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Deep Story Plot Generator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER = (100, 149, 237)
CLEAR_COLOR = (200, 50, 50)
CLEAR_HOVER = (255, 80, 80)

TITLE_FONT = pygame.font.SysFont("arial", 40)
TEXT_FONT = pygame.font.SysFont("arial", 22)
BUTTON_FONT = pygame.font.SysFont("arial", 26)

# Define story components to mix and match
characters = [
    "A young orphan",
    "A cynical detective",
    "An ambitious scientist",
    "A rebellious pirate",
    "A gifted wizard",
    "An android searching for identity",
    "A time traveler",
    "A secret agent",
    "A small-town journalist",
    "A fearless explorer"
]

settings = [
    "in a post-apocalyptic world",
    "in a haunted mansion",
    "on a distant alien planet",
    "in a bustling metropolis",
    "in an ancient magical kingdom",
    "in a secret underwater city",
    "during a civil war",
    "in a futuristic cyberpunk city",
    "on a mysterious island",
    "in a virtual reality simulation"
]

conflicts = [
    "must solve a murder mystery",
    "is trying to stop an impending war",
    "is trying to unlock a hidden power",
    "has to survive against impossible odds",
    "is seeking revenge against a powerful enemy",
    "is caught in a conspiracy",
    "must prevent an ancient evil from awakening",
    "is torn between two worlds",
    "is racing against time to save a loved one",
    "discovers a shocking secret about their past"
]

goals = [
    "to save their kingdom",
    "to find a legendary treasure",
    "to protect a secret that could change the world",
    "to bring peace to warring factions",
    "to prove their innocence",
    "to discover the truth about their origins",
    "to escape a dangerous prison",
    "to prevent a catastrophic event",
    "to unite divided people",
    "to achieve ultimate power"
]

twists = [
    "but they soon realize things are not what they seem.",
    "however, they must confront their deepest fears.",
    "only to discover a betrayal from someone close.",
    "but an unexpected ally changes everything.",
    "and they face a difficult moral choice.",
    "while uncovering a hidden conspiracy.",
    "but their actions might cause more harm than good.",
    "and they must sacrifice something dear to them.",
    "but the true enemy is within.",
    "and nothing will ever be the same again."
]

class Button:
    def __init__(self, text, x, y, w, h, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = hover_color

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        text_surf = BUTTON_FONT.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

def draw_text_center(surface, text, y, font, color=BLACK):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(WIDTH // 2, y))
    surface.blit(text_surf, text_rect)

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines

def generate_plot():
    # Randomly choose one element from each category and combine them into a plot
    char = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    goal = random.choice(goals)
    twist = random.choice(twists)

    plot = f"{char} {setting} {conflict} {goal}, {twist}"
    return plot

generate_btn = Button("Generate Plot", 100, 320, 160, 50, BUTTON_COLOR, BUTTON_HOVER)
clear_btn = Button("Clear", 340, 320, 120, 50, CLEAR_COLOR, CLEAR_HOVER)

current_plot = ""

running = True
while running:
    screen.fill(WHITE)
    draw_text_center(screen, "Deep Story Plot Generator", 60, TITLE_FONT)

    generate_btn.draw(screen)
    clear_btn.draw(screen)

    if current_plot:
        lines = wrap_text(current_plot, TEXT_FONT, WIDTH - 60)
        start_y = 150
        line_height = TEXT_FONT.get_height() + 5
        for i, line in enumerate(lines):
            draw_text_center(screen, line, start_y + i * line_height, TEXT_FONT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if generate_btn.is_clicked(event):
            current_plot = generate_plot()

        if clear_btn.is_clicked(event):
            current_plot = ""

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
