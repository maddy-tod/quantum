# https://nbviewer.jupyter.org/github/QISKit/qiskit-acqua-tutorials/blob/master/artificial_intelligence/svm_qkernel.ipynb
from qiskit_acqua.svm.data_preprocess import *
from qiskit_acqua.input import get_input_instance
from qiskit_acqua import run_algorithm
from datasets import *

sample_Total, training_input, test_input, class_labels = Breast_cancer(training_size=20, test_size=10, n=2, PLOT_DATA=True)
# n = 2 is the dimension of each data pointtotal_array, label_to_labelclass = get_points(test_input, class_labels)
total_array, label_to_labelclass = get_points(test_input, class_labels)

params = {
    'problem': {'name': 'svm_classification'},
    'backend': {'name': 'local_qasm_simulator', 'shots':100},
    'algorithm': {
        'name': 'SVM_QKernel',
        'print_info' : False
    }
}


algo_input = get_input_instance('SVMInput')
algo_input.training_dataset  = training_input
algo_input.test_dataset = test_input
algo_input.datapoints = total_array
result = run_algorithm(params,algo_input)

print("kernel matrix during the training:")
kernel_matrix = result['kernel_matrix_training']
img = plt.imshow(np.asmatrix(kernel_matrix),interpolation='nearest',origin='upper',cmap='bone_r')
plt.show()

print("testing success ratio: ", result['test_success_ratio'])
print("predicted labels:", result['predicted_labels'])