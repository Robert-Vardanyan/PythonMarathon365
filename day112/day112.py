import pygame
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os
import random

# --- Init ---
pygame.init()
WIDTH, HEIGHT = 1000, 700
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Photo Collage Generator")
font = pygame.font.SysFont(None, 32)

# --- Hidden Tk root for file dialogs ---
root = tk.Tk()
root.withdraw()

# --- Globals ---
image_paths = []
original_order = []
collage_surface = None
cols, rows = 3, 2
margin = 10
border_color = BLACK
border_width = 4


def select_images():
    global image_paths, original_order
    files = filedialog.askopenfilenames(filetypes=[("Images", "*.png *.jpg *.jpeg")])
    image_paths = list(files)
    original_order = list(image_paths)


def save_collage(surface):
    if surface:
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if path:
            pygame.image.save(surface, path)
            print("Collage saved to:", path)


def create_collage(image_paths, cols, rows, margin, border_width=0, border_color=BLACK):
    collage = pygame.Surface((WIDTH, HEIGHT))
    collage.fill(WHITE)

    cell_width = (WIDTH - (cols + 1) * margin) // cols
    cell_height = (HEIGHT - (rows + 1) * margin) // rows

    for index, path in enumerate(image_paths[:cols * rows]):
        try:
            pil_img = Image.open(path)
            pil_img.thumbnail((cell_width - 2 * border_width, cell_height - 2 * border_width))
            img = pygame.image.fromstring(pil_img.tobytes(), pil_img.size, pil_img.mode)

            x = margin + (index % cols) * (cell_width + margin)
            y = margin + (index // cols) * (cell_height + margin)

            # Draw border
            border_rect = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(collage, border_color, border_rect)

            # Center image inside cell
            img_rect = img.get_rect(center=border_rect.center)
            collage.blit(img, img_rect.topleft)
        except Exception as e:
            print(f"Error loading {path}: {e}")

    return collage


def draw_button(text, rect, active=False):
    color = (0, 150, 200) if not active else (0, 200, 255)
    pygame.draw.rect(screen, color, rect, border_radius=8)
    label = font.render(text, True, WHITE)
    screen.blit(label, (rect.centerx - label.get_width() // 2, rect.centery - label.get_height() // 2))


def main():
    global collage_surface, image_paths

    # Buttons
    btn_generate = pygame.Rect(30, HEIGHT - 60, 170, 40)
    btn_save = pygame.Rect(220, HEIGHT - 60, 130, 40)
    btn_shuffle = pygame.Rect(370, HEIGHT - 60, 120, 40)
    btn_reset = pygame.Rect(510, HEIGHT - 60, 100, 40)
    btn_load = pygame.Rect(630, HEIGHT - 60, 140, 40)

    running = True
    while running:
        screen.fill(GRAY)

        if collage_surface:
            screen.blit(collage_surface, (0, 0))

        draw_button("Generate Collage", btn_generate)
        draw_button("Save", btn_save)
        draw_button("Shuffle", btn_shuffle)
        draw_button("Reset", btn_reset)
        draw_button("Load Images", btn_load)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_generate.collidepoint(event.pos):
                    if image_paths:
                        collage_surface = create_collage(image_paths, cols, rows, margin, border_width, border_color)
                elif btn_save.collidepoint(event.pos):
                    save_collage(collage_surface)
                elif btn_shuffle.collidepoint(event.pos):
                    random.shuffle(image_paths)
                    collage_surface = create_collage(image_paths, cols, rows, margin, border_width, border_color)
                elif btn_reset.collidepoint(event.pos):
                    image_paths = list(original_order)
                    collage_surface = create_collage(image_paths, cols, rows, margin, border_width, border_color)
                elif btn_load.collidepoint(event.pos):
                    select_images()
                    collage_surface = create_collage(image_paths, cols, rows, margin, border_width, border_color)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
