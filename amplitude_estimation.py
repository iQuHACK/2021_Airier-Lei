from qiskit import *
from qiskit.circuit.library import *
from .job import execute

def _Q(A):
    # A_inv = A.inverse()
    pass

def amplitude_estimation(A, M=2 ** 5, N=1):
    qc = QuantumCircuit(M + N, N)
    qc.append(A, range(M, M + N))

    # for i in range(M):
    #     qc.h(i)
    # # here
    # for i in range(M):
    #     qc.h(i)
    qc.measure(range(M, M + N), range(N))
    return qc

def test_amplitude_estimation():
    qc = amplitude_estimation(HGate)
    print(qc)
    execute(qc)
  
test_amplitude_estimation()
