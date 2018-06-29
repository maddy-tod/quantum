# Classic examples algorithms
This document provides a brief summary of the quantum algorithms that you will hear about a lot if you ever look at any resources on quantum computing.

*A circuit which provides an output (somewhat magically) is called an oracle, an example is step 2 of Grover's algorithm*


## Grover's algorithm
This is a classic example of a quantum algorithm. It is a search algorithm for an unsorted list, which on a classical computer would be O(n/2) where n is the number of elements in the list. Grover's algorithm achieves O(root n) which is the theoretical maximum.

The problem is encoded into a function f where f(x) = 0 for every x except for the desired element d when f(d) = 1.

The state is the multiplied by -1 raised to the power of f(x). This has the effect that only the desired item is mapped to it opposite, all other elements are left unchanged. This is called the reflection.

### Amplitude amplification
This is the process Grover's algorithm (and many others) use to increase the chance the correct answer is returned.

If we measured the encoded state, it would return any state with equal probability (1/N). This is equivalent to just guessing, so on average it would be the same as a classical computer. Therefore what must be done is increase the chance of the correct state being returned, and reduce the chance of the others until it is almost certain the correct result will be returned. This is done by amplifying the amplitude of the desired state.

### Algorithm
1. Put all qubits into the uniform superposition - so all amplitudes are the same (and equal to 1/root N)
2. Apply the reflection - so only the amplitude of the goal result is flipped and consequently the average amplitude is lowered
3. Then apply another rotation which can be thought of as equivalent to subtracting the distance each amplitude is away from the average from each amplitude, and then converting all the amplitudes back to being positive. Eg if we had the amplitude 3 that was 1 away from the average it would become 2, and if we had the amplitude -2 and the average was 3 it would become -7 which would then be flipped to + 7. (NB amplitudes are complex numbers, I have just used real numbers here for simplicity) This has the effect of reducing the average
4. Steps 2 and 3 need to be repeated root N times
5. Measure



## Deutsch-Jozsa Algorithm
Consider a functions f(x) can return either 0 or 1. We are told that it is either constant (so it returns 1 for all x or it returns 0 for all x) or balanced (it returns 1 50% of the time and 0 50% of the time). The goal is to work out which it is. Classically, there is no better way than just to search through all inputs which takes up to 2^n-1 + 1 tries (where n is the length of the input string) but using the Deutsch-Jozsa Algorithm it can be done in just one function evaluation.

### Algorithm
1. Initialise all qubits to |0>
2. Apply an H gate to each qubit
3. Apply the oracle circuit as in Grover's
4. Apply an H gate to each qubit again
5. Measure each qubit - if they are all 0 then f is a constant function



## Bernstein-Vazirani Algorithm
This solves the problem of error correcting a string of binary numbers given a parity check digit. Classically this can be solved in O(n) time using Gaussian elimination, where n is the length of the string. Using a quantum computer this can be solved in O(2), provided each bit is correct more than half the time. When noise is introduced it is fatal to the classical method as Gaussian elimination now no longer works, but with quantum computers all that is necessary is a few additional tries until it is clear which bit (0 or 1) is most common for each slot.


## Shor's algorithm
This solves the problem of factoring a large number into 2 prime numbers, and is very important as it provides an O(d^3) way to do this. The fact it is computationally difficult to do this is the basis of RSA encryption, so when it becomes possible to use Shor's algorithm all of this ubiquitous form of encryption will be broken. The version presented here requires only 10d qubits and is O(d^3) where d is the number of digits.

Factoring is simple if you can find the period of the modular exponential function. This can be described as :\
Given integers N and a, find the smallest positive integer r  such that (a^r)−1 is a multiple of N. R is called the period of a modulo N.
