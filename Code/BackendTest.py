# Import the QISKit SDK
from datetime import time
from pprint import pprint
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QISKitError
from qiskit import available_backends, execute, register, get_backend, compile
#from qiskit import least_busy

# Create a Quantum Register with 1 qubit.
q = QuantumRegister(1)
# Create a Classical Register with 1 bits.
c = ClassicalRegister(1)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.measure(q[0], c[0])

# Set your API Token.
# You can get it from https://quantumexperience.ng.bluemix.net/qx/account,
# looking for "Personal Access Token" section.
QX_TOKEN = 'ce5faaeedf5de0257bd0b2bc21aa6399fcbe2d1ff6e1c676024e9fda557fc87963638e8952e5cb502c5df7d4e9d89bf8ae6cf517fb8385d67093cd63c2c72db9'
QX_URL = "https://quantumexperience.ng.bluemix.net/api"

# Authenticate with the IBM Q API in order to use online devices.
# You need the API Token and the QX URL.
register(QX_TOKEN, QX_URL)


# Compile and run the Quantum Program on a real device backend
job_exp = execute(qc, 'ibmqx4', shots=1024, max_credits=10)

backend = get_backend('ibmqx4')

lapse = 0
interval = 10

while not job_exp.done:
    print('Status @ {} seconds'.format(interval * lapse))
    api.get_job(job_exp.id)['infoqueue']['position']
    print(job_exp.status)
    time.sleep(interval)
    lapse += 1
    pprint(get_backend(backend).status)
print(job_exp.status)


result = job_exp.result()

# Show the results
print(result)
print(result.get_data())


"""

print(available_backends())
backend = available_backends({'simulator': False})[0]

# Compile and run the Quantum circuit on a simulator backend
qobj = compile(qc, backend=backend, shots=2)
job = get_backend(backend).run(qobj)

lapse = 0
interval = 10

while not job.done:
    print('Status @ {} seconds'.format(interval * lapse))
    backend.get_job(job.id)['infoqueue']['position']
    print(job.status)
    time.sleep(interval)
    lapse += 1
    pprint(get_backend(backend).status)
print(job.status)

"""