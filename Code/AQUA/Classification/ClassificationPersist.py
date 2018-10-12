
import importlib
datasets = importlib.import_module('Code.AQUA.Classification.datasets')

from qiskit_aqua.utils import split_dataset_to_data_and_labels, map_label_to_class_name
from qiskit_aqua.input import get_input_instance
from qiskit_aqua import run_algorithm, get_feature_map_instance, get_algorithm_instance, get_multiclass_extension_instance
import matplotlib.pyplot as plt
import numpy as np

n = 2 # dimension of each data point
training_dataset_size = 20
testing_dataset_size = 10

sample_Total, training_input, test_input, class_labels = datasets.userDefinedData(training_size=training_dataset_size,
                                                                     test_size=testing_dataset_size,
                                                                     n=n, gap=0.3, PLOT_DATA=False)

datapoints, class_to_label = split_dataset_to_data_and_labels(test_input)
print(class_to_label)
print(datapoints)

svm = get_algorithm_instance("QSVM.Kernel")
svm.random_seed = 10598
svm.setup_quantum_backend(backend='statevector_simulator')

feature_map = get_feature_map_instance('SecondOrderExpansion')
feature_map.init_args(num_qubits=2, depth=2, entanglement='linear')

svm.init_args(training_input, test_input, datapoints[0], feature_map)


result = svm.run()

print("kernel matrix during the training:")
kernel_matrix = result['kernel_matrix_training']
img = plt.imshow(np.asmatrix(kernel_matrix),interpolation='nearest',origin='upper',cmap='bone_r')
plt.show()

print("testing success ratio: ", result['testing_accuracy'])
print("predicted classes:", result['predicted_classes'])

predicted_labels = svm.predict(datapoints[0])

predicted_classes = map_label_to_class_name(predicted_labels, svm.label_to_class)
print("ground truth: {}".format(datapoints[1]))
print("prediction:   {}".format(predicted_labels))