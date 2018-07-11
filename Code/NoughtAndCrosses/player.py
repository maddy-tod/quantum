class Player :
    def __init__(self, givenLetter):
        self.letter = givenLetter
        if givenLetter == 'S':
            self.notLetter = 'X'
        else :
            self.notLetter = 'S'

    def takeTurn(self, board):
        return board


