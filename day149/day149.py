import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎁 Greeting Card Generator")
font = pygame.font.SysFont("arial", 32)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 182, 193)
SKY = (135, 206, 235)
LIME = (144, 238, 144)

background_colors = [WHITE, PINK, SKY, LIME]
bg_index = 0

text_input = ""
input_active = True

save_button = pygame.Rect(650, 20, 120, 40)
color_button = pygame.Rect(650, 80, 120, 40)

def draw_text_center(text, y, color=BLACK):
    render = font.render(text, True, color)
    rect = render.get_rect(center=(WIDTH//2, y))
    screen.blit(render, rect)

def draw_input_box():
    pygame.draw.rect(screen, WHITE, (100, 500, 600, 40))
    pygame.draw.rect(screen, BLACK, (100, 500, 600, 40), 2)
    input_text = font.render(text_input, True, BLACK)
    screen.blit(input_text, (110, 505))

def save_card():
    pygame.image.save(screen, "greeting_card.png")
    print("Card saved as greeting_card.png")

running = True
while running:
    screen.fill(background_colors[bg_index])

    draw_text_center("🎈 Create Your Greeting Card!", 50)
    draw_text_center(text_input, 300)
    draw_input_box()

    pygame.draw.rect(screen, SKY, save_button)
    pygame.draw.rect(screen, PINK, color_button)

    save_text = font.render("💾 Save", True, BLACK)
    color_text = font.render("🎨 Color", True, BLACK)
    screen.blit(save_text, (save_button.x + 10, save_button.y + 5))
    screen.blit(color_text, (color_button.x + 10, color_button.y + 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if save_button.collidepoint(event.pos):
                save_card()
            elif color_button.collidepoint(event.pos):
                bg_index = (bg_index + 1) % len(background_colors)

        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]
            elif event.key == pygame.K_RETURN:
                input_active = False
            else:
                text_input += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
