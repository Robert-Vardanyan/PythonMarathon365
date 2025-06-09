import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Story Adventure")
font = pygame.font.SysFont("arial", 20)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 200, 255)
BUTTON_HOVER = (150, 250, 255)

# Простейшая история с 30 точками
story = {
    "start": {"text": "You wake up in a forest. Go left or right?", "choices": {"Left": "1", "Right": "2"}},
    "1": {"text": "You see a river. Swim or walk?", "choices": {"Swim": "3", "Walk": "4"}},
    "2": {"text": "You find a cave. Enter or avoid?", "choices": {"Enter": "5", "Avoid": "6"}},
    "3": {"text": "The current is strong. You struggle. Keep swimming or go back?", "choices": {"Keep swimming": "7", "Go back": "8"}},
    "4": {"text": "You find a bridge. Cross it or stay?", "choices": {"Cross": "9", "Stay": "10"}},
    "5": {"text": "Inside is a bear! Run or fight?", "choices": {"Run": "11", "Fight": "12"}},
    "6": {"text": "You find berries. Eat or ignore?", "choices": {"Eat": "13", "Ignore": "14"}},
    "7": {"text": "You make it to the other side. Rest or explore?", "choices": {"Rest": "15", "Explore": "16"}},
    "8": {"text": "You reach shore safely. You rest.", "choices": {}},
    "9": {"text": "The bridge collapses! Jump or hold on?", "choices": {"Jump": "17", "Hold on": "18"}},
    "10": {"text": "You get bored. Move on or sleep?", "choices": {"Move on": "19", "Sleep": "20"}},
    "11": {"text": "You escape! But you're tired. Nap or continue?", "choices": {"Nap": "21", "Continue": "22"}},
    "12": {"text": "The bear wins. You died.", "choices": {}},
    "13": {"text": "They were poisonous! You died.", "choices": {}},
    "14": {"text": "Smart choice. You walk further.", "choices": {"Climb hill": "23", "Enter fog": "24"}},
    "15": {"text": "You are attacked while sleeping. You died.", "choices": {}},
    "16": {"text": "You find a sword! Keep or drop?", "choices": {"Keep": "25", "Drop": "26"}},
    "17": {"text": "You land hard. Injured. Crawl or shout?", "choices": {"Crawl": "27", "Shout": "28"}},
    "18": {"text": "You fall. You died.", "choices": {}},
    "19": {"text": "You find a house. Knock or peek?", "choices": {"Knock": "29", "Peek": "30"}},
    "20": {"text": "You oversleep and freeze. You died.", "choices": {}},
    "21": {"text": "You wake refreshed. Climb tree or walk?", "choices": {"Climb": "26", "Walk": "25"}},
    "22": {"text": "You trip and fall. You died.", "choices": {}},
    "23": {"text": "You see a lake. Fish or swim?", "choices": {"Fish": "30", "Swim": "28"}},
    "24": {"text": "The fog hides a monster. You died.", "choices": {}},
    "25": {"text": "Sword helps you survive. You win!", "choices": {}},
    "26": {"text": "You find a hidden path to safety. You win!", "choices": {}},
    "27": {"text": "You crawl to safety. You win!", "choices": {}},
    "28": {"text": "No one hears. You freeze. You died.", "choices": {}},
    "29": {"text": "A kind old man helps you. You win!", "choices": {}},
    "30": {"text": "The door was trapped. You died.", "choices": {}}
}

current_node = "start"

def draw_text(text, x, y, max_width):
    words = text.split()
    line = ""
    lines = []
    for word in words:
        if font.size(line + word)[0] > max_width:
            lines.append(line)
            line = word + " "
        else:
            line += word + " "
    lines.append(line)

    for i, l in enumerate(lines):
        rendered = font.render(l.strip(), True, BLACK)
        screen.blit(rendered, (x, y + i * 25))

def draw_buttons(choices):
    buttons = []
    for i, (label, target) in enumerate(choices.items()):
        rect = pygame.Rect(100, 250 + i * 60, 600, 40)
        mouse = pygame.mouse.get_pos()
        color = BUTTON_HOVER if rect.collidepoint(mouse) else BUTTON_COLOR
        pygame.draw.rect(screen, color, rect, border_radius=10)
        text = font.render(label, True, BLACK)
        screen.blit(text, (rect.x + 10, rect.y + 10))
        buttons.append((rect, target))
    return buttons

def main():
    global current_node
    running = True
    while running:
        screen.fill(WHITE)
        node = story[current_node]

        draw_text(node["text"], 100, 50, 600)
        buttons = draw_buttons(node["choices"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect, target in buttons:
                    if rect.collidepoint(event.pos):
                        current_node = target

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
