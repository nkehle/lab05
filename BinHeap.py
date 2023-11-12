# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5

from heapq import heappush, heappop, heapify

class BinHeap:
    # init the python list to structure the heap
    def __init__(self):
        self.heap = []

    # returns the location of the parent for any index i
    def parent(self, i):
        return self.heap[(i-1)/2]

    # initialize the bin heap based on the list of v objects Ex -> [(1, 5), (2, 3), (3, 8), (4, 1)]
    def init_list(self, v, s):
        self.heap = list(v)  # copy the list of tuples directly
        self.heap[0] = (s[0], s[1]) # place s as the root
        heapify(self.heap)  # rearrange

    # insert an object v, ex [1, 2] vertex 1 with key 2
    def insert(self, v):
        heappush(self.heap, v)

    # returns the object with the smallest key
    def find_min(self):
        return self.heap[0]

    # return the object with the smallest key and delete the object from the heap
    def delete_min(self):
        return heappop(self.heap)

    # find the object with the given label and decrease its key to the new key
    def decrease_key(self, label, new_key):
        index = self.find_index(label)
        self.heap[index][1] = new_key  # update the key
        heapify(self.heap)  # rearrange

    # finds the index that has the matching target label
    def find_index(self, target):
        for index, (current_key, current_label) in self.heap:
            if current_label == target:
                return index
        # if not found
        return -1

    def print_tree(self,):
        height = (len(self.heap) - 1).bit_length()
        current_level = 0
        current_position = 0

        while current_level < height:
            nodes_in_level = 2 ** current_level
            spacing = (height - current_level) * 5
            mid = 1

            for _ in range(nodes_in_level):
                if current_position < len(self.heap):
                    node = self.heap[current_position]
                    print(' ' * spacing, f"({node[0]}, {node[1]})", end=" " * (mid - 1))
                    current_position += 1
                else:
                    break
            print()
            current_level += 1



v = [(1, 5), (2, 3), (3, 8), (4, 2), (5, 7)]
que = BinHeap()
que.init_list(v, (0,0))


print(que.heap)
que.print_tree()