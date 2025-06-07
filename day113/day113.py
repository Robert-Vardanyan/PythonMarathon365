import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, LIGHT_YELLOW, GRAY = (255, 255, 255), (0, 0, 0), (255, 255, 180), (220, 220, 220)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Highlighter")
font = pygame.font.SysFont(None, 32)
clock = pygame.time.Clock()

# Input Fields
text_input = ""
highlight_input = ""
active_text = False
active_highlight = False

text_rect = pygame.Rect(WIDTH//2 - 300, 100, 600, 40)
highlight_rect = pygame.Rect(WIDTH//2 - 300, 180, 600, 40)
button_rect = pygame.Rect(WIDTH//2 - 75, 250, 150, 40)

highlighted_result = []

def highlight_text(text, highlight):
    words = text.split(' ')
    result = []
    for word in words:
        if highlight.lower() in word.lower():
            result.append((word, True))
        else:
            result.append((word, False))
    return result

def draw():
    screen.fill(WHITE)

    # Draw input boxes
    pygame.draw.rect(screen, GRAY if active_text else BLACK, text_rect, 2)
    pygame.draw.rect(screen, GRAY if active_highlight else BLACK, highlight_rect, 2)
    pygame.draw.rect(screen, (0, 150, 200), button_rect, border_radius=6)

    # Labels
    label1 = font.render("Enter text:", True, BLACK)
    label2 = font.render("Highlight word/phrase:", True, BLACK)
    screen.blit(label1, (text_rect.x, text_rect.y - 30))
    screen.blit(label2, (highlight_rect.x, highlight_rect.y - 30))

    # Texts
    txt_surface = font.render(text_input, True, BLACK)
    screen.blit(txt_surface, (text_rect.x + 10, text_rect.y + 8))

    hlt_surface = font.render(highlight_input, True, BLACK)
    screen.blit(hlt_surface, (highlight_rect.x + 10, highlight_rect.y + 8))

    # Button
    btn_text = font.render("Highlight", True, WHITE)
    screen.blit(btn_text, (button_rect.x + 30, button_rect.y + 8))

    # Result
    if highlighted_result:
        x, y = WIDTH//2 - 300, 320
        for word, is_highlighted in highlighted_result:
            color = BLACK
            if is_highlighted:
                bg = LIGHT_YELLOW
                word_surface = font.render(word, True, color, bg)
            else:
                word_surface = font.render(word, True, color)
            screen.blit(word_surface, (x, y))
            x += word_surface.get_width() + 10
            if x > WIDTH - 100:
                x = WIDTH//2 - 300
                y += 40

    pygame.display.flip()

# Main Loop
running = True
while running:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            active_text = text_rect.collidepoint(event.pos)
            active_highlight = highlight_rect.collidepoint(event.pos)
            if button_rect.collidepoint(event.pos):
                highlighted_result = highlight_text(text_input, highlight_input)

        if event.type == pygame.KEYDOWN:
            if active_text:
                if event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode
            elif active_highlight:
                if event.key == pygame.K_BACKSPACE:
                    highlight_input = highlight_input[:-1]
                else:
                    highlight_input += event.unicode

    clock.tick(30)

pygame.quit()
