# Import the utils
import utils
import re

# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute


# Create a Quantum Register with 2 qubits.
q = QuantumRegister(2)
# Create a Classical Register with 2 bits.
c = ClassicalRegister(2)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)

# These parts are common to all searches
def setup() :
    qc.h(q[0])
    qc.h(q[1])

def end():
    qc.h(q[0])
    qc.h(q[1])

    qc.x(q[0])
    qc.x(q[1])

    qc.h(q[1])

    qc.cx(q[0], q[1])

    qc.h(q[1])

    qc.x(q[0])
    qc.x(q[1])

    qc.h(q[0])
    qc.h(q[1])

    # Add a Measure gate to see the state.
    qc.measure(q, c)

# Change the oracle depending on what the user wants to find
def oracle(input) :

    # Exact configuration came from the website
    if input[0] == '0' :
        qc.s(q[0])
    if input[1] == '0':
        qc.s(q[1])


    qc.h(q[1])
    qc.cx(q[0], q[1])
    qc.h(q[1])

    if input[0] =='0' :
        qc.s(q[0])
    if input[1] == '0':
        qc.s(q[1])




setup()

# Get a valid thing to search for from the user
inp = input("What are you looking for?")
while not re.match("^(0|1){2}$", inp) :
    inp = input("What are you looking for?")

# Add the search specific gates
oracle(inp)

end()


# Compile and run the Quantum circuit on a simulator backend
job_sim = execute(qc, "local_qasm_simulator")
sim_result = job_sim.result()

# Show the results
print("simulation: ", sim_result)
# Returns a dict
utils.pprint(sim_result.get_counts(qc))

print("You were looking for " + inp)
print("This was found " + str(sim_result.get_counts(qc).get(inp)) + " times")




