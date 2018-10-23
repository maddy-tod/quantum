# https://nbviewer.jupyter.org/github/QISKit/qiskit-acqua-tutorials/blob/master/artificial_intelligence/svm_qkernel.ipynb

"""
This file shows an example of how to load and plot data

"""

from qiskit_aqua.utils import split_dataset_to_data_and_labels, map_label_to_class_name
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


def classify(location='',file='testClassify.csv',class_labels=[r'A', r'B'], train_size=100, test_size=50) :

    # Title is defined in usedDefinedData function - can edit if needed but that file is from the
    # tutorial
    sample_Total, training_input, test_input, class_labels = datasets.userDefinedData(location,
                                                                             file,
                                                                             [r'1', r'61'], #class_labels,
                                                                             training_size=train_size,
                                                                             test_size=test_size,
                                                                             n=2, # normally n = 2, but can be bigger - timed out with n = 3
                                                                             PLOT_DATA=True)



    # n = 2 is the dimension of each data point
    # replaced get_points with split_dataset_to_data_and_labels

    datapoints, class_to_label = split_dataset_to_data_and_labels(test_input)
    label_to_class = {label: class_name for class_name, label in class_to_label.items()}
    print(class_to_label)
    

    params = {
        'problem': {'name': 'svm_classification', 'random_seed': 10598},
        'algorithm': {
            'name': 'QSVM.Kernel'
        },
        'backend': {'name': 'qasm_simulator', 'shots': 1024},
        'feature_map': {'name': 'SecondOrderExpansion', 'depth': 2, 'entanglement': 'linear'}
    }

    algo_input = get_input_instance('SVMInput')
    algo_input.training_dataset = training_input
    algo_input.test_dataset = test_input
    algo_input.datapoints = datapoints[0]

    import time
    start_time = time.time()
    print("Running algorithm")
    result = run_algorithm(params, algo_input)

    time_taken_secs = (time.time() - start_time)
    time_taken_format = str(int(time_taken_secs / 60)) + ":" + str((time_taken_secs % 60))
    print("--- %s ---" % time_taken_format)



    print(result)
    print("kernel matrix during the training:")
    kernel_matrix = result['kernel_matrix_training']
    img = plt.imshow(np.asmatrix(kernel_matrix), interpolation='nearest', origin='upper', cmap='bone_r')
    plt.show()

    print("testing success ratio: ", result['testing_accuracy'])

    # from new notebook
    print("testing success ratio: ", result['testing_accuracy'])
    print("predicted classes:", result['predicted_classes'])

    print("ground truth: {}".format(map_label_to_class_name(datapoints[1], label_to_class)))
    print("predicted:    {}".format(result['predicted_classes']))


    #TODO takes over 3 hours!!!!!!

# This classifies the height weight dataset into 3 distinct bands
#classify()


# All seems to only be one colour of data atm?
classify(file="KansasData.csv", class_labels=[r'1', r'61'], train_size=50, test_size=10)


