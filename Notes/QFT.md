# Quantum Fourier transform
The quantum Fourier transform(QFT) is at the heart of many quantum algorithms. It is not independently useful as the state it creates cannot be directly measured, as it is all about the amplitudes. It does not act on the data stored by the system like classical transformations but rather upon the state of the system itself.

Each state has an amplitude, and the transformations are applied to these.

There is no single operator that transforms a state into its QFT so it must be built up. The resulting amplitudes are related linearly to the originals, so there must be some linear operator which performs the transformation, which can be deduced from the discrete Fourier transform.

I would also recommend [these lecture slides](http://www.cs.bham.ac.uk/internal/courses/intro-mqc/current/lecture06_handout.pdf).

## Discrete Fourier transform
A good explanation of it can be found [here](http://www.math.mcgill.ca/darmon/courses/12-13/nt/projects/Fangxi-Lin.pdf) and [this video](https://www.youtube.com/watch?v=spUNpyF58BY) also gives a good visual explanation. An additional reference can also be found  [here](http://www-bcf.usc.edu/~tbrun/Course/lecture13.pdf).

***
[Previous](SimplePrograms.md) - [Contents](../README.md) - [Next](ClassicAlgorithms.md)
