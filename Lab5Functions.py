import random

import numpy as np
import math




def getRandomGraph(n, m, maxWeight):
    adj_matrix = np.zeros((n, n), dtype=int)

    if(m > n):
        print(adj_matrix)
        return adj_matrix

    for i in range(0, m):
        for j in range(0, n):
            edge_weight = random.randint(0, maxWeight)
            print(edge_weight)
            adj_matrix[i][j] = edge_weight
            adj_matrix[j][i] = edge_weight

    np.fill_diagonal(adj_matrix, 0)

    print(adj_matrix)
    return adj_matrix

def Graph2DisjointSets(A):
    A = getRandomGraph()
    #for vertices in A:
        #Makeset(vertice)

getRandomGraph(5, 5, 12)

def test():
    getRandomGraph(10, 6, 10)