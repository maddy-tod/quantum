# Dirac Notation
This notation is used to describe states the quantum computer can be in. It is used elsewhere in the notes but this is a summary. The idea behind it is that when denoted like this, the important part of the vectors (aka the numbers) do not have to be denoted as a subscript.

|x> is the representation of the vector x, and in Dirac notation vectors are known as kets. Essentially anything that describes the vector is put inside the | >. Vectors are used to describe the state of the qubit.

<x|y> is the inner product (or dot product or scalar product) of the vectors x and y\
This leads to the conclusion that x and y are orthogonal if <x|y> = 1. Further, <x|x> >0 when |x> != 0.

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
