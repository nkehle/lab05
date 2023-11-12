# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5

import random
import numpy as np
import Disjoint
import Kruskals
import Prims

def test():
    # Example usage:
    #A = getRandomGraph(3, 3, 3)
    A = np.array([[0, 2, 3],
                  [2, 0, 1],
                  [3, 1, 0]])
    print("Adjacency Matrix:\n", A)
    print("Kruskals: ", Kruskals.kruskals_mst(A))
    print("Prims: ", Prims.prim_mst(A))


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


test()



