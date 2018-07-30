"""
This file was made to test the efficiency of Grover search with different numbers of variables/rules
"""

from qiskit_acqua import run_algorithm
from time import time


sat_cnf3 = """
c Example DIMACS 3-sat, with 3 solutions: 1 -2 3 0, -1 -2 -3 0, 1 2 -3 0
p cnf 3 5
-1 -2 -3  0
1 -2 3 0
1 2 -3 0
1 -2 -3 0
-1 2 3 0
"""

sat_cnf35 = """
c Example DIMACS 3-sat, with 3 solutions: 1 -2 3 0, -1 -2 -3 0, 1 2 -3 0
p cnf 3 5
-1 -2 -3  0
1 -2 3 0
1 2 -3 0
1 -2 -3 0
-1 2 3 0
"""
sat_cnf36 = """
c Example DIMACS 3-sat, with 3 solutions: 1 -2 3 0, -1 -2 -3 0, 1 2 -3 0
p cnf 3 6
-1 -2 -3  0
1 -2 3 0
1 2 -3 0
1 -2 -3 0
-1 2 3 0
1 2 0
"""
sat_cnf37 = """
c Example DIMACS 3-sat, with 3 solutions: 1 -2 3 0, -1 -2 -3 0, 1 2 -3 0
p cnf 3 7
-1 -2 -3  0
1 -2 3 0
1 2 -3 0
1 -2 -3 0
-1 2 3 0
1 2 0
-1 -3 0
"""
sat_cnf38 = """
c Example DIMACS 3-sat, with 3 solutions: 1 -2 3 0, -1 -2 -3 0, 1 2 -3 0
p cnf 3 8
-1 -2 -3  0
1 -2 3 0
1 2 -3 0
1 -2 -3 0
-1 2 3 0
1 2 0
-1 -3 0
-2 -3 0
"""
sat_cnf4 = """
c Example DIMACS 3-sat, with 3 solutions: 1 -2 3 0, -1 -2 -3 0, 1 2 -3 0
p cnf 4 5
-1 -2 -3 4 0
1 -2 3 0
1 2 -3 0
1 -2 -3 0
-1 2 3 0
"""

sat_cnf5 = """
c Example DIMACS 3-sat, with 3 solutions: 1 -2 3 0, -1 -2 -3 0, 1 2 -3 0
p cnf 5 5
-1 -2 -3 4 0
1 -2 3 0
1 2 -3 5 0
1 -2 -3 0
-1 2 3 0
"""

sat_cnf6 = """
c Example DIMACS 3-sat, with 3 solutions: 1 -2 3 0, -1 -2 -3 0, 1 2 -3 0
p cnf 6 5
-1 -2 -3 4 0
1 -2 3 5 -6 0
1 2 -3 0
1 -2 -3 0
-1 2 3 0
"""

sat_cnf8 = """
c Example DIMACS 3-sat, with 3 solutions: 1 -2 3 0, -1 -2 -3 0, 1 2 -3 0
p cnf 8 5
-1 -2 -3 4 0
1 -2 3 5 -6 0
1 2 -3 7 0
1 -2 -3 -8 0
-1 2 3 0
"""


sat_cnf9 = """
c Example DIMACS 3-sat, with 3 solutions: 1 -2 3 0, -1 -2 -3 0, 1 2 -3 0
p cnf 9 5
-1 -2 -3 4 0
1 -2 3 5 -6 0
1 2 -3 7 0
1 -2 -3 -8 9 0
-1 2 3 0
"""



def run(currentTest):
    params = {
        'problem': {'name': 'search'},
        'algorithm': {'name': 'Grover'},
        'oracle': {'name': 'SAT', 'cnf': currentTest},
        'backend': {'name': 'local_qasm_simulator'}
    }

    result = run_algorithm(params)
    print(result['result'])


#tests = [sat_cnf3, sat_cnf4, sat_cnf5,sat_cnf6, sat_cnf8, sat_cnf9]
tests = [sat_cnf35, sat_cnf36, sat_cnf37, sat_cnf38]
index = 5
for test in tests:
    t0 = time()
    run(test)
    t1 = time()

    print("Test " + str(index) + " took %.2f" %(t1-t0))

    index += 1

