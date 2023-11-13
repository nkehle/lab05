# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 5

import timeit
from matplotlib import pyplot as plt
import matplotlib
import Kruskals
import Prims
import HelperFucntions
matplotlib.use('TkAgg')


"""
    Compares the average runtimes of Kruskal's and Prim's algorithms for generating Minimum Spanning Trees (MSTs)
    on random graphs of different sizes and edge densities.
    Parameters:
        - sizes (list): List of graph sizes to test.
    Returns:
        - avg_kruskals (list): Averages of Kruskal's algorithm runtimes for each graph size.
        - avg_prims (list): Averages of Prim's algorithm runtimes for each graph size.
    """
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
        edge_densities = [0.1, 0.25, 0.5, 0.66, 0.75, 0.90, 1.0]

        for i in range(repeats):
            for density in edge_densities:
                arr = HelperFucntions.getRandomGraph(size, size, 50, density)

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
sizes = (5, 10, 20, 50, 100, 200)
avg_kruskals, avg_prims = compareTime(sizes)
print("Kruskals AVG: ", avg_kruskals, "\nPrims AVG:    ", avg_prims)

# plot quick sort
plt.plot(sizes, avg_kruskals, label='Kruskals', color='red', linestyle='-')
# plot random
plt.plot(sizes, avg_prims, label='Prims', color='blue', linestyle='-')

# labels
plt.title('Runtime of MST Kruskals vs Prims')
plt.xlabel('Graph Size With Increasing Edge Density up to 90%')
plt.ylabel('Average Runtime (Seconds)')
plt.grid = True
plt.legend()

# show plotting
plt.show()
