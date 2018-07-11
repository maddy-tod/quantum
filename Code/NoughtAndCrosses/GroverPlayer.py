from player import Player
from qiskit_acqua import run_algorithm

class GroverPlayer(Player) :

    # move to file at some point
    rules_cnf = """
    c All the rules that can be applied to play tic tac toe
    c The current configuration is appended at the end
    c Current idea is val -> all options
    p cnf 9 2
    -1 -2 -3 -4 -5 -7 -9 0
    """




    def __init__(self, givenLetter):
        super(GroverPlayer, self).__init__(givenLetter)


    def takeTurn(self, board):

        # Turn the current board config into SAT
        currentConfig = ""
        index = 1
        for row in board:
            for col in row:
                if col == self.letter:
                    currentConfig = currentConfig + str(-index) + " "
                elif col == self.notLetter:
                    currentConfig = currentConfig + str(index) + " "
                index += 1

        # Add the current config to the rules
        if len(currentConfig) > 1 :
            currentConfig += "0"

            self.rules_cnf += currentConfig


        newBoard = self.runGrover()


        return self.convertFromSAT(newBoard, board)

    def runGrover(self) :


        params = {
            'problem': {'name': 'search'},
            'algorithm': {'name': 'Grover'},
            'oracle': {'name': 'SAT', 'cnf': self.rules_cnf},
            'backend': {'name': 'local_qasm_simulator'}
        }

        result = run_algorithm(params)
        print(result['result'])
        return result['result']



    def convertFromSAT(self, newBoard, board) :

        index = 0
        for row in board:
            for col in row:
                if newBoard[index] < 0 and board[row][col] == '0' :
                    board[row][col] = self.letter
                    return board

        print("oh dear :(")
        return board
