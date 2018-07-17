from player import Player
from qiskit_acqua import run_algorithm
import itertools


class GroverPlayer(Player) :

    # move to file at some point
    rules_cnf = """
    c All the rules that can be applied to play tic tac toe
    c The current configuration is appended at the end
    c Current idea is a coordinate system 
    c and currently only pays attention to row/col
    p cnf 6 3
    -1 -2 -3 0
    -4 -5 -6 0
    """




    def __init__(self, givenLetter):
        super(GroverPlayer, self).__init__(givenLetter)


    def takeTurn(self, board):

        # Turn the current board config into SAT
        # Any opposing letters are added as true variables
        currentConfig = ""
        alreadyAdded = []

        for col in range (0, len(board)) :
            for row in range (0, len(board[col])):

                if board[col][row] == self.notLetter :

                    vals_to_add = [str(col + 1) ,str(row + 4)]
                    if vals_to_add[0] in alreadyAdded:
                        vals_to_add[0] = ""
                    if vals_to_add[1] in alreadyAdded:
                        vals_to_add[1] = ""
                    currentConfig = currentConfig + vals_to_add[0] + " " + vals_to_add[1] + " "

                    alreadyAdded.append(vals_to_add[0])
                    alreadyAdded.append(vals_to_add[1])

        currentRules = self.rules_cnf

        # Add the current config to the rules
        if len(currentConfig) > 0 :
            currentConfig += "0"
            currentRules += currentConfig


       
        newBoard = self.runGrover(currentRules)

        return self.convertFromSAT(newBoard, board)

    @staticmethod
    def runGrover(currentRules) :
        

        params = {
            'problem': {'name': 'search'},
            'algorithm': {'name': 'Grover'},
            'oracle': {'name': 'SAT', 'cnf': currentRules},
            'backend': {'name': 'local_qasm_simulator'}
        }

        result = run_algorithm(params)
        print(result['result'])
        return result['result']



    def convertFromSAT(self, newBoard, board) :

        newBoard = list(filter(lambda x: x < 0, newBoard))
        newBoard = list(map(lambda x : x*-1, newBoard))

        rows = [x for x in newBoard if x < 4]
        cols = [x for x in newBoard if x not in rows]
        print("cols = ")
        print(cols)
        rows = list(map(lambda x : x-1 , rows))
        cols = list(map(lambda x : x-4 , cols))

        if len(newBoard) == 0 :
            print("o fudge")
            return board

        
        # gen all possible coords
        for x, y in itertools.product(rows, cols):
            print(str(x) + " " + str(y)) 
            if board[x][y] == '0' :
                board[x][y] = self.letter
                print(str(x) + " !!!! " + str(y))
                return board


        print("o fudge 2.0")
        return self.chooseRandomly(board)




# First attempt - too many variables and too many rules
"""
    c All the rules that can be applied to play tic tac toe
    c The current configuration is appended at the end
    c Current idea is val -> all options
    p cnf 9 10
    -1 -2 -3 -4 -5 -7 -9 0
    -2 -1 -3 -5 -8 0
    -3 -1 -2 -5 -6 -7 -9 0
    -4 -1 -5 -6 -7 0
    -5 -1 -2 -3 -4 -6 -7 -8 -9 0
    -6 -3 -4 -5 -9 0
    -7 -1 -3 -4 -5 -8 -9 0
    -8 -2 -5 -7 -9 0
    -9 -1 -3 -5 -6 -7 -8 0
    """