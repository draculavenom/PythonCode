import pygame
import random
from SharedResources import SharedResources
from GameSelector import GameSelector
from Button import Button

class FigureColor:
    def __init__(self):
        self.resources = SharedResources()
        self.COLORS = ["BLACK", "WHITE", "RED", "GREEN"]
        self.textColor = "PURPLE"

        self.WIDTH = 800
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.gameSelector = None
        self.button = Button(self.unselectGame, "Go back", self.WIDTH / 7,self.HEIGHT / 7 + 60)
        self.limitFigures = 10
        
        self.initializeGame()
        
    def initializeGame(self):
        self.pressed_keys = []
        self.figure_color = []
        self.correctAnswers = ""
        self.i = -1
        self.pressed = ''
        self.running = True
        self.finish = False
        self.shape_type = ""
        self.color = ""
        self.clock = pygame.time.Clock()
    
    def setGameSelector(self, gameSelector):
        self.gameSelector = gameSelector
    
    def setScreen(self, screen):
        self.screen = screen
        self.WIDTH = screen.get_width()
        self.HEIGHT = screen.get_height()

# Function to draw a circle
    def draw_circle(self, pos, color, radius=40):
        pygame.draw.circle(self.screen, color, pos, radius)
    
    # Function to draw a triangle
    def draw_triangle(self, pos, color, size=60):
        points = [
            pos,
            (pos[0] + size, pos[1] + size),
            (pos[0] - size, pos[1] + size)
        ]
        pygame.draw.polygon(self.screen, color, points)
    
    # Function to draw a rectangle
    def draw_rectangle(self, pos, color, size=(80, 40)):
        pygame.draw.rect(self.screen, color, pygame.Rect(pos, size))
    
    # Function to draw a square
    def draw_square(self, pos, color, size=60):
        self.draw_rectangle(pos, color, size=(size, size))
    
    def chooseFigureColor(self, ps, pc):
        shape_type = random.choice(["circle", "triangle", "rectangle", "square"])
        if shape_type in ["rectangle", "square"]:
            color = random.randint(0,1)
        elif shape_type == "circle":
            color = random.randint(1,3)
        elif shape_type == "triangle":
            color = random.randint(0,3)
            while color == 1:
                color = random.randint(0,3)
        while (shape_type, color) == (ps, pc):
            shape_type = random.choice(["circle", "triangle", "rectangle", "square"])
            if shape_type in ["rectangle", "square"]:
                color = random.randint(0,1)
            elif shape_type == "circle":
                color = random.randint(1,3)
            elif shape_type == "triangle":
                color = random.randint(0,3)
                while color == 1:
                    color = random.randint(0,3)
        return (shape_type, color)
    
    def display_instructions(self):
        text = "In the game, you will see 4 figures"
        label_text = self.resources.label_font.render(text, True, self.resources.colorsMap[self.textColor])
        self.screen.blit(label_text, (self.WIDTH / 7,self.HEIGHT / 7))
        text = "you need to press 'J' if you see an Circle or the color white"
        label_text = self.resources.label_font.render(text, True, self.resources.colorsMap[self.textColor])
        self.screen.blit(label_text, (self.WIDTH / 7,self.HEIGHT / 7 + 30))
        text = "and 'K' if you see a Triangle or the color black"
        label_text = self.resources.label_font.render(text, True, self.resources.colorsMap[self.textColor])
        self.screen.blit(label_text, (self.WIDTH / 7,self.HEIGHT / 7 + 60))
    
    def display_results(self):
        text = "Game's over"
        label_text = self.resources.label_font.render(text, True, self.resources.colorsMap[self.textColor])
        self.screen.blit(label_text, (self.WIDTH / 7,self.HEIGHT / 7))
        intSum = 0
        self.correctAnswers = ""
        for i in range(len(self.figure_color)):
            if ("circle" in self.figure_color[i] or "- 1" in self.figure_color[i]):
                self.correctAnswers += "J, "
                if self.pressed_keys[i] == 'J':
                    intSum += 1
            elif ("triangle" in self.figure_color[i] or "- 0" in self.figure_color[i]):
                self.correctAnswers += "F, "
                if self.pressed_keys[i] == 'F':
                    intSum += 1
            
        text = "Answered right: " + str(intSum)
        label_text = self.resources.label_font.render(text, True, self.resources.colorsMap[self.textColor])
        self.screen.blit(label_text, (self.WIDTH / 7,self.HEIGHT / 7 + 30))
        self.button.draw(self.screen)
        #self.debug()
    
    def unselectGame(self):
        if self.gameSelector != None:
            self.gameSelector.unselectGame()
            self.initializeGame()
    
    def debug(self):
        text = "DV Debug"
        print(pygame.time.get_ticks())
        print(self.pressed_keys)
        print(self.correctAnswers)
        print(self.figure_color)
        label_text = self.resources.label_font.render(text, True, self.resources.colorsMap[self.textColor])
        self.screen.blit(label_text, (self.WIDTH / 7,self.HEIGHT - self.HEIGHT / 7))
    
    
    def mainController(self):
        if not self.finish:
            if pygame.time.get_ticks() <= 500:
                self.screen.fill(self.resources.colorsMap["BG_COLOR"])
                self.display_instructions()
                pygame.display.update()
            
            if len(self.figure_color) == self.i + 1 and len(self.pressed_keys) <= self.i:
                if len(self.figure_color) == len(self.pressed_keys) + 2:
                    self.pressed_keys.append('-')
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
                if event.type == pygame.KEYDOWN:
                    if len(self.figure_color) == self.i + 1 and len(self.pressed_keys) <= self.i:
                        if event.key == pygame.K_f:
                            self.pressed_keys.append('F')
                        elif event.key == pygame.K_j:
                            self.pressed_keys.append('J')
                
            if pygame.time.get_ticks() % 1200 <= 10:
                self.i += 1
                if self.i == self.limitFigures:
                    self.finish = True
                    if len(self.figure_color) > len(self.pressed_keys):
                        self.pressed_keys.append('-')
                    return
                self.screen.fill(self.resources.colorsMap["BG_COLOR"])
                self.display_instructions()
                shape_type, color = self.chooseFigureColor(self.shape_type, self.color)
                pos = (self.WIDTH // 2, self.HEIGHT // 2)
            
                # Draw the chosen shape based on type
                self.figure_color.append(shape_type + " - " + str(color))
                if shape_type == "circle":
                    self.draw_circle(pos, self.COLORS[color])
                elif shape_type == "triangle":
                    self.draw_triangle(pos, self.COLORS[color])
                elif shape_type == "rectangle":
                    self.draw_rectangle(pos, self.COLORS[color])
                else:
                    self.draw_square(pos, self.COLORS[color])
                
                text = "Figure: " + str(self.i + 1)
                label_text = self.resources.label_font.render(text, True, self.resources.colorsMap[self.textColor])
                self.screen.blit(label_text, ((self.WIDTH / 7)*3,self.HEIGHT / 7 + 120))
                
                #self.debug()
                pygame.display.update()
        else:
            self.screen.fill(self.resources.colorsMap["BG_COLOR"])
            self.display_results()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if self.gameSelector != None:
                    self.button.handle_event(event)
        self.clock.tick(60)
