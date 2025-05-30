import pygame
import sys
import calendar
from datetime import datetime

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("📅 Calendar Viewer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
RED = (220, 20, 60)
GREEN = (34, 139, 34)

# Fonts
font_title = pygame.font.SysFont("Arial", 36)
font_days = pygame.font.SysFont("Arial", 24)
font_dates = pygame.font.SysFont("Arial", 28)

# Initial month and year (current)
current_year = datetime.now().year
current_month = datetime.now().month
today = datetime.now().day
today_month = current_month
today_year = current_year

# Button class for Prev and Next
class Button:
    def __init__(self, rect, color, text):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.text = text
        self.text_surf = font_days.render(text, True, BLACK)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surf, self.text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def draw_calendar(year, month):
    screen.fill(WHITE)
    
    # Draw title with month and year
    month_name = calendar.month_name[month]
    title_text = f"{month_name} {year}"
    title_surf = font_title.render(title_text, True, BLACK)
    title_rect = title_surf.get_rect(center=(WIDTH // 2, 40))
    screen.blit(title_surf, title_rect)

    # Draw day names
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    start_x = 50
    start_y = 100
    cell_width = 90
    cell_height = 50

    for i, day in enumerate(days):
        # Weekend days color
        color = RED if i >= 5 else BLACK
        day_surf = font_days.render(day, True, color)
        day_rect = day_surf.get_rect(center=(start_x + i * cell_width + cell_width // 2, start_y))
        screen.blit(day_surf, day_rect)

    # Draw dates
    cal = calendar.Calendar(firstweekday=0)  # Monday is 0
    month_days = list(cal.itermonthdays(year, month))
    
    row = 0
    col = 0
    for day in month_days:
        if day == 0:
            col += 1
            if col > 6:
                col = 0
                row += 1
            continue
        x = start_x + col * cell_width + cell_width // 2
        y = start_y + 40 + row * cell_height + cell_height // 2

        # Weekend day color
        color = RED if col >= 5 else BLACK

        day_text = str(day)
        day_surf = font_dates.render(day_text, True, color)
        day_rect = day_surf.get_rect(center=(x, y))

        # If this day is today, draw circle behind it
        if (day == today and month == today_month and year == today_year):
            radius = 20
            pygame.draw.circle(screen, GREEN, (x, y), radius)
            day_surf = font_dates.render(day_text, True, WHITE)
            day_rect = day_surf.get_rect(center=(x, y))

        screen.blit(day_surf, day_rect)

        col += 1
        if col > 6:
            col = 0
            row += 1

# Create buttons
button_prev = Button((100, 520, 100, 40), LIGHT_BLUE, "< Prev")
button_next = Button((500, 520, 100, 40), LIGHT_BLUE, "Next >")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if button_prev.is_clicked(pos):
                current_month -= 1
                if current_month < 1:
                    current_month = 12
                    current_year -= 1
            elif button_next.is_clicked(pos):
                current_month += 1
                if current_month > 12:
                    current_month = 1
                    current_year += 1

    draw_calendar(current_year, current_month)
    button_prev.draw(screen)
    button_next.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
