# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5
import numpy as np

import BinHeap

def prim_mst(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    que = BinHeap.BinHeap()
    mst = []
    false_mst = []

    # Initialization step
    for v in range(num_vertices):
        que.insert((v, float('inf')))

    start_vertex = 0
    que.decrease_key(start_vertex, 0)
    false_mst.append(start_vertex)

    while que.heap:  # retrieve nodes from priority queue
        u = que.find_min()
        e = que.nodes[u[0]]["index"]
        if u[0] not in false_mst:
            false_mst.append(u[0])
            mst.append((e, u[0]))
        u = que.delete_min()
        u_label = u[0]
        # Adjust distances
        for v in range(num_vertices):
            if adjacency_matrix[u_label, v] > 0 and que.nodes.get(v) is not None:
                weight = adjacency_matrix[u_label, v]
                if weight < que.heap[que.nodes[v]["index"]][1]:
                    que.decrease_key(v, weight)
                    que.nodes[v]["index"] = u[0]
                    #print(que.nodes[v]["index"])
    return mst


B  = np.array([
    [0, 3, 2, 0],
    [3, 0, 0, 1],
    [2, 0, 0, 1],
    [0, 1, 1, 0]
])

adjacency_matrix = np.array([
    [0, 8, 2, 6, 1, 7, 3, 5, 9, 10],
    [9, 0, 3, 7, 2, 10, 6, 4, 1, 8],
    [2, 7, 0, 10, 4, 1, 8, 6, 5, 3],
    [8, 3, 5, 0, 10, 9, 4, 7, 2, 6],
    [6, 1, 10, 4, 0, 8, 2, 3, 7, 5],
    [7, 10, 1, 3, 5, 0, 9, 8, 4, 2],
    [3, 6, 7, 9, 8, 2, 0, 1, 10, 4],
    [5, 4, 8, 2, 7, 3, 10, 0, 6, 1],
    [1, 9, 6, 5, 3, 4, 7, 10, 0, 2],
    [10, 2, 4, 8, 6, 5, 1, 2, 3, 0]
])

print("Kruskals: ", prim_mst(adjacency_matrix))