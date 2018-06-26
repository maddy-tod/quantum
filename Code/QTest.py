# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute

# Create a Quantum Register with 2 qubits.
q = QuantumRegister(2)
# Create a Classical Register with 2 bits.
c = ClassicalRegister(2)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)


def bellState():
    # Add a H gate on qubit 0, putting this qubit in superposition.
    qc.h(q[0])
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
    # the qubits in a Bell state.
    qc.cx(q[0], q[1])


def twoH() :
    # Add a H gate on qubit 0, putting this qubit in superposition.
    qc.h(q[0])
    qc.h(q[1])


#bellState()
twoH()



# See a list of available local simulators
# print("Local backends: ", available_backends({'local': True}))

# Add a Measure gate to see the state.
qc.measure(q, c)
# Compile and run the Quantum circuit on a simulator backend
job_sim = execute(qc, "local_qasm_simulator")
sim_result = job_sim.result()

# Show the results
print("simulation: ", sim_result)
# Returns a dict
print(sim_result.get_counts(qc))
pprint(sim_result.get_counts(qc))




