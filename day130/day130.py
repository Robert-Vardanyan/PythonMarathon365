import pygame
import requests
import threading

pygame.init()

# Размер окна
WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Definition Viewer")

# Шрифты и цвета
FONT = pygame.font.SysFont(None, 28)
INPUT_FONT = pygame.font.SysFont(None, 32)
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
INPUT_COLOR_ACTIVE = (100, 200, 255)
INPUT_COLOR_INACTIVE = (70, 70, 70)

clock = pygame.time.Clock()

# Поле ввода по центру
input_box = pygame.Rect(WIDTH // 2 - 330, 30, 660, 40)
active = False
user_text = ''

definitions = []
loading = False
error_msg = ''

def fetch_definition(word):
    global definitions, loading, error_msg
    loading = True
    error_msg = ''
    definitions = []
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        meanings = data[0]['meanings']

        for meaning in meanings:
            part_of_speech = meaning['partOfSpeech']
            defs = [d['definition'] for d in meaning['definitions']]
            definitions.append((part_of_speech, defs))
    except requests.exceptions.HTTPError:
        error_msg = f"No definition found for '{word}'."
    except Exception as e:
        error_msg = f"Error: {e}"
    loading = False

def draw_text(text, pos, font, color=TEXT_COLOR, max_width=800):
    words = text.split(' ')
    lines = []
    line = ''
    for word in words:
        test_line = line + word + ' '
        if font.size(test_line)[0] > max_width:
            lines.append(line)
            line = word + ' '
        else:
            line = test_line
    lines.append(line)

    y_offset = 0
    for line in lines:
        txt_surf = font.render(line.strip(), True, color)
        screen.blit(txt_surf, (pos[0], pos[1] + y_offset))
        y_offset += font.get_height() + 8  # увеличен зазор между строками
    return y_offset

def main():
    global active, user_text, definitions, loading, error_msg

    running = True
    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN and user_text.strip() != '':
                    threading.Thread(target=fetch_definition, args=(user_text.strip(),), daemon=True).start()
                    user_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if len(user_text) < 50:
                        user_text += event.unicode

        # Отрисовка поля ввода
        color = INPUT_COLOR_ACTIVE if active else INPUT_COLOR_INACTIVE
        pygame.draw.rect(screen, color, input_box, 2)
        txt_surface = INPUT_FONT.render(user_text, True, TEXT_COLOR)
        screen.blit(txt_surface, (input_box.x + 10, input_box.y + 5))

        y_offset = 100

        if loading:
            loading_surf = FONT.render("Loading...", True, (255, 255, 0))
            screen.blit(loading_surf, (WIDTH // 2 - loading_surf.get_width() // 2, y_offset))
        elif error_msg:
            y_offset += draw_text(error_msg, (50, y_offset), FONT, color=(255, 80, 80))
        elif definitions:
            for pos_tag, defs in definitions:
                part_surf = FONT.render(f"{pos_tag}:", True, (150, 255, 150))
                screen.blit(part_surf, (50, y_offset))
                y_offset += part_surf.get_height() + 5
                for i, d in enumerate(defs, 1):
                    def_text = f"{i}. {d}"
                    y_offset += draw_text(def_text, (70, y_offset), FONT)
                y_offset += 15
        else:
            # Подсказка, когда ничего не введено
            info_text = "Type a word and press Enter to fetch definition."
            info_surface = FONT.render(info_text, True, (180, 180, 180))
            screen.blit(info_surface, (WIDTH // 2 - info_surface.get_width() // 2, y_offset))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
