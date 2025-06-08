import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Trivia App")

FONT = pygame.font.SysFont(None, 28)
BIG_FONT = pygame.font.SysFont(None, 40)
SMALL_FONT = pygame.font.SysFont(None, 24)

BG_COLOR = (30, 30, 30)
TEXT_COLOR = (230, 230, 230)
BUTTON_COLOR = (70, 70, 150)
BUTTON_HOVER = (100, 100, 200)

clock = pygame.time.Clock()

# Trivia data with categories
trivia_data = {
    "Science": [
        {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": 1},
        {"question": "Water's chemical formula?", "options": ["H2O", "CO2", "O2", "NaCl"], "answer": 0},
    ],
    "History": [
        {"question": "Who was the first president of the USA?", "options": ["Lincoln", "Washington", "Jefferson", "Adams"], "answer": 1},
        {"question": "Year WW2 ended?", "options": ["1945", "1939", "1918", "1960"], "answer": 0},
    ],
    "Math": [
        {"question": "What is 7 * 8?", "options": ["54", "56", "64", "58"], "answer": 1},
        {"question": "Square root of 81?", "options": ["9", "8", "7", "10"], "answer": 0},
    ],
}

# Button helper class
class Button:
    def __init__(self, rect, text):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = BUTTON_COLOR

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=8)
        txt_surf = FONT.render(self.text, True, TEXT_COLOR)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

def draw_text(surface, text, pos, font=FONT, color=TEXT_COLOR):
    lines = text.split('\n')
    y_offset = 0
    for line in lines:
        txt_surf = font.render(line, True, color)
        surface.blit(txt_surf, (pos[0], pos[1] + y_offset))
        y_offset += txt_surf.get_height() + 5

def main():
    state = "category"  # states: category, question, result
    selected_category = None
    question_index = 0
    score = 0
    selected_option = None

    # Create category buttons dynamically
    categories = list(trivia_data.keys())
    cat_buttons = []
    button_width = 150
    button_height = 50
    gap = 20
    total_width = len(categories) * button_width + (len(categories) - 1) * gap
    start_x = (WIDTH - total_width) // 2
    y_pos = HEIGHT // 2 - button_height // 2
    for i, cat in enumerate(categories):
        rect = (start_x + i * (button_width + gap), y_pos, button_width, button_height)
        cat_buttons.append(Button(rect, cat))

    option_buttons = []

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if state == "category":
                    for btn in cat_buttons:
                        if btn.is_hovered(mouse_pos):
                            selected_category = btn.text
                            question_index = 0
                            score = 0
                            state = "question"
                            selected_option = None
                            option_buttons.clear()
                            # Setup option buttons
                            q = trivia_data[selected_category][question_index]
                            opt_width = 500
                            opt_height = 40
                            opt_start_x = (WIDTH - opt_width) // 2
                            opt_start_y = HEIGHT // 2
                            gap_opt = 15
                            for i, opt in enumerate(q["options"]):
                                rect = (opt_start_x, opt_start_y + i*(opt_height+gap_opt), opt_width, opt_height)
                                option_buttons.append(Button(rect, opt))

                elif state == "question":
                    for i, btn in enumerate(option_buttons):
                        if btn.is_hovered(mouse_pos):
                            selected_option = i

                elif state == "result":
                    # Restart quiz on click
                    state = "category"
                    selected_category = None
                    question_index = 0
                    score = 0
                    selected_option = None
                    option_buttons.clear()

            elif event.type == pygame.KEYDOWN:
                if state == "question" and selected_option is not None:
                    # Check answer on Enter key
                    if event.key == pygame.K_RETURN:
                        correct = trivia_data[selected_category][question_index]["answer"]
                        if selected_option == correct:
                            score += 1
                        question_index += 1
                        selected_option = None
                        option_buttons.clear()
                        if question_index >= len(trivia_data[selected_category]):
                            state = "result"
                        else:
                            # Setup next question option buttons
                            q = trivia_data[selected_category][question_index]
                            opt_width = 500
                            opt_height = 40
                            opt_start_x = (WIDTH - opt_width) // 2
                            opt_start_y = HEIGHT // 2
                            gap_opt = 15
                            for i, opt in enumerate(q["options"]):
                                rect = (opt_start_x, opt_start_y + i*(opt_height+gap_opt), opt_width, opt_height)
                                option_buttons.append(Button(rect, opt))

        # Draw UI based on state
        if state == "category":
            title = BIG_FONT.render("Select a Category", True, TEXT_COLOR)
            title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 4))
            screen.blit(title, title_rect)

            for btn in cat_buttons:
                btn.color = BUTTON_HOVER if btn.is_hovered(mouse_pos) else BUTTON_COLOR
                btn.draw(screen)

        elif state == "question":
            q = trivia_data[selected_category][question_index]
            question_text = f"Q{question_index + 1}: {q['question']}"
            draw_text(screen, question_text, (50, HEIGHT // 6), BIG_FONT)

            for i, btn in enumerate(option_buttons):
                # Highlight selected option
                if selected_option == i:
                    btn.color = (100, 180, 100)  # green highlight
                else:
                    btn.color = BUTTON_COLOR
                btn.draw(screen)

            instr_text = "Click an option and press ENTER to confirm"
            instr = SMALL_FONT.render(instr_text, True, (180, 180, 180))
            screen.blit(instr, (WIDTH//2 - instr.get_width()//2, HEIGHT - 40))

        elif state == "result":
            result_text = f"You scored {score} out of {len(trivia_data[selected_category])}!"
            draw_text(screen, result_text, (WIDTH//2 - 150, HEIGHT//2 - 40), BIG_FONT)
            replay_text = "Click anywhere to play again"
            replay = FONT.render(replay_text, True, (180, 180, 180))
            screen.blit(replay, (WIDTH//2 - replay.get_width()//2, HEIGHT//2 + 40))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
