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


def kraskuls_algorithm(G):
    graph = Disjoint.Graph()
    edges = []
    A = []

    # get the list of edges
    for i in range(G.shape[0]):
        for j in range(i + 1, G.shape[1]):
            if G[i, j] != 0:
                edges.append((i, j, G[i, j]))

    sorted(edges, key=lambda x: x[2])

    for i in range(len(G)):
        graph.make_set(i)

    for edge in edges:
        u = edge[0]
        v = edge[1]
        if graph.find_set(u) != graph.find_set(v):
            A.append((graph.find_set(u), graph.find_set(v)))
            graph.union(u, v)

    return A


def test():
    A = getRandomGraph(3, 3, 3)
    print(A)
    print(kraskuls_algorithm(A))


test()