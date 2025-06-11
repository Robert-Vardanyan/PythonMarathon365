import pygame
import sys
import requests
import pyttsx3

pygame.init()
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("📚 Dictionary with Auto Add via API & TTS")
font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

# --- Initial dictionary with definitions ---
dictionary = {
    "python": "A high-level programming language.",
    "pygame": "A library for making games in Python.",
    "function": "A block of code that performs a task.",
    "variable": "A name that stores a value.",
    "loop": "A way to repeat a block of code."
}

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

user_input = ""
definition = ""
translation = ""
not_found = False
loading_translation = False
message = ""  # For status messages

def draw_interface():
    screen.fill((245, 245, 245))
    title = font.render("📘 Type a word:", True, (0, 0, 0))
    screen.blit(title, (20, 20))

    input_box = pygame.Rect(20, 60, 560, 40)
    pygame.draw.rect(screen, (255, 255, 255), input_box)
    pygame.draw.rect(screen, (0, 0, 0), input_box, 2)

    input_text = font.render(user_input, True, (0, 0, 0))
    screen.blit(input_text, (30, 65))

    y = 130
    if definition:
        def_title = font.render("🧠 Definition:", True, (0, 0, 0))
        screen.blit(def_title, (20, y))
        y += 40

        wrapped_text = wrap_text(definition, font, 560)
        for i, line in enumerate(wrapped_text):
            screen.blit(font.render(line, True, (0, 0, 0)), (20, y + i * 30))
        y += len(wrapped_text)*30 + 10

    if translation:
        trans_title = font.render("🌐 Translation (Russian):", True, (0, 0, 0))
        screen.blit(trans_title, (20, y))
        y += 40

        wrapped_trans = wrap_text(translation, font, 560)
        for i, line in enumerate(wrapped_trans):
            screen.blit(font.render(line, True, (0, 0, 0)), (20, y + i * 30))
        y += len(wrapped_trans)*30 + 10

    if loading_translation:
        loading_text = font.render("⏳ Loading...", True, (100, 100, 100))
        screen.blit(loading_text, (20, y))
        y += 40

    if not_found:
        error_text = font.render("❌ Word not found.", True, (200, 0, 0))
        screen.blit(error_text, (20, y))
        y += 40

    if message:
        msg_text = small_font.render(message, True, (0, 100, 0))
        screen.blit(msg_text, (20, HEIGHT - 60))

    hint = small_font.render("Enter - Search & Add | ESC - Clear | S - Speak", True, (100, 100, 100))
    screen.blit(hint, (20, HEIGHT - 30))

def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current = ""
    for word in words:
        test_line = current + word + " "
        if font.size(test_line)[0] <= max_width:
            current = test_line
        else:
            lines.append(current)
            current = word + " "
    lines.append(current)
    return lines

def translate_text(text, source="en", target="ru"):
    try:
        url = "https://libretranslate.com/translate"
        payload = {
            "q": text,
            "source": source,
            "target": target,
            "format": "text"
        }
        response = requests.post(url, data=payload, timeout=5)
        if response.status_code == 200:
            result = response.json()
            return result.get("translatedText", "")
        else:
            return ""
    except Exception:
        return ""

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                key = user_input.strip().lower()
                if not key:
                    continue

                if key in dictionary:
                    definition = dictionary[key]
                    not_found = False
                    message = f"Word '{key}' found in local dictionary."
                    translation = translate_text(key)
                else:
                    loading_translation = True
                    message = "Word not found locally. Querying API..."
                    pygame.display.flip()

                    # Получаем перевод
                    translation = translate_text(key)
                    if translation:
                        definition = f"[Auto-added] Translation: {translation}"
                        dictionary[key] = definition
                        not_found = False
                        message = f"Word '{key}' added to dictionary."
                    else:
                        definition = ""
                        not_found = True
                        message = f"Word '{key}' not found via API."

                    loading_translation = False

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_ESCAPE:
                user_input = ""
                definition = ""
                translation = ""
                not_found = False
                message = ""
            elif event.key == pygame.K_s:
                if definition:
                    speak_text(definition)
                elif translation:
                    speak_text(translation)
            else:
                if len(user_input) < 30 and event.unicode.isprintable():
                    user_input += event.unicode

    draw_interface()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
