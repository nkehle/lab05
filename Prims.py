
import random
import BinHeap
import numpy as np
import Lab5Functions

def prim_mst(G):
    mst = []
    v_list = Lab5Functions.verticelist(G)
    adj_list = Lab5Functions.adjacency_list(G)
    queue = BinHeap.BinHeap()
    #queue.init_list(v_list, G[0])
    #print(queue.heap)

    for v in v_list:
        queue.insert((v, float('inf')))

    start_vertex = 0
    queue.decrease_key(start_vertex, 0)

    #print(queue.heap)

    while queue.heap:
        u = queue.delete_min()
        v_list.remove(u[0])

        print(u)
        for v in adj_list[u[0]]:

            if v in v_list:
                weight = G[u[0], v]
                if weight < queue.heap[queue.nodes[v]["index"]][1]:
                    print(weight)

                    queue.decrease_key(v, weight)
                    mst.append((u[0], v))  # Include weight in mst
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