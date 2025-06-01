import pygame
import sys

pygame.init()

# Bigger window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roman Numeral Converter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
LIGHT_GRAY = (230, 230, 230)
BLUE = (100, 149, 237)
DARK_BLUE = (70, 100, 180)
RED = (220, 50, 50)
GREEN = (50, 180, 50)
YELLOW = (255, 255, 150)

FONT = pygame.font.SysFont("arial", 28)
SMALL_FONT = pygame.font.SysFont("arial", 18)
TITLE_FONT = pygame.font.SysFont("arial", 42, bold=True)

clock = pygame.time.Clock()

# Roman numeral mappings
ROMAN_MAP = [
    ("M",  1000),
    ("CM", 900),
    ("D",  500),
    ("CD", 400),
    ("C",  100),
    ("XC", 90),
    ("L",  50),
    ("XL", 40),
    ("X",  10),
    ("IX", 9),
    ("V",  5),
    ("IV", 4),
    ("I",  1)
]

def int_to_roman(num):
    if not (0 < num < 4000):
        return "Number out of range (1-3999)"
    result = ""
    for roman, val in ROMAN_MAP:
        while num >= val:
            result += roman
            num -= val
    return result

def roman_to_int(s):
    s = s.upper()
    i = 0
    total = 0
    for roman, val in ROMAN_MAP:
        while s[i:i+len(roman)] == roman:
            total += val
            i += len(roman)
            if i > len(s):
                return None
        if i >= len(s):
            break
    if i != len(s):
        return None
    return total

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = LIGHT_GRAY
        self.text = text
        self.txt_surface = FONT.render(text, True, BLACK)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state if clicked
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = YELLOW
            else:
                self.active = False
                self.color = LIGHT_GRAY

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return "ENTER"
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if len(self.text) < 20:
                    self.text += event.unicode
            self.txt_surface = FONT.render(self.text, True, BLACK)
        return None

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8)
        screen.blit(self.txt_surface, (self.rect.x + 15, self.rect.y + 12))
        pygame.draw.rect(screen, BLACK, self.rect, 3, border_radius=8)

    def get_text(self):
        return self.text.strip()

    def clear(self):
        self.text = ''
        self.txt_surface = FONT.render('', True, BLACK)

class Button:
    def __init__(self, text, x, y, w, h, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        is_hover = self.rect.collidepoint(mouse_pos)
        pygame.draw.rect(screen, self.hover_color if is_hover else self.color, self.rect, border_radius=10)
        text_surf = FONT.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

class RomanConverterApp:
    def __init__(self):
        # Center input box
        input_w, input_h = 500, 60
        input_x = (WIDTH - input_w) // 2
        input_y = 140
        self.input_box = InputBox(input_x, input_y, input_w, input_h)
        self.result = ""
        self.error = ""

        # Buttons stacked vertically, centered horizontally
        btn_w, btn_h = 300, 60
        btn_x = (WIDTH - btn_w) // 2
        btn_y_start = input_y + input_h + 50
        btn_gap = 25

        self.btn_to_roman = Button("Convert to Roman", btn_x, btn_y_start, btn_w, btn_h, BLUE, DARK_BLUE)
        self.btn_to_int = Button("Convert to Number", btn_x, btn_y_start + (btn_h + btn_gap), btn_w, btn_h, BLUE, DARK_BLUE)
        self.btn_clear = Button("Clear", btn_x, btn_y_start + 2 * (btn_h + btn_gap), btn_w, btn_h, RED, (255, 100, 100))

    def convert_to_roman(self):
        self.error = ""
        text = self.input_box.get_text()
        if not text.isdigit():
            self.error = "Input must be a positive integer (1-3999)."
            self.result = ""
            return
        num = int(text)
        if not (1 <= num <= 3999):
            self.error = "Number out of range (1-3999)."
            self.result = ""
            return
        self.result = int_to_roman(num)

    def convert_to_int(self):
        self.error = ""
        text = self.input_box.get_text().upper()
        if not text:
            self.error = "Input cannot be empty."
            self.result = ""
            return
        num = roman_to_int(text)
        if num is None:
            self.error = "Invalid Roman numeral."
            self.result = ""
            return
        self.result = str(num)

    def clear(self):
        self.input_box.clear()
        self.result = ""
        self.error = ""

    def handle_event(self, event):
        enter_pressed = self.input_box.handle_event(event)
        if self.btn_to_roman.is_clicked(event):
            self.convert_to_roman()
        elif self.btn_to_int.is_clicked(event):
            self.convert_to_int()
        elif self.btn_clear.is_clicked(event):
            self.clear()
        elif enter_pressed == "ENTER":
            text = self.input_box.get_text()
            if text.isdigit():
                self.convert_to_roman()
            else:
                self.convert_to_int()

    def draw(self, screen):
        screen.fill(WHITE)
        # Title centered top
        title_surf = TITLE_FONT.render("Roman Numeral Converter", True, BLACK)
        screen.blit(title_surf, ((WIDTH - title_surf.get_width()) // 2, 40))

        # Input label centered above input box
        input_label = FONT.render("Enter number or Roman numeral:", True, BLACK)
        screen.blit(input_label, ((WIDTH - input_label.get_width()) // 2, self.input_box.rect.y - 40))

        # Draw input box
        self.input_box.draw(screen)

        # Draw buttons stacked vertically
        self.btn_to_roman.draw(screen)
        self.btn_to_int.draw(screen)
        self.btn_clear.draw(screen)

        # Draw error or result **above** tooltips area
        message_y = self.btn_clear.rect.bottom + 10
        if self.error:
            error_surf = FONT.render(self.error, True, RED)
            screen.blit(error_surf, ((WIDTH - error_surf.get_width()) // 2, message_y))
            message_y += error_surf.get_height() + 5
        elif self.result:
            result_surf = FONT.render(f"Result: {self.result}", True, GREEN)
            screen.blit(result_surf, ((WIDTH - result_surf.get_width()) // 2, message_y))
            message_y += result_surf.get_height() + 5

        # Tooltips below the message
        tooltip_gap = 5
        tooltips = [
            "Convert integer (1-3999) to Roman numeral",
            "Convert Roman numeral to integer",
            "Clear input and result"
        ]
        for i, tip in enumerate(tooltips):
            tip_surf = SMALL_FONT.render(tip, True, GRAY)
            tip_x = (WIDTH - tip_surf.get_width()) // 2
            tip_y = message_y + i * (tip_surf.get_height() + tooltip_gap)
            screen.blit(tip_surf, (tip_x, tip_y))


def main():
    app = RomanConverterApp()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            app.handle_event(event)

        app.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
