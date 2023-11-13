# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5

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


