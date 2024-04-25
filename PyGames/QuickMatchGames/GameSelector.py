import pygame
from SharedResources import SharedResources
from Button import Button

class GameSelector:
    def __init__(self):
        self.game = ""
        self.textColor = "PURPLE"
        self.gameSelected = ""

        self.WIDTH = 800
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        self.uiElements()
    
    def setScreen(self, screen):
        self.screen = screen
        self.resources = SharedResources()
        self.WIDTH = screen.get_width()
        self.HEIGHT = screen.get_height()
        self.running = True
        self.screen.fill(self.resources.colorsMap["BG_COLOR"])
    
    def uiElements(self):
        self.button = Button(self.selectFigureColorGame, "Figure Color Game")
    
    def mainController(self):
        self.display_text("Select a game")
        pygame.display.update()
        self.game = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.button.handle_event(event)
        
        self.button.draw(self.screen)
    
    def selectFigureColorGame(self):
        self.screen.fill(self.resources.colorsMap["BG_COLOR"])
        self.gameSelected = "figureColor"
    
    def unselectGame(self):
        self.screen.fill(self.resources.colorsMap["BG_COLOR"])
        self.gameSelected = ""
    
    def display_text(self, text = ""):
        label_text = self.resources.label_font.render(text, True, self.resources.colorsMap[self.textColor])
        self.screen.blit(label_text, (self.WIDTH / 7,self.HEIGHT / 7))
    