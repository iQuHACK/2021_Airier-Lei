# Calculating e Using Monte Carlo Methods and Quantum Amplitude Estimation

Aaron Lamoreaux, Rachel Johnson, James Rayman

# Abstract

Quantum amplitude estimation techniques, as described in [1], may be used to compute the expected value of a quantum Monte Carlo algorithm more accurately than the naive, classical method. In this project, we implement a quantum Monte Carlo algorithm for e=2.71828... and apply quantum amplitude estimation. 

# Inspiration 

None of us have programmed using Qiskit before, and we aren't too knowledgable in quantum computing. So, we wanted a project which was not too difficult but still challenging enough for us to learn something. We got the idea of approximating a mathematical constant from [4], although we did not use the same technique as the demo.

# Description

Consider a list of random variables `x_1`, `x_2`, ..., each between 0 and 1. Let `N` be the least `n` such that `x_1 + x_2 + ... x_n > 1`. Then, the expected value of `N` is e [5]. The Monte Carlo speedup method described in [1] requires an invertable quantum algorithm as input, so we wrote a quantum Monte Carlo algorithm to simulate this process of adding up random numbers. A circuit can be constructed with `A(bits, trials)` in `stochastic.py`. `A(bits, trials)` returns a gate that calculates `trials` random numbers, each with `bits` bits of precision, adds them up one by one, and records the number of numbers needed for the sum to exceed 1. If the sum never exceeds 1, the circuit returns `trials+1`. Calling `run_bare()` in `stochastic.py` runs `A(4, 3)` 10000 times to calculate e. Using a simulator, we received a value of 2.7392.

Using quantum amplitude estimation, it is no longer necessary to run the experiment 10000 times to get an accurate estimate of e.

Calling `run()` in `stochastic.py` will run quantum amplitude estimation for `A(1, 2)`.

`notebook.ipynb` can be used to run the quantum amplitude estimation and to print circuit diagrams. 

[3] describes the techniques behind quantum amplitude estimation which is where we see the quadratic improvement in the dependence on epsilon. The technique is very similar to the ideas behind Grover's algorithm and in fact if you pick `A` to be Hadamard on `n` qubits, you end up with exactly Grover's diffusion operator. These are used in [1] in order to approximate the output of `A` by basically running `A` on `n` qubits and then using a rotation (unitary `W`) based off of the output of `A` in order to allow us to estimate the amplitudes of the terms corresponding to the output of `A`. We implemented the algorithm 1 described in order to run our experiment.  

However, quantum amplitude estimation only performs better asymptotically in the dependence on the error epsilon which means we need less total samples from the algorithm `A`. At such a small number of qubits, it is actually much faster to simulate the circuit by running `A` repeatedly.

# Future Work

It is possible to reduce the number of qubits used in our Monte Carlo simulation. Doing so will increase the efficiency of our algorithm, allowing us to improve the precision without running out of qubits.

This method could also be used to approximate other mathematical constants. We got the idea from a calculation of pi and we estimated e, but the quantum speedup method can be applied to other Monte Carlo simulations as well. For example, these techniques for lowering dependence on the error could be useful in some algorithms widely used in classical contexts, for example sketching and streaming algorithms.

# References

1. Montanaro, Ashley. "Quantum speedup of Monte Carlo methods." arXiv:1504.06987 (2017)
2. Noto, Takuna. "Quantum circuit to estimate pi using quantum amplitude estimation." arXiv:2008.02623 (2020)
3. Brassard, Giles, Peter Høyer, Michele Mosca, and Alain Tapp. "Quantum Amplitude Amplification and Estimation." arXiv:quant-ph/0005055 (2000)
4. https://qiskit.org/textbook/ch-demos/piday-code.html
5. Russell, K. G. " Estimating the Value of e by Simulation" jstor:2685243 (1991)

