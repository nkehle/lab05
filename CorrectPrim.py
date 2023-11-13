# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5
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
                    print(que.nodes[v]["index"])
    return mst