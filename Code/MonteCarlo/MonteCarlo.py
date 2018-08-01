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

    adder(size)

    qc.measure(q,c)

def adder(size):
    # size is the number of qubits per number to be added
    # must be > = 2

    carry = 3 * size
    a = 0
    b = size
    sum = 2 * size

    # deal with the 1st digit
    # set the carry
    qc.ccx(q[a+2], q[b+2], q[carry])
    # add to the sum
    qc.cx(q[a+2], q[sum+2])
    qc.cx(q[b+2], q[sum+2])

    # add the carry to the next sum digit
    qc.cx(q[carry], q[sum+1])
    # reset the carry
    qc.ccx(q[a+2], q[b+2], q[carry])

    # get carry for new digits
    qc.ccx(q[a+1], q[b+1], q[carry])
    qc.ccx(q[sum+1], q[b+1], q[carry])
    qc.ccx(q[a+1], q[sum+1], q[carry])

    # add the new digits
    qc.cx(q[a+1], q[sum+1])
    qc.cx(q[b+1], q[sum+1])

    # add the carry to the next sum digit
    qc.cx(q[carry], q[sum])
    # reset the carry
    qc.ccx(q[a+1], q[b+1], q[carry])
    qc.x(q[sum+1])
    qc.ccx(q[b+1], q[sum+1], q[carry])
    qc.ccx(q[a+1], q[sum+1], q[carry])
    qc.x(q[sum+1])

    # set the next carry
    qc.ccx(q[a], q[b], q[carry])
    qc.ccx(q[sum], q[b], q[carry])
    qc.ccx(q[a], q[sum], q[carry])

    # add the new digits
    qc.cx(q[a], q[sum])
    qc.cx(q[b], q[sum])


def run():
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
        a = int(res[0:3], 2)
        b = int(res[3:6], 2)
        ans = int(res[6:9], 2)
        carry =  int(res[9], 2) * 8

        # display results
        print(str(a) + " + " + str(b) + " = " + str(ans) + " + " + str(carry))
        #print(str(res[0:2]) + " + " + str(res[2:4]) + " = " + str(res[4:6]) + " + " + str(res[6]))

def main():
    size = input("How many qubits would you like to add?")
    while not size.isdecimal():
        size = input("How many qubits would you like to add?")

    prepareCircuit(int(size))
    run()

main()