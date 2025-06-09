import pygame
from collections import deque

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 20, 20
CELL_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()

# Maze grid (0 = path, 1 = wall)
maze = [[0]*COLS for _ in range(ROWS)]

# Add random walls
import random
for y in range(ROWS):
    for x in range(COLS):
        if random.random() < 0.25:
            maze[y][x] = 1

# Start and end
start = (0, 0)
end = (ROWS-1, COLS-1)
maze[start[0]][start[1]] = 0
maze[end[0]][end[1]] = 0

def draw_maze(path=set(), visited=set()):
    screen.fill(WHITE)
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if (y, x) == start:
                pygame.draw.rect(screen, GREEN, rect)
            elif (y, x) == end:
                pygame.draw.rect(screen, RED, rect)
            elif (y, x) in path:
                pygame.draw.rect(screen, YELLOW, rect)
            elif (y, x) in visited:
                pygame.draw.rect(screen, BLUE, rect)
            elif maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, GRAY, rect, 1)
    pygame.display.update()

def bfs(start, end):
    queue = deque([start])
    visited = set([start])
    parent = {}
    
    while queue:
        current = queue.popleft()

        draw_maze(path=set(), visited=visited)
        pygame.time.delay(20)
        
        if current == end:
            break
        
        y, x = current
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < ROWS and 0 <= nx < COLS:
                if maze[ny][nx] == 0 and (ny, nx) not in visited:
                    queue.append((ny, nx))
                    visited.add((ny, nx))
                    parent[(ny, nx)] = (y, x)
    
    # Reconstruct path
    path = []
    node = end
    while node != start:
        path.append(node)
        node = parent.get(node)
        if node is None:
            return []
    path.append(start)
    path.reverse()
    return path

# Main loop
solved = False
running = True
path = []

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not solved:
                path = bfs(start, end)
                solved = True

    if solved:
        draw_maze(path=set(path))
    else:
        draw_maze()

pygame.quit()
