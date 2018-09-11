# https://nbviewer.jupyter.org/github/QISKit/qiskit-acqua-tutorials/blob/master/artificial_intelligence/svm_qkernel.ipynb

"""
This file shows an example of how to load and plot data

"""

from qiskit_acqua.svm.data_preprocess import *
from qiskit_acqua.input import get_input_instance
from qiskit_acqua import run_algorithm
import numpy as np
import matplotlib.pyplot as plt
from datasets import *


def classify(location='',file='testClassify.csv',class_labels=[r'A', r'B', r'C']) :

    # Title is defined in usedDefinedData function - can edit if needed but that file is from the
    # tutorial
    sample_Total, training_input, test_input, class_labels = userDefinedData(location,
                                                                             file,
                                                                             class_labels,
                                                                             training_size=500,
                                                                             test_size=200,
                                                                             n=2,
                                                                             PLOT_DATA=True)

    # n = 2 is the dimension of each data pointtotal_array, label_to_labelclass = get_points(test_input, class_labels)
    total_array, label_to_labelclass = get_points(test_input, class_labels)

    """
    sample_total <class 'numpy.ndarray'>
    training_input <class 'dict'>
    test_input <class 'dict'>
    class_labels <class 'list'>
    """

    params = {
        'problem': {'name': 'svm_classification'},
        'backend': {'name': 'local_qasm_simulator', 'shots': 100},
        'algorithm': {
            'name': 'SVM_QKernel',
            'print_info': True
        }
    }

    algo_input = get_input_instance('SVMInput')
    algo_input.training_dataset = training_input
    # could change the test input here - but still would require the correct results
    algo_input.test_dataset = test_input
    algo_input.datapoints = total_array
    result = run_algorithm(params, algo_input)

    print("kernel matrix during the training:")
    kernel_matrix = result['kernel_matrix_training']
    img = plt.imshow(np.asmatrix(kernel_matrix), interpolation='nearest', origin='lower', cmap='bone_r')
    plt.show()

    print("testing success ratio: ", result['test_success_ratio'])
    print("predicted labels:", result['predicted_labels'])



# This classifies the height weight dataset into 3 distinct bands
#classify(location="")

classify(file="bank1000.csv")

