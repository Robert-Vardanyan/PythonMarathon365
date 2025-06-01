import pygame
import sys

pygame.init()

# Screen setup - bigger window
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Expense Splitter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
LIGHT_GRAY = (220, 220, 220)
LIGHT_BLUE = (173, 216, 230)
GREEN = (50, 180, 50)
RED = (180, 50, 50)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER = (100, 149, 237)
INPUT_ACTIVE = (255, 255, 180)
INPUT_INACTIVE = (240, 240, 240)

FONT = pygame.font.SysFont("arial", 22)
SMALL_FONT = pygame.font.SysFont("arial", 16)
TITLE_FONT = pygame.font.SysFont("arial", 36, bold=True)

clock = pygame.time.Clock()

class Button:
    def __init__(self, text, x, y, w, h, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = hover_color

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        text_surf = FONT.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = INPUT_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, BLACK)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = INPUT_ACTIVE if self.active else INPUT_INACTIVE

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
                self.color = INPUT_INACTIVE
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if len(self.text) < 30:
                    self.text += event.unicode
            self.txt_surface = FONT.render(self.text, True, BLACK)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.txt_surface, (self.rect.x + 7, self.rect.y + 5))
        pygame.draw.rect(surface, BLACK, self.rect, 2)

    def get_text(self):
        return self.text.strip()

class ExpenseSplitter:
    def __init__(self):
        self.participants = []
        self.expenses = []

        # Inputs
        self.participant_input = InputBox(220, 80, 250, 35)

        self.desc_input = InputBox(220, 160, 350, 35)
        self.amount_input = InputBox(220, 220, 150, 35)
        self.paid_by_input = InputBox(220, 280, 200, 35)
        self.shared_by_input = InputBox(220, 340, 350, 35)

        # Buttons
        self.add_participant_btn = Button("Add Participant", 500, 80, 180, 35, BUTTON_COLOR, BUTTON_HOVER)
        self.add_expense_btn = Button("Add Expense", 600, 340, 180, 40, BUTTON_COLOR, BUTTON_HOVER)
        self.calculate_btn = Button("Calculate Splits", 600, 400, 180, 40, BUTTON_COLOR, BUTTON_HOVER)
        self.clear_btn = Button("Clear All", 600, 460, 180, 40, RED, (255, 80, 80))

        self.result = ""

    def add_participant(self):
        name = self.participant_input.get_text()
        if name and name not in self.participants:
            self.participants.append(name)
            self.participant_input.text = ""
            self.participant_input.txt_surface = FONT.render('', True, BLACK)
            self.result = f"Participant '{name}' added."
        else:
            self.result = "Enter a unique participant name."

    def add_expense(self):
        desc = self.desc_input.get_text()
        amount_text = self.amount_input.get_text()
        paid_by = self.paid_by_input.get_text()
        shared_by = self.shared_by_input.get_text()

        if not desc or not amount_text or not paid_by or not shared_by:
            self.result = "Fill all expense fields."
            return
        try:
            amount = float(amount_text)
            if amount <= 0:
                self.result = "Amount must be positive."
                return
        except ValueError:
            self.result = "Amount must be a number."
            return

        if paid_by not in self.participants:
            self.result = f"Payer '{paid_by}' not found."
            return

        shared_list = [p.strip() for p in shared_by.split(',')]
        if not shared_list:
            self.result = "Shared by cannot be empty."
            return
        for p in shared_list:
            if p not in self.participants:
                self.result = f"Participant '{p}' not found."
                return

        self.expenses.append({
            'description': desc,
            'amount': amount,
            'paid_by': paid_by,
            'shared_by': shared_list
        })

        # Clear expense inputs
        self.desc_input.text = ""
        self.desc_input.txt_surface = FONT.render('', True, BLACK)
        self.amount_input.text = ""
        self.amount_input.txt_surface = FONT.render('', True, BLACK)
        self.paid_by_input.text = ""
        self.paid_by_input.txt_surface = FONT.render('', True, BLACK)
        self.shared_by_input.text = ""
        self.shared_by_input.txt_surface = FONT.render('', True, BLACK)

        self.result = "Expense added."

    def calculate_splits(self):
        balances = {p: 0 for p in self.participants}
        for exp in self.expenses:
            amount = exp['amount']
            paid_by = exp['paid_by']
            shared_by = exp['shared_by']
            split_amount = amount / len(shared_by)
            balances[paid_by] += amount
            for p in shared_by:
                balances[p] -= split_amount

        lines = []
        for p, bal in balances.items():
            if bal > 0:
                lines.append(f"{p} should receive ${bal:.2f}")
            elif bal < 0:
                lines.append(f"{p} owes ${-bal:.2f}")
            else:
                lines.append(f"{p} is settled up")

        self.result = "\n".join(lines) if lines else "No data to calculate."

    def clear_all(self):
        self.participants.clear()
        self.expenses.clear()
        self.result = ""

    def handle_event(self, event):
        self.participant_input.handle_event(event)
        self.desc_input.handle_event(event)
        self.amount_input.handle_event(event)
        self.paid_by_input.handle_event(event)
        self.shared_by_input.handle_event(event)

        if self.add_participant_btn.is_clicked(event):
            self.add_participant()

        if self.add_expense_btn.is_clicked(event):
            self.add_expense()

        if self.calculate_btn.is_clicked(event):
            self.calculate_splits()

        if self.clear_btn.is_clicked(event):
            self.clear_all()

    def draw(self, surface):
        surface.fill(WHITE)

        # Title
        title_surf = TITLE_FONT.render("Expense Splitter", True, BLACK)
        title_rect = title_surf.get_rect(center=(WIDTH//2, 40))
        surface.blit(title_surf, title_rect)

        # Participants input and hint
        surface.blit(FONT.render("Participant Name:", True, BLACK), (40, 85))
        self.participant_input.draw(surface)
        self.add_participant_btn.draw(surface)
        surface.blit(SMALL_FONT.render("Enter participant's unique name", True, GRAY), (220, 115))

        # Expense inputs and hints
        surface.blit(FONT.render("Expense Description:", True, BLACK), (40, 165))
        self.desc_input.draw(surface)
        surface.blit(SMALL_FONT.render("Brief description of expense", True, GRAY), (220, 195))

        surface.blit(FONT.render("Amount ($):", True, BLACK), (40, 225))
        self.amount_input.draw(surface)
        surface.blit(SMALL_FONT.render("Enter amount (numbers only)", True, GRAY), (220, 255))

        surface.blit(FONT.render("Paid By (name):", True, BLACK), (40, 285))
        self.paid_by_input.draw(surface)
        surface.blit(SMALL_FONT.render("Who paid? Must be participant", True, GRAY), (220, 315))

        surface.blit(FONT.render("Shared By (comma-separated):", True, BLACK), (40, 345))
        self.shared_by_input.draw(surface)
        surface.blit(SMALL_FONT.render("Who shares this expense? Must be participants", True, GRAY), (220, 375))

        # Buttons
        self.add_expense_btn.draw(surface)
        self.calculate_btn.draw(surface)
        self.clear_btn.draw(surface)

        # Participants list
        surface.blit(FONT.render("Participants:", True, BLACK), (40, 420))
        for i, p in enumerate(self.participants):
            surface.blit(FONT.render(f"- {p}", True, BLACK), (60, 450 + i*25))

        # Expenses list
        surface.blit(FONT.render("Expenses (last 8):", True, BLACK), (400, 420))
        for i, exp in enumerate(self.expenses[-8:]):  # show last 8 expenses
            exp_text = f"{exp['description']}: ${exp['amount']:.2f}, paid by {exp['paid_by']}, shared by {', '.join(exp['shared_by'])}"
            surface.blit(FONT.render(exp_text, True, BLACK), (410, 450 + i*25))

        # Result box
        pygame.draw.rect(surface, LIGHT_GRAY, (20, HEIGHT - 120, WIDTH - 40, 100))
        result_lines = self.result.split('\n')
        for i, line in enumerate(result_lines):
            surface.blit(FONT.render(line, True, BLACK), (30, HEIGHT - 110 + i*25))


def main():
    splitter = ExpenseSplitter()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            splitter.handle_event(event)

        splitter.draw(screen)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
