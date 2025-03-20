# # Example adjacency matrix for 7 cities
# Rows and columns represent cities 1 to 7
# Distance from city i to city j is stored in matrix[i][j]
# Assume distances are symmetric (bidirectional)

import numpy as np

# Example graph with 7 cities (distances are symmetric)
distances = np.array([
    [0, 10, 15, 20, 25, 30, 35],
    [10, 0, 12, 18, 22, 28, 32],
    [15, 12, 0, 10, 14, 20, 25],
    [20, 18, 10, 0, 8, 15, 18],
    [25, 22, 14, 8, 0, 10, 12],
    [30, 28, 20, 15, 10, 0, 5],
    [35, 32, 25, 18, 12, 5, 0]
])

print("Adjacency Matrix:")
print(distances)
## Using Dynamic Programming to solve the Travelling Salesman Problem (TSP)
# Function to solve TSP using Dynamic Programming (Held-Kary algorithm)
import numpy as np
from itertools import combinations

def tsp_dynamic_programming(distances):
    n = len(distances)
    # Memoization table: dp[mask][i] = shortest path from city 0 to city i, visiting all cities in mask
    dp = np.full((1 << n, n), np.inf)
    dp[1][0] = 0  # Starting at city 0

    # Iterate over all subsets of cities
    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue  # Skip if city i is not in the subset
            for j in range(n):
                if i == j or not (mask & (1 << j)):
                    continue  # Skip if city j is not in the subset or i == j
                dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << i)][j] + distances[j][i])

    # Find the minimum cost to return to the starting city (city 0)
    final_mask = (1 << n) - 1
    min_cost = min(dp[final_mask][i] + distances[i][0] for i in range(n))

    return min_cost


min_cost = tsp_dynamic_programming(distances)
print(f"Minimum TSP cost using Dynamic Programming: {min_cost}")




