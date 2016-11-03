#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of MinHas_LSH_02817.
# https://github.com/josl/MinHash_02817

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros & Kosai Al-Nakeeb
# <bellod.cisneros@gmail.com & kosai@cbs.dtu.dk>

import pickle
from scipy.spatial import cKDTree
import numpy as np
import math
from collections import defaultdict


coefficients = set()


class HashPermutation():
    global coefficients

    def __init__(self, N, p=None):
        self.p = p
        self.a, self.b = self.get_coefficients()
        self.N = N

    def get_coefficients(self):
        a = np.random.randint(1, self.p, size=1)[0]
        b = np.random.randint(0, self.p, size=1)[0]
        if (a, b) in coefficients:
            return self.get_coefficients()
        coefficients.add((a, b))
        return (a, b)

    def random_prime(n):
        for random_n in range(n * 500, n * 2000):
            if random_n <= 1:
                continue
            else:
                for i in range(2, int(np.sqrt(random_n)) + 1, 2):
                    if random_n % i == 0:
                        break
                if random_n % i == 0:
                    continue
                return random_n

    def hash(self, x):
        return (((self.a * x) + self.b) % self.p) % self.N


class MinHash():
    # Reference: http://www.mmds.org/mmds/v2.1/ch03-lsh.pdf

    def __init__(self, dist, sparse_matrix, k_permutations):
        global coefficients
        self.dist = dist
        self.sparse_matrix = sparse_matrix
        self.point_set = {}
        self.point_dict = {}
        self.k_permutations = k_permutations
        self.dimensions = self.sparse_matrix.shape[1]
        self.n_points = self.sparse_matrix.shape[0]
        self.signatures = [
            np.array([math.inf for i in range(0, self.k_permutations)])
            for j in range(0, self.n_points)
        ]
        self.neighbors = defaultdict(set)
        self.hash_permutations = []

        p = HashPermutation.random_prime(self.n_points)
        for k in range(0, self.k_permutations):
            perm = HashPermutation(self.n_points, p)
            self.hash_permutations.append(perm.hash)
        self.permutations = {}

    def signature_distance(self, a, b):
        intersect = (a == b).sum()
        return intersect / self.k_permutations

    def createMinHash(self):
        for col_j in range(0, self.n_points):
            for sign_i, hash_func in enumerate(self.hash_permutations):
                for row_i in self.sparse_matrix[col_j].indices:
                    hash_row = hash_func(row_i)
                    if hash_row < self.signatures[col_j][sign_i]:
                        self.signatures[col_j][sign_i] = hash_row

    def find_neighbors(self):
        for index_a, point_a in enumerate(self.signatures):
            for index_b, point_b in enumerate(self.signatures):
                dist = 1 - self.signature_distance(point_a, point_b)
                if dist <= self.dist:
                    self.neighbors[index_a].add(index_b)
