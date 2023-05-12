import numpy as np

HEIGHT = 5
WIDTH = 6

def miniMaxAlgo(the_player, board):
    global player, opponent
    player = 1
    opponent = 2
    if (the_player == 2):
        opponent = 1
        player = 2
    return findBestMove(board)
            
def checkWinner(the_board):
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

def miniMax(the_board, heightMap, depth, isMax, alpha, beta):
    score = 0
    if checkWinner(the_board) == 3: # tied
        return 0
    elif checkWinner(the_board) == player: # win
        score = 10
        return score
    elif checkWinner(the_board) == opponent: # lose
        score = -10
        return score
    if depth == 6:
        return 0

    if isMax:	
        best = -1000
        for j in range(WIDTH):
            if heightMap[j]<HEIGHT:
                heightMap[j] += 1
                the_board[HEIGHT-int(heightMap[j])][j] = player
                new_best = max(best, miniMax(the_board, heightMap, depth + 1, not isMax, alpha, beta))
                the_board[HEIGHT-int(heightMap[j])][j] = 0
                heightMap[j] -= 1
                # alpha-beta pruning
                if new_best > best:
                    best = new_best
                if best >= beta:
                    return best
                if best > alpha:
                    alpha = best
        return new_best
    else:
        best = 1000
        for j in range(WIDTH):
            if heightMap[j]<HEIGHT:
                heightMap[j] += 1
                the_board[HEIGHT-int(heightMap[j])][j] = opponent
                new_best = min(best, miniMax(the_board, heightMap, depth + 1, not isMax, alpha, beta))
                the_board[HEIGHT-int(heightMap[j])][j] = 0
                heightMap[j] -= 1
                # alpha-beta pruning
                if new_best < best:
                    best = new_best
                if best <= alpha:
                    return best
                if best < beta:
                    beta = best
        return new_best

def findBestMove(the_board):
    bestVal = -1000
    bestMove = -1
    # get height map
    heightMap = np.zeros((WIDTH))
    for j in range(WIDTH):
        for i in range(HEIGHT):
            if the_board[HEIGHT-1-i][j] != 0:
                heightMap[j] += 1
	# find best move
    for j in range(WIDTH):
        if heightMap[j]<HEIGHT:
            # move
            heightMap[j] += 1
            the_board[HEIGHT-int(heightMap[j])][j] = player
            moveVal = miniMax(the_board, heightMap, 0, False, -1000, 1000)
            the_board[HEIGHT-int(heightMap[j])][j] = 0
            heightMap[j] -= 1
            if (moveVal > bestVal):				
                bestMove = j
                bestVal = moveVal
    return bestMove