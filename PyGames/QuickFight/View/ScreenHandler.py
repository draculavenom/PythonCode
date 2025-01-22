import pygame

class ScreenHandler:
    def __init__(self):
        self.width = 1000
        self.height = 800
        self.screen = None

    def start(self, title = "DV Games"):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()