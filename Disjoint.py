# Test git

class DisjointSet:
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

    def union(self, u, v):
        if u in self.dict and v in self.dict:
            # find the labels for both
            u_label = self.FindSet(u)
            v_label = self.FindSet(v)

            # turn all the keys with v into u labels
            for key in self.dict:
                if self.dict[key] == v_label:
                    self.dict[key] = u_label

            return u_label


dis1 = DisjointSet()
dis2 = DisjointSet()
dis1.make_set('a')
dis1.make_set('b')
dis1.make_set('c')

dis2.make_set('b')
dis2.make_set('g')
dis2.make_set('f')

print(dis1.dict)
print(dis2.dict)