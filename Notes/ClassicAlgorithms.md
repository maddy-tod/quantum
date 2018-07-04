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


***
[Previous](QFT.md) - [Contents](../README.md) - [Next](Teleportation.md)
