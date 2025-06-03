import pygame
import sys

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pong Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 6

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Fonts
font = pygame.font.SysFont("Arial", 36)


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def main():
    # Initial positions
    left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y

    left_score = 0
    right_score = 0

    running = True
    while running:
        clock.tick(60)
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collision with top/bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        # Ball collision with paddles
        if ball.colliderect(left_paddle) and ball_speed_x < 0:
            ball_speed_x *= -1
        if ball.colliderect(right_paddle) and ball_speed_x > 0:
            ball_speed_x *= -1

        # Score update and ball reset
        if ball.left <= 0:
            right_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_speed_x = -BALL_SPEED_X
        if ball.right >= WIDTH:
            left_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_speed_x = BALL_SPEED_X

        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        # Draw scores
        draw_text(str(left_score), font, WHITE, WIDTH // 4, 20)
        draw_text(str(right_score), font, WHITE, WIDTH * 3 // 4, 20)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
