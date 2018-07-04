# Multi-qubit gates
|> is called the ket, and in multi-qubit gates there are now 2 numbers inside it giving the states |00>, |01>, |10> and |11>. The first number is the state of the 2nd qubit and the second of the 1st qubit - ie it's back to front. It is easy to remember by thinking that the right most number is always the 1st qubit.

Though there are 2-qubit gates, there are not any higher order gates due to the technical challenges of building them. These operations are built up from 1 and 2 qubit gates.

*Any multi-qubit logic gate can be made up from CNOT and single qubit gates*


### CNOT gate
Similar to an if statement. If the control bit (the right most bit) is 1, then flip the other bit else leave it.
This gives it the 'Truth table' below :

| Before | After |
| ---    | ---   |
| \|00>  | \|00> |
| \|10>  | \|10> |
| \|01>  | \|11> |
| \|11>  | \|01> |

#### NB in the composer the small circle represents the control qubit, and the large circle with a plus represents the affected qubit

CNOT gates are difficult to make, so their numbers should be kept as low as possible.


### Toffoli Gates
These are classical gates that can also be implemented on a quantum computer due to the fact the gate is its own inverse. A Toffoli gate can be thought of as a CCNOT gate - so a NOT gate with 2 control wires. This is implemented as 3 inputs - a,b,c -  and 3 outputs - a,b, c XOR (a AND b).

This principle can also be expanded for example a NAND gate can be implemented when c = 1. (It can be helpful to draw these circuits out to work through examples)


### Entanglement
Entanglement is not technically a gate, but can be induced as a combination of gates. Entanglement causes 2 qubits to behave in ways which are individually random, but not independent.
#### An entangled state cannot be described as simply a list of the states of the individual qubits
The state (|00> +|01>)/ root 2 is not entangled as the 1st qubit (right most) is in the superposed single qubit state (|0> +|1>)/root 2. However the state (|01> + |10>)/root 2 is entangled.
When you measure one qubit in an entangled state it behaves randomly, but the result of the measurement allows you to completely predict how the other qubit would behave is measured in the same way. This *never* occurs in unentangled states.
These diagrams show Bell states, and the graphs below show that the results are exactly what you would expect them to be.
![Bell states composer](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/bellstate1y9ihszbafvpfogvi.png)
![Bell states graph](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/bellstate23fjnac7mh0ejyvi.png)


### 3 qubit states
The superposition between the states where all 3 qubits are in the |0> state and the one where all 3 qubits are in the |1> state is called the GHZ state. This is written (1/root 2)(|000> - |111>).

The combined properties of a 3 qubit system can be predicted - eg what happens if we measure all 3 qubits in the X direction (XXX) - but the individual outcomes per qubit cannot be predicted. When all 3 qubits are measured in the X direction the result is always -1. If 2 are measured in the Y direction and 1 in the X we get 1. The result is calculated by multiplying all the values read together, where a read 0 is mapped to a 1, and a read 1 is mapped to a -1.


### Spooky Action at a distance
A helpful [video](https://www.youtube.com/watch?v=ZuvK-od647c) explaining entanglement and Bell tests.

Einstein described entanglement as spooky action at a distance as it seemed to suggest that the qubits could communicate at speeds faster than the speed of light, which went against his theory of relativity. He theorised that the particles 'agreed' before they were separated and measured which spin they would have, however the Bell test disproves this. Over several Bell tests you can show  statistically that the theory of local variables must not be true, and a GHZ circuit can also show this but in one run.


### Circuits
For quantum computers to work, all the gates they use must be reversible - so you can go from output to input as well as input to output. This is an issue when interfacing with conventional circuits as not all the gates they use are reversible. For example the input 11 to an AND gate is the only possible input to produce a 1, however if we get the output 0 there are 3 possible inputs - 00, 01 and 10. To get around this a trick is used. This is adding a control wire (often called d) down which the value 0 is always sent. This is then XOR'd with the output of the function to give the overall output. This is used to make the number of outputs equal to the number of inputs. The inputs are a, b and d, and the outputs are a,b and c (which is d xor the result of F(a,b) where F is the function implemented by the gate).

In reality this technique is not often used as it requires a lot more memory and there are optimisations that can be made.

Quantum circuits are also not allowed loops or any 'copying' of values (as this is against the laws of quantum mechanics).

### Unitary Matrices
All gates can be written in the form of matrices, which can then be multiplied by the matrix (a,b) to give the resulting values of a and b. However, there are some limitations on what the matrices can be due to [the Born Rule](Intro.md). The result of this is that the matrices that can be represented must be unitary. This means that the [adjoint of the matrix](https://en.wikipedia.org/wiki/Adjugate_matrix) when multiplied by the gate matrix must give the identity matrix (ie *U^t * U = I*).

This unitary constraint is the only constraint on the types of operation that can be implemented by a quantum gate! Not all classical gates are unitary - for example there is a necessary loss of information from the output of an AND gate as it goes from 2 bits to just 1, and if you know the output bit was 0 there is no way to tell what the input bits were.
