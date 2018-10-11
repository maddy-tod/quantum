# https://nbviewer.jupyter.org/github/QISKit/qiskit-acqua-tutorials/blob/master/artificial_intelligence/svm_qkernel.ipynb

"""
This file shows an example of how to load and plot data

"""

from qiskit_aqua.utils import split_dataset_to_data_and_labels
from qiskit_aqua.input import get_input_instance
from qiskit_aqua import run_algorithm
import numpy as np
import matplotlib.pyplot as plt



from qiskit_aqua.input import get_input_instance
from qiskit_aqua import run_algorithm
import numpy as np
import matplotlib.pyplot as plt
from qiskit import Aer



import importlib
datasets = importlib.import_module('Code.AQUA.Classification.datasets')

# This classifies the height weight dataset into 3 distinct bands
# must be sure these numbers are the correct size for the input data
# classify(train_size=20, test_size=5)

# Classifies a much larger dataset of banking data - more attributes and more rows so it takes much longer
# Trying to estimate based on a phone call if they will stay with the company
# NB trained with 500 and tested with 100 and timed out, also with 400 and 100, and 400 and 50, and 300 and 50.
# 200 and 50 is fine, but timed out with 250 and 50
# 200 and 200 is fine - so it depends on the size of the training set
# classify(file="bank1000.csv", class_labels=[r'Yes', r'No'], train_size=100, test_size=50)

"""
def classify(location='', file='testClassify.csv', class_labels=[r'A', r'B'], train_size=200, test_size=50):
    # Title is defined in usedDefinedData function - can edit if needed but that file is from the
    # tutorial

    #sample_Total, training_input, test_input, class_labels = datasets.userDefinedData(location, file, class_labels,training_size=train_size,
     #                                                                        test_size=test_size,
      #                                                                       n=2, PLOT_DATA=False)

    sample_Total, training_input, test_input, class_labels = datasets.ad_hoc_data(training_size=20,
                                                                         test_size=10,
                                                                         n=2, gap=0.3, PLOT_DATA=True)


    


    # n = 2 is the dimension of each data point
    datapoints, class_to_label = split_dataset_to_data_and_labels(test_input)

    params = {
        'problem': {'name': 'svm_classification', 'random_seed': 10598},
        'algorithm': {
            'name': 'QSVM.Kernel'
        },
        'backend': {'name': 'qasm_simulator', 'shots': 10},
        'feature_map': {'name': 'SecondOrderExpansion', 'depth': 2, 'entanglement': 'linear'}
     }

    algo_input = get_input_instance('SVMInput')
    algo_input.training_dataset = training_input
    algo_input.test_dataset = test_input
    algo_input.datapoints = datapoints[0]  # 0 is data, 1 is labels

    print("running algo")
    result = run_algorithm(params, algo_input)
    print("kernel matrix during the training:")
    kernel_matrix = result['kernel_matrix_training']
    img = plt.imshow(np.asmatrix(kernel_matrix), interpolation='nearest', origin='upper', cmap='bone_r')
    plt.show()

    print("testing success ratio: ", result['testing_accuracy'])
    print("predicted classes:", result['predicted_classes'])

"""

def classify(location='',file='testClassify.csv',class_labels=[r'A', r'B'], train_size=200, test_size=50) :

    # Title is defined in usedDefinedData function - can edit if needed but that file is from the
    # tutorial
    sample_Total, training_input, test_input, class_labels = datasets.userDefinedData(location,
                                                                             file,
                                                                            [0,1], #class_labels,
                                                                             training_size=train_size,
                                                                             test_size=test_size,
                                                                             n=2, # normally n = 2, but can be bigger - timed out with n = 3
                                                                             PLOT_DATA=True)

    # n = 2 is the dimension of each data point
    # replaced get_points with split_dataset_to_data_and_labels
    total_array, label_to_labelclass = split_dataset_to_data_and_labels(test_input, class_labels)

    """
    sample_total <class 'numpy.ndarray'>
    training_input <class 'dict'>
    test_input <class 'dict'>
    class_labels <class 'list'>
    """

    params = {
        'problem': {'name': 'svm_classification'},
        'backend': {'name': 'qasm_simulator', 'shots': 10},
        'algorithm': {
            'name': 'QSVM.Kernel', #SVM_QKernel
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


classify(file="bank1000.csv", class_labels=[r'Yes', r'No'], train_size=20, test_size=5)


