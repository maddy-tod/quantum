# Single qubit gates
Gates are used to control the quantum computer, and bare similarities to gates in a classical computer such as AND and XOR. These gates can be visualised as moving the vector around the Bloch sphere. It is essential for quantum computation that all transformations can be reversed, except measurement which is generally only used at the end of a program. It turns out that this rule that computations must be reversible is not actually limiting, as is explained [later](Circuits.md).


### X gate (or X rotation)
Similar to a classical NOT gate. It can be called a rotation as it rotates the state by pi radians(180 degrees) around the X axis, so if you started in |0> you rotate to |1> and vice versa. It can also be applied to superpositions of states which is equivalent to saying :\
a|0> + b|1> ----> X GATE ----> a|1> + b|0> \
So the amplitudes associated with |0> and |1> have been swapped by the X gate.

### H gate (for Hadamard gate)
Puts the qubit into an equal superposition state - so P(1) = P(0) = 0.5
If we apply an H gate to the |0> state, we get |+> which is a fancy way of saying the above. |-> is the same as |+> but it points in the opposite direction, so |-> can be achieved by running an X gate then an H gate (aka applying an H gate to |1>). The line |+> to |-> is therefore perpendicular to the line |1> to |0>.

NB running H H Measure returns 0 with P(0) = 1. This is because the H gate can be thought to move the vector through 90 degrees, so applying it twice takes it inline with the vertical axis again. Similarly X H H Measure return 1 with P(1) = 1.


### Measurement gate
The measurement can only measure along the Z axis (ie up or down) so if the vector is perpendicular to this it's 50:50 what the measurement will return. Consequently experimentally the difference between |+> and |-> cannot be measured, so what we have to do is perform rotations to get the vector in line with the standard basis and then use the conventional measurement gate.

A helpful comparison drawn by the book is that a measurement gate does not measure in the conventional sense. It is not like measuring Alice's weight, but like measuring her IQ using a test. This is because the former reveals a preexisting property of Alice, but the latter test only reveals what happens when she has an IQ test, not a numerical property she already had. That is to say, the qubit does not have a preexisting value of 1 or 0, but it can only be established when measured,

Once a qubit, or a set of qubits, has been measured no further information about their coefficients can be deduced. This loss of information when a state is measured is known as the reduction or collapse of the state. In most places this is not useful, so measurements are not done until the end of the program. However, some algorithms take advantage of this to reduce the noise accumulated by applying a measurement gate part way through the calculation.

Measurement gates can also be used to initialise a quantum system by measuring all qubits, and then applying X gates to those that returned 1. This puts the system in the |000> state. Sometimes measurements can be used to get rid of any unwanted information prior to further calculation by measuring and resetting the qubit to |0>.

### Z gate
180 degree rotation around the vertical axis (the Z axis).
So when applied to a vector that is aligned with the axis it does nothing.
![Z gate with no change](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/blocksphere-4-3-1o7ta37ydp0dg3nmi.png)
However, if an H gate is applied first, the vector is now perpendicular to the Z axis so the Z gate changes it from the |+> state to the |-> state.
![Z gate when applied after an H gate](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/h-z-gatepk7ti2a9u9emte29.png)

### S gate
90 degree rotation around the Z axis. The state achieved by applying an H gate and then an S gate is called | -> >, and its opposite is | <- >

### S^t gate
-90 degree rotation (ie the opposite of S). SS^t returns the vector to its original state.

### T gate
45 degree rotation around the Z axis

### T^t gate
-45 degree rotation around the Z axis

This is a helpful visualisation of all the gates effect on the vector marked in orange.
![All gates effect](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/4-163ijhyer00ktn8kt9.png)


# Probabilities
The sequence of gates can effect the probability of measuring a 1 or a 0.
If vector is vertically up : P(0) = 1
If vector is vertically down : P(1) = 1
#### NB an H gate must be applied before measuring these vectors
If vector is horizontally forward : P(0) = 1
If vector is horizontally backward : P(1) = 1

Gates then effect these probabilities by moving the vector.\
E.g.
  If we do H S H : P(0) = P(1) = 0.5
  This is because this makes a vector that points directly right on the page, and so it has an equal chance of being moved to |0> or |1> under the H gate.

![Table of all gates and probabilities](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/rotation-tabletkaljcjy6869a4i.png)


### Circuits
For quantum computers to work, all the gates they use must be reversible - so you can go from output to input as well as input to output. This is an issue when interfacing with conventional circuits as not all the gates they use are reversible. For example the input 11 to an AND gate is the only possible input to produce an output of 1. However if we get the output 0 there are 3 possible inputs - 00, 01 and 10. To get around this a trick is used, as in the Toffoli gate in [the next file](MultiQubitGates.md). This is adding a control wire (often called d) down which the value 0 is always sent. This is then XOR'd with the output of the function to give the overall output. This is used to make the number of outputs equal to the number of inputs. The inputs are a, b and d, and the outputs are a,b and c (which is d xor the result of F(a,b) where F is the function implemented by the gate).

In reality this technique is not often used as it requires a lot more memory and there are often optimisations that can be made.

Quantum circuits are also not allowed loops or any 'copying' of values (as this is against the laws of quantum mechanics).


### Unitary Matrices
Another way to think about the reversibility constraint is using matrices. All gates can be written in the form of matrices, which can then be multiplied by the matrix (a,b) made up of the coefficients of the qubit's vector, to give the resulting values of a and b. However, there are some limitations on what the matrices can be due to [the Born Rule](Intro.md). The result of this is that the matrices that can be represented must be unitary. This means that the [adjoint of the matrix](https://en.wikipedia.org/wiki/Adjugate_matrix) when multiplied by the gate matrix must give the identity matrix (ie *U^t * U = I*).

This unitary constraint is the only constraint on the types of operation that can be implemented by a quantum gate! Not all classical gates are unitary - as shown above there is a necessary loss of information from the output of an AND gate as it goes from 2 bits to just 1, but there are ways to convert gates to be unitary.


***
[Previous](Intro.md) - [Contents](../README.md) - [Next](MultiQubitGates.md)
