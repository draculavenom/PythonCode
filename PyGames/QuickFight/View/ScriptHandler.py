import pygame

class ScriptHandler:
    def __init__(self):
        self.player1script = None
        self.player2script = None
        
    def validateScript(self, text, player):
        print(text)
        actions = []
        if "\n" in text:
            lines = text.split("\n")
            if len(lines) == 6:
                for line in lines:
                    actionType = line.split(" ")
                    piece = self.validatePiece(actionType[0])
                    if piece == None:
                        print("fails because action is bad")
                        return False
                    action = self.validateAction(actionType[1])
                    if action == None:
                        print("fails because action is bad")
                        return False
                    directions = self.validateDirection(actionType[2:], piece, action)
                    print(directions)
                    if directions == None or directions[0] == None:
                        print("fails because directions are bad")
                        return False
                    actions.append((piece, action, directions))
                if player == 1:
                    self.player1script = actions
                    return True
                elif player == 2:
                    self.player2script = actions
                    return True
                else:
                    print("fails because the player is not 1 or 2")
                    return False
            else:
                print("fails because the jump lines are not 6")
                return False
        print("fails because the text doesn't have jump lines")
        return False

    def validatePiece(self, text):
        if text in ["kn", "ca"]:
            return "Knight"
        if text in ["ar"]:
            return "Archer"
        if text in ["as"]:
            return "Assasin"
        return None
        
    def validateAction(self, text):
        if text in ["m", "mo", "mu"]:
            return "move"
        if text in ["a", "at", "atk", "ata", "att"]:
            return "attack"
        return None
    
    def validateDirection(self, texts, piece, action):
        dirrections = []
        if (piece == "Archer" and action == "attack") or (piece == "Assasin" and action == "move"):
            for text in texts:
                dirrections.append(self.validateSingleDirection(text))
        else:
            dirrections.append(self.validateSingleDirection(texts[0]))
        return dirrections
    
    def validateSingleDirection(self, text):
        if text in ["up", "u", "ar", "arr", "UP", "U", "AR", "ARR"]:
            return "up"
        elif text in ["d", "do", "down", "ab", "aba", "D", "DO", "DOWN", "AB", "ABA"]:
            return "down"
        elif text in ["right", "r", "ri", "de", "der", "RIGHT", "R", "RI", "DE", "DER"]:
            return "right"
        elif text in ["left", "le", "l", "i", "iz", "izq", "LEFT", "LE", "L", "I", "IZ", "IZQ"]:
            return "left"
        print("single direction not working on: " + text)
        return None
    
    def executeScriptForPlayer(self, player, gameHandler, boardUI):
        print("execution in process...")
        if player == 1:
            for s in self.player1script:
                piece = self.getPieceFromPlayer(gameHandler.player1, s[0])
                if s[1] == "move":
                    if len(s) == 3:
                        nx, ny = self.getCoordinates(piece.x, piece.y, s[2])
                        gameHandler.board.movePiece(piece, ny, nx)
                    elif len(s) == 4:
                        nx, ny = self.getCoordinates(piece.x, piece.y, s[2])
                        gameHandler.board.movePiece(piece, ny, nx)
                        nx, ny = self.getCoordinates(piece.x, piece.y, s[3])
                        gameHandler.board.movePiece(piece, ny, nx)
                    elif len(s) == 5:
                        nx, ny = self.getCoordinates(piece.x, piece.y, s[2])
                        gameHandler.board.movePiece(piece, ny, nx)
                        nx, ny = self.getCoordinates(piece.x, piece.y, s[3])
                        gameHandler.board.movePiece(piece, ny, nx)
                        nx, ny = self.getCoordinates(piece.x, piece.y, s[4])
                        gameHandler.board.movePiece(piece, ny, nx)
                elif s[1] == "attack":
                    if 3 <= len(s) <= 5:
                        nx, ny = self.getCoordinatesX(piece, s[2:])
                        if gameHandler.board.matrix[nx][ny] == None:
                            print("attack didn't hit anyone")
                        else:
                            piece2 = gameHandler.board.matrix[nx][ny]
                            piece2.getDamage(piece.atk, piece.bonus)
                            print(piece2.type + " was damaged")
                boardUI.updateBoard()#456123: not working
            return True
        #elif player == 2:
            
        return False
    
    def getPieceFromPlayer(self, player, text):
        piece = None
        if text == "Knight":
            piece = player.knight
        elif text == "Archer":
            piece = player.archer
        elif text == "Assasin":
            piece = player.assasin
        return piece
    
    def getCoordinates(self, x, y, direction):
        if direction == "up":
            return (x - 1, y)
        if direction == "down":
            return (x + 1, y)
        if direction == "right":
            return (x, y + 1)
        if direction == "left":
            return (x, y - 1)
        return (x - 1, y)
    
    def getCoordinatesX(self, piece, directions):
        x, y = self.getCoordinates(piece.x, piece.y, directions)
        i = 1
        while(i < len(directions)):
            x, y = self.getCoordinates(x, y, directions)
            i += 1
        return (x, y)
            