# Multi-qubit gates
|> is called the ket, and in multi-qubit gates there are now 2 numbers inside it giving the states |00>, |01>, |10> and |11>. The first number is the state of the 2nd qubit and the second of the 1st qubit - ie it's back to front. It is easy to remember by thinking that the right most number is always the 1st qubit.

Though there are 2-qubit gates, there are not any higher order gates due to the technical challenges of building them. These operations are built up from 1 and 2 qubit gates.

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
