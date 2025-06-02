import pygame
import sys
import datetime

pygame.init()

# Window setup
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Day Finder")

# Colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
BLUE = (0, 120, 215)
RED = (200, 0, 0)
GREEN = (0, 150, 0)

FONT = pygame.font.SysFont("arial", 28)
SMALL_FONT = pygame.font.SysFont("arial", 20)

# Input box class
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = GRAY
        self.color_active = BLUE
        self.color = self.color_inactive
        self.text = text
        self.txt_surface = FONT.render(text, True, BLACK)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state if clicked
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    pass  # Do nothing on Enter here
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 4 and event.unicode.isdigit():
                        self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, BLACK)

    def draw(self, screen):
        # Draw rect and text
        screen.fill(WHITE, self.rect)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def get_text(self):
        return self.text

# Button class
class Button:
    def __init__(self, x, y, w, h, text, color=BLUE):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.txt_surface = FONT.render(text, True, WHITE)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=6)
        screen.blit(self.txt_surface, (self.rect.centerx - self.txt_surface.get_width() // 2,
                                       self.rect.centery - self.txt_surface.get_height() // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def get_day_of_week(day, month, year):
    try:
        date = datetime.date(year, month, day)
        return date.strftime("%A")
    except Exception:
        return None

def main():
    clock = pygame.time.Clock()

    # Create input boxes for day, month, year
    box_width = 60
    box_height = 40
    spacing = 20
    start_x = (WIDTH - (box_width * 3 + spacing * 2)) // 2
    start_y = 100

    day_box = InputBox(start_x, start_y, box_width, box_height)
    month_box = InputBox(start_x + box_width + spacing, start_y, box_width, box_height)
    year_box = InputBox(start_x + 2 * (box_width + spacing), start_y, box_width + 40, box_height)

    # Button
    find_button = Button(WIDTH//2 - 70, start_y + 80, 140, 50, "Find Day")

    # Result text
    result_text = ""
    result_color = BLACK

    running = True
    while running:
        screen.fill(WHITE)

        # Draw title
        title_surface = FONT.render("Enter a date (DD MM YYYY)", True, BLACK)
        screen.blit(title_surface, (WIDTH//2 - title_surface.get_width()//2, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            day_box.handle_event(event)
            month_box.handle_event(event)
            year_box.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if find_button.is_clicked(event.pos):
                    try:
                        day = int(day_box.get_text())
                        month = int(month_box.get_text())
                        year = int(year_box.get_text())
                        day_name = get_day_of_week(day, month, year)
                        if day_name:
                            result_text = f"{day}/{month}/{year} is a {day_name}"
                            result_color = GREEN
                        else:
                            result_text = "Invalid date! Please try again."
                            result_color = RED
                    except ValueError:
                        result_text = "Please enter valid numbers!"
                        result_color = RED

        # Draw input boxes
        day_box.draw(screen)
        month_box.draw(screen)
        year_box.draw(screen)

        # Draw labels
        day_label = SMALL_FONT.render("Day", True, BLACK)
        month_label = SMALL_FONT.render("Month", True, BLACK)
        year_label = SMALL_FONT.render("Year", True, BLACK)
        screen.blit(day_label, (day_box.rect.centerx - day_label.get_width() // 2, day_box.rect.y - 25))
        screen.blit(month_label, (month_box.rect.centerx - month_label.get_width() // 2, month_box.rect.y - 25))
        screen.blit(year_label, (year_box.rect.centerx - year_label.get_width() // 2, year_box.rect.y - 25))

        # Draw button
        find_button.draw(screen)

        # Draw result
        if result_text:
            result_surface = FONT.render(result_text, True, result_color)
            screen.blit(result_surface, (WIDTH//2 - result_surface.get_width()//2, HEIGHT - 80))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
