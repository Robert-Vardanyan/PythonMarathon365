import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Element Symbol Quiz")

FONT = pygame.font.SysFont(None, 40)
SMALL_FONT = pygame.font.SysFont(None, 30)

# Element data: element name -> symbol
elements = {
    "Hydrogen": "H",
    "Oxygen": "O",
    "Carbon": "C",
    "Nitrogen": "N",
    "Sodium": "Na",
    "Chlorine": "Cl",
    "Iron": "Fe",
    "Gold": "Au",
    "Silver": "Ag",
    "Calcium": "Ca",
}

element_list = list(elements.keys())
index = 0

input_text = ""
message = ""
message_color = (0, 0, 0)

correct_count = 0
wrong_count = 0
quiz_finished = False

def draw_text(text, font, color, surface, x, y):
    txt_obj = font.render(text, True, color)
    txt_rect = txt_obj.get_rect(center=(x, y))
    surface.blit(txt_obj, txt_rect)

def next_element():
    global index, input_text, message
    index += 1
    input_text = ""
    message = ""

clock = pygame.time.Clock()

while True:
    screen.fill((240, 240, 240))

    if not quiz_finished:
        draw_text("Element Symbol Quiz", FONT, (0, 0, 0), screen, WIDTH//2, 40)

        if index < len(element_list):
            draw_text(f"Element: {element_list[index]}", FONT, (0, 0, 255), screen, WIDTH//2, 100)

            input_box = pygame.Rect(WIDTH//2 - 150, 150, 300, 50)
            pygame.draw.rect(screen, (255, 255, 255), input_box)
            pygame.draw.rect(screen, (0, 0, 0), input_box, 2)

            txt_surface = FONT.render(input_text, True, (0, 0, 0))
            screen.blit(txt_surface, (input_box.x + 10, input_box.y + 10))

            draw_text(message, FONT, message_color, screen, WIDTH//2, 230)
            draw_text("Type symbol and press ENTER", SMALL_FONT, (50, 50, 50), screen, WIDTH//2, 280)
            draw_text("Backspace to delete", SMALL_FONT, (50, 50, 50), screen, WIDTH//2, 310)

        else:
            # All questions done
            quiz_finished = True

    else:
        # Show results screen
        total = correct_count + wrong_count
        accuracy = (correct_count / total) * 100 if total > 0 else 0
        draw_text("🎉 Congratulations! 🎉", FONT, (0, 150, 0), screen, WIDTH//2, 80)
        draw_text(f"Quiz Completed!", FONT, (0, 0, 0), screen, WIDTH//2, 140)
        draw_text(f"Correct Answers: {correct_count}", FONT, (0, 150, 0), screen, WIDTH//2, 200)
        draw_text(f"Wrong Answers: {wrong_count}", FONT, (200, 0, 0), screen, WIDTH//2, 250)
        draw_text(f"Accuracy: {accuracy:.2f}%", FONT, (0, 0, 255), screen, WIDTH//2, 300)
        draw_text("Press ESC to quit", SMALL_FONT, (100, 100, 100), screen, WIDTH//2, 350)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if quiz_finished:
                # Quit on ESC when quiz finished
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            else:
                if event.key == pygame.K_RETURN:
                    if index < len(element_list):
                        answer = elements[element_list[index]].lower()
                        guess = input_text.lower().strip()
                        if guess == answer:
                            message = "Correct! 🎉"
                            message_color = (0, 150, 0)
                            correct_count += 1
                        else:
                            message = f"Wrong! Correct symbol: {elements[element_list[index]]}"
                            message_color = (200, 0, 0)
                            wrong_count += 1
                        pygame.time.set_timer(pygame.USEREVENT + 1, 2000)  # Show message 2 sec

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                else:
                    if event.unicode.isalpha():
                        input_text += event.unicode

        elif event.type == pygame.USEREVENT + 1:
            next_element()
            pygame.time.set_timer(pygame.USEREVENT + 1, 0)
            message = ""

    pygame.display.flip()
    clock.tick(30)
