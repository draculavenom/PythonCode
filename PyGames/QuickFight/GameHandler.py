from Model.Player import Player
from Model.Board import Board
from View.ScriptHandler import ScriptHandler
import random

class GameHandler:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player("2")
        self.board = Board()
        self.setInitialPiecesPerPlayer()
        self.round = 1
        self.turn = None
        self.playerTurn()
        self.scripts = ScriptHandler()
    
    def setInitialPiecesPerPlayer(self):
        self.board.setPiece(self.player1.knight, 0, 1)
        self.board.setPiece(self.player1.archer, 0, 2)
        self.board.setPiece(self.player1.assasin, 0, 3)
        self.board.setPiece(self.player2.knight, 4, 3)
        self.board.setPiece(self.player2.archer, 4, 2)
        self.board.setPiece(self.player2.assasin, 4, 1)
    
    def playerTurn(self):
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1
        self.turn = random.randint(1, 2)
    
    