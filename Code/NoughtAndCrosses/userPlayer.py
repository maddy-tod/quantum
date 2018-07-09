from player import Player

class UserPlayer(Player) :


    def __init__(self, givenLetter):
        super(UserPlayer, self).__init__(givenLetter)


    def takeTurn(self, board):

        print('Its your turn!')
        move = input('Enter your move from 0 to 8 ')
        while not move.isdigit():
            move = input('Enter your move from 0 to 8 ')

        move = int(move)
        movePair = (int(int(move) / 3), int(move) % 3)
        while board[movePair[0]][movePair[1]] != '0' or move > 8:
            move = int(input('Oops try again that space is already taken! Enter your move from 0 to 1 '))
            movePair = (int(int(move) / 3), int(move) % 3)


        board[movePair[0]][movePair[1]] = self.letter

        return board


