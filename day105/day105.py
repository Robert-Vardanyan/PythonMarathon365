import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Blackjack")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
GRAY = (220, 220, 220)
RED = (178, 34, 34)

font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 36)

# Cards and deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = []

def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

def shuffle_deck(deck):
    random.shuffle(deck)

def card_value(card):
    rank = card[0]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    return int(rank)

def calculate_score(hand):
    score = sum(card_value(card) for card in hand)
    # Adjust for Aces
    aces = sum(1 for card in hand if card[0] == 'A')
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

def draw_hand(hand, x, y, label):
    win.blit(font.render(label, True, BLACK), (x, y - 30))
    for i, card in enumerate(hand):
        pygame.draw.rect(win, GRAY, (x + i * 80, y, 60, 90), border_radius=6)
        text = font.render(f"{card[0]}{card[1][0]}", True, BLACK)
        win.blit(text, (x + i * 80 + 5, y + 30))

def draw_button(rect, text, active):
    pygame.draw.rect(win, RED if active else BLACK, rect, border_radius=6)
    label = font.render(text, True, WHITE)
    win.blit(label, (rect.centerx - label.get_width() // 2, rect.centery - label.get_height() // 2))

# Initial game state
deck = create_deck()
shuffle_deck(deck)

player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]
player_standing = False
game_over = False
result = ""

# Buttons
hit_button = pygame.Rect(100, 500, 100, 40)
stand_button = pygame.Rect(250, 500, 100, 40)
restart_button = pygame.Rect(400, 500, 120, 40)

clock = pygame.time.Clock()

def reset_game():
    global deck, player_hand, dealer_hand, player_standing, game_over, result
    deck = create_deck()
    shuffle_deck(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    player_standing = False
    game_over = False
    result = ""

running = True
while running:
    win.fill(GREEN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hit_button.collidepoint(event.pos) and not player_standing and not game_over:
                player_hand.append(deck.pop())
                if calculate_score(player_hand) > 21:
                    result = "Player busts! Dealer wins."
                    game_over = True
            elif stand_button.collidepoint(event.pos) and not game_over:
                player_standing = True
                while calculate_score(dealer_hand) < 17:
                    dealer_hand.append(deck.pop())
                player_score = calculate_score(player_hand)
                dealer_score = calculate_score(dealer_hand)
                if dealer_score > 21 or player_score > dealer_score:
                    result = "Player wins!"
                elif player_score < dealer_score:
                    result = "Dealer wins!"
                else:
                    result = "It's a tie!"
                game_over = True
            elif restart_button.collidepoint(event.pos):
                reset_game()

    # Draw hands
    draw_hand(player_hand, 100, 350, "Player")
    if player_standing or game_over:
        draw_hand(dealer_hand, 100, 100, "Dealer")
    else:
        hidden_hand = [('?', '?')] + dealer_hand[1:]
        draw_hand(hidden_hand, 100, 100, "Dealer")

    # Buttons
    draw_button(hit_button, "Hit", hit_button.collidepoint(pygame.mouse.get_pos()))
    draw_button(stand_button, "Stand", stand_button.collidepoint(pygame.mouse.get_pos()))
    draw_button(restart_button, "Restart", restart_button.collidepoint(pygame.mouse.get_pos()))

    # Result
    if result:
        win.blit(big_font.render(result, True, BLACK), (WIDTH // 2 - 150, HEIGHT // 2 - 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
