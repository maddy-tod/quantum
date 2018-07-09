from player import Player
import random
class RandomPlayer(Player) :


    def __init__(self, givenLetter):
        super(RandomPlayer, self).__init__(givenLetter)


    def takeTurn(self, board):
        print('Its the random computers turn!')

        move = random.randint(0,8)
        movePair = (int(int(move) / 3), int(move) % 3)

        while board[movePair[0]][movePair[1]] != '0' :
            move = random.randint(0, 8)
            movePair = (int(int(move) / 3), int(move) % 3)

        board[movePair[0]][movePair[1]] = self.letter

        return board