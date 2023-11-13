# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5
import numpy as np
import BinHeap
import random


def prim_mst(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    que = BinHeap.BinHeap()
    mst = []

    # Initialization step
    for v in range(num_vertices):
        que.insert((v, float('inf')))

    start_vertex = 0
    que.decrease_key(start_vertex, 0)

    while que.heap:  # retrieve nodes from priority queue
        u = que.delete_min()
        u_label = u[0]

        # Adjust distances
        for v in range(num_vertices):
            if adjacency_matrix[u_label, v] > 0 and que.nodes.get(v) is not None:
                weight = adjacency_matrix[u_label, v]
                if weight < que.heap[que.nodes[v]["index"]][1]:
                    que.decrease_key(v, weight)
                    mst.append((u_label, v, weight))  # Include weight in mst

    return mst

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



A = np.array([
    [0, 3, 2, 0],
    [3, 0, 0, 1],
    [2, 0, 0, 5],
    [0, 1, 5, 0]
])

print("Adjacency Matrix:\n", A)
print("Kruskals: ", prim_mst(A))