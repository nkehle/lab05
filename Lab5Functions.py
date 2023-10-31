import random

import numpy as np
import math

import Disjoint


def getRandomGraph(n, m, maxWeight):
    adj_matrix = np.zeros((n, n), dtype=int)

    if(m > n):
        print(adj_matrix)
        return adj_matrix

    for i in range(0, m):
        for j in range(0, n):
            edge_weight = random.randint(1, maxWeight)
            adj_matrix[i][j] = edge_weight
            adj_matrix[j][i] = edge_weight

    np.fill_diagonal(adj_matrix, 0)
    return adj_matrix

def Graph2DisjointSets(A):
    g1 = Disjoint.Graph()
    for i in range((A.shape[0])):
        g1.make_set(str(i))
    return g1


def test():
    A = getRandomGraph(10, 10, 10)
    g1 = Graph2DisjointSets(A)
    g1.union('1', '2')
    g1.union('2', '3')
    g1.union('3', '4')
    g1.union('4', '5')
    g1.union('5', '6')
    g1.union('6', '7')
    print(g1.dict)

test()

