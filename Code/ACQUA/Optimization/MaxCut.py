# Code is from the AQUA tutorial

# useful additional packages
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np
import networkx as nx
import random as r

from qiskit.tools.visualization import plot_histogram
from qiskit_acqua import Operator, run_algorithm, get_algorithm_instance
from qiskit_acqua.input import get_input_instance
from qiskit_acqua.ising import maxcut


def maxCut(graph=None, n=5):

    G = graph

    # if Graph isn't provided, create a sample one
    if G is None :
       G = makeGraph(num=n)

    # colour every node red and show the starting graph
    colors = ['r' for _ in G.nodes()]
    pos = nx.spring_layout(G)
    default_axes = plt.axes(frameon=True)
    nx.draw_networkx(G, node_color=colors, node_size=600, alpha=.8, ax=default_axes, pos=pos)
    plt.show()

    # Computing the weight matrix from the graph and display it
    w = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            temp = G.get_edge_data(i, j, default=0)
            if temp != 0:
                w[i, j] = temp['weight']
    print(w)

    # Map to Ising problem
    qubitOp, offset = maxcut.get_maxcut_qubitops(w)
    algo_input = get_input_instance('EnergyInput')
    algo_input.qubit_op = qubitOp

    algorithm_cfg = {
        'name': 'VQE',
        'operator_mode': 'grouped_paulis'
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
        'backend': {'name': 'local_qasm_simulator', 'shots': 100}
    }

    # run the algorithm and print the results
    result = run_algorithm(params, algo_input)
    x = maxcut.sample_most_likely(len(w), result['eigvecs'][0])
    print('energy:', result['energy'])
    print('time:', result['eval_time'])
    print('maxcut objective:', result['energy'] + offset)
    print('solution:', maxcut.get_graph_solution(x))
    print('solution objective:', maxcut.maxcut_value(x, w))
    plot_histogram(result['eigvecs'][0])

    # colour the nodes that don't recieve a freebie red, else blue
    colors = ['r' if maxcut.get_graph_solution(x)[i] == 0 else 'b' for i in range(n)]
    nx.draw_networkx(G, node_color=colors, node_size=600, alpha=.8, pos=pos)
    plt.show()


def makeGraph(file=None, num=5):

    # NB can use qiskit_aqua.ising.maxcut.random_graph to make a much nicer (cleverer) random graph


    # Graph of the problem
    # Either created randomly or read from a file
    G = None

    # Number of nodes in the graph
    if not num :
        num = 5
    if not file :
        # Generating a graph of 4 nodes

        G = nx.Graph()
        G.add_nodes_from(np.arange(0, num, 1))

        # tuple is (i,j,weight) where (i,j) is the edge
        elist = []

        # prevent infinite looping
        failed = False
        # add random number of edges
        for count in range (0, r.randint(num,num*3)) :
            start = r.randint(0,num)
            end = r.randint(0,num)

            # no self links
            while start ==  end :
                end = r.randint(0, num)

            # don't have repeated edges
            if ((start,end) or (end,start)) in elist :
                count -=1
                if failed :
                    # already failed on the last try, so stop trying
                    break
                failed = True
            else :
                elist.append((start,end))
                failed = False

        print(elist)

        # TODO - see if can pattern match better to remove the need for two lists
        # Create new lists with the random weights
        finalelist = []
        for (s,e) in elist:
            # choose a random number between 0.1 and 1.5 to 1dp
            weight = round(r.uniform(0.1, 1.5),1)
            finalelist.append((s,e, weight))

        print(finalelist)

        G.add_weighted_edges_from(finalelist)

    return G



maxCut(n=10)