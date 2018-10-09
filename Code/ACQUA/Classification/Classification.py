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


def classify(location='',file='testClassify.csv',class_labels=[r'A', r'B'], train_size=200, test_size=50) :

    # Title is defined in usedDefinedData function - can edit if needed but that file is from the
    # tutorial
    sample_Total, training_input, test_input, class_labels = userDefinedData(location,
                                                                             file,
                                                                             class_labels,
                                                                             training_size=train_size,
                                                                             test_size=test_size,
                                                                             n=2, # normally n = 2, but can be bigger - timed out with n = 3
                                                                             PLOT_DATA=True)

    # n = 2 is the dimension of each data point
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
#classify()

# Classifies a much larger dataset of banking data - more attributes and more rows so it takes much longer
# Trying to estimate based on a phone call if they will stay with the company
# NB trained with 500 and tested with 100 and timed out, also with 400 and 100, and 400 and 50, and 300 and 50.
# 200 and 50 is fine, but timed out with 250 and 50
# 200 and 200 is fine - so it depends on the size of the training set
classify(file="bank1000.csv", class_labels=[r'Yes', r'No'], train_size=200, test_size=50)

