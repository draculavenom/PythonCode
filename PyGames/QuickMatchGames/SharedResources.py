import pygame

class SharedResources:
    def __init__(self):
        self.colorsMap = {"BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "YELLOW": (255, 255, 0),
        "PURPLE": (128, 0, 128),
        "ORANGE": (255, 165, 0),
        "PINK": (255, 192, 203),
        "TEAL": (0, 128, 128),
        "BROWN": (139, 69, 19),
        "GRAY": (128, 128, 128),
        "NAVY_BLUE": (0, 0, 128),
        "LIME_GREEN": (0, 255, 127),
        "SKY_BLUE": (135, 206, 235),
        "BG_COLOR": (196, 196, 196),
        "GRAY_180": (180, 180, 180),
        "GRAY_150": (150, 150, 150),
        "GRAY_230": (230, 230, 230)
        }
        self.label_font = pygame.font.SysFont('Arial', 20)