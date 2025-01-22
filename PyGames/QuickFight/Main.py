import pygame
from View.ScreenHandler import ScreenHandler
from GameHandler import GameHandler
from View.BoardUI import BoardUI

screenHandler = ScreenHandler()
pygame.init()
screenHandler.start("Quick Fight")
gameHandler = GameHandler()
boardUI = BoardUI(gameHandler)
boardUI.setScreen(screenHandler.screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        boardUI.handleEvents(event)
    
pygame.quit()

"""
I need a gameHandler --> which will check if there is a valid move for a piece
I need something to create the board for the first time and create each piece for each player
I need something that helps each player create their script

"""