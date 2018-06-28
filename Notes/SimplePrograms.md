# Simple programs
When you start to link gates up together you can build up further operators or programs.

## Swapping the states of two qubits
This score swaps the states of 2 qubits. I would recommend working through the inputs and outputs with a piece of paper, just to get your head around how it works (and that it does actually work!).
![swap image](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/swapedtm8jhiv1ckgldi.png)
It is worth noting that in the real device this cannot be done between all pairs of qubits because not all pairs are linked.

There are further examples [here](https://quantumexperience.ng.bluemix.net/qx/tutorial?sectionId=full-user-guide&page=004-Quantum_Algorithms~2F061-Basic_Circuit_Identities_and_Larger_Circuits).

## Grover's algorithm
This is a classic example of a quantum algorithm. It is an undordered search algorithm, which on a classical computer would be O(n/2) where n is the number of elements in the list. Grover's algorithm achieves O(root n) which is the theoretical maximum.

The problem is encoded into a function f where f(x) = 0 for every x except for the desired element d when f(d) = 1.
