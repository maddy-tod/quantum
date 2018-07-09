from userPlayer import UserPlayer
from TGatePlayer import TGatePlayer
from randomPlayer import RandomPlayer
import sys, os

# Takes a sting of 1s and 0s to represent the board
def printBoard(board) :

    for row in board:
        rowStr = ""
        for element in row:
            rowStr = rowStr + element + "  "
        print(rowStr)




def finished(board) :
    for i in range(0, 3):
        if board[i][0] != '0' and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return True, board[i][0]
        if board[0][i] != '0' and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return True, board[0][i]

    if board[1][1] != '0':
        if board[0][0] == board[1][1] and board[0][0] == board[2][2] :
            return True, board[1][1]
        if board[0][2] == board[1][1] and board[2][0] == board[1][1]:
            return True, board[1][1]


    # Check to see if the board is complete
    for i in range (0, len(board)) :
        for j in range(0, len(board[i])):
            if board[i][j] == '0':
                return False, '0'
    return True, 'No one'



def playGameWithPlayers(playerOne, playerTwo):
    board = [['0', '0', '0'], ['0', '0', '0'],['0', '0', '0']]

    print("Welcome to quantum noughts and crosses!")


    isPlayerOneTurn = True;
    while not finished(board)[0] :
        printBoard(board)
        if isPlayerOneTurn :
            playerOne.takeTurn(board)
        else :
            playerTwo.takeTurn(board)
        isPlayerOneTurn = not isPlayerOneTurn

    printBoard(board)
    print(finished(board)[1] + " won!")
    return finished(board)[1]

def playGame():
    playerOne = UserPlayer('X')
    playerTwo = TGatePlayer('S')

    playGameWithPlayers(playerOne, playerTwo)


# Uncomment this line to play
#playGame()
