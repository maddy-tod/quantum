
##Qubits
Qubits are the basic units of information. They are labelled |0> and |1> and can be thought of as the 2 energy levels, where |0> is called ground because it is the lower of the 2 energies. |0> and |1> are called the standard basis vectors as they form the basis of the subspace (ie any other vector can be created as a linear combination of these 2 vectors).

Qubits can also have a phase. This is denoted by putting coefficients in front of the vectors - a|0> + b|1>. Coefficients can be positive, negative or real.
What this formula is saying is that the state is made up of a straightforward linear combination of |0> and |1>, in the proportions given by a and b.
#### If we take the absolute value of a or b and square it, we get the probability of measuring the 0 or the 1 outcome respectively.

##Bloch Sphere
We visualise qubits as spheres, and the Bloch Sphere is the specific one used. It has a radius of 1. A point on its surfaces represents the state of a qubit.
![qubit image](https://en.wikipedia.org/wiki/Bloch_sphere)
The angle from the centre to the surface point is used to describe the state. This allows for any possibly qubit state, no matter the coefficients, to be represented. By convetion, the 'North Pole' of the Bloch Sphere is |0> and the opposite pole is |1>. Because of this, the angle theta will always be between 0 and 180 (or pi) degrees, where 180 is |1>. There is another angle phi which describes the rotation around the vertical axis. If phi is non-zero, there has been a change in the phase of the qubit.


## Superposition
A linear combination of both the |0> and |1> states. If the chance of it being |0> is equal to the chance of it being |1> it is said to be in an equal superposition state. If this is the case, then the expected value for the experiment is 0.5 (though only 1 or 0 can ever be observed).

##Entanglement
Observing the first of 2 entangled qubits cayuses it to behave randomly, but tells you exactly how the other bit would behave if it was also observed.
The qubits can be arbitrarily far apart.

After measuring a qubit, it becomes a classical bit ie it looses any entanglement or superposition it previously had.
The results from measuring a qubit, over a series of tests, is often shown as a histogram, where the highest point is the most likely result. If you are using multiple qubits, the results are treated as binary numbers.
