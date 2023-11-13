# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5

import mstSupport

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
    g = mstSupport.Disjoint()

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


"""
    Finds the Minimum Spanning Tree (MST) of a connected, undirected graph using Prim's algorithm.

    Parameters:
    - adjacency_matrix (2D array): Represents the weighted edges between vertices.

    Returns:
    - mst (list): List of edges forming the MST.
    """
def prim_mst(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    que = mstSupport.BinHeap()
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
        e = que.nodes[u[0]]["parent"]

        if u[0] not in false_mst:
            false_mst.append(u[0])
            mst.append((e, u[0], u[1]))
        u = que.delete_min()
        u_label = u[0]

        # Adjust distances
        for v in range(num_vertices):
            if adjacency_matrix[u_label, v] > 0 and que.nodes.get(v) is not None:
                weight = adjacency_matrix[u_label, v]
                if weight < que.heap[que.nodes[v]["index"]][1]:
                    que.decrease_key(v, weight)
                    que.nodes[v]["parent"] = u[0]
    return mst