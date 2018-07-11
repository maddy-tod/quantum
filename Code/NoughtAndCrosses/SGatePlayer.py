# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from player import Player
import random

# Exactly the same as the T gate player but with S gates

class SGatePlayer(Player) :


    def __init__(self, givenLetter):
        super(SGatePlayer, self).__init__(givenLetter)



    def takeTurn(self, board):
        print('Its the quantum computers turn!')
        qc = createQCircuit(self, board)

        # Compile and run the Quantum circuit on a simulator backend
        job_sim = execute(qc, "local_qasm_simulator", shots=100)
        sim_result = job_sim.result()

        # Show the results
        print("simulation: ", sim_result)

        bestMoves = []
        bestVal = 0;

        # iterate over and get the best move - store list of fairly good moves though
        # key is binary string and value is the number of hits
        for key, value in sim_result.get_counts(qc).items():
            print(key + " = " + str(value))
            if not key == "000000000":
                if value > bestVal:
                    bestMoves.append(key)
                    bestVal = value

        if bestVal == 0:
            print("Oh no the computer didn't find anything :(")
            # need to return a random val
            x = random.randint(0, 2)
            y = random.randint(0, 2)

            while board[x][y] != '0' :
                x = random.randint(0, 2)
                y = random.randint(0, 2)

            board[x][y] = self.letter
            return board

        # Start from the end of the array of moves - as this is where the best move will be
        for config in reversed(bestMoves):
            # Iterates over a string returning a tuple of an incrementing index and the element
            for index, val in enumerate(config):
                if val == "1":
                    index = (int(index / 3), index % 3)
                    if board[index[0]][index[1]] == '0':
                        board[index[0]][index[1]] = self.letter
                        return board

        print("Oh no the computer didn't find anything :(")
        return board


def createQCircuit(self, board):
    # Create a Quantum Register with the necessary number of qubits
    q = QuantumRegister(9)
    # Create a Classical Register with the necessary number of bits
    c = ClassicalRegister(9)
    # Create a Quantum Circuit
    qc = QuantumCircuit(q, c)

    index = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == self.notLetter:
                qc.x(q[index])
            else:
                qc.h(q[index])
            index+=1

    index = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == self.notLetter:
                # add T gate to every option
                # row checks
                if i + 1 < 3 :
                    qc.s(q[index+1])
                if i - 1 >= 0:
                    qc.s(q[index-1])
                # column checks
                if j + 1 < 3 and index+3 < 9:
                    qc.s(q[index+3])
                if j - 1 >= 0 and index-3 >= 0:
                    qc.s(q[index-3])
                # diagonal checks
                if i == j :
                    qc.s(q[0])
                    qc.s(q[4])
                    qc.s(q[8])
                if (i == 0 and j == 2) or (i == 2 and j == 0):
                    qc.s(q[2])
                    qc.s(q[4])
                    qc.s(q[6])

            index += 1

    # apply an H gate and measure
    qc.h(q)
    qc.measure(q, c)
    return qc

