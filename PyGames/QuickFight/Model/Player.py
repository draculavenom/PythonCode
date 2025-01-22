from Model.Piece import Piece

class Player:
    def __init__(self, name = "1"):
        self.name = "Player " + name
        self.knight = Piece()
        self.knight.knightType()
        self.knight.setImage(name)
        self.archer = Piece()
        self.archer.archerType()
        self.archer.setImage(name)
        self.assasin = Piece()
        self.assasin.assasinType()
        self.assasin.setImage(name)
        