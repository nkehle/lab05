# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5
import Disjoint
def kruskals_mst(G):
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
