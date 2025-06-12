import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎵 Simple Playlist Manager")

font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

playlist = []
input_text = ""
input_active = False
message = ""
message_time = 0  # For clearing message after delay

def draw_text(text, x, y, font, color=(0,0,0)):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

selected_index = -1

running = True
while running:
    screen.fill((240, 240, 255))

    draw_text("🎵 Simple Playlist Manager", 100, 10, big_font)

    # Draw playlist
    y = 60
    for i, song in enumerate(playlist):
        color = (0, 0, 180) if i == selected_index else (0, 0, 0)
        draw_text(f"{i+1}. {song}", 30, y, font, color)
        y += 30

    # Instructions
    if not input_active:
        draw_text("Press 'A' to add song, 'D' to delete selected", 30, HEIGHT - 70, font)
        if selected_index != -1:
            draw_text("Selected: " + playlist[selected_index], 30, HEIGHT - 40, font)
    else:
        draw_text("Enter song name:", 30, HEIGHT - 100, font)
        draw_text(input_text, 30, HEIGHT - 70, font)

    # Show message briefly
    if message and time.time() - message_time < 3:  # Show message for 3 seconds
        draw_text(message, 30, HEIGHT - 40, font, (200, 0, 0))
    elif time.time() - message_time >= 3:
        message = ""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if not input_active:
                if event.key == pygame.K_a:
                    input_active = True
                    input_text = ""
                    message = ""
                elif event.key == pygame.K_d:
                    if selected_index != -1:
                        removed = playlist.pop(selected_index)
                        message = f"Removed: {removed}"
                        message_time = time.time()
                        # Adjust selected index after removal
                        if selected_index >= len(playlist):
                            selected_index = len(playlist) - 1
                    else:
                        message = "No song selected!"
                        message_time = time.time()
                elif event.key == pygame.K_UP:
                    if len(playlist) > 0:
                        if selected_index == -1:
                            selected_index = 0
                        else:
                            selected_index = (selected_index - 1) % len(playlist)  # Wrap around
                elif event.key == pygame.K_DOWN:
                    if len(playlist) > 0:
                        if selected_index == -1:
                            selected_index = 0
                        else:
                            selected_index = (selected_index + 1) % len(playlist)  # Wrap around
            else:
                if event.key == pygame.K_RETURN:
                    if input_text.strip():
                        song_name = input_text.strip()
                        if song_name in playlist:
                            message = "Song already in playlist!"
                        else:
                            playlist.append(song_name)
                            message = f"Added: {song_name}"
                        message_time = time.time()
                        input_active = False
                    else:
                        message = "Song name cannot be empty!"
                        message_time = time.time()
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
