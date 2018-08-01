# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
import math

# Let user choose a max value for the random number
max = input('Enter your max bound ')

# Calculate how many bits are needed to achieve this
numBits = int(math.log(int(max), 2))

# Create a Quantum Register with the necessary number of qubits
q = QuantumRegister(numBits)
# Create a Classical Register with the necessary number of bits
c = ClassicalRegister(numBits)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)

# Set all gates to be 50/50 1 or 0, and measure all of them
qc.h(q)
qc.measure(q, c)

# Compile and run the Quantum circuit on a simulator backend
# Run twice to avoid annoying deprecation message (not relevant here)
job_sim = execute(qc, "local_qasm_simulator", shots=2)
sim_result = job_sim.result()

# Show the results
print("simulation: ", sim_result)

# return the result to the user
for key, value in sim_result.get_counts(qc).items():
    print('Your random number is ' + str(int(key, 2)))
    break

