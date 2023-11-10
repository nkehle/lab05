# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5


class Graph:
    def __init__(self):
        self.dict = {}  # initialize an empty dictionary

    def make_set(self, key):
        if key not in self.dict:      # adds the keys with themselves as the label
            self.dict[key] = key

    def find_set(self, v):
        if v not in self.dict: # not in a set
            return None
        if v in self.dict and v == self.dict[v]:  # its label is itself
            return self.dict[v]

    def union(self, v, u):
        for key in self.dict:
            if self.dict[key] == u:
                self.dict[key] = v
        return u

