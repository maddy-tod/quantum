"""
General idea to use a quantum algorithm to solve monte carlo problems
1. Prepare all qubits into an equal superposition
    - currently 2 per input var
2. Run circuit 100 times
3. Will return info that can be turned into probability function

Circuit consists of
- Prepare all qubits into equal superposition
- Run through part of circuit which corresponds to conventional calculation
- Measure

"""


from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

import math
import sys
import os
sys.path.append(os.path.abspath('../QUtils'))
from qutils import pprint


# Create a Quantum Register with base size
q = QuantumRegister(10)
# Create a Classical Register with base size
c = ClassicalRegister(10)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)



def prepareCircuit(size):

    global q, c, qc
    # Create a Quantum Register with base size
    q = QuantumRegister((size * 3) + 1)
    # Create a Classical Register with base size
    c = ClassicalRegister((size * 3) + 1)
    # Create a Quantum Circuit
    qc = QuantumCircuit(q, c)




    # the 1st 2 size qubits into an equal superposition
    # they are the ones which are used to store the inputs
    for i in range (2*size):
        qc.h(q[i])


    # set A to have a normal distribution
    normal(0,size)


    adder(size)

    qc.measure(q,c)


# NB CURRENTLY ONLY FOR 3 QUBITS
def normal(base, size) :
    for i in range (0, size):
        qc.s(q[base+i])

    pi = math.pi
    # add the gates to get the normal distribution

    # makes 111 less likely
    qc.crz(-0.3 * pi, q[base + 2], q[base + 1])
    qc.crz(-0.3 * pi, q[base + 1], q[base])

    # some how encourages 100
    qc.x(q[base + 2])
    qc.crz(-0.3 * pi, q[base], q[base + 1])
    qc.crz(-0.3 * pi, q[base + 1], q[base + 2])
    qc.crz(-0.3 * pi, q[base], q[base + 2])
    qc.x(q[base + 2])

    for i in range (0, size):
        qc.h(q[base+i])

def adder(size):
    # size is the number of qubits per number to be added
    # must be > = 2

    carry = 3 * size
    a = 0
    b = size
    sum = 2 * size
    iter = size - 1

    # deal with the 1st digit
    # set the carry
    qc.ccx(q[a+iter], q[b+iter], q[carry])
    # add to the sum
    qc.cx(q[a+iter], q[sum+iter])
    qc.cx(q[b+iter], q[sum+iter])

    # add the carry to the next sum digit
    qc.cx(q[carry], q[sum+(iter - 1)])
    # reset the carry
    qc.ccx(q[a+iter], q[b+iter], q[carry])


    # start, end, step
    for i in range (iter-1, -1, -1 ):
        # set carry for new digits
        qc.ccx(q[a+i], q[b+i], q[carry])
        qc.ccx(q[sum+i], q[b+i], q[carry])
        qc.ccx(q[a+i], q[sum+i], q[carry])

        # add the new digits to sum
        qc.cx(q[a+i], q[sum+i])
        qc.cx(q[b+i], q[sum+i])


        if (i - 1 >= 0) :
            # add the carry to the next sum digit - -1 as for next digit
            qc.cx(q[carry], q[sum + i - 1])

            # reset the carry
            qc.ccx(q[a + i], q[b + i], q[carry])
            qc.x(q[sum + i])
            qc.ccx(q[b + i], q[sum + i], q[carry])
            qc.ccx(q[a + i], q[sum + i], q[carry])
            qc.x(q[sum + i])


def run(size):
    # Compile and run the Quantum circuit on a simulator backend
    job_sim = execute(qc, "local_qasm_simulator", shots=1000)
    sim_result = job_sim.result()

    # Show the results
    print("simulation: ", sim_result)
    pprint(sim_result.get_counts(qc))

    print()
    for res, c in sim_result.get_counts(qc).items() :
        # reverse the result
        res = res[::-1]

        # extract results into variables
        a = int(res[0:size], 2)
        b = int(res[size:(2*size)], 2)
        ans = int(res[(2*size):(3*size)], 2)
        carry =  int(res[(3*size)], 2) * (2 ** size)

        # display results
        print(str(a) + " + " + str(b) + " = " + str(ans) + " + " + str(carry))
        #print(str(res[0:2]) + " + " + str(res[2:4]) + " = " + str(res[4:6]) + " + " + str(res[6]))

def main():
    size = input("How many qubits would you like to add?")
    while not size.isdecimal():
        size = input("How many qubits would you like to add?")

    prepareCircuit(int(size))
    run(int(size))

main()