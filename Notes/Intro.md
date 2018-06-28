
## Qubits
Qubits are the basic units of information. They are labelled |0> and |1> and can be thought of as the 2 energy levels, where |0> is called ground because it is the lower of the 2 energies. |0> and |1> are called the standard basis vectors as they form the basis of the subspace (ie any other vector can be created as a linear combination of these 2 vectors).

Qubits can also have a phase. This is denoted by putting coefficients in front of the vectors - a|0> + b|1>. Coefficients can be positive, negative or real.
What this formula is saying is that the state is made up of a straightforward linear combination of |0> and |1>, in the proportions given by a and b.\
#### If we take the absolute value of a or b and square it, we get the probability of measuring the 0 or the 1 outcome respectively. This is known as the Born Rule, after Max Born who first proposed it.
However, the state should not be considered to be 0 with P(0)= = a^2 and 1 with P(1)=b^2 as this ignored the fact it is a superposition, and it can be seen from the probabilities in the [Single qubit gates file](Notes/SingleQubitGates.md) that this cannot be the case. It is better to think that the qubit takes both values at once.


## Bloch Sphere
We visualise qubits as spheres, and the Bloch Sphere is the specific one used. It has a radius of 1. A point on its surfaces represents the state of a qubit.
![qubit image](https://en.wikipedia.org/wiki/Bloch_sphere#/media/File:Bloch_sphere.svg)
The angle from the centre to the surface point is used to describe the state. This allows for any possible qubit state, no matter the coefficients, to be represented. By convention, the 'North Pole' of the Bloch Sphere is |0> and the opposite pole is |1>. Because of this, the angle theta will always be between 0 and 180 (or pi) degrees, where 180 is |1>. There is another angle phi which describes the rotation around the vertical axis. If phi is non-zero, there has been a change in the phase of the qubit.


## Superposition
A linear combination of both the |0> and |1> states. If the chance of it being |0> is equal to the chance of it being |1> it is said to be in an equal superposition state. If this is the case, then the expected value for the experiment is 0.5 (though only 1 or 0 can ever be observed).

|z> = a|0> + b|1> \
|z> is said to be the superposition of the states |0> and |1>, with amplitudes a and b.

## Entanglement
Observing the first of 2 entangled qubits causes it to behave randomly, but tells you exactly how the other bit would behave if it was also observed. The states of the 2 qubits cannot be described independently of each other.
The qubits can be arbitrarily far apart.

A helpful [video](https://www.youtube.com/watch?v=ZuvK-od647c) explaining entanglement and Bell tests.


## Measurement
After measuring a qubit, it becomes a classical bit ie it looses any entanglement or superposition it previously had.
The results from measuring a qubit, over a series of tests, is often shown as a histogram, where the highest point is the most likely result. If you are using multiple qubits, the results are treated as binary numbers.

## Decoherence
Decoherence occurs when some outside force (eg heat energy that is absorbed by the chip) interferes with the computation and makes the results unusable. If these errors occur at a small enough rate they can be corrected. The methods used are different from those used on classical computers but it is still possible.

This can be visualised using the Bloch sphere. In a pure state (uncorrupted state), the vector has length one as it touches the surface of the sphere. If it has been interfered with, the vector will have a length of less than 1 and so sit inside the sphere.

One important measure of decoherence is T1. This is the time it takes the |1> state to decay to the |0> or ground state. This is imporant because it lets you know the length of time calculations will be reliable for, before the values stored change. This is called *energy relaxation*.

T2 is a measure of decoherence on superposition states. It is called *dephasing* and is in terms of time.
