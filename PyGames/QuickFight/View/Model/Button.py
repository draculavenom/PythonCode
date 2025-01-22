import pygame
from Model.SharedResources import SharedResources

class Button:
    """
    This class creates a button object with text and functionality.
    """
    def __init__(self, func_name, text = "Button", x = 120, y = 120, width = 150, height = 50):
        self.resources = SharedResources()
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.idle_color = self.resources.colorsMap["GRAY_150"]
        self.hover_color = self.resources.colorsMap["GRAY_230"]
        self.click_color = self.resources.colorsMap["GRAY_180"]
        self.current_color = self.idle_color
        self.text_color = self.resources.colorsMap["PURPLE"]
        self.func_name = func_name  # Method to be called on click
        self.screen = None
    
    def changeColors(self, idle_color, hover_color, click_color):
        self.idle_color = self.resources.colorsMap[idle_color]
        self.hover_color = self.resources.colorsMap[hover_color]
        self.click_color = self.resources.colorsMap[click_color]
        self.current_color = self.idle_color
    
    def draw(self, screen):
        self.screen = screen
        # Render the text
        text_surface = self.resources.font.render(self.text, True, self.text_color)
        text_x = self.x + (self.width - text_surface.get_width()) // 2
        text_y = self.y + (self.height - text_surface.get_height()) // 2
    
        # Draw the button rectangle
        pygame.draw.rect(screen, self.current_color, (self.x, self.y, self.width, self.height))
        
        # Draw the text on the button
        screen.blit(text_surface, (text_x, text_y))
    
    def handle_event(self, event):
        # Check if mouse is hovering over the button
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if self.is_mouse_over(pos):
                self.current_color = self.hover_color
                self.draw(self.screen)
            else:
                self.current_color = self.idle_color
                self.draw(self.screen)
        
        # Check if mouse clicks the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.is_mouse_over(pos):
                self.current_color = self.click_color
                self.draw(self.screen)
                self.func_name()
    
    def is_mouse_over(self, pos):
        mouse_x, mouse_y = pos
        return mouse_x >= self.x and mouse_x <= self.x + self.width and mouse_y >= self.y and mouse_y <= self.y + self.height
