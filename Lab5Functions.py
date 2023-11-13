# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5

import random
import BinHeap
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


def verticelist(adj_matrix):
    num_vertices = len(adj_matrix)
    vertices = list(range(num_vertices))
    return vertices

def adjacency_list(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    adj_list = {}

    for i in range(num_vertices):
        neighbors = []
        for j in range(num_vertices):
            if adjacency_matrix[i][j] != 0:
                neighbors.append(j)
        adj_list[i] = neighbors

    return adj_list

# def test():
#     A = getRandomGraph(3, 3, 3)
#     print(A)
#     print(kraskuls_algorithm(A))
#
#
# test()