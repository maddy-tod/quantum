# Code is from the AQUA tutorial

# useful additional packages
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np
import networkx as nx

from qiskit.tools.visualization import plot_histogram
from qiskit_acqua import Operator, run_algorithm, get_algorithm_instance
from qiskit_acqua.input import get_input_instance
from qiskit_acqua.ising import maxcut




# Generating a graph of 4 nodes

n=5 # Number of nodes in graph
G=nx.Graph()
G.add_nodes_from(np.arange(0,n,1))

# tuple is (i,j,weight) where (i,j) is the edge
elist=[(0,1,1.0),(0,2,1.0),(0,3,1.0),(1,2,1.0),(2,3,1.0),(1,4,1.0)]

G.add_weighted_edges_from(elist)

colors = list(map(lambda x: 'r' if x%2 == 0 else'b', G.nodes()))
pos = nx.spring_layout(G)
default_axes = plt.axes(frameon=True)
nx.draw_networkx(G, node_color=colors, node_size=600, alpha=.8, ax=default_axes, pos=pos)
plt.show()

# Computing the weight matrix from the random graph
w = np.zeros([n,n])
for i in range(n):
    for j in range(n):
        temp = G.get_edge_data(i,j,default=0)
        if temp != 0:
            w[i,j] = temp['weight']
print(w)




print("Brute forcing it")
best_cost_brute = 0
for b in range(2**n):
    # x is the row being checked
    x = [int(t) for t in reversed(list(bin(b)[2:].zfill(n)))]
    #print(x)
    cost = 0
    for i in range(n):
        for j in range(n):
            #print(str(cost) + " + " + str(w[i,j]) + " * " + str(x[i])+ " * "+ str(1-x[j]))
            cost = cost + w[i,j]*x[i]*(1-x[j])
    if best_cost_brute < cost:
        best_cost_brute = cost
        xbest_brute = x
    print('case = ' + str(x)+ ' cost = ' + str(cost))

colors = ['r' if xbest_brute[i] == 0 else 'b' for i in range(n)]
nx.draw_networkx(G, node_color=colors, node_size=600, alpha=.8, pos=pos)
plt.show()
print('\nBest solution = ' + str(xbest_brute) + ' cost = ' + str(best_cost_brute))




qubitOp, offset = maxcut.get_maxcut_qubitops(w)
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
    'backend': {'name': 'local_statevector_simulator', 'shots' : 100}
}

result = run_algorithm(params, algo_input)

x = maxcut.sample_most_likely(len(w), result['eigvecs'][0])
print('energy:', result['energy'])
print('time:', result['eval_time'])
print('maxcut objective:', result['energy'] + offset)
print('solution:', maxcut.get_graph_solution(x))
print('solution objective:', maxcut.maxcut_value(x, w))

colors = ['r' if maxcut.get_graph_solution(x)[i] == 0 else 'b' for i in range(n)]
nx.draw_networkx(G, node_color=colors, node_size=600, alpha = .8, pos=pos)
plt.show()






# run quantum algorithm with shots
params['backend']['name'] = 'local_qasm_simulator'
params['backend']['shots'] = 100

result = run_algorithm(params, algo_input)
x = maxcut.sample_most_likely(len(w), result['eigvecs'][0])
print('energy:', result['energy'])
print('time:', result['eval_time'])
print('maxcut objective:', result['energy'] + offset)
print('solution:', maxcut.get_graph_solution(x))
print('solution objective:', maxcut.maxcut_value(x, w))
plot_histogram(result['eigvecs'][0])

colors = ['r' if maxcut.get_graph_solution(x)[i] == 0 else 'b' for i in range(n)]
nx.draw_networkx(G, node_color=colors, node_size=600, alpha = .8, pos=pos)
plt.show()