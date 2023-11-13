# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5

import random
import numpy as np

"""
    Implementation of a disjoint-set data structure for union-find operations.

    Methods:
    - __init__(): Initialize an empty dictionary to represent the disjoint sets.
    - make_set(key): Add a new set with the given key.
    - find_set(v): Find the representative (label) of the set containing vertex v.
    - union(v, u): Union the sets containing vertices v and u.
"""
class Disjoint:
    def __init__(self):
        self.dict = {}  # initialize an empty dictionary

    def make_set(self, key):
        if key not in self.dict:      # adds the keys with themselves as the label
            self.dict[key] = key

    def find_set(self, v):
        if v not in self.dict: # not in a set
            return None
        if v in self.dict: # and v == self.dict[v]:  # its label is itself
            return self.dict[v]

    def union(self, v, u):
        for key in self.dict:
            if self.dict[key] == u:
                self.dict[key] = v
        return u

"""
    Implementation of a binary heap as the priority queue 

    Methods:
    - init_list(v, s): Initialize the heap with a list of vertices and a starting vertex.
    - insert(x): Insert a new element into the heap.
    - find_min(): Return the element with the minimum key.
    - delete_min(): Remove and return the element with the minimum key.
    - decrease_key(label, new_key): Decrease the key of a specified element in the heap.
    - perc_up(i): Move an element up the heap to maintain the heap property.
    - heapify(i): Heapify the subtree rooted at the specified index.
    - swap(i, j): Swap elements at indices i and j in the heap and update their indices in the associative dictionary.
    """
class BinHeap:
    def __init__(self):
        self.heap = []
        self.nodes = {}

    def init_list(self, v, s):
        # set the values to infinite
        self.heap = [(key, float('inf')) for key in v]
        for i, (label, _) in enumerate(self.heap):
            self.nodes[label] = {"index": i, "parent": -1}   # create the associative dict
        self.decrease_key(s, 0)

    def insert(self, x):
        label, key = x
        self.heap.append((label, float('inf')))
        self.nodes[label] = {"index": len(self.heap) - 1, "parent": -1}
        self.decrease_key(label, key)   # this will adjust inside with heapify

    def find_min(self):
        return self.heap[0]

    def delete_min(self):
        if not self.heap:
            return None

        min_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self.nodes[last_element[0]]["index"] = 0
            self.heapify(0)

        del self.nodes[min_element[0]]
        return min_element

    def decrease_key(self, label, new_key):
        if label not in self.nodes:
            return  # label not in the heap

        index = self.nodes[label]["index"]
        if new_key < self.heap[index][1]:
            self.heap[index] = (label, new_key)
            self.perc_up(index)     # rearranges the heap

    def perc_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][1] < self.heap[parent][1]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def heapify(self, i):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i

        if left_child < len(self.heap) and self.heap[left_child][1] < self.heap[smallest][1]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child][1] < self.heap[smallest][1]:
            smallest = right_child

        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.nodes[self.heap[i][0]]["index"] = i
        self.nodes[self.heap[j][0]]["index"] = j



"""
    Generates a random connected, undirected graph represented by an adjacency matrix.
    Parameters:
        - n (int): Number of vertices.
        - m (int): Number of edges.
        - maxWeight (int): Maximum edge weight.
    Returns:
        - adj_matrix (2D array): Adjacency matrix representing the random graph.
    """
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


"""Converts a graph represented by an adjacency matrix to disjoint sets.
    Parameters:
        - A (2D array): Adjacency matrix representing the graph.
    Returns:
        - g1 (Disjoint.Disjoint): Disjoint sets representing the graph.
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


# used for not increasing densitites
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