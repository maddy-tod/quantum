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

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.svm import SVC

table = pd.read_csv('data/bank1000classical.csv')
print(table)

features = ["age","job","marital","education","default","balance","housing","loan","contact","day","month","duration","campaign","pdays","previous"]

data = table[features]
outcomes = table['poutcome']

data_train, data_test, labels_train, labels_test = train_test_split(data, outcomes, random_state=154)

scaler = MinMaxScaler()
data_train = scaler.fit_transform(data_train)
data_test = scaler.transform(data_test)


svm = SVC()
svm.fit(data_train, labels_train)
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(data_train, labels_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(data_test, labels_test)))