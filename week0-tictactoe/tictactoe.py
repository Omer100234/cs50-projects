"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    counter = 0
    for row in board:
        for col in row:
            if(col != EMPTY):
                counter+=1
    if (counter%2==0):
        return X
    return O


def actions(board):
    s = set()
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                s.add((i,j))
    
    return s


def result(board, action):
    turn = player(board)
    b2 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    for i in range(3):
        for j in range(3):
            b2[i][j]=board[i][j]

    b2[action[0]][action[1]] = turn
    return b2


def winner(board):
    for i in board:
        if(i[0]==i[1] and i[0]==i[2] and i[0]!=EMPTY):  #checks rows
            return i[0]
        
    for i in range(3):
        if(board[0][i]==board[1][i] and board[0][i]==board[2][i] and board[0][i]!=EMPTY): #checks collumns
            return board[0][i]
        
    if (board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]!=EMPTY):   #checks diagonals
        return board[0][0]
    if (board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]!=EMPTY):
        return board[0][2]
    return None

def terminal(board):
    if (winner(board)==EMPTY and actions(board)):
        return False
    
    return True


def utility(board):
    w=winner(board)
    if(w==X):
        return 1
    if(w==O):
        return -1
    return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for a in actions(board):
        v = max(v, min_value(result(board, a)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for a in actions(board):
        v = min(v, max_value(result(board, a)))
    return v



def minimax(board):
    if terminal(board):
        return None

    current = player(board)
    best_action = None

    if current == X:
        best_score = float("-inf")
        for a in actions(board):
            score = min_value(result(board, a))
            if score > best_score:
                best_score = score
                best_action = a
    else:
        best_score = float("inf")
        for a in actions(board):
            score = max_value(result(board, a))
            if score < best_score:
                best_score = score
                best_action = a

    return best_action
