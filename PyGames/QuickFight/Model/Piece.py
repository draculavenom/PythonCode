import pygame

class Piece:
    def __init__(self):
        self.type = ""
        self.hp = 10
        self.atk = 2
        self.mov = 1
        self.dist = 1
        self.bonus = []
        self.x = 0
        self.y = 0
        self.image = None
        self.image_rect = None
    
    def knightType(self):
        self.type = "Knight"
        self.bonus = ["Assasin", 2]
    
    def archerType(self):
        self.type = "Archer"
        self.hp = 5
        self.atk = 1
        self.dist = 3
        self.bonus = ["Knight", 2]
    
    def assasinType(self):
        self.type = "Assasin"
        self.hp = 7
        self.mov = 3
        self.bonus = ["Archer", 1]
    
    def setImage(self, playerNum):
        if self.type == "Knight":
            image = "shield"
        elif self.type == "Assasin":
            image = "daggers"
        elif self.type == "Archer":
            image = "BowArrow"
        image += playerNum
        self.image = pygame.image.load("images/" + image + ".png")
        self.image = self.image.convert_alpha()
        self.image_rect = self.image.get_rect()
    
    def getDamage(self, amount, incomingBonus):
        self.hp -= amount
        if len(incomingBonus) == 2 and self.type == incomingBonus[0]:
            self.hp -= incomingBonus[1]