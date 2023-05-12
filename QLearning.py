import numpy as np

HEIGHT = 5
WIDTH = 6
# rewards
WIN_VALUE = 1.0
LOSS_VALUE = 0.0 
TIED_VALUE = 0.5

alpha=0.9 # learning rate
gamma=0.95 # discount factor
q_init=0.6 # init q table

class PlayQlearning():
    def __init__(self, player):
        self.QTable = {}
        self.history = []
        self.player = 1
        self.opponent = 2
        if (player == 2):
            self.opponent = 1
            self.player = 2

    def checkWinner(self, the_board):
    # check column
        for i in range(HEIGHT-3):
            for j in range(WIDTH):
                if the_board[i][j]!=0 and the_board[i+1][j]==the_board[i][j] and the_board[i+2][j]==the_board[i][j] and the_board[i+3][j]==the_board[i][j]:
                    return the_board[i][j]
        # check row
        for j in range(WIDTH-3):
            for i in range(HEIGHT):
                if the_board[i][j]!=0 and the_board[i][j+1]==the_board[i][j] and the_board[i][j+2]==the_board[i][j] and the_board[i][j+3]==the_board[i][j]:
                    return the_board[i][j]
        # check diagonal left
        for i in range(3,HEIGHT):
            for j in range(WIDTH-3):
                if the_board[i][j]!=0 and the_board[i-1][j+1]==the_board[i][j] and the_board[i-2][j+2]==the_board[i][j] and the_board[i-3][j+3]==the_board[i][j]:
                    return the_board[i][j]
        # check diagonal right
        for i in range(HEIGHT-3):
            for j in range(3):
                if the_board[i][j]!=0 and the_board[i+1][j+1]==the_board[i][j] and the_board[i+2][j+2]==the_board[i][j] and the_board[i+3][j+3]==the_board[i][j]:
                    return the_board[i][j]
        # not finished
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if the_board[i][j] == 0:
                    return 0
        # tied
        return 3

    # give the np board a special index
    def indexBoard(self, the_board):
        index = ""
        for i in range(HEIGHT):
            for j in range(WIDTH):
                index += str(the_board[i][j])
        return index

    def getQValue(self, board_index):
        if board_index in self.QTable:
            value = self.QTable[board_index]
        else:
            value = q_init*np.ones((WIDTH))
            self.QTable[board_index] = value
        return value
    
    def getQTable(self):
        return self.QTable

    def checkPosAvaliable(self, y, the_board):
        if y<0 or y>=WIDTH:
            return False
        if the_board[0][y] != 0:
            return False
        return True

    def findBestMove(self, the_board):
        # get the max pos
        boardIndex = self.indexBoard(the_board)
        qValue = self.getQValue(boardIndex)
        while True:
            maxIndex = np.argmax(qValue) # get the max value index
            if self.checkPosAvaliable(maxIndex, the_board):
                break
            else:
                qValue[maxIndex] = -1.0
        self.history.append((boardIndex, maxIndex))
        return maxIndex

    def finalResult(self, winner):
        if winner == 3:
            final_value = TIED_VALUE
        elif winner == self.player:
            final_value = WIN_VALUE
        elif winner == self.opponent:
            final_value = LOSS_VALUE

        self.history.reverse()
        next_max = -1.0
        for h in self.history:
            qValue = self.getQValue(h[0])
            if next_max < 0:  # first loop
                qValue[h[1]] = final_value
            else:
                qValue[h[1]] = qValue[h[1]] * (1.0-alpha) + alpha * gamma * next_max

            next_max = qValue.max()
            #self.QTable[h[0]] = qValue
    
    def newGame(self):
        self.history = []