# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5

import random
import timeit

import numpy as np
from matplotlib import pyplot as plt

import Disjoint
import Kruskals
import Prims
import matplotlib

def test():
    # Example usage:
    #A = getRandomGraph(3, 3, 3)
    A = np.array([[0, 2, 3],
                  [2, 0, 1],
                  [3, 1, 0]])

    print("Adjacency Matrix:\n", A)
    print("Kruskals: ", Kruskals.kruskals_mst(A))
    print("Prims: ", Prims.prim_mst(A))
    print("------------------------")
    print("Expected: (0, 1), (1, 2)")


def getRandomGraph(n, m, maxWeight):
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
    return adj_matrix

def Graph2DisjointSets(A):
    g1 = Disjoint.Graph()
    for i in range((A.shape[0])):
        g1.make_set(str(i))
    return g1


def compareTime(sizes):
    repeats = 10

    # store the averages
    avg_kruskals = []
    avg_prims = []

    for size in sizes:
        # to store the total time for the average
        kruskals_count = prims_count = 0

        # to store runtimes for each iteration
        kruskals_runtimes = []
        prims_runtimes = []

        # Calculate edge density for the given size
        edge_densities = [0.1, 0.25, 0.5, 0.66, 0.75]
        edges = [int(size * density) for density in edge_densities]

        for j in range(repeats):
            arr = np.random.randint(1, size + 1, size=size)
            mid = len(arr) // 2

            # run the quick sort and time
            kruskal_time = timeit.timeit(lambda: Kruskals.kruskals_mst(arr), setup="pass", number=1)
            kruskals_count += kruskal_time
            kruskals_runtimes.append(kruskal_time)

            # run the random and time
            prims_time = timeit.timeit(lambda: Prims.prim_mst(arr), setup="pass", number=1)
            prims_count += prims_time
            prims_runtimes.append(prims_time)

        # add the averages to their respected lists
        avg_kruskals.append(round((kruskals_count / repeats), 5))  # round to 5 decimals
        avg_prims.append(round((prims_count / repeats), 5))  # round to 5 decimals


    return avg_kruskals, avg_prims


''' ** PLOTTING THE GRAPHS WITH AVERAGE TIMES ** '''

# Example usage with sizes ranging from 5 to 10
sizes = range(5, 10)
avg_kruskals, avg_prims = compareTime(sizes)
print("Kruskals AVG: ", avg_kruskals, "\nPrims AVG:    ", avg_prims)

# plot quick sort
plt.plot(sizes, avg_kruskals, label='QuickSort', color='red', linestyle='-')
# plot random
plt.plot(sizes, avg_prims, label='Random', color='blue', linestyle='-')

# labels
plt.xlabel('Graph Size (Number of Vertices)')
plt.ylabel('Average Runtime')
plt.grid = True
plt.legend()

# show plotting
plt.show()


