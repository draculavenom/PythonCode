import pygame
from Model.SharedResources import SharedResources
from View.Model.Text import Text
from View.Model.InputField import InputField
from View.Model.Button import Button

class BoardUI:
    def __init__(self, gameHandler):
        self.gameHandler = gameHandler
        self.screen = None
        self.WIDTH = 0
        self.HEIGHT = 0
        self.running = True
        self.gridSize = 14
        self.squareSize = 0
        self.initialPos = 0
        self.initialTextPos = self.gridSize // 2
        self.player1Text = []
        self.player2Text = []
        
        self.input_field1 = None
        self.button1 = None
    
    def setScreen(self, screen):
        self.screen = screen
        self.resources = SharedResources()
        self.WIDTH = screen.get_width()
        self.HEIGHT = screen.get_height()
        self.setSquareSize()
        self.running = True
        self.screen.fill(self.resources.colorsMap["BG_COLOR"])
        self.drawBoard()
        self.scriptInput() #456123: this should be removed once I have the logic to create the script inside the game
        pygame.display.update()
    
    def updateBoard(self):
        self.screen.fill(self.resources.colorsMap["BG_COLOR"])
        self.drawBoard()
        pygame.display.update()
    
    def setSquareSize(self):
        self.squareSize = self.WIDTH // self.gridSize
        self.initialPos = self.squareSize
        self.initialTextPos *= self.squareSize
    
    def drawBoard(self):
        #pygame.draw.rect(self.screen, self.resources.colorsMap["BLACK"], (self.initialPos, self.initialPos, self.squareSize, self.squareSize), 2)
        #"""
        for i in range(1, self.gameHandler.board.size + 1):
            posX = self.initialPos * i
            for j in range(1, self.gameHandler.board.size + 1):
                posY = self.initialPos * j
                pygame.draw.rect(self.screen, self.resources.colorsMap["BLACK"], (posX, posY, self.squareSize, self.squareSize), 2)
        #"""
        
        posX = self.initialPos# + (self.gameHandler.player1.knight.image_rect[2] // 2)
        posY = self.initialPos# + (self.gameHandler.player1.knight.image_rect[3] // 2)
        xl = self.gameHandler.player1.knight.image_rect[2]
        yl = self.gameHandler.player1.knight.image_rect[3]
        self.screen.blit(self.gameHandler.player1.knight.image, (posX * self.gameHandler.player1.knight.x + posX,posY * self.gameHandler.player1.knight.y + posY,xl,yl))
        self.screen.blit(self.gameHandler.player1.archer.image, (posX * self.gameHandler.player1.archer.x + posX,posY * self.gameHandler.player1.archer.y + posY,xl,yl))
        self.screen.blit(self.gameHandler.player1.assasin.image, (posX * self.gameHandler.player1.assasin.x + posX,posY * self.gameHandler.player1.assasin.y + posY,xl,yl))
        self.screen.blit(self.gameHandler.player2.knight.image, (posX * self.gameHandler.player2.knight.x + posX,posY * self.gameHandler.player2.knight.y + posY,xl,yl))
        self.screen.blit(self.gameHandler.player2.archer.image, (posX * self.gameHandler.player2.archer.x + posX,posY * self.gameHandler.player2.archer.y + posY,xl,yl))
        self.screen.blit(self.gameHandler.player2.assasin.image, (posX * self.gameHandler.player2.assasin.x + posX,posY * self.gameHandler.player2.assasin.y + posY,xl,yl))
        self.drawPlayersInfo()
        
    def drawPlayersInfo(self):
        pygame.draw.rect(self.screen, self.resources.colorsMap["BLACK"], (self.initialTextPos, self.initialPos, (self.gridSize // 2 - 1) * self.squareSize, self.squareSize * 5), 2)
        #Player 1 Info
        y = self.initialTextPos + 2
        self.player1Text.append(Text(self.screen, "Round: " + str(self.gameHandler.round) + " Player " + str(self.gameHandler.turn) + " starts", self.initialPos, y))
        self.player1Text[0].show()
        self.player1Text.append(Text(self.screen, "Player 1", self.initialPos + self.resources.text_size + 5, y))
        self.player1Text[1].show()
        self.player1Text.append(Text(self.screen, "Knight", self.initialPos + (self.resources.text_size + 5) * 2, y))
        self.player1Text[2].show()
        self.player1Text.append(Text(self.screen, "HP: " + str(self.gameHandler.player1.knight.hp), self.initialPos + (self.resources.text_size + 5) * 3, y))
        self.player1Text[3].show()
        self.player1Text.append(Text(self.screen, "Archer", self.initialPos + (self.resources.text_size + 5) * 5, y))
        self.player1Text[4].show()
        self.player1Text.append(Text(self.screen, "HP: " + str(self.gameHandler.player1.archer.hp), self.initialPos + (self.resources.text_size + 5) * 6, y))
        self.player1Text[5].show()
        self.player1Text.append(Text(self.screen, "Assasin", self.initialPos + (self.resources.text_size + 5) * 8, y))
        self.player1Text[6].show()
        self.player1Text.append(Text(self.screen, "HP: " + str(self.gameHandler.player1.assasin.hp), self.initialPos + (self.resources.text_size + 5) * 9, y))
        self.player1Text[7].show()
        #Player 2 Info
        y = (self.gridSize // 2 + self.gridSize // 4) * self.squareSize
        self.player2Text.append(Text(self.screen, "Player 2", self.initialPos + self.resources.text_size + 5, y))
        self.player2Text[0].show()
        self.player2Text.append(Text(self.screen, "Knight", self.initialPos + (self.resources.text_size + 5) * 2, y))
        self.player2Text[1].show()
        self.player2Text.append(Text(self.screen, "HP: " + str(self.gameHandler.player2.knight.hp), self.initialPos + (self.resources.text_size + 5) * 3, y))
        self.player2Text[2].show()
        self.player2Text.append(Text(self.screen, "Archer", self.initialPos + (self.resources.text_size + 5) * 5, y))
        self.player2Text[3].show()
        self.player2Text.append(Text(self.screen, "HP: " + str(self.gameHandler.player2.archer.hp), self.initialPos + (self.resources.text_size + 5) * 6, y))
        self.player2Text[4].show()
        self.player2Text.append(Text(self.screen, "Assasin", self.initialPos + (self.resources.text_size + 5) * 8, y))
        self.player2Text[5].show()
        self.player2Text.append(Text(self.screen, "HP: " + str(self.gameHandler.player2.assasin.hp), self.initialPos + (self.resources.text_size + 5) * 9, y))
        self.player2Text[6].show()
    
    def scriptInput(self):
        posX = self.initialPos
        posY = self.initialPos * 7
        self.input_field1 = InputField((posX, posY, self.initialPos * 3, self.initialPos * 3), color="SKY_BLUE_WHITE", active_color="SKY_BLUE")
        self.input_field1.updateText("kn m do\nkn m do\nar m do\nas m do do do\nar a do do do\nkn a up")
        self.input_field1.render(self.screen)
        self.button1 = Button(self.validateScript1, text = "OK", x = self.initialPos * 5, y = self.initialPos * 7, width = self.initialPos, height = self.initialPos)
        self.button1.changeColors("SKY_BLUE", "SKY_BLUE_WHITE", "BLUE")
        self.button1.draw(self.screen)
    
    def validateScript1(self):
        scriptValidation = self.gameHandler.scripts.validateScript(self.input_field1.text, 1)
        print(scriptValidation)
        if scriptValidation:
            self.gameHandler.scripts.executeScriptForPlayer(1, self.gameHandler, self)
            x = 0
            #disable the button
            #disable to write in the input
        else:
            #keep trying
            x = 0
        return False
    
    def executeScripts(self):
        self.gameHandler.scripts.executeScriptForPlayer(1, self.gameHandler, self)
        
    def handleEvents(self, event):
        self.input_field1.handle_event(event)
        self.button1.handle_event(event)
        