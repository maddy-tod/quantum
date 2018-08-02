# Import the utils
import math
import sys
import os
sys.path.append(os.path.abspath('../QUtils'))
from qutils import pprint, graph

# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute


# Create a Quantum Register with 2 qubits.
q = QuantumRegister(3)
# Create a Classical Register with 2 bits.
c = ClassicalRegister(3)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)


# move the qubits into a superpostion such that when they have an H gate and a Measure
# applied they are equally likely to collapse to 0 or 1
qc.h(q)
qc.s(q)

pi = math.pi
# add the gates to get the normal distribution

# makes 111 less likely
qc.crz(-0.3*pi, q[2], q[1])
qc.crz(-0.3*pi, q[1], q[0])

# some how encourages 100
qc.x(q[2])
qc.crz(-0.3*pi, q[0], q[1])
qc.crz(-0.3*pi, q[1], q[2])
qc.crz(-0.3*pi, q[0], q[2])
qc.x(q[2])


qc.h(q)
# Add a Measure gate to see the state.
qc.measure(q, c)
# Compile and run the Quantum circuit on a simulator backend
job_sim = execute(qc, "local_qasm_simulator", shots=1000)
sim_result = job_sim.result()

# Show the results
print("simulation: ", sim_result)
# Returns a dict
pprint(sim_result.get_counts(qc))
graph(sim_result.get_counts(qc))