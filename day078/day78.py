import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Calculator")

FONT = pygame.font.SysFont(None, 50)
SMALL_FONT = pygame.font.SysFont(None, 30)

# Colors
BG_COLOR = (30, 30, 30)
BUTTON_COLOR = (70, 70, 70)
BUTTON_HOVER = (100, 100, 100)
TEXT_COLOR = (255, 255, 255)
DISPLAY_COLOR = (50, 50, 50)
CLEAR_COLOR = (200, 50, 50)  # Red for C button
BUTTON_BORDER_COLOR = (255, 255, 255)  # White border

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

btn_w = WIDTH // 4
btn_h = 70

input_text = ""
error = False

def draw_text(text, font, color, surface, x, y):
    txt_obj = font.render(text, True, color)
    txt_rect = txt_obj.get_rect(center=(x, y))
    surface.blit(txt_obj, txt_rect)

def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error"

clock = pygame.time.Clock()

while True:
    screen.fill(BG_COLOR)

    # Draw display area
    display_rect = pygame.Rect(10, 10, WIDTH - 20, 80)
    pygame.draw.rect(screen, DISPLAY_COLOR, display_rect, border_radius=10)
    
    # Display input text, right aligned with padding
    display_surface = FONT.render(input_text, True, TEXT_COLOR)
    display_pos = display_surface.get_rect(right=display_rect.right - 15, centery=display_rect.centery)
    screen.blit(display_surface, display_pos)

    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_clicked = True

    # Draw buttons
    for row_i, row in enumerate(buttons):
        for col_i, btn_text in enumerate(row):
            x = col_i * btn_w
            y = 100 + row_i * btn_h
            if row_i == 4:  # last row with '=' button full width
                if btn_text == '=':
                    btn_rect = pygame.Rect(0, y, WIDTH, btn_h)
            else:
                btn_rect = pygame.Rect(x, y, btn_w, btn_h)

            # Determine button color
            if btn_text == 'C':
                color = CLEAR_COLOR
                border = False
            else:
                if btn_rect.collidepoint(mouse_pos):
                    color = BUTTON_HOVER
                else:
                    color = BUTTON_COLOR
                border = True

            # Draw button rectangle
            pygame.draw.rect(screen, color, btn_rect, border_radius=10)

            # Draw border for all except C button
            if border:
                pygame.draw.rect(screen, BUTTON_BORDER_COLOR, btn_rect, width=2, border_radius=10)

            # Draw button text
            draw_text(btn_text, FONT, TEXT_COLOR, screen, btn_rect.centerx, btn_rect.centery)

            # Handle clicks
            if mouse_clicked and btn_rect.collidepoint(mouse_pos):
                if btn_text == 'C':
                    input_text = ""
                    error = False
                elif btn_text == '=':
                    if input_text:
                        result = calculate(input_text)
                        if result == "Error":
                            input_text = "Error"
                            error = True
                        else:
                            input_text = result
                            error = False
                else:
                    if error:
                        input_text = ""
                        error = False
                    input_text += btn_text

    pygame.display.flip()
    clock.tick(30)
