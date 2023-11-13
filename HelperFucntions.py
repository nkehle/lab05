# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5

import random
import numpy as np
import Disjoint

"""
    Generates a random connected, undirected graph represented by an adjacency matrix.
    Parameters:
        - n (int): Number of vertices.
        - m (int): Number of edges.
        - maxWeight (int): Maximum edge weight.
    Returns:
        - adj_matrix (2D array): Adjacency matrix representing the random graph.
    """
"""def getRandomGraph(n, m, maxWeight):
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
    return adj_matrix"""


"""Converts a graph represented by an adjacency matrix to disjoint sets.
    Parameters:
        - A (2D array): Adjacency matrix representing the graph.
    Returns:
        - g1 (Disjoint.Graph): Disjoint sets representing the graph.
    """
def Graph2DisjointSets(A):
    g1 = Disjoint.Graph()
    for i in range((A.shape[0])):
        g1.make_set(str(i))
    return g1

"""
    Creates a list of vertices based on an adjacency matrix.
    Parameters:
        - adj_matrix (2D array): Adjacency matrix representing the graph.
    Returns:
        - vertices (list): List of vertices.
    """
def verticelist(adj_matrix):
    num_vertices = len(adj_matrix)
    vertices = list(range(num_vertices))
    return vertices

"""
    Generates an adjacency list based on an adjacency matrix.
    Parameters:
        - adjacency_matrix (2D array): Adjacency matrix representing the graph.
    Returns:
        - adj_list (dict): Adjacency list representing the graph.
    """
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


# used for increasing the densities
def getRandomGraph(n, m, maxWeight, density):
    adj_matrix = np.zeros((n, n), dtype=int)
    count = 0
    max = int(((n*m))* 2 * density)

    if (m > n):
        print(adj_matrix)
        return adj_matrix

    for i in range(0, m):
        for j in range(0, n):
            if count < max:
                edge_weight = random.randint(1, maxWeight)
                count += 1
            else:
                edge_weight = 0
            adj_matrix[i][j] = edge_weight
            adj_matrix[j][i] = edge_weight

    np.fill_diagonal(adj_matrix, 0)
    return adj_matrix