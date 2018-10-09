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



# THIS IS A DIRECT COPY FROM https://github.com/Qiskit/aqua/blob/2fa314ce9a90a2060404cd5d46f2d45f0806918e/qiskit_aqua/algorithms/components/oracles/sat.py
# SIMPLY WITH COMMENTS ADDED FOR CLARITY


import itertools
import operator
import logging
from qiskit import QuantumRegister, QuantumCircuit
from qiskit_aqua.algorithms.components.oracles import Oracle

logger = logging.getLogger(__name__)


class SAT(Oracle):
    SAT_CONFIGURATION = {
        'name': 'SAT',
        'description': 'Satisfiability Oracle',
        'input_schema': {
            '$schema': 'http://json-schema.org/schema#',
            'id': 'sat_oracle_schema',
            'type': 'object',
            'properties': {
                'cnf': {
                    'type': 'string',
                },
            },
            'additionalProperties': False
        }
    }

    def __init__(self, configuration=None):
        super().__init__(configuration or self.SAT_CONFIGURATION.copy())
        self._cnf = None
        self._qr_ancilla = None
        self._qr_clause = None
        self._qr_outcome = None
        self._qr_variable = None

    def init_args(self, cnf):

        # Remove all comments and blank lines
        # ls is array of what is left
        ls = [
            l.strip() for l in cnf.split('\n')
            if len(l) > 0 and not l.strip()[0] == 'c'
        ]

        # Extract the info from the p line
        headers = [l for l in ls if l[0] == 'p']
        if len(headers) == 1:
            p, sig, nv, nc = headers[0].split()
            assert p == 'p' and sig == 'cnf'
        else:
            raise ValueError('Invalid cnf format for SAT.')

        # num variables, num clauses
        h_nv, h_nc = int(nv), int(nc)

        # Split into arrays of strings, where each string represents a clause, store in overall array
        cs = [
            c.strip()
            for c in ' '.join(
                [l for l in ls if not l[0] == 'p']
            ).split(' 0') if len(c) > 0
        ]

        # Store the cnf as arrays of ints, in an overall array
        self._cnf = [
            [int(v) for v in c.split() if not int(v) == 0]
            for c in cs
            if (
                len(c.replace('0', '')) > 0
            ) and (
                '0' <= c[0] <= '9' or c[0] == '-'
            )
        ]

        # Check that the counts given are correct with what was read
        nv = max(set([abs(v) for v in list(itertools.chain.from_iterable(self._cnf))]))
        nc = len(self._cnf)
        if not h_nv == nv:
            logger.warning('Inaccurate variable count {} in cnf header, actual count is {}.'.format(h_nv, nv))
        if not h_nc == nc:
            logger.warning('Inaccurate clause count {} in cnf header, actual count is {}.'.format(h_nc, nc))


        # Initialise registers based on input info
        self._qr_outcome = QuantumRegister(1, name='o')
        self._qr_variable = QuantumRegister(nv, name='v')
        self._qr_clause = QuantumRegister(nc, name='c')
        num_ancillae = max(max(nc, nv) - 2, 0)
        if num_ancillae > 0:
            self._qr_ancilla = QuantumRegister(num_ancillae, name='a')

    def variable_register(self):
        return self._qr_variable

    def ancillary_register(self):
        return self._qr_ancilla

    def outcome_register(self):
        return self._qr_outcome

    def _logic_or(self, circuit, conj_expr, conj_index):

        # get the absolute values - ie turn -1 into 1
        qs = [abs(v) for v in conj_expr]

        # get the control, ancilla and target bits
        # NB -1 as variables in CNF must start from 1
        ctl_bits = [self._qr_variable[idx - 1] for idx in qs]
        anc_bits = [self._qr_ancilla[idx] for idx in range(len(qs) - 2)]
        tgt_bits = self._qr_clause[conj_index]

        # Add X gates to all +ve variables
        for idx in [v for v in conj_expr if v > 0]:
            circuit.x(self._qr_variable[idx - 1])

        # Add CNOT
        circuit.cnx(ctl_bits, anc_bits, tgt_bits)

        # Add more X gates to all +ve variables
        for idx in [v for v in conj_expr if v > 0]:
            circuit.x(self._qr_variable[idx - 1])

    def construct_circuit(self):
        # Add all the registers to the circuit
        if self._qr_ancilla:
            qc = QuantumCircuit(self._qr_variable, self._qr_clause, self._qr_ancilla, self._qr_outcome)
        else:
            qc = QuantumCircuit(self._qr_variable, self._qr_clause, self._qr_outcome)

        # init all clause qubit to 1:
        qc.x(self._qr_clause)

        # build all clause
        for conj_index, conj_expr in enumerate(self._cnf):
            # add a logical or between all the values in that clause
            self._logic_or(qc, conj_expr, conj_index)

        # keep results
        qc.cnx(
            [self._qr_clause[i] for i in range(len(self._qr_clause))],
            [self._qr_ancilla[i] for i in range(len(self._qr_ancilla))] if self._qr_ancilla else [],
            self._qr_outcome[0]
        )

        # reverse, de-entanglement
        for conj_index, conj_expr in reversed(list(enumerate(self._cnf))):
            self._logic_or(qc, conj_expr, conj_index)
        return qc

    def evaluate_classically(self, assignment):
        assignment_set = set(assignment)
        for clause in self._cnf:
            if assignment_set.isdisjoint(clause):
                return False
        return True

    def interpret_measurement(self, measurement, *args, **kwargs):
        top_measurement = max(measurement.items(), key=operator.itemgetter(1))[0]
        return [(var + 1) * (int(tf) * 2 - 1) for tf, var in zip(top_measurement[::-1], range(len(top_measurement)))]