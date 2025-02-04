import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("Breaking bricks")

bat = pygame.image.load("images/paddle.png")
bat = bat.convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen.get_height() - 100

ball = pygame.image.load("images/football.png")
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (202, 202)
ball_speed = (3.0, 3.0)
ball_served = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

brick = pygame.image.load("images/brick.png")
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []
brick_rows = 5
brick_gap = 10
brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap) // 2


for y in range(brick_rows):
    bricky = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickx = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickx, bricky))

clock = pygame.time.Clock()
game_over = False
while not game_over:
    dt = clock.tick(50)
    screen.fill((0, 0, 0))
    
    for b in bricks:
        screen.blit(brick, b)
    
    screen.blit(bat, bat_rect)
    screen.blit(ball, ball_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
    pressed = pygame.key.get_pressed()
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        ball_served = True
    bat_rect[0] = x;
    
    if bat_rect[0] + bat_rect.width >= ball_rect[0] >= bat_rect[0] and ball_rect[1] + ball_rect.height >= bat_rect[1] and sy > 0:
        sy *= -1
        sx *= 1.10
        sy *= 1.10
        continue
    
    delete_brick = None
    for b in bricks:
        bx, by = b
        if bx <= ball_rect[0] <= bx + brick_rect.width and by <= ball_rect[1] <= by + brick_rect.height:
            delete_brick = b
            
            if ball_rect[0] <= bx + 2 or ball_rect[0] >= bx + brick_rect.width - 1:
                sx *= -1
            if ball_rect[1] <= by + 2 or ball_rect[1] >= by + brick_rect.height - 1:
                sy *= -1
            break
            
    if delete_brick is not None:
        bricks.remove(delete_brick)
    
    #ball moving top
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1
    
    #ball moving left
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx *= -1
    
    #ball moving botton
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        #ball_rect[1] = screen.get_height() - ball_rect.height
        #sy *= -1
        ball_served = False
        ball_rect.topleft = ball_start
    
    #ball moving right
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        sx *= -1
    
    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy
        
    
    
        
    pygame.display.update()

pygame.quit()