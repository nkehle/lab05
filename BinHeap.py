# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5
import heapq


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


# Example usage:
"""heap = BinHeap()
heap.init_list(["1", "2", "3", "4", "5"], "3")
print(heap.heap)
heap.insert(("6", -100))
print(heap.heap)"""



"""pq.insert(("6", 2))
print(pq.heap)
print(pq.nodes)

pq.decrease_key("1", 4)
print(pq.heap)
print(pq.nodes)

print(pq.find_min())
print(pq.delete_min())
print(pq.heap)
print(pq.nodes)"""


"""from heapq import heappush, heappop, heapify


structure for the tuple is (key, label)
class BinHeap:
    # init the python list to structure the heap
    def __init__(self):
        self.heap = []

    # returns the location of the parent for any index i
    def parent(self, i):
        return self.heap[(i-1)/2]

    # initialize the bin heap based on the list of v objects Ex -> [(1, 5), (2, 3), (3, 8), (4, 1)]
    def init_list(self, v, s):
        for tuple in v:
            self.heap.append((tuple[1], tuple[0]))

        self.heap[0] = (s[1], s[0]) # place s as the root
        heapify(self.heap)  # rearrange

    # insert an object v, ex [1, 2] vertex 1 with key 2
    def insert(self, v):
        new_v = (v[1],v[0])
        heappush(self.heap, new_v)

    # returns the object with the smallest key
    def find_min(self):
        return self.heap[0]

    # return the object with the smallest key and delete the object from the heap
    def delete_min(self):
        return heappop(self.heap)

    # find the object with the given label and decrease its key to the new key
    def decrease_key(self, label, new_key):
        index = self.find_index(label)
        self.heap[index] = (label, new_key)  # update the key
        heapify(self.heap)  # rearrange

    # finds the index that has the matching target label
    def find_index(self, target):
        for i in range(len(self.heap)):
            if self.heap[i] == target:
                return i
        # if not found
        return -1

    # prints the tree with some spacing
    def print_tree(self):
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
                    print(' ' * spacing, f"({node[1]}, {node[0]})", end=" " * (mid - 1))
                    current_position += 1
                else:
                    break
            print()
            current_level += 1


v = [(1, 5), (2, 2), (3, 21)]
que = BinHeap()
que.init_list(v, (1, 5))
print(que.heap, '\n')
que.print_tree()

que.insert((4, 0))
print(que.heap, '\n')
que.print_tree()
"""

