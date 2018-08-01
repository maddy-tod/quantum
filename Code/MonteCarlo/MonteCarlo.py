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


# Create a Quantum Register with 4 qubit.
q = QuantumRegister(10)
# Create a Classical Register with 4 bits.
c = ClassicalRegister(10)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)



def prepareCircuit():
    # the 1st 4 qubits into an equal superposition
    # they are the ones which are used to store the inputs
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])
    qc.h(q[3])
    qc.h(q[4])
    qc.h(q[5])

    adder()

    qc.measure(q,c)

def adder():

    """   qc.ccx(q[1], q[3], q[6])
    qc.cx(q[3], q[5])
    qc.cx(q[1], q[5])
    qc.cx(q[0], q[4])
    qc.cx(q[2], q[4])

    qc.cx(q[6], q[4])
    """
    # deal with the 1st digit
    # set the carry
    qc.ccx(q[2], q[5], q[9])
    # add to the sum
    qc.cx(q[2], q[8])
    qc.cx(q[5], q[8])

    # add the carry to the next sum digit
    qc.cx(q[9], q[7])
    # reset the carry
    qc.ccx(q[2], q[5], q[9])

    # get carry for new digits
    qc.ccx(q[1], q[4], q[9])
    qc.ccx(q[7], q[4], q[9])
    qc.ccx(q[1], q[7], q[9])

    # add the new digits
    qc.cx(q[1], q[7])
    qc.cx(q[4], q[7])

    # add the carry to the next sum digit
    qc.cx(q[9], q[6])
    # reset the carry -  not working
    qc.ccx(q[1], q[4], q[9])
    qc.x(q[7])
    qc.ccx(q[4], q[7], q[9])
    qc.ccx(q[1], q[7], q[9])
    qc.x(q[7])

    #qc.ccx(q[1], q[4], q[9])
    #qc.ccx(q[7], q[4], q[9])
    #qc.ccx(q[1], q[7], q[9])


    # set the next carry
    qc.ccx(q[0], q[3], q[9])
    qc.ccx(q[6], q[3], q[9])
    qc.ccx(q[0], q[6], q[9])

    # add the new digits
    qc.cx(q[0], q[6])
    qc.cx(q[3], q[6])




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
    prepareCircuit()
    run()

main()