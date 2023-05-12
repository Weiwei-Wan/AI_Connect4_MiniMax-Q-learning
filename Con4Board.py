import numpy as np

HEIGHT = 5
WIDTH = 6

class Board():
    def __init__(self):
        self.board = np.zeros((HEIGHT,WIDTH))

    def playerMove(self, y, player):
        for i in range(HEIGHT-1, -1, -1):
            if self.board[i,y]==0:
                self.board[i,y] = player
                break
    
    def getBoard(self):
        return self.board

    # 0: no winner, go on #1: player1 win #2: player2 win #3: tied game
    def checkWinner(self):
        # check column
        for i in range(HEIGHT-3):
            for j in range(WIDTH):
                if self.board[i][j]!=0 and self.board[i+1][j]==self.board[i][j] and self.board[i+2][j]==self.board[i][j] and self.board[i+3][j]==self.board[i][j]:
                    return self.board[i][j]
        # check row
        for j in range(WIDTH-3):
            for i in range(HEIGHT):
                if self.board[i][j]!=0 and self.board[i][j+1]==self.board[i][j] and self.board[i][j+2]==self.board[i][j] and self.board[i][j+3]==self.board[i][j]:
                    return self.board[i][j]
        # check diagonal left
        for i in range(3,HEIGHT):
            for j in range(WIDTH-3):
                if self.board[i][j]!=0 and self.board[i-1][j+1]==self.board[i][j] and self.board[i-2][j+2]==self.board[i][j] and self.board[i-3][j+3]==self.board[i][j]:
                    return self.board[i][j]
        # check diagonal right
        for i in range(HEIGHT-3):
            for j in range(3):
                if self.board[i][j]!=0 and self.board[i+1][j+1]==self.board[i][j] and self.board[i+2][j+2]==self.board[i][j] and self.board[i+3][j+3]==self.board[i][j]:
                    return self.board[i][j]
        # not finished
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if self.board[i][j] == 0:
                    return 0
        # tied
        return 3