# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute


# Create a Quantum Register with 1 qubit.
q = QuantumRegister(1)
# Create a Classical Register with 1 bits.
c = ClassicalRegister(1)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.measure(q[0], c[0])


# Compile and run the Quantum circuit on a simulator backend
job_sim = execute(qc, "local_qasm_simulator", shots=10)
sim_result = job_sim.result()

# Show the results
print("simulation: ", sim_result)

currentMax = 0
currentVal = 0

for key, value in sim_result.get_counts(qc).items():
    if value > currentMax :
        currentMax = value
        currentVal = int(key)

res = "Your coin flip returned "
if currentVal > 0 :
    res += "HEADS"
else :
    res += "TAILS"


print(res)
