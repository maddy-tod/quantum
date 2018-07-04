# Quantum Teleportation
Once particles are entangled they can be used to teleport information. [This video](https://www.youtube.com/watch?v=DxQK1WDYI_k) provides a very good summary of how it works.

The first idea to teleport a quantum state might be to just work out the coefficients of the state and transmit those classically. However this does not work as you cannot work out the coefficients explained in previous files, when a qubit is measured it collapses to a |0> or a |1>. Moreover, we cannot simply make a copy of the state and send that as this violates the no-cloning theorem. A further consequence of the no-cloning theorem is that the original copy of the state will be destroyed in producing the 2nd state - otherwise this 2nd state would be a clone of the first.

## No-cloning theorem
This theorem states it is impossible to create an identical copy of an arbitrary unknown quantum state, and has been proven mathematically. Videos such as [this one](https://www.youtube.com/watch?v=owPC60Ue0BE) explain the mathematical proof.

The implications of this is that it is not possible to clone humans (or anything else) perfectly, however thats not to say that they could not make very good copies. A more relevant implication is that conventional error correcting methods cannot be used on quantum computers - for example you can't simply make a copy of the quantum state that you can keep as a back up and use for correcting errors later, as is often done in classical computers.

## Preparation
In order for Alice to be able to teleport a quantum state to Bob they must each have one of an entangled pair of qubits. This pair should be in the state (|00> + |11>)/(root 2). Alice also needs a qubit whose state she wishes to transmit to Bob which is in the state a0|0> + a1|1>. The tensor product of Alices qubit and the entangled pair can then be calculated

Alice then performs operations on her qubits.
1. She sends then through a CNOT gate
2. She sends one of the qubits through an H gate
3. She measures the state of both qubits - which alters Bobs qubit due to the fact they are entangled

## Results
Alice now knows the state her qubit is in, and can use this to work out what state Bob's qubit must be in. Using this, she can classically send to Bob the series of transformations he must perform on his qubit in order to get it to look like the qubit Alice was attempting to send. Once he has performed these Bob has the teleported copy of the state!

*NB as Alice's copy of the qubit was destroyed in the teleportation process and Bob's qubit is identical to the original qubit, the qubit has been teleported from Alice to Bob*

The qubit whose state Alice transmitted to Bob is now completely entangled and so no longer represents the initial state, so Alice no longer has a copy of the data she sent.

It is worth noting that this has actually been achieved over a distance of 25km!

The maths is written out [here](http://www.cs.bham.ac.uk/internal/courses/intro-mqc/current/lecture09_handout.pdf).

***
[Previous](ClassicAlgorithms.md) - [Contents](../README.md)
