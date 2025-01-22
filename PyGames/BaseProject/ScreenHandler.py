import pygame

class ScreenHandler:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = None

    def start(self, title = "DV Games"):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()