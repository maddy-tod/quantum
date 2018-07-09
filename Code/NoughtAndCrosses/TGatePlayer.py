# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from player import Player

class TGatePlayer(Player) :


    def __init__(self, givenLetter):
        super(TGatePlayer, self).__init__(givenLetter)



    def takeTurn(self, board):
        print('Its the quantum computers turn!')
        qc = createQCircuit(board)

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
            return board

        for j in range(0, len(bestMoves)):
            for i, c in enumerate(bestMoves[j]):
                if c == "1":
                    index = (int(i / 3), i % 3)
                    if board[index[0]][index[1]] == '0':
                        board[index[0]][index[1]] = 'S'
                        return board

        print("Oh no the computer didn't find anything :(")
        return board


def createQCircuit(board):
    # Create a Quantum Register with the necessary number of qubits
    q = QuantumRegister(9)
    # Create a Classical Register with the necessary number of bits
    c = ClassicalRegister(9)
    # Create a Quantum Circuit
    qc = QuantumCircuit(q, c)

    index = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 'X':
                qc.x(q[index])
            else:
                qc.h(q[index])
            index+=1

    index = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 'X':
                # add T gate to every option
                # row checks
                if i + 1 < 3 :
                    qc.t(q[index+1])
                if i - 1 >= 0:
                    qc.t(q[index-1])
                # column checks
                if j + 1 < 3 and index+3 < 9:
                    qc.t(q[index+3])
                if j - 1 >= 0 and index-3 >= 0:
                    qc.t(q[index-3])
                # diagonal checks
                if i == j :
                    qc.t(q[0])
                    qc.t(q[4])
                    qc.t(q[8])
                if (i == 0 and j == 2) or (i == 2 and j == 0):
                    qc.t(q[2])
                    qc.t(q[4])
                    qc.t(q[6])

            index += 1

    # apply an H gate and measure
    qc.h(q)
    qc.measure(q, c)
    return qc








"""
    # Attempt 2 - Pairs of CNOT gates based off close indices
    # Add the gates specific to this board
    index = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 'X':
                # just a test at this point
                if index - 3 >= 0:
                    qc.h(q[index - 3])
                if index + 3 < 9:
                    qc.h(q[index + 3])

                if index - 3 >= 0 and index + 3 < 9:
                    qc.cx(q[index+3], q[index - 3])

                # deal with vertical moves only currently
                if index - 3 >= 0 :
                    qc.cx(q[index], q[index-3])
                if index + 3 < 9 :
                    qc.cx(q[index], q[index+3])
            index += 1
    qc.measure(q, c)
    return qc

"""

""" Attempt 1 - cycle of CNOT gates

    # Add the gates specific to this board
    index = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 'X':
                print("Setting " + str(i) + " " + str(j) + " to have an H gate")
                qc.h(q[index])

    # Set up loop of CNOT gates - currently just loop could be later refined
    # usage - cx(ctl, tgt)
    for i in range(0, 7):
        qc.cx(q[i], q[i + 1])
    qc.cx(q[8], q[0])

    qc.measure(q, c)

    return qc
"""

