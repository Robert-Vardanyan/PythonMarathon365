import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Recipe Picker")

font = pygame.font.SysFont('arial', 22)
big_font = pygame.font.SysFont('arial', 28)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 180, 255)
HOVER = (150, 220, 255)

recipes = [
    "Spaghetti Carbonara\n- Pasta\n- Eggs\n- Bacon\n- Cheese",
    "Chicken Stir Fry\n- Chicken\n- Veggies\n- Soy Sauce\n- Rice",
    "Pancakes\n- Flour\n- Eggs\n- Milk\n- Baking Powder",
    "Tacos\n- Tortillas\n- Ground Beef\n- Lettuce\n- Cheese",
    "Tomato Soup\n- Tomatoes\n- Onion\n- Garlic\n- Cream"
]

current_recipe = "Click to get a recipe!"

def draw_text(text, x, y, max_width):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        txt = font.render(line, True, BLACK)
        screen.blit(txt, (x, y + i * 30))

def main():
    global current_recipe
    running = True
    button_rect = pygame.Rect(200, 300, 200, 50)

    while running:
        screen.fill(WHITE)

        # Draw title
        title = big_font.render("Random Recipe Picker", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))

        # Draw current recipe
        draw_text(current_recipe, 80, 100, 440)

        # Draw button
        mouse = pygame.mouse.get_pos()
        color = HOVER if button_rect.collidepoint(mouse) else BLUE
        pygame.draw.rect(screen, color, button_rect, border_radius=10)
        button_text = font.render("Pick Recipe", True, BLACK)
        screen.blit(button_text, (button_rect.x + 40, button_rect.y + 15))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    current_recipe = random.choice(recipes)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
