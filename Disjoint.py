# Test git

class Graph:
    def __init__(self):
        self.dict = {}  # initialize an empty dictionary

    def make_set(self, key):
        if key not in self.dict:      # adds the keys with themselves as the label
            self.dict[key] = key

    def FindSet(self, v):
        if v not in self.dict: # not in a set
            return None
        if v in self.dict and v == self.dict[v]:  # its label is itself
            return self.dict[v]

    def union(self, v, u):
        for key in self.dict:
            if self.dict[key] == v:
                self.dict[key] = u
        return u

