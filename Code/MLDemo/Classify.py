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

import importlib
classifier = importlib.import_module('Code.AQUA.Classification.Classifier')


classifier.classify(file="bank1000.csv", class_labels=[r'Yes', r'No'], train_size=100, test_size=50)

# works with 2 and 1, and 2 and 2, but nothing else ..?
# can'r test more then 2 as test_size is 0.25 - ie 25% of 8 which is 2
# classifier.classify(file="Wheat.csv", class_labels=[r'Bad', r'Ok', r'Good'], train_size=2, test_size=2)