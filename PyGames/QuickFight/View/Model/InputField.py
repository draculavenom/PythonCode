import pygame
from Model.SharedResources import SharedResources

class InputField:
    def __init__(self, rect, text="", color="WHITE", active_color="GRAY"):
        self.rect = pygame.Rect(rect)
        self.resource = SharedResources()
        self.text = text
        self.color = self.resource.colorsMap[color]
        self.active_color = self.resource.colorsMap[active_color]
        self.active = False
        self.screen = None
    
    def updateText(self, text):
        self.text = text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.render(self.screen)
            pygame.display.update()
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text += "\n"  # Add a newline character when Enter key is pressed
                    self.render(self.screen)
                    pygame.display.update()
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.render(self.screen)
                    pygame.display.update()
                else:
                    self.text += event.unicode
                    self.render(self.screen)
                    pygame.display.update()

    def render(self, surface):
        pygame.draw.rect(surface, self.active_color if self.active else self.color, self.rect)
        text_surface = self.resource.font.render(self.text, True, self.resource.colorsMap["BLACK"])
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        self.screen = surface