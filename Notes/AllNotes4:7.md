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


# Multi-qubit gates
|> is called the ket, and in multi-qubit gates there are now 2 numbers inside it giving the states |00>, |01>, |10> and |11>. The first number is the state of the 2nd qubit and the second of the 1st qubit - ie it's back to front. It is easy to remember by thinking that the right most number is always the 1st qubit.

Though there are 2-qubit gates, there are not any higher order gates due to the technical challenges of building them. Higher order operations are built up from 1 and 2 qubit gates.

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
These are classical gates that can also be implemented on a quantum computer due to the fact they already have an inverse - the gate itself. A Toffoli gate can be thought of as a CCNOT gate - so a NOT gate with 2 control wires. This is implemented as 3 inputs - a,b,c -  and 3 outputs - a,b, c XOR (a AND b), and workign through an example it can be see how the inputs can be recovered from the results (via another pass through the gate).

This principle can also be expanded for example a NAND gate can be implemented when c = 1. (It can be helpful to draw these circuits out to work through examples)


### Entanglement
Entanglement is not technically a gate, but can be induced by a combination of gates. Entanglement causes 2 qubits to behave in ways which are individually random, but not independent.
#### An entangled state cannot be described as simply a list of the states of the individual qubits
The state (|00> +|01>)/ root 2 is not entangled as the 1st qubit (right most) is in the superposed single qubit state (|0> +|1>)/root 2, and the 2nd qubit can be described similarly. However the state (|01> + |10>)/root 2 is entangled.
When you measure one qubit in an entangled state it behaves randomly, but the result of the measurement allows you to completely predict how the other qubit would behave is measured in the same way. This would not be the case if the qubits were unentangled and so independent of eachother.
These diagrams show Bell states, and the graphs below show that the results are exactly what you would expect them to be.
![Bell states composer](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/bellstate1y9ihszbafvpfogvi.png)
![Bell states graph](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/bellstate23fjnac7mh0ejyvi.png)


### 3 qubit states
The superposition between the states where all 3 qubits are in the |0> state and the one where all 3 qubits are in the |1> state is called the GHZ state. This is written (1/root 2)(|000> - |111>).

The combined properties of a 3 qubit system can be predicted - eg what happens if we measure all 3 qubits in the X direction (XXX) - but the individual outcomes per qubit cannot be predicted. When all 3 qubits are measured in the X direction the result is always -1. If 2 are measured in the Y direction and 1 in the X we get 1. The result is calculated by multiplying all the values read together, where a read 0 is mapped to a 1, and a read 1 is mapped to a -1.


### Spooky Action at a distance
A helpful [video](https://www.youtube.com/watch?v=ZuvK-od647c) explaining entanglement and Bell tests.

Einstein described entanglement as spooky action at a distance as it seemed to suggest that the qubits could communicate at speeds faster than the speed of light, which went against his theory of relativity. He theorised that the particles 'agreed' before they were separated and measured which spin they would have, however the Bell test disproves this. Over several Bell tests you can show  statistically that the theory of local variables must not be true, and a GHZ circuit can also show this but in one run.






# Simple programs
When you start to link gates up together you can build up further operators and even programs.

## Swapping the states of two qubits
This score swaps the states of 2 qubits. I would recommend working through the inputs and outputs with a piece of paper, just to get your head around how it works (and that it does actually work!).
![swap image](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/swapedtm8jhiv1ckgldi.png)
It is worth noting that in the real device this cannot be done between all pairs of qubits because not all pairs are linked.

There are further examples [here](https://quantumexperience.ng.bluemix.net/qx/tutorial?sectionId=full-user-guide&page=004-Quantum_Algorithms~2F061-Basic_Circuit_Identities_and_Larger_Circuits).


# Classic examples algorithms
This document provides a brief summary of the quantum algorithms that you will hear about a lot if you ever look at any resources on quantum computing.

*A circuit which provides an output (somewhat magically) is called an oracle, an example is step 2 of Grover's algorithm*


## Grover's algorithm
This is a classic example of a quantum algorithm. It is a search algorithm for an unsorted list. The best algorithm on a classical computer would achieve O(n/2) where n is the number of elements in the list, whereas Grover's algorithm for a quantum computer achieves O(root n), which is also the theoretical maximum.

The problem is encoded into a function f where f(x) = 0 for every x except for the desired element d when f(d) = 1.

During the algorithm, the state is the multiplied by -1 raised to the power of f(x). This has the effect that only the desired item is mapped to it opposite, all other elements are left unchanged, as -1^0 = 1. This is called the reflection or the oracle.

### Amplitude amplification
This is the process Grover's algorithm (and many others) use to increase the chance the correct answer is returned.

If we measured the encoded state, it would return any state with equal probability (1/N). This is because each qubit is in the equal superposition and so each qubit has a 50:50 chance of returning 0 and 1. The result of this is that every binary number output is equally likely, which is equivalent to just guessing. On average this would be the same as a classical computer. Therefore what must be done is increase the chance of the correct state being returned, and reduce the chance of the others until it is almost certain the correct result will be returned. This is done by amplifying the amplitude of the desired state. This occurs in step 3 of the algorithm. The graphs on [this page](https://quantumexperience.ng.bluemix.net/qx/tutorial?sectionId=full-user-guide&page=004-Quantum_Algorithms~2F070-Grover%27s_Algorithm) illustrate the process well.

### Algorithm
1. Put all qubits into the uniform superposition - so all amplitudes are the same (and equal to 1/root N)
2. Apply the reflection - so only the amplitude of the goal result is flipped and consequently the average amplitude is lowered
3. Then apply another rotation which can be thought of as equivalent to subtracting the distance each amplitude is away from the average from each amplitude, and then converting all the amplitudes back to being positive. Eg if we had the amplitude 3 that was 1 away from the average it would become 2, and if we had the amplitude -2 and the average was 3 it would become -7 which would then be flipped to + 7. (NB amplitudes are complex numbers, I have just used real numbers here for simplicity)
4. Steps 2 and 3 need to be repeated root N times
5. Measure all qubits




## Deutsch-Jozsa Algorithm
Consider a functions f(x) can return either 0 or 1. We are told that it is either constant (so it returns 1 for all x or it returns 0 for all x) or balanced (it returns 1 50% of the time and 0 50% of the time). The goal is to work out which it is. Classically, there is no better way than just to search through all inputs which takes up to 2^n-1 + 1 tries (where n is the length of the input string) but using the Deutsch-Jozsa Algorithm it can be done in just one function evaluation.

### Algorithm
1. Initialise all qubits to |0>
2. Apply an H gate to each qubit
3. Apply the oracle circuit as in Grover's
4. Apply an H gate to each qubit again
5. Measure each qubit - if they are all 0 then f is a constant function

There is no known practical use of the Deutsch-Jozsa algorithm but it does do well to demonstrate the speed up that can be achieved when using quantum computers.

## Bernstein-Vazirani Algorithm
This solves the problem of error correcting a string of binary numbers given a parity check digit. Classically this can be solved in O(n) time using Gaussian elimination, where n is the length of the string. Using a quantum computer this can be solved in O(2), provided each bit is correct more than half the time. When noise is introduced it is fatal to the classical method as Gaussian elimination now no longer works, but with quantum computers all that is necessary is a few additional tries until it is clear which bit (0 or 1) is most common for each slot.


## Shor's algorithm
This solves the problem of factoring a large number into 2 prime numbers, and is very important as it provides an O(d^3) way to do this. The fact it is computationally difficult to do this is the basis of RSA encryption, so when it becomes possible to use Shor's algorithm all of this ubiquitous form of encryption will be broken. The version presented here requires only 10d qubits and is O(d^3) where d is the number of digits.

Factoring is simple if you can find the period of the modular exponential function. This problem can be described as :\
Given integers N and a, find the smallest positive integer r  such that (a^r)−1 is a multiple of N. r is called the period of a modulo N.\
This is equivalent to saying a^r = 1 (mod N).
This problem is well defined as long as a and N share no common factors (ie gcd(a, N) = 1) and it is this step of the process that can be efficiently simulated by a quantum computer.


## Algorithm
1. Choose a random number a between 2 and N-1 (where N is the number you want to factor and so N = p1 * p2 where px is prime)
2. Check to see if N and a share any prime factors - if so make the prime factor p1 and p2 can then easily be worked out
3. Use quantum computer to work out r which is the period of a mod N, if r is even stop else repeat with different a (NB r is very likely to be even, so although this could cause an infinite loop it is very unlikely)\
 *r is therefore the smallest integer such that (a^r) - 1 is a multiple of N*
4. Using algebra we can find the factors  \
(a^r) - 1 = ((a^r) -1)((a^r) + 1) -- this is the difference of 2 squares rule\
If we assume neither of the 2 terms calculated are multiples of N but their product is (due to the way r is defined) then the 2 terms must be p1 and p2. If they are a multiple of N (eg 2N, 5N etc), then we must give up and start again from step 1. *It can be shown that this second case is very unlikely to happen, so on average no more than 2 calls to the quantum computer are needed*

[This post](http://algassert.com/post/1718) has a good in depth explanation of both the quantum part of the algorithm and the overall process.


# Quantum Fourier transform
The quantum Fourier transform(QFT) is at the heart of many quantum algorithms. It is not independently useful as the state it creates cannot be directly measured, as it is all about the amplitudes. It does not act on the data stored by the system like classical transformations but rather upon the state of the system itself.

Each state has an amplitude, and the transformations are applied to these.

There is no single operator that transforms a state into its QFT so it must be built up. The resulting amplitudes are related linearly to the originals, so there must be some linear operator which performs the transformation, which can be deduced from the discrete Fourier transform.

I would also recommend [these lecture slides](http://www.cs.bham.ac.uk/internal/courses/intro-mqc/current/lecture06_handout.pdf).

## Discrete Fourier transform
A good explanation of it can be found [here](http://www.math.mcgill.ca/darmon/courses/12-13/nt/projects/Fangxi-Lin.pdf) and [this video](https://www.youtube.com/watch?v=spUNpyF58BY) also gives a good visual explanation. An additional reference can also be found  [here](http://www-bcf.usc.edu/~tbrun/Course/lecture13.pdf).



# Dirac Notation
This notation is used to describe states the quantum computer can be in. It is used elsewhere in the notes but this is a summary. The idea behind it is that when denoted like this, the important part of the vectors (aka the numbers) do not have to be denoted as a subscript.

|x> is the representation of the column vector x, and in Dirac notation vectors are known as kets. Essentially anything that describes the vector is put inside the | >. Vectors are used to describe the state of the qubit. < x | is known as a bra and it represents a row vector.

<x|y> is the inner product (or dot product or scalar product) of the vectors x and y\
This leads to the conclusion that x and y are orthogonal if <x|y> = 1. Further, <x|x> > 0 when |x> != 0.

An equivalence that is important to remember if you ever look at any other resources is : |ax + by> = a|x> + b|y>
Computer scientists prefer the RHS, but mathematicians prefer the LHS. This can be expanded as you would expect : \
<x| ax1 + by1> = a<x|x1> + b<x|y1> \
The coefficients can also be assembled into a vector as (a,b).

As the coefficients can be real the following equation is also true :\
<x|y> = <y|x>*  where (u + iv)* = u - iv



## Tensor product
Vector a of size M and vector b of size N give the tensor product a *x* b of size MN, with components of all the possible products of pairs of values taken from a and b.\
EG (x1x2) *x* (y1y2) = (x1y1, x1y2, x2y1, x2y2)

If we use (1,0) to represent |0> and (0,1) to represent |1>, calculating the tensor product of a number (eg 110) will result in a column vector of 0's, with a 1 in the entry that represents this number, counting from 0.
