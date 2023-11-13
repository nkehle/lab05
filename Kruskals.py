# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5

import Disjoint

"""
    Finds the Minimum Spanning Tree (MST) of a connected, undirected graph using Kruskal's algorithm.
    Parameters:
        - G (2D array): Adjacency matrix representing the graph.
    Returns:
        - result (list): List of edges forming the MST.
    """
def kruskals_mst(G):
    num_vertices = len(G)
    edges = []

    # create a list of edges from the adjacency matrix
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if G[i][j] != 0:
                edges.append((i, j, G[i][j]))

    verticies = [num for num in range(num_vertices)]

    # sort edges by weight
    edges.sort(key=lambda x: x[2])
    g = Disjoint.Graph()

    for v in verticies:
        g.make_set(v)

    result = []

    for edge in edges:
        u, v, weight = edge
        u_parent = g.find_set(u)
        v_parent = g.find_set(v)

        if u_parent != v_parent:
            result.append(edge)
            g.union(u_parent, v_parent)

    return result

