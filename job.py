from qiskit.providers.jobstatus import JobStatus
from qiskit.tools.visualization import plot_histogram
from qiskit import *
from time import sleep

def execute(qc, verbose=True):
    backend = Aer.get_backend('unitary_simulator')
    job = execute(qc, backend)

    while job.status() is not JobStatus.DONE:
        if verbose:
            print("Job status:", job.status()) 
        sleep(5)

    result = job.result()
    print(result.get_counts())