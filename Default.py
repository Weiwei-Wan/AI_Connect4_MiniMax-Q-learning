import random

HEIGHT = 5
WIDTH = 6

def defaltAlgo(the_player, board):
    # check row win
    for i in range(HEIGHT):
        # left
        for j in range(1, WIDTH-2):
            if board[i][j]!=0 and board[i][j+1]==board[i][j] and board[i][j+2]==board[i][j] and board[i][j-1]==0:
                if board[i-1][j-1]!=0:
                    return j-1 # i, j-1
        # right
        for j in range(3):
            if board[i][j]!=0 and board[i][j+1]==board[i][j] and board[i][j+2]==board[i][j] and board[i][j+3]==0:
                if board[i-1][j+3]!=0:
                    return j+3 #i, j+3
    # check column win
    for j in range(WIDTH):
        for i in range(1, HEIGHT-2):
            if board[i][j]!=0 and board[i+1][j]==board[i][j] and board[i+2][j]==board[i][j] and board[i-1][j]==0:
                return j #i-1, j
    # check diagonal win left
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i<HEIGHT-1 and j>0 and i-2>0 and j+2<WIDTH and board[i][j]!=0 and board[i-1][j+1]==board[i][j] and board[i-2][j+2]==board[i][j] and board[i+1][j-1]==0 and (i+1==HEIGHT-1 or board[i+2][j-1]!=0):
                return j-1 # i+1, j-1
            if i-3>0 and j+3<WIDTH and board[i][j]!=0 and board[i-1][j+1]==board[i][j] and board[i-2][j+2]==board[i][j] and board[i-3][j+3]==0 and board[i-2][j+3]!=0:
                return j+3 # i-3, j+3
    # check diagonal win right
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i>0 and j>0 and i+2<HEIGHT and j+2<WIDTH and board[i][j]!=0 and board[i+1][j+1]==board[i][j] and board[i+2][j+2]==board[i][j] and board[i-1][j-1]==0 and board[i][j-1]!=0:
                return j-1 # i-1, j-1
            if i+3<HEIGHT and j+3<WIDTH and board[i][j]!=0 and board[i+1][j+1]==board[i][j] and board[i+2][j+2]==board[i][j] and board[i+3][j+3]==0 and (i+3==HEIGHT-1 or board[i+4][j+3]!=0):
                return j+3 # i+3, j+3

    choices = []
    for j in range(WIDTH):
        for i in range(HEIGHT):
            if board[i][j] == 0:
                choices.append(j)
                break
        
    final_choice = random.choice(choices)
    return final_choice
    