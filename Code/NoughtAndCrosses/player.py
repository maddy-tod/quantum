import random

class Player :
    def __init__(self, givenLetter):
        self.letter = givenLetter
        if givenLetter == 'S':
            self.notLetter = 'X'
        else :
            self.notLetter = 'S'

    def takeTurn(self, board):
        return board

    def chooseRandomly(self, board) :
        x = random.randint(0,2)
        y = random.randint(0,2)

        while board[x][y] != '0':
            x = random.randint(0, 2)
            y = random.randint(0, 2)

        board[x][y] = self.letter

        return board
