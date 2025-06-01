import pygame
import sys
from datetime import datetime

pygame.init()

# Constants
WIDTH, HEIGHT = 700, 550
BG_COLOR = (245, 245, 245)
TEXT_COLOR = (30, 30, 30)
INPUT_BG = (230, 230, 230)
INPUT_ACTIVE_BG = (210, 230, 255)
SELECTED_BG = (200, 220, 255)
BUTTON_BG = (100, 150, 250)
BUTTON_HOVER_BG = (70, 120, 230)
BUTTON_TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.SysFont('consolas', 22)
LINE_HEIGHT = FONT.get_height() + 10
SCROLL_SPEED = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minimalistic Journal App")

def load_entries(filename="journal.txt"):
    entries = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f.read().splitlines():
                if "|||" in line:
                    timestamp, text = line.split("|||", 1)
                    entries.append((timestamp, text))
    except FileNotFoundError:
        pass
    return entries

def save_entries(entries, filename="journal.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for timestamp, text in entries:
            f.write(f"{timestamp}|||{text}\n")

# Button class for reuse
class Button:
    def __init__(self, rect, text):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.hovered = False

    def draw(self, surface):
        color = BUTTON_HOVER_BG if self.hovered else BUTTON_BG
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        text_surf = FONT.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)

# Render entries with timestamp aligned right and truncated if needed
def render_entries(surface, entries, offset, selected_idx):
    y = 10 - offset
    right_margin = 10
    max_text_width = WIDTH - 40 - 150  # leave space for timestamp on right

    for idx, (timestamp, text) in enumerate(entries):
        if idx == selected_idx:
            pygame.draw.rect(surface, SELECTED_BG, (5, y - 2, WIDTH - 20, LINE_HEIGHT))

        # Render timestamp on right
        timestamp_surf = FONT.render(timestamp, True, TEXT_COLOR)
        timestamp_width = timestamp_surf.get_width()
        timestamp_x = WIDTH - right_margin - timestamp_width
        timestamp_y = y

        # Truncate text to fit left space (with ellipsis if needed)
        available_width = timestamp_x - 20  # 20px padding on left
        rendered_text = text
        text_surf = FONT.render(rendered_text, True, TEXT_COLOR)
        while text_surf.get_width() > available_width and len(rendered_text) > 3:
            rendered_text = rendered_text[:-4] + "..."
            text_surf = FONT.render(rendered_text, True, TEXT_COLOR)

        # Draw entry text
        surface.blit(text_surf, (10, y))
        # Draw timestamp
        surface.blit(timestamp_surf, (timestamp_x, timestamp_y))
        y += LINE_HEIGHT

# Draw input box with active color and send arrow button
def draw_input_box(surface, rect, text, active):
    bg_color = INPUT_ACTIVE_BG if active else INPUT_BG
    pygame.draw.rect(surface, bg_color, rect, border_radius=8)

    # Text
    input_surface = FONT.render(text, True, TEXT_COLOR)
    surface.blit(input_surface, (rect.x + 8, rect.y + (rect.height - FONT.get_height()) // 2))

    # Send arrow on right side
    arrow_text = "▶"
    arrow_surf = FONT.render(arrow_text, True, BUTTON_BG)
    arrow_rect = arrow_surf.get_rect()
    arrow_rect.centery = rect.centery
    arrow_rect.right = rect.right - 10
    surface.blit(arrow_surf, arrow_rect)
    return arrow_rect  # return arrow rect for click detection

# Initialize variables
entries = load_entries()
input_text = ""
scroll_offset = 0
max_scroll = max(0, len(entries) * LINE_HEIGHT - (HEIGHT - 130))
selected_idx = None
editing_mode = False
input_active = False

input_box = pygame.Rect(10, HEIGHT - 90, WIDTH - 20, 50)
btn_edit = Button((10, HEIGHT - 30, 140, 34), "Edit Entry")    # wider button
btn_delete = Button((160, HEIGHT - 30, 160, 34), "Delete Entry")  # wider button

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BG_COLOR)

    render_entries(screen, entries, scroll_offset, selected_idx)

    # Draw input box and get arrow rect
    arrow_rect = draw_input_box(screen, input_box, input_text, input_active)

    mouse_pos = pygame.mouse.get_pos()
    for btn in [btn_edit, btn_delete]:
        btn.hovered = btn.is_hovered(mouse_pos)
        btn.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_entries(entries)
            running = False

        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text.strip():
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                        if editing_mode and selected_idx is not None:
                            entries[selected_idx] = (timestamp, input_text.strip())
                            editing_mode = False
                        else:
                            entries.append((timestamp, input_text.strip()))
                            max_scroll = max(0, len(entries) * LINE_HEIGHT - (HEIGHT - 130))
                            scroll_offset = max_scroll
                        input_text = ""
                        selected_idx = None
                        max_scroll = max(0, len(entries) * LINE_HEIGHT - (HEIGHT - 130))
                    # else ignore empty input
                else:
                    if event.unicode.isprintable():
                        input_text += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                # Check if clicked inside input box
                if input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False

                # Check if clicked on send arrow
                if arrow_rect.collidepoint(event.pos) and input_active:
                    if input_text.strip():
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                        if editing_mode and selected_idx is not None:
                            entries[selected_idx] = (timestamp, input_text.strip())
                            editing_mode = False
                        else:
                            entries.append((timestamp, input_text.strip()))
                            max_scroll = max(0, len(entries) * LINE_HEIGHT - (HEIGHT - 130))
                            scroll_offset = max_scroll
                        input_text = ""
                        selected_idx = None
                        max_scroll = max(0, len(entries) * LINE_HEIGHT - (HEIGHT - 130))

                # Check if clicking on an entry
                y_start = 10 - scroll_offset
                clicked_index = None
                for i in range(len(entries)):
                    entry_rect = pygame.Rect(5, y_start + i * LINE_HEIGHT, WIDTH - 20, LINE_HEIGHT)
                    if entry_rect.collidepoint(event.pos):
                        clicked_index = i
                        break
                if clicked_index is not None:
                    selected_idx = clicked_index
                    editing_mode = False
                    input_text = ""

                # Check buttons
                if btn_edit.is_hovered(event.pos):
                    if selected_idx is not None:
                        editing_mode = True
                        input_active = True
                        input_text = entries[selected_idx][1]
                elif btn_delete.is_hovered(event.pos):
                    if selected_idx is not None:
                        del entries[selected_idx]
                        selected_idx = None
                        editing_mode = False
                        input_text = ""
                        max_scroll = max(0, len(entries) * LINE_HEIGHT - (HEIGHT - 130))
                        scroll_offset = min(scroll_offset, max_scroll)

            elif event.button == 4:  # Scroll up
                scroll_offset = max(scroll_offset - SCROLL_SPEED * LINE_HEIGHT, 0)
            elif event.button == 5:  # Scroll down
                scroll_offset = min(scroll_offset + SCROLL_SPEED * LINE_HEIGHT, max_scroll)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
