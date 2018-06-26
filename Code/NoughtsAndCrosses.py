# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute


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
                if (i == 0 and j == 2) or (i == 2 and j == 2):
                    qc.t(q[2])
                    qc.t(q[4])
                    qc.t(q[6])

            index += 1

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





# Takes a sting of 1s and 0s to represent the board
def printBoard(board) :

    for row in board:
        rowStr = ""
        for element in row:
            rowStr = rowStr + element + "  "
        print(rowStr)




def userTurn(board):
    print('Its your turn!')
    move = input('Enter your move from 0 to 8 ')
    while not move.isdigit() :
        move = input('Enter your move from 0 to 8 ')


    move = int(move)
    movePair = (int(int(move)/3), int(move) %3)
    while board[movePair[0]][movePair[1]] != '0' or move > 8:
        move = int (input('Oops try again that space is already taken! Enter your move from 0 to 1 '))
        movePair = (int(int(move)/3), int(move) %3)

    board[movePair[0]][movePair[1]] = 'X'

def computerTurn(board):
    print('Its the computers turn!')
    qc = createQCircuit(board)

    # Compile and run the Quantum circuit on a simulator backend
    job_sim = execute(qc, "local_qasm_simulator", shots=1000)
    sim_result = job_sim.result()

    # Show the results
    print("simulation: ", sim_result)


    bestMoves = []
    bestVal = 0;

    # iterate over and get the best move - store list of fairly good moves though
    for key, value in sim_result.get_counts(qc).items():
        #print(key + " " + str(value))
        if not key == "000000000" :
            if value > bestVal :
                bestMoves.append(key)
                bestVal = value


    if bestVal == 0 :
        print("Oh no the computer didn't find anything :(")
        return

    for j in range (0,len(bestMoves)):
        for i, c in enumerate(bestMoves[j]):
            if c == "1":
                index = (int(i/3), i%3)
                if board[index[0]][index[1]] == '0':
                    board[index[0]][index[1]] = 'S'
                    return

    print("Oh no the computer didn't find anything :(")


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

def playGame():
    board = [['0', '0', '0'], ['0', '0', '0'],['0', '0', '0']]

    print("Welcome to quantum noughts and crosses!")

    isUserTurn = True;
    while not finished(board)[0] :
        printBoard(board)
        if isUserTurn :
            userTurn(board)
        else :
            computerTurn(board)
        isUserTurn = not isUserTurn

    printBoard(board)
    print(finished(board)[1] + " won!")


playGame()