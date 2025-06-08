import pygame
import sys
import random
import math
import numpy as np

pygame.init()
FONT = pygame.font.SysFont(None, 28)
SMALL_FONT = pygame.font.SysFont(None, 22)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gradient Background Generator with Blur")

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
TEXT_COLOR = pygame.Color('white')
BG_COLOR = (30, 30, 30)

clock = pygame.time.Clock()

def lerp(color1, color2, t):
    # Linear interpolation between two colors
    return (
        int(color1[0] + (color2[0] - color1[0]) * t),
        int(color1[1] + (color2[1] - color1[1]) * t),
        int(color1[2] + (color2[2] - color1[2]) * t),
    )

def blur_surface(surface, radius=5):
    # Simple box blur using numpy for given radius
    arr = pygame.surfarray.array3d(surface).astype(np.float32)
    kernel_size = radius * 2 + 1
    padded = np.pad(arr, ((radius, radius), (radius, radius), (0,0)), mode='edge')
    blurred = np.zeros_like(arr)
    for y in range(arr.shape[1]):
        for x in range(arr.shape[0]):
            region = padded[x:x+kernel_size, y:y+kernel_size]
            blurred[x,y] = region.mean(axis=(0,1))
    blurred = blurred.astype(np.uint8)
    return pygame.surfarray.make_surface(blurred)

class InputBox:
    # Class for input text box
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        # Handle mouse and keyboard events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.color = COLOR_INACTIVE
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 10:
                        self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, TEXT_COLOR)

    def update(self):
        # Adjust width to fit text
        width = max(100, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Draw box and text
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

def generate_colors(n):
    # Generate list of n random RGB colors
    colors = []
    for _ in range(n):
        colors.append((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    return colors

def create_multi_gradient(width, height, colors, angle_deg):
    # Create a gradient surface with multiple colors and given angle
    angle = math.radians(angle_deg)
    surface = pygame.Surface((width, height))
    dx = math.cos(angle)
    dy = math.sin(angle)

    # Calculate min and max projections to normalize interpolation
    projections = []
    for x in [0, width]:
        for y in [0, height]:
            projections.append(x*dx + y*dy)
    p_min = min(projections)
    p_max = max(projections)
    p_range = p_max - p_min if p_max != p_min else 1

    arr = np.zeros((width, height, 3), dtype=np.uint8)
    segment_len = 1 / (len(colors) - 1)

    for x in range(width):
        for y in range(height):
            p = (x*dx + y*dy - p_min) / p_range
            segment_index = min(int(p / segment_len), len(colors) - 2)
            local_t = (p - segment_index*segment_len) / segment_len
            c1 = colors[segment_index]
            c2 = colors[segment_index+1]
            arr[x,y] = lerp(c1, c2, local_t)

    return pygame.surfarray.make_surface(arr)

def draw_text(surface, text, pos, font=FONT, color=TEXT_COLOR):
    # Draw text on surface at given position
    txt_surf = font.render(text, True, color)
    surface.blit(txt_surf, pos)

def main():
    input_boxes = []
    input_width = 140
    input_height = 32
    margin_y = 50
    start_y = 60  # Start y shifted down to make room for labels
    start_x = 100
    
    # Labels for inputs placed above input boxes
    labels = ['Width (px)', 'Height (px)', 'Number of Colors (2-10)', 'Angle (0-360°)']

    # Default values for inputs
    defaults = ['800', '600', '3', '45']

    # Create input boxes
    for i, default in enumerate(defaults):
        input_boxes.append(InputBox(start_x, start_y + i*(input_height+margin_y), input_width, input_height, default))

    button_rect = pygame.Rect(250, start_y + 4*(input_height+margin_y) + 10, 140, 40)

    generated_surface = None
    blur_radius = 8

    info_text = "Enter parameters, then click 'Generate' or press G. Press R to regenerate, S to save."

    running = True
    while running:
        screen.fill(BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle events for each input box
            for box in input_boxes:
                box.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    # On generate button click, parse input and generate gradient
                    try:
                        w = int(input_boxes[0].text)
                        h = int(input_boxes[1].text)
                        n_colors = int(input_boxes[2].text)
                        angle = float(input_boxes[3].text)
                        if w < 100 or h < 100 or n_colors < 2 or n_colors > 10 or not (0 <= angle <= 360):
                            raise ValueError
                    except:
                        print("Invalid inputs! Width and height >=100; colors 2-10; angle 0-360.")
                        continue
                    colors = generate_colors(n_colors)
                    generated_surface = create_multi_gradient(w, h, colors, angle)
                    generated_surface = blur_surface(generated_surface, blur_radius)
                    print("Gradient generated.")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    # Generate gradient using 'G' key
                    try:
                        w = int(input_boxes[0].text)
                        h = int(input_boxes[1].text)
                        n_colors = int(input_boxes[2].text)
                        angle = float(input_boxes[3].text)
                        if w < 100 or h < 100 or n_colors < 2 or n_colors > 10 or not (0 <= angle <= 360):
                            raise ValueError
                    except:
                        print("Invalid inputs! Width and height >=100; colors 2-10; angle 0-360.")
                        continue
                    colors = generate_colors(n_colors)
                    generated_surface = create_multi_gradient(w, h, colors, angle)
                    generated_surface = blur_surface(generated_surface, blur_radius)
                    print("Gradient generated.")

                if event.key == pygame.K_r:
                    # Regenerate gradient with current params using 'R' key
                    if generated_surface:
                        try:
                            w = int(input_boxes[0].text)
                            h = int(input_boxes[1].text)
                            n_colors = int(input_boxes[2].text)
                            angle = float(input_boxes[3].text)
                        except:
                            continue
                        colors = generate_colors(n_colors)
                        generated_surface = create_multi_gradient(w, h, colors, angle)
                        generated_surface = blur_surface(generated_surface, blur_radius)
                        print("Gradient regenerated.")

                if event.key == pygame.K_s:
                    # Save generated image as 'background.png' using 'S' key
                    if generated_surface:
                        try:
                            pygame.image.save(generated_surface, "background.png")
                            print("Image saved as background.png")
                        except Exception as e:
                            print("Failed to save image:", e)

        # Draw labels above each input box
        for i, label in enumerate(labels):
            label_pos = (input_boxes[i].rect.x, input_boxes[i].rect.y - 25)
            draw_text(screen, label, label_pos)

        # Update and draw input boxes
        for box in input_boxes:
            box.update()
            box.draw(screen)

        # Draw generate button
        pygame.draw.rect(screen, (70,130,180), button_rect)
        draw_text(screen, "Generate (G)", (button_rect.x + 10, button_rect.y + 7), font=FONT, color=TEXT_COLOR)

        # Draw info text at bottom
        draw_text(screen, info_text, (20, HEIGHT - 30), font=SMALL_FONT, color=(200, 200, 200))

        # If generated gradient exists, show it scaled on right half of screen
        if generated_surface:
            max_w, max_h = WIDTH//2 - 40, HEIGHT - 80
            surf_w, surf_h = generated_surface.get_size()
            scale = min(max_w / surf_w, max_h / surf_h, 1)
            disp_surf = pygame.transform.smoothscale(generated_surface, (int(surf_w*scale), int(surf_h*scale)))
            screen.blit(disp_surf, (WIDTH//2 + 20, 40))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
