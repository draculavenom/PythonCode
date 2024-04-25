import pygame
#import random
from FigureColor import FigureColor
from GameSelector import GameSelector

# Define screen dimensions
WIDTH = 800
HEIGHT = 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Shapes Game")
clock = pygame.time.Clock()
label_font = pygame.font.SysFont('Arial', 20)

pressed_keys = []
figure_color = []
i = -1
pressed = ''
running = True
finish = False
shape_type = ""
color = ""

gameSelector = GameSelector()
gameSelector.setScreen(screen)
figureColor = FigureColor()
figureColor.setScreen(screen)
figureColor.setGameSelector(gameSelector)
game_selected = ""
while running:
    
    if game_selected == "":
        gameSelector.mainController()
        running = gameSelector.running
        game_selected = gameSelector.gameSelected
    
    if game_selected == "figureColor":
        figureColor.mainController()
        running = figureColor.running
        game_selected = gameSelector.gameSelected
    

# Quit Pygame
pygame.quit()
