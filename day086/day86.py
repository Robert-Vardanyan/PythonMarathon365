import pygame
import random
from datetime import datetime

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Chatbot")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (230, 230, 230)
BLUE = (100, 149, 237)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
YELLOW = (255, 215, 0)

FONT = pygame.font.SysFont("arial", 20)
FONT_SMALL = pygame.font.SysFont("arial", 16)

input_box = pygame.Rect(10, HEIGHT - 40, WIDTH - 20, 30)
color_inactive = LIGHT_GRAY
color_active = BLUE
color = color_inactive

active = False
user_text = ""
chat_log = []

def draw_text(surface, text, color, rect, font, aa=True, bkg=None):
    y = rect.top
    line_spacing = -2

    # get the height of the font
    font_height = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + font_height > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], aa, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += font_height + line_spacing

        # remove the text we just blitted
        text = text[i:]

def simple_bot_response(user_msg):
    msg = user_msg.lower()

    if "hello" in msg or "hi" in msg:
        responses = [
            ("Hello! How can I assist you today?", GREEN),
            ("Hi there! What can I do for you?", BLUE),
            ("Hey! How's it going?", YELLOW)
        ]
        return random.choice(responses)

    elif "how are you" in msg:
        responses = [
            ("I'm just a bot, but I'm doing great! Thanks for asking.", GREEN),
            ("Feeling good, thanks! How about you?", BLUE),
            ("All systems operational!", YELLOW)
        ]
        return random.choice(responses)

    elif "help" in msg:
        responses = [
            ("Sure! You can ask me anything or just chat with me.", GREEN),
            ("I'm here to help! What do you need?", BLUE),
            ("Feel free to ask me any questions.", YELLOW)
        ]
        return random.choice(responses)

    elif "time" in msg:
        return (f"The current time is {datetime.now().strftime('%H:%M')}.", GREEN)

    elif "name" in msg:
        responses = [
            ("I'm your friendly Pygame chatbot.", GREEN),
            ("You can call me ChatBot!", BLUE),
            ("I'm your digital assistant.", YELLOW)
        ]
        return random.choice(responses)

    elif "bye" in msg or "exit" in msg or "quit" in msg:
        responses = [
            ("Goodbye! Have a nice day.", RED),
            ("See you later!", RED),
            ("Take care!", RED)
        ]
        return random.choice(responses)

    else:
        responses = [
            ("That's interesting! Tell me more.", BLUE),
            ("Hmm, I see...", GREEN),
            ("Can you explain that a bit more?", YELLOW),
            ("I’m not sure I understand, but I’m here to listen.", BLUE)
        ]
        return random.choice(responses)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    # Draw chat log
    y_offset = 10
    for text, color_text in chat_log[-15:]:
        draw_text(screen, text, color_text, pygame.Rect(10, y_offset, WIDTH-20, 25), FONT)
        y_offset += 30

    # Draw input box
    pygame.draw.rect(screen, color, input_box, 2)

    # Render user input text
    txt_surface = FONT.render(user_text, True, BLACK)
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                active = True
                color = color_active
            else:
                active = False
                color = color_inactive

        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    if user_text.strip() != "":
                        # Add user text to chat log
                        chat_log.append((f"You: {user_text}", BLACK))
                        # Get bot response
                        response, resp_color = simple_bot_response(user_text)
                        chat_log.append(("Bot: " + response, resp_color))
                        user_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
