# https://nbviewer.jupyter.org/github/QISKit/qiskit-acqua-tutorials/blob/master/artificial_intelligence/svm_qkernel.ipynb
from qiskit_acqua.svm.data_preprocess import *
from qiskit_acqua.input import get_input_instance
from qiskit_acqua import run_algorithm
from datasets import *
from sklearn.datasets.base import load_data
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#sample_Total, training_input, test_input, class_labels = Digits(training_size=20, test_size=10, n=2, PLOT_DATA=True)
# n = 2 is the dimension of each data pointtotal_array, label_to_labelclass = get_points(test_input, class_labels)
#total_array, label_to_labelclass = get_points(test_input, class_labels)




def loadData():
    #class_labels = [r'A', r'B']
    #data = datasets.load_files(container_path="numData/A")

    class_labels = [r'A', r'B', r'C']
    data, target, target_names = load_data('numData' , 'test.csv')

    sample_train, sample_test, label_train, label_test = train_test_split(
        data, target, test_size=0.3, random_state=22)

    # Now we standarize for gaussian around 0 with unit variance
    std_scale = StandardScaler().fit(sample_train)
    sample_train = std_scale.transform(sample_train)
    sample_test = std_scale.transform(sample_test)

    # Now reduce number of features to number of qubits
    pca = PCA(n_components=2).fit(sample_train)
    sample_train = pca.transform(sample_train)
    sample_test = pca.transform(sample_test)

    # Scale to the range (-1,+1)
    samples = np.append(sample_train, sample_test, axis=0)
    minmax_scale = MinMaxScaler((-1, 1)).fit(samples)
    sample_train = minmax_scale.transform(sample_train)
    sample_test = minmax_scale.transform(sample_test)

    training_size = 9
    test_size = 9

    # Pick training size number of samples from each distro
    training_input = {key: (sample_train[label_train == k, :])[:training_size] for k, key in enumerate(class_labels)}
    test_input = {key: (sample_train[label_train == k, :])[training_size:(
            training_size + test_size)] for k, key in enumerate(class_labels)}

    PLOT_DATA = True

    if PLOT_DATA:
        for k in range(0, 9):
            plt.scatter(sample_train[label_train == k, 0][:training_size],
                        sample_train[label_train == k, 1][:training_size])

        plt.title("PCA dim. reduced text dataset")
        plt.show()

    return sample_train, training_input, test_input, class_labels




sample_Total, training_input, test_input, class_labels = loadData()
# n = 2 is the dimension of each data pointtotal_array, label_to_labelclass = get_points(test_input, class_labels)
total_array, label_to_labelclass = get_points(test_input, class_labels)






"""
sample_total <class 'numpy.ndarray'>
training_input <class 'dict'>
test_input <class 'dict'>
class_labels <class 'list'>
"""

print("IT RETURNS ")
print(sample_Total)
print(training_input)

i = 0
for k,v in training_input.items():
    print(str(k) + "?!")
    #print(type(v))
    #i+=1
    #if(i == 10):
     #   break
#print(test_input)
print()
for k,v in test_input.items():
    print(str(k))
    #print(type(v))

print(class_labels)




params = {
    'problem': {'name': 'svm_classification'},
    'backend': {'name': 'local_qasm_simulator', 'shots':100},
    'algorithm': {
        'name': 'SVM_QKernel',
        'print_info' : True
    }
}

algo_input = get_input_instance('SVMInput')
algo_input.training_dataset  = training_input
algo_input.test_dataset = test_input
algo_input.datapoints = total_array
result = run_algorithm(params,algo_input)

print("kernel matrix during the training:")
kernel_matrix = result['kernel_matrix_training']
#img = plt.imshow(np.asmatrix(kernel_matrix),interpolation='nearest',origin='upper',cmap='bone_r')
#plt.show()

print("testing success ratio: ", result['test_success_ratio'])
print("predicted labels:", result['predicted_labels'])














