# useful additional packages
import matplotlib.pyplot as plt
import matplotlib.axes as axes

import numpy as np
import networkx as nx

from qiskit.tools.visualization import plot_histogram
from qiskit_aqua import Operator, run_algorithm, get_algorithm_instance
from qiskit_aqua.input import get_input_instance
from qiskit_aqua.ising import tsp


# This takes very long to complete

def draw_tsp_solution(G, order, colors, pos):
    G2 = G.copy()
    n = len(order)
    for i in range(n):
        j = (i + 1) % n
        G2.add_edge(order[i], order[j])
    default_axes = plt.axes(frameon=True)
    nx.draw_networkx(G2, node_color=colors, node_size=600, alpha=.8, ax=default_axes, pos=pos)
    plt.show()



# 4 is the limit where it becomes unfeasibly slow when run on simulator
n = 4
num_qubits = n ** 2
ins = tsp.random_tsp(n)
G = nx.Graph()
G.add_nodes_from(np.arange(0, n, 1))
colors = ['r' for node in G.nodes()]
pos = {k: v for k, v in enumerate(ins.coord)}
default_axes = plt.axes(frameon=True)
nx.draw_networkx(G, node_color=colors, node_size=600, alpha=.8, ax=default_axes, pos=pos)
plt.show()
print('distance\n', ins.w)

qubitOp, offset = tsp.get_tsp_qubitops(ins)
algo_input = get_input_instance('EnergyInput')
algo_input.qubit_op = qubitOp

algorithm_cfg = {
    'name': 'VQE',
    'operator_mode': 'matrix'
}

optimizer_cfg = {
    'name': 'SPSA',
    'max_trials': 300
}

var_form_cfg = {
    'name': 'RY',
    'depth': 5,
    'entanglement': 'linear'
}

params = {
    'problem': {'name': 'ising', 'random_seed': 10598},
    'algorithm': algorithm_cfg,
    'optimizer': optimizer_cfg,
    'variational_form': var_form_cfg,
    'backend': {'name': 'local_statevector_simulator', 'shots': 100}
}

result = run_algorithm(params,algo_input)
print('energy:', result['energy'])
print('time:', result['eval_time'])
x = tsp.sample_most_likely(result['eigvecs'][0])
print('feasible:', tsp.tsp_feasible(x))
z = tsp.get_tsp_solution(x)
print('solution:', z)
print('solution objective:', tsp.tsp_value(z, ins.w))
draw_tsp_solution(G, z, colors, pos)