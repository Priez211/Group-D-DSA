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



