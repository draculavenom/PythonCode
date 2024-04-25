import pygame
from pygame.locals import *

def moveXY(pressed, x, y, dt, xl, yl):
    if pressed[K_UP] and y > 0:
        y -= 0.5 * dt
    if pressed[K_DOWN] and y < yl:
        y += 0.5 * dt
    if pressed[K_LEFT] and x > 0:
        x -= 0.5 * dt
    if pressed[K_RIGHT] and x < xl:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        x = 0
        y = 0
    return x, y

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)

globalWidth = 60
globalHeight = 60
sprite1 = pygame.image.load("images/football.png")
sprite1 = pygame.transform.scale(sprite1, (globalWidth, globalHeight))

pygame.display.set_caption("Hello Sprite")
screen.fill((0, 0, 0))

x = 0
y = 0
clock = pygame.time.Clock()
game_over = False
while not game_over:
    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            x -= globalWidth/2
            y -= globalHeight/2
            
    pressed = pygame.key.get_pressed()
    x, y = moveXY(pressed, x, y, dt, screen.get_width() - globalWidth, screen.get_height() - globalHeight)
    
    screen.fill((0, 0, 0))
    screen.blit(sprite1, (x, y))
    pygame.display.update()
pygame.quit()