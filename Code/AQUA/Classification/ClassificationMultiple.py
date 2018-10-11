# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================


from qiskit_aqua.utils import split_dataset_to_data_and_labels
from qiskit_aqua.input import get_input_instance
from qiskit_aqua import run_algorithm
import numpy as np

import importlib
datasets = importlib.import_module('Code.AQUA.Classification.datasets')


n = 2  # dimension of each data point
sample_Total, training_input, test_input, class_labels = datasets.Wine(training_size=20,
                                                              test_size=10, n=n, PLOT_DATA=True)

temp = [test_input[k] for k in test_input]
total_array = np.concatenate(temp)


aqua_dict = {
    'problem': {'name': 'svm_classification', 'random_seed': 10598},
    'algorithm': {
        'name': 'QSVM.Kernel'
    },
    'feature_map': {'name': 'SecondOrderExpansion', 'depth': 2, 'entangler_map': {0: [1]}},
    'multiclass_extension': {'name': 'AllPairs'},
    'backend': {'name': 'qasm_simulator', 'shots': 100}
}

algo_input = get_input_instance('SVMInput')
algo_input.training_dataset = training_input
algo_input.test_dataset = test_input
algo_input.datapoints = total_array

import time
start_time = time.time()
print("Running algorithm")
result = run_algorithm(aqua_dict, algo_input)


time_taken_secs = (time.time() - start_time)
time_taken_format = str(int(time_taken_secs / 60)) + ":" + ((time_taken_secs % 60))
print("--- %s ---" % time_taken_format)

for k,v in result.items():
    print("'{}' : {}".format(k, v))