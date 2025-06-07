import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship - Improved")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (220, 20, 60)
GRAY = (200, 200, 200)
GREEN = (50, 205, 50)
YELLOW = (255, 255, 102)
DARK_BLUE = (0, 51, 102)

font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 40)

GRID_SIZE = 10
CELL_SIZE = 35
MARGIN = 5
TOP_MARGIN = 80
LEFT_MARGIN_PLAYER = 50
LEFT_MARGIN_CPU = 550

SHIP_SIZES = [5, 4, 3, 3, 2]
SHIP_NAMES = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]

EMPTY = 0
SHIP = 1
MISS = 2
HIT = 3
SUNK = 4  # Добавим состояние для потопленных клеток (квадраты)

HORIZONTAL = 0
VERTICAL = 1

def draw_text(text, x, y, color=BLACK, font_obj=font):
    label = font_obj.render(text, True, color)
    screen.blit(label, (x, y))

def create_board():
    return [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def place_ships_randomly(board):
    ships = []
    for ship_len in SHIP_SIZES:
        placed = False
        while not placed:
            direction = random.choice([HORIZONTAL, VERTICAL])
            if direction == HORIZONTAL:
                row = random.randint(0, GRID_SIZE - 1)
                col = random.randint(0, GRID_SIZE - ship_len)
                if all(board[row][col+i] == EMPTY for i in range(ship_len)):
                    for i in range(ship_len):
                        board[row][col+i] = SHIP
                    ships.append([(row, col+i) for i in range(ship_len)])
                    placed = True
            else:
                row = random.randint(0, GRID_SIZE - ship_len)
                col = random.randint(0, GRID_SIZE - 1)
                if all(board[row+i][col] == EMPTY for i in range(ship_len)):
                    for i in range(ship_len):
                        board[row+i][col] = SHIP
                    ships.append([(row+i, col) for i in range(ship_len)])
                    placed = True
    return ships

def draw_grid(board, left, top, show_ships, hits_board=None, sunk_ships=None, mark_around_sunk=None):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = left + col * (CELL_SIZE + MARGIN)
            y = top + row * (CELL_SIZE + MARGIN)
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLUE, rect)
            
            cell = board[row][col]
            if hits_board:
                cell = hits_board[row][col]

            # Нарисуем состояния
            if cell == MISS:
                pygame.draw.circle(screen, WHITE, rect.center, CELL_SIZE // 6)
            elif cell == HIT:
                pygame.draw.circle(screen, RED, rect.center, CELL_SIZE // 3)
            elif cell == SUNK:
                pygame.draw.rect(screen, RED, rect.inflate(-8, -8))
            elif mark_around_sunk and mark_around_sunk[row][col] == MISS:
                # Белая точка вокруг потопленного корабля
                pygame.draw.circle(screen, WHITE, rect.center, CELL_SIZE // 6)
            elif show_ships and board[row][col] == SHIP:
                pygame.draw.rect(screen, DARK_BLUE, rect.inflate(-8, -8))

            pygame.draw.rect(screen, BLACK, rect, 2)

def mark_around_cells(ship_cells):
    # Возвращает список ячеек вокруг корабля (в том числе диагонали), где кораблей быть не может
    around = set()
    for (r, c) in ship_cells:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                rr, cc = r + dr, c + dc
                if 0 <= rr < GRID_SIZE and 0 <= cc < GRID_SIZE and (rr, cc) not in ship_cells:
                    around.add((rr, cc))
    return around

def update_sunk_and_marks(board, hits_board, ships):
    sunk_ships = []
    mark_around_sunk = [[None]*GRID_SIZE for _ in range(GRID_SIZE)]

    for ship in ships:
        if all(hits_board[r][c] == HIT for r,c in ship):
            sunk_ships.append(ship)
            for r,c in ship:
                hits_board[r][c] = SUNK
            # Помечаем вокруг корабля белыми точками
            around = mark_around_cells(ship)
            for rr, cc in around:
                if hits_board[rr][cc] == EMPTY:
                    mark_around_sunk[rr][cc] = MISS
    return sunk_ships, mark_around_sunk

def all_ships_sunk(ships, hits_board):
    return all(all(hits_board[r][c] in (HIT, SUNK) for r,c in ship) for ship in ships)

def get_cell_from_pos(pos, left, top):
    x, y = pos
    if x < left or y < top:
        return None
    col = (x - left) // (CELL_SIZE + MARGIN)
    row = (y - top) // (CELL_SIZE + MARGIN)
    if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:
        return row, col
    return None

def draw_labels():
    draw_text("Your Board", LEFT_MARGIN_PLAYER, TOP_MARGIN - 40, BLACK, big_font)
    draw_text("Computer Board", LEFT_MARGIN_CPU, TOP_MARGIN - 40, BLACK, big_font)
    draw_text("Click on Computer's Board to fire", WIDTH//2 - 130, 20, BLACK, font)

def count_remaining_ships(ships, hits_board):
    # Возвращает словарь {длина_корабля: количество_оставшихся}
    counts = {}
    for ship in ships:
        sunk = all(hits_board[r][c] in (HIT, SUNK) for r,c in ship)
        if not sunk:
            counts[len(ship)] = counts.get(len(ship), 0) + 1
    return counts

def main():
    clock = pygame.time.Clock()

    player_board = create_board()
    computer_board = create_board()

    player_ships = place_ships_randomly(player_board)
    computer_ships = place_ships_randomly(computer_board)

    player_hits = create_board()
    computer_hits = create_board()

    player_turn = True
    game_over = False
    winner = None

    info_msg = "Your turn. Click to fire on computer's board."

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and player_turn and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                cell = get_cell_from_pos(pos, LEFT_MARGIN_CPU, TOP_MARGIN)
                if cell:
                    r, c = cell
                    if player_hits[r][c] == EMPTY:
                        if computer_board[r][c] == SHIP:
                            player_hits[r][c] = HIT
                            info_msg = "Hit!"
                        else:
                            player_hits[r][c] = MISS
                            info_msg = "Miss!"
                            player_turn = False

            if not game_over and not player_turn:
                pygame.time.wait(700)
                candidates = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if computer_hits[r][c] == EMPTY]
                if candidates:
                    r, c = random.choice(candidates)
                    if player_board[r][c] == SHIP:
                        computer_hits[r][c] = HIT
                        info_msg = "Computer hit your ship!"
                    else:
                        computer_hits[r][c] = MISS
                        info_msg = "Computer missed."
                        player_turn = True

            if not game_over:
                # Обновляем состояние потопленных кораблей
                sunk_computer, marks_computer = update_sunk_and_marks(computer_board, player_hits, computer_ships)
                sunk_player, marks_player = update_sunk_and_marks(player_board, computer_hits, player_ships)

                if all_ships_sunk(computer_ships, player_hits):
                    game_over = True
                    winner = "You win!"
                    info_msg = winner

                elif all_ships_sunk(player_ships, computer_hits):
                    game_over = True
                    winner = "Computer wins!"
                    info_msg = winner

            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()  # Перезапуск игры

        screen.fill(GRAY)
        draw_labels()

        # Рисуем сетки и пометки
        draw_grid(player_board, LEFT_MARGIN_PLAYER, TOP_MARGIN, True, computer_hits, sunk_player, marks_player)
        draw_grid(computer_board, LEFT_MARGIN_CPU, TOP_MARGIN, False, player_hits, sunk_computer, marks_computer)

        # Показываем, где компьютер попадал по твоему полю (красные/белые круги)
        # (Это сделано выше в draw_grid, где переданы hits_board)

        # Счётчик оставшихся кораблей по длинам у игрока и компьютера
        player_remaining = count_remaining_ships(player_ships, computer_hits)
        computer_remaining = count_remaining_ships(computer_ships, player_hits)

        def draw_ship_counts(counts, x, y, title):
            draw_text(title, x, y, BLACK, big_font)
            offset = 30
            for length in sorted(counts.keys(), reverse=True):
                draw_text(f"Ships size {length}: {counts[length]}", x, y + offset, BLACK)
                offset += 25

        draw_ship_counts(player_remaining, LEFT_MARGIN_PLAYER, HEIGHT - 130, "Your Ships Left")
        draw_ship_counts(computer_remaining, LEFT_MARGIN_CPU, HEIGHT - 130, "Computer Ships Left")

        draw_text(info_msg, WIDTH//2 - 150, HEIGHT - 50, BLACK, big_font)

        if game_over:
            draw_text("Game Over! Press R to restart.", WIDTH//2 - 140, HEIGHT//2 + 100, RED, big_font)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
