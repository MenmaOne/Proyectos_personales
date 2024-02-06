import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
WITHE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = BALL_SPEED, BALL_SPEED

paddel_width, paddel_height = 15, 60
left_paddel_x, right_paddel_x = 10, WIDTH - 25
left_paddel_y, right_paddel_y = HEIGHT // 2 - paddel_height // 2, HEIGHT - paddel_height // 2
paddel_speed = 7
score_left, score_right = 0, 0

#Display score
font = pygame.font.Font(None, 36)

def reset_ball():
    return WIDTH // 2, HEIGHT // 2, BALL_SPEED, BALL_SPEED


#game loop
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddel_y > 0: 
        left_paddel_y -= paddel_speed
    if keys[pygame.K_s] and left_paddel_y < HEIGHT - paddel_height:
        left_paddel_y += paddel_speed
    if keys[pygame.K_UP] and left_paddel_y > 0: 
        left_paddel_y -= paddel_speed
    if keys[pygame.K_DOWN] and left_paddel_y < HEIGHT - paddel_height:
        left_paddel_y += paddel_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if(
        left_paddel_x < ball_x < right_paddel_x + paddel_width and left_paddel_y < ball_y < right_paddel_y + paddel_height
    ) or (
        right_paddel_x < ball_x < right_paddel_x + paddel_width and right_paddel_y < ball_y < right_paddel_y + paddel_height
    ):
        ball_speed_x = -ball_speed_y

    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_speed_y = -ball_speed_y
    
    if ball_x <= 0:
        score_right += 1
        ball_x, ball_y, ball_speed_x, ball_speed_y = reset_ball()
    
    if ball_x >= WIDTH: 
        score_left += 1
        ball_x, ball_y, ball_speed_x, ball_speed_y = reset_ball()
    
    screen.fill(BLACK)
    pygame.draw.rect(screen, WITHE, (left_paddel_x, left_paddel_y, paddel_width, paddel_height))
    pygame.draw.rect(screen, WITHE, (right_paddel_x, right_paddel_y, paddel_width, paddel_height))
    pygame.draw.ellipse(screen, WITHE, (ball_x - 10, ball_y - 10, 20, 20))
    score_display = font.render(f"{score_left} - {score_right}", True, WITHE)
    screen.blit(score_display, (WIDTH // 2 - 40, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)
