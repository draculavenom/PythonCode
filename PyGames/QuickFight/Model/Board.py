

class Board:
    def __init__(self):
        self.size = 5
        self.matrix = [[None] * self.size for _ in range(self.size)]
    
    def setPiece(self, piece, y, x):
        self.matrix[x][y] = piece
        piece.x = x
        piece.y = y
    
    def movePiece(self, piece, ny, nx):
        if self.matrix[piece.x][piece.y] == piece and (0 <= nx <= 4 and 0 <= ny <= 4) and self.matrix[nx][ny] == None:
            self.matrix[piece.x][piece.y] = None
            self.matrix[nx][ny] = piece
            piece.x = nx
            piece.y = ny
            return True
        return False