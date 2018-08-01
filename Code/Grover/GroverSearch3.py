# Import the utils
import utils
import re

# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute


q  = None
c  = None
qc = None


# These parts are common to all searches
def setup() :

    global q,c,qc
    # Create a Quantum Register with 2 qubits.
    q = QuantumRegister(3)
    # Create a Classical Register with 2 bits.
    c = ClassicalRegister(3)
    # Create a Quantum Circuit
    qc = QuantumCircuit(q, c)

    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])

def tp(reg):
    global qc

    qc.t(reg)
    qc.t(reg)
    qc.t(reg)
    qc.t(reg)
    qc.t(reg)
    qc.t(reg)
    qc.t(reg)

def ccz():
    # definition from here https://www.researchgate.net/figure/282611947_Fig-1-a-Schematic-circuit-of-a-half-adder-where-a-and-b-represent-inputs-and-sum-and
    global q, qc
    qc.cx(q[1], q[2])
    tp(q[2])
    qc.cx(q[0], q[2])
    qc.t(q[2])
    qc.cx(q[1], q[2])
    tp(q[2])
    qc.cx(q[0], q[2])
    qc.t(q[1])
    qc.t(q[2])
    qc.cx(q[0], q[1])
    tp(q[1])
    qc.cx(q[0], q[1])
    qc.t(q[0])


def end():
    global q, c, qc

    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])

    qc.x(q[0])
    qc.x(q[1])
    qc.x(q[2])

    #CCZ gate
    ccz()

    qc.x(q[0])
    qc.x(q[1])
    qc.x(q[2])

    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])

    # Add a Measure gate to see the state.
    qc.measure(q, c)

# Change the oracle depending on what the user wants to find
def oracle(inp) :
    global q, qc

     # oracle info from here https://arxiv.org/pdf/1703.10535.pdf
    if inp[2] == '0':
        qc.x(q[0])
    if inp[1] == '0':
        qc.x(q[1])
    if inp[0] == '0':
        qc.x(q[2])


    # CCZ gate
    ccz()

    if inp[2] == '0':
        qc.x(q[0])
    if inp[1] == '0':
        qc.x(q[1])
    if inp[0] == '0':
        qc.x(q[2])




def runGrover(config):
    setup()


    # Add the search specific gates
    oracle(config)

    end()

    # Compile and run the Quantum circuit on a simulator backend
    job_sim = execute(qc, "local_qasm_simulator")
    sim_result = job_sim.result()

    # Show the results
    print("simulation: ", sim_result)
    # Returns a dict
    utils.pprint(sim_result.get_counts(qc))

    print("Searching for : " + config)
    print("Found         : " + utils.getMax(sim_result.get_counts(qc)))
    print("This was found " + str(sim_result.get_counts(qc).get(config)) + " times")


options = ["000", "100","010","001","110","101","011","111"]

for option in options:
    runGrover(option)




