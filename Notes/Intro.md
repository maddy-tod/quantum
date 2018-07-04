# Introduction
This file gives a first introduction to terms which are used elsewhere in the repo.

## Qubits
Qubits are the basic units of information. They are similar to conventional bits except they can hold much more information. This is due to the fact the information is stored as a vector - not just a 1 or a 0 as in conventional bits. The two  directions of the vector are labelled |0> and |1> and can be thought of as the 2 energy levels, where |0> is called ground because it is the lower of the 2 energies. |0> and |1> are called the standard basis vectors as they form the basis of the subspace (ie any other vector can be created as a linear combination of these 2 vectors). There are other vectors which can from a basis, for example the vectors orthogonal to |0> and |1> form another basis. However using |0> and |1> is the standard. This is also the direction a qubit can be measured in.

We distinguish between the classical 1 and 0, and |0> and |1> to show the difference between qubit states and measurements. A qubit can never be in the state 0 - as this is a classical state. It can be measured and return 0, which implies the qubit is in the state |0>. This is because the state of a qubit must always be a vector and 0 (or 1) is not a vector but rather a scalar value.

Qubits can also have a phase. This is denoted by putting coefficients in front of the vectors - a|0> + b|1>. Coefficients can be positive, negative or real.
What this formula is saying is that the state is made up of a straightforward linear combination of |0> and |1>, in the proportions given by a and b - so it is simply a vector in the |0> and |1> directions.

#### *If we take the absolute value of a or b and square it, we get the probability of measuring the 0 or the 1 outcome respectively. This is known as the Born Rule, after Max Born who first proposed it.*

This is a very useful (and astounding) fact. However, it is important that the state should not be considered to be 0 with P(0)= a^2 and 1 with P(1)=b^2 as this ignores the fact it is a [superposition](#superposition), and it can be seen from the probabilities in the [Single qubit gates file](Notes/SingleQubitGates.md) that this cannot be the case. It is better to think that the qubit takes both values at once, and returns each result with the calculated probability.


## Bloch Sphere
We visualise qubits as spheres, and the Bloch Sphere is the specific one used. It has a radius of 1. A point on its surfaces represents the state of a qubit.
![qubit image](https://en.wikipedia.org/wiki/Bloch_sphere#/media/File:Bloch_sphere.svg)
The angle from the centre to the surface point is used to describe the state. This allows for any possible qubit state, no matter the coefficients, to be represented. By convention, the 'North Pole' of the Bloch Sphere is |0> and the opposite pole is |1>. Because of this, the angle theta will always be between 0 and 180 (or pi) degrees, where 180 is |1>. There is another angle phi which describes the rotation around the vertical axis. If phi is non-zero, there has been a change in the phase of the qubit.

This representation makes it clear to visualise the vectors described above, and to see where the probabilities come from (using Pythagoras - as the sphere has radius 1).


## Superposition
A superposition is a linear combination of both the |0> and |1> states. If the chance of it being |0> is equal to the chance of it being |1> it is said to be in an equal superposition state. In this case a = b = (root 2)/2 , which can be calculated using the Born Rule. Further, the expected value for the experiment is 0.5 (though only 1 or 0 can ever be observed).

|z> = a|0> + b|1> \
|z> is said to be the superposition of the states |0> and |1>, with amplitudes a and b.

## Entanglement
Qubits can become entangled with each other which means that the results when they are both measured are too strongly correlated to assume they are independent form each other. Observing the first of 2 entangled qubits causes it to behave randomly, but tells you exactly how the other qubit would behave if it was also observed. This means that states of the 2 qubits cannot be described independently of each other. There is no distance limit on entanglement- qubits can be arbitrarily far apart as once they have become entangled it stays.

A helpful [video](https://www.youtube.com/watch?v=ZuvK-od647c) explaining entanglement and Bell tests.


## Measurement
Once a qubit is measured it is said to collapse to either a 1 or a 0. The act of measuring the qubit causes the vector to align with one of the poles - so any entanglement or superposition it previously had is lost. A measurement then returns a classical 1 or 0 corresponding to the state which the qubit collapsed to. The results from measuring a qubit, over a series of tests, is often shown as a histogram, where the highest point is the most likely result. If you are using multiple qubits, the results are treated as binary numbers.

## Decoherence
Decoherence occurs when some outside force (eg heat energy that is absorbed by the chip) interferes with the computation and makes the results unusable. If these errors occur at a small enough rate they can be corrected. The methods used are different from those used on classical computers but it is still possible with a small enough error.

This can be visualised using the Bloch sphere. In a pure state (uncorrupted state), the vector has length one as it touches the surface of the sphere. If it has been interfered with, the vector will have a length of less than 1 and so sit inside the sphere.

One important measure of decoherence is T1. This is the time it takes the |1> state to decay to the |0> or ground state. This is important because it lets you know the length of time calculations will be reliable for, before the values stored change. This is called *energy relaxation*. T2 is a measure of decoherence on superposition states. It is called *dephasing* and is in terms of time.
